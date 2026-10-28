# Lista 5 — Questão 1 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Considere o problema de encontrar o valor máximo em um vetor contendo n números reais. Projete
um algoritmo usando o paradigma divisão e conquista para esse problema. Considere que n é um
número par. Projete duas abordagens, conforme indicado:
(a) (0.5 ponto) Projete um algoritmo para resolver o problema considerando um subproblema de
tamanho n − 1.
(b) (0.5 ponto) Projete um algoritmo para resolver o problema dividindo-o em dois subproblemas
de tamanho n/2.
(c) (0.5 ponto) Qual abordagem produz um algoritmo assintoticamente mais eficiente no pior caso?
Justifique sua resposta. Respostas sem justificativas não serão consideradas."

Formulário fornecido pela lista (Teorema Mestre, forma de Brassard & Bratley): sejam as
constantes naturais a ≥ 1, b ≥ 2 e k ≥ 0; f(n) = c·n^k com c > 0 real; T(n) = aT(n/b) + f(n);
n potência exata de b; T leva naturais em reais positivos e é assintoticamente não decrescente.
Então T(n) ∈ θ(n^k) se a < b^k; θ(n^k·lg n) se a = b^k; θ(n^(log_b a)) se a > b^k.

## SOLUÇÃO FINAL

### 0. Convenções
Vetor A[1..n] de reais, n ≥ 1. Custo medido em operações primitivas do modelo RAM (CLRS 3ª ed.,
§2.2): cada linha executada dos pseudocódigos abaixo, fora o tempo gasto dentro das chamadas
recursivas, custa uma constante. Contam-se também, à parte, as **comparações entre elementos**
do vetor, que é a medida usual para este problema.

Custo de uma chamada, fora as chamadas recursivas que ela faz:
  – com n = 1 (caso base): uma constante d > 0;
  – com n ≥ 2: depende do ramo tomado na combinação (o ramo "senão" executa uma linha a mais),
    mas fica sempre entre duas constantes 0 < c′ ≤ c″, onde c″ é o custo quando o ramo
    "senão" é tomado.
As contas abaixo são feitas com uma constante genérica c; com c = c″ elas dão o custo de **pior
caso**, e com c = c′ uma cota inferior do custo de **qualquer** entrada.

Sobre "n é par": os dois algoritmos são escritos para **todo** n ≥ 1, e precisam ser. Em (a) o
subproblema tem tamanho n − 1, que é ímpar; em (b), n par garante apenas que a **primeira**
divisão é exatamente n/2 + n/2 — já com n = 6 os subproblemas têm tamanho 3, que se dividem em
2 + 1. Um algoritmo que só funcionasse para n par não se aplicaria aos próprios subproblemas.

### (a) Um subproblema de tamanho n − 1

```
MaxA(A, n)                  ▷ devolve max{A[1], …, A[n]},  n ≥ 1
1  se n = 1 então devolva A[1]
2  m ← MaxA(A, n − 1)       ▷ conquista: máximo dos n − 1 primeiros
3  se m ≥ A[n] então devolva m
4  senão devolva A[n]       ▷ combina: compara com o último
```
Chamada inicial: MaxA(A, n).

**Correção.** P(n): "MaxA(A, n) devolve max{A[1..n]}", para todo n ≥ 1.
Base n = 1: a linha 1 devolve A[1] = max{A[1]}.
H.i.: seja n ≥ 2 e suponha P(n − 1) (note que n − 1 ≥ 1, então P(n − 1) está no domínio).
Passo: pela h.i., a linha 2 obtém m = max{A[1..n−1]}; as linhas 3–4 devolvem o maior entre m e
A[n], e max{A[1..n]} = max(max{A[1..n−1]}, A[n]). Logo P(n). ∎

**Custo.** Uma execução de MaxA(A, n) faz n chamadas no total (a inicial e n − 1 recursivas,
com tamanhos n, n − 1, …, 1): uma com tamanho 1, de custo d, e n − 1 com tamanho ≥ 2, cada uma
de custo entre c′ e c″. Com c constante, a recorrência correspondente é
  T_a(1) = d,   T_a(n) = T_a(n − 1) + c  para n ≥ 2,
e sua forma fechada é T_a(n) = d + c·(n − 1) para todo n ≥ 1.
Prova por indução: n = 1 dá d + 0 = d ✓; se vale para n − 1 (n ≥ 2),
T_a(n) = d + c(n − 2) + c = d + c(n − 1) ✓.
Logo **toda** entrada de tamanho n custa entre d + c′(n − 1) e d + c″(n − 1).
**Pior caso.** O vetor estritamente crescente toma o ramo "senão" (linha 4) em todas as n − 1
combinações, pois ali A[n] é maior que todos os anteriores; seu custo é d + c″(n − 1), que é
também a cota superior de qualquer entrada. Portanto o custo de pior caso é exatamente
  T_a^pior(n) = d + c″·(n − 1).
Θ(n) com c₁ = min(c″, d), c₂ = c″ + d, n₀ = 1:
  – cota inferior: d + c″(n − 1) ≥ min(c″,d)·1 + min(c″,d)·(n − 1) = min(c″,d)·n;
  – cota superior: d + c″(n − 1) ≤ d·n + c″·n = (c″ + d)·n, pois n ≥ 1.
Em n = n₀ = 1: min(c″,d) ≤ d ≤ c″ + d ✓. (As mesmas contas com c′ mostram que até o melhor
caso é Θ(n).)
(Este algoritmo não é da forma aT(n/b) + f(n): o Teorema Mestre não se aplica; resolve-se por
expansão, como acima.)
Comparações entre elementos: C_a(1) = 0 e C_a(n) = C_a(n − 1) + 1, logo **C_a(n) = n − 1** —
esta contagem não depende dos valores do vetor.
Chamadas (contando a inicial): n. Profundidade da pilha: n.

### (b) Dois subproblemas de tamanho n/2

```
MaxB(A, i, j)                  ▷ devolve max{A[i], …, A[j]},  i ≤ j
1  se i = j então devolva A[i]
2  q ← ⌊(i + j)/2⌋             ▷ divide ao meio
3  esq ← MaxB(A, i, q)         ▷ conquista a metade esquerda
4  dir ← MaxB(A, q + 1, j)     ▷ conquista a metade direita
5  se esq ≥ dir então devolva esq
6  senão devolva dir           ▷ combina
```
Chamada inicial: MaxB(A, 1, n).

**Tamanhos.** Seja s = j − i + 1 ≥ 2. A metade esquerda tem q − i + 1 = ⌊(j − i)/2⌋ + 1 =
⌊(s − 1)/2⌋ + 1 = ⌈s/2⌉ elementos; a direita tem s − ⌈s/2⌉ = ⌊s/2⌋. Para s ≥ 2 os dois são
≥ 1 e < s, então a recursão termina. Com s = n par, os dois têm exatamente n/2, como pede o
enunciado.

**Correção.** Indução forte em s: P(s): "MaxB devolve o máximo de qualquer trecho de s ≥ 1
elementos". Base s = 1: linha 1. Passo (s ≥ 2): pela h.i. aplicada aos tamanhos ⌈s/2⌉ e ⌊s/2⌋,
ambos em [1, s − 1], esq = máximo da metade esquerda e dir = máximo da metade direita; o máximo
do trecho é o maior dos dois, que as linhas 5–6 devolvem. ∎

**Custo.** Com as constantes da §0 (d no caso base; c, entre c′ e c″, na parte não recursiva
de uma chamada com s ≥ 2, isto é, linhas 1–5 e mais a 6 quando executada):
  T_b(1) = d,   T_b(s) = T_b(⌈s/2⌉) + T_b(⌊s/2⌋) + c  para s ≥ 2.
Forma fechada **exata para todo s ≥ 1** (não é preciso supor potência de 2):
  T_b(s) = d·s + c·(s − 1).
Prova por indução forte: s = 1 dá d ✓; para s ≥ 2, pela h.i.,
T_b(s) = d⌈s/2⌉ + c(⌈s/2⌉ − 1) + d⌊s/2⌋ + c(⌊s/2⌋ − 1) + c = d·s + c(s − 2) + c = d·s + c(s − 1) ✓,
usando ⌈s/2⌉ + ⌊s/2⌋ = s.
(Equivalentemente: há s chamadas de tamanho 1 e s − 1 de tamanho ≥ 2, num total de 2s − 1.)
Logo toda entrada de tamanho n custa entre d·n + c′(n − 1) e d·n + c″(n − 1).
**Pior caso.** No vetor estritamente crescente, em toda combinação o máximo da metade direita é
maior que o da esquerda, e o ramo "senão" (linha 6) é tomado em todas as n − 1 combinações; o
custo é d·n + c″(n − 1), a cota superior. Portanto
  T_b^pior(n) = d·n + c″·(n − 1).
Θ(n) com c₁ = d, c₂ = c″ + d, n₀ = 1: d·n ≤ d·n + c″(n − 1) ≤ (c″ + d)·n para n ≥ 1.
Em n = 1: d ≤ d ≤ c″ + d ✓.

**Confirmação pelo Teorema Mestre** (n potência exata de 2, onde a recorrência vira
T_b(n) = 2T_b(n/2) + c = 2T_b(n/2) + c·n⁰): a = 2, b = 2, k = 0, c > 0; b^k = 2⁰ = 1 < 2 = a,
isto é, a > b^k — **terceira linha** do formulário: T_b(n) ∈ Θ(n^(log₂ 2)) = Θ(n). A hipótese
"T não decrescente" vale: T_b(s) = (c + d)s − c é crescente em s. Para n par que não é potência
de 2 vale a forma fechada exata acima, que dá a mesma classe.
Comparações entre elementos: C_b(1) = 0, C_b(s) = C_b(⌈s/2⌉) + C_b(⌊s/2⌋) + 1, logo
**C_b(n) = n − 1** (mesma indução, com o custo de base 0 e o de combinação 1) — também
independente dos valores. Chamadas (contando a inicial): 2n − 1. Profundidade da pilha:
1 + ⌈lg n⌉.

### (c) Qual é assintoticamente mais eficiente no pior caso?

**Nenhuma das duas.** Ambas levam tempo **Θ(n)** no pior caso:
  T_a^pior(n) = d + c″(n − 1) ∈ Θ(n)   e   T_b^pior(n) = d·n + c″(n − 1) ∈ Θ(n),
com as testemunhas exibidas em (a) e (b). Como as duas estão em Θ(n), vale T_a^pior ∈ Θ(T_b^pior):
nenhuma é assintoticamente melhor. O desvio que depende dos dados (linhas 3–4 em MaxA, 5–6 em
MaxB) só altera o custo de cada chamada dentro da faixa constante [c′, c″]; por isso até o
melhor caso de cada uma é Θ(n) — a classe não depende da entrada, só as constantes.

Mais do que isso: as duas fazem **exatamente o mesmo número de comparações entre elementos,
n − 1**, qualquer que seja a entrada. A divisão ao meio não reduz trabalho — ela só organiza o
mesmo número de comparações numa árvore balanceada em vez de numa cadeia. Em chamadas (contando
a inicial), (b) até faz mais: 2n − 1 contra n — diferença de constante, não de classe.

**Por que dividir ao meio não dá lg n aqui.** A intuição da busca binária engana: lá há **um**
subproblema de tamanho n/2 (a = 1, T(n) = T(n/2) + c ∈ Θ(lg n)); aqui há **dois** (a = 2). No
nível i da árvore de recursão de MaxB há 2^i chamadas, cada uma com custo de combinação
constante: o trabalho de cada nível dobra enquanto o tamanho cai pela metade, e a soma dos
níveis dá n − 1 combinações.

**Nenhuma abordagem pode ser melhor que Θ(n).** Considere qualquer algoritmo determinístico
correto que acessa o vetor só lendo posições, ao custo de ao menos uma operação por leitura.
Ele precisa ler as n posições: se numa entrada ele nunca lê A[p], troque A[p] por um valor maior
que o valor devolvido e que todos os demais elementos; a execução não muda (A[p] não é lido), a
saída não muda, e agora está errada. Logo todo algoritmo gasta ao menos n operações, isto é,
Ω(n) (c = 1, n₀ = 1), e as duas abordagens são ótimas.

**A diferença que existe é de espaço, não de tempo:** a pilha de recursão tem profundidade n em
(a) e 1 + ⌈lg n⌉ em (b). Com A passado por referência e cada quadro de pilha de tamanho
constante, isso é Θ(n) contra Θ(lg n) de memória auxiliar; para o segundo, lg n ≤ 1 + ⌈lg n⌉ ≤
2 lg n para todo n ≥ 2 (c₁ = 1, c₂ = 2, n₀ = 2; em n = 2: 1 ≤ 2 ≤ 2). n₀ = 1 não serve, pois
lg 1 = 0 e a profundidade em n = 1 é 1.

## RESPOSTA
(a) MaxA: resolve A[1..n−1] recursivamente e compara o resultado com A[n].
    Recorrência T_a(n) = T_a(n−1) + c; pior caso (vetor estritamente crescente)
    T_a(n) = d + c″(n−1) ∈ Θ(n); n − 1 comparações em toda entrada.
(b) MaxB: divide em duas metades (⌈n/2⌉ e ⌊n/2⌋; exatamente n/2 e n/2 na primeira divisão, pois
    n é par), resolve cada uma e devolve o maior dos dois resultados.
    T_b(n) = 2T_b(n/2) + c ⇒ Θ(n) pelo Teorema Mestre (n potência de 2; a = 2 > b^k = 1,
    terceira linha); para todo n, pior caso exatamente T_b(n) = dn + c″(n−1) ∈ Θ(n);
    n − 1 comparações em toda entrada.
(c) Nenhuma é assintoticamente mais eficiente: ambas são Θ(n) no pior caso (e mesmo no melhor),
    com exatamente n − 1 comparações; e Θ(n) é ótimo, pois todo algoritmo precisa ler as n
    posições. A única diferença assintótica é a profundidade da pilha: Θ(n) em (a), Θ(lg n)
    em (b).
