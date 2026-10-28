# Lista 5 — Questão 2 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Resolva o seguinte problema:
a) (0.5 ponto) Dado um vetor A [.] de tamanho infinito no qual as primeiras m posições contêm
números inteiros em ordem crescente e as demais posições são preenchidas com o valor ∞. Não se
conhece o valor de m. Descreva um algoritmo que recebe um valor inteiro x como entrada e
encontra uma posição no vetor contendo o valor x, se tal posição existir, em tempo o(n). (Se você
não se sente confortável com o fato do vetor ter comprimento infinito, assuma em vez disso
comprimento de tamanho n, contudo você não conhece esse comprimento. Assuma, também, que a
implementação da estrutura de dados vetor em sua linguagem de programação preferida retorna a
mensagem de erro ∞ sempre que elementos A[i] com i > n são acessados).
b) (0.5 ponto) Argumente que seu algoritmo tem a complexidade solicitada."

## SOLUÇÃO FINAL

### 0. Modelo
Posições 1, 2, 3, …; A[1..m] são inteiros em ordem crescente (o argumento abaixo vale também
para ordem não decrescente, com repetições); A[i] = ∞ para i > m; m ≥ 0 é desconhecido. O
valor ∞ é tratado como maior que todo inteiro, então a sequência inteira A[1], A[2], … é não
decrescente:
  (Monotonia)  i < i′  ⇒  A[i] ≤ A[i′].
Na versão de comprimento finito n (desconhecido), as posições m < i ≤ n contêm ∞ e o acesso a
i > n devolve ∞; o algoritmo enxerga exatamente a mesma sequência que na versão infinita, e
m ≤ n.
Custo: cada acesso A[i] e cada operação aritmética ou comparação custa Θ(1) (modelo RAM);
conta-se o número de acessos ao vetor, e o tempo é no máximo uma constante vezes esse número.

**Tamanho da entrada.** Na versão infinita o único parâmetro é m, e o(n) se lê com n = m; na
versão finita, n é o comprimento e m ≤ n. Define-se
  f(m) = 2⌊lg m⌋ + 3 para m ≥ 1,   f(0) = 2.
f é não decrescente em m ≥ 0 (f(0) = 2 < 3 = f(1), e ⌊lg m⌋ não decresce), de modo que
f(m) ≤ f(n) em qualquer das leituras, sempre que m ≤ n.

### (a) O algoritmo: galope seguido de busca binária

```
BuscaIlimitada(A, x)
 1  i ← 1
 2  enquanto A[i] < x faça        ▷ fase 1 (galope): testa as posições 1, 2, 4, 8, …
 3      i ← 2·i
 4  lo ← ⌊i/2⌋ + 1;  hi ← i        ▷ se i = 1, então lo = hi = 1
 5  enquanto lo ≤ hi faça          ▷ fase 2: busca binária em A[lo..hi]
 6      meio ← ⌊(lo + hi)/2⌋;  v ← A[meio]
 7      se v = x então devolva meio
 8      se v < x então lo ← meio + 1
 9      senão hi ← meio − 1
10  devolva "x não está no vetor"
```
A ideia: não se conhece o fim da parte útil, então se procura, dobrando o índice, a primeira
potência de 2 cujo conteúdo já é ≥ x. Isso delimita um trecho onde x tem de estar, e nele se
faz a busca binária usual. Nenhum passo usa m ou n. Na fase 2 cada volta lê o vetor **uma**
vez (linha 6) e guarda o valor em v.

### (b) Correção e complexidade

**Lema 1 (a fase 1 termina, e quantas voltas dá).** Seja J o número de vezes que o corpo da
linha 3 executa. Então i = 2^J ao fim da fase 1, e
  J = 0 se m = 0;   J ≤ ⌊lg m⌋ + 1 se m ≥ 1.
Prova. O teste A[i] < x só é verdadeiro se A[i] é finito, isto é, i ≤ m (pois ∞ < x é falso).
Logo, cada vez que o corpo executa, o valor corrente i = 2^t satisfaz 2^t ≤ m, com t = 0, 1, 2, …
em sequência. Se m = 0, A[1] = ∞ e o laço não executa: J = 0. Se m ≥ 1, os valores de t com
2^t ≤ m são 0, 1, …, ⌊lg m⌋ — no máximo ⌊lg m⌋ + 1 deles —, e portanto o corpo executa no
máximo ⌊lg m⌋ + 1 vezes; em particular a fase 1 sempre termina. ∎

**Lema 2 (invariante ao fim da fase 1).** Ao fim da fase 1, A[i] ≥ x (o laço parou) e, se
J ≥ 1, A[i/2] < x (o teste anterior foi verdadeiro, na posição i/2 = 2^(J−1)).

**Lema 3 (x, se existe, está em A[lo..hi]).** Se existe p com A[p] = x, então existe uma tal
posição em [lo, hi].
Prova. Se A[i] = x, a própria posição i = hi serve. Se A[i] > x, seja p qualquer posição com
A[p] = x. Para p ≥ i, a Monotonia daria A[p] ≥ A[i] > x; logo p < i = hi. Se J ≥ 1, para
p ≤ i/2 a Monotonia daria A[p] ≤ A[i/2] < x; logo p > i/2, isto é, p ≥ ⌊i/2⌋ + 1 = lo. Se J = 0,
lo = 1 ≤ p trivialmente. ∎

**Lema 4 (busca binária).** Invariante do laço 5–9: "toda posição de [lo₀, hi₀] com valor x está
em [lo, hi]", onde [lo₀, hi₀] é o trecho inicial. Vale no início. Se v = A[meio] < x, toda
posição p ≤ meio tem A[p] ≤ A[meio] < x, então descartar [lo, meio] preserva o invariante; se
v > x, toda posição p ≥ meio tem A[p] > x, e descartar [meio, hi] o preserva. Logo, se o laço
termina sem devolver, [lo, hi] ficou vazio e x não ocorre em [lo₀, hi₀] — e, pelo Lema 3, não
ocorre no vetor. Reciprocamente, o algoritmo só devolve meio quando A[meio] = x. As posições com
∞ dentro do trecho não atrapalham: ∞ > x, e o trecho continua ordenado.
Número de voltas: se o trecho tem L ≥ 1 posições, após uma volta sem retorno ele tem no máximo
⌊L/2⌋ (a esquerda [lo, meio − 1] tem ⌊(L − 1)/2⌋ ≤ ⌊L/2⌋ posições; a direita [meio + 1, hi]
tem ⌈(L − 1)/2⌉ = ⌊L/2⌋). Depois de r voltas, no máximo ⌊L/2^r⌋; como uma volta só começa com
trecho não vazio, r voltas executadas implicam L/2^(r−1) ≥ 1, isto é, r ≤ ⌊lg L⌋ + 1. ∎

**Correção.** Pelos Lemas 3 e 4, o algoritmo devolve uma posição p com A[p] = x quando x
ocorre no vetor, e responde que x não está quando não ocorre. ∎

**Contagem de acessos — cota superior.** Fase 1: J + 1 acessos (J testes verdadeiros e o falso
que encerra). Fase 2: o trecho tem L = hi − lo + 1 = i − ⌊i/2⌋ posições, isto é, L = 2^(J−1)
se J ≥ 1 e L = 1 se J = 0; pelo Lema 4, no máximo ⌊lg L⌋ + 1 voltas, com **uma** leitura por
volta (linha 6): no máximo J leituras se J ≥ 1, e 1 leitura se J = 0. Total:
  J = 0:  no máximo 1 + 1 = 2 acessos;
  J ≥ 1:  no máximo (J + 1) + J = 2J + 1 ≤ 2(⌊lg m⌋ + 1) + 1 = 2⌊lg m⌋ + 3  (Lema 1).
Como J ≥ 1 exige m ≥ 1, conclui-se: **para todo m ≥ 0, no máximo f(m) acessos** (f(m) =
2⌊lg m⌋ + 3 para m ≥ 1, e f(0) = 2). O tempo total é no máximo K·f(m) para uma constante
K > 0 (cada volta de cada laço faz Θ(1) operações além do acesso), isto é, O(lg m) para m ≥ 2.
A cota é atingida quando m = 2^t − 1 e x > A[m] (conferido por força bruta para m ≤ 699:
atingida em m = 1, 3, 7, 15, …, 511).

**Contagem de acessos — cota inferior (pior caso).** Seja m ≥ 1 e tome x = A[m] + 1 (inteiro,
maior que todo elemento finito). Então A[2^t] < x para toda posição 2^t ≤ m, e o teste da linha
2 é verdadeiro exatamente para t = 0, 1, …, ⌊lg m⌋: J = ⌊lg m⌋ + 1, e só a fase 1 já faz
J + 1 = ⌊lg m⌋ + 2 acessos. Logo o pior caso W(m) (máximo de acessos sobre as entradas com esse
m) satisfaz
  ⌊lg m⌋ + 2 ≤ W(m) ≤ 2⌊lg m⌋ + 3   para todo m ≥ 1.
Testemunhas de W ∈ Θ(lg m): c₁ = 1, c₂ = 5, m₀ = 2. A cota inferior vale porque
⌊lg m⌋ + 2 > lg m; a superior, porque 2⌊lg m⌋ + 3 ≤ 2 lg m + 3 lg m = 5 lg m quando lg m ≥ 1,
isto é, m ≥ 2. Em m = m₀ = 2: lg 2 = 1, e 1 ≤ W(2) ≤ 5 (de fato W(2) = 4). m₀ = 1 não serve:
lg 1 = 0.

**Por que isso é o(n).** Pela definição (CLRS 3ª ed., §3.1), g(n) ∈ o(n) se para **toda**
constante c > 0 existe n₀ > 0 tal que 0 ≤ g(n) < c·n para todo n ≥ n₀.
Lema 5. 2^j ≥ j² para todo inteiro j ≥ 4.
  Base j = 4: 16 ≥ 16. Passo: se 2^j ≥ j² com j ≥ 4, então 2^(j+1) = 2·2^j ≥ 2j², e
  2j² − (j + 1)² = j² − 2j − 1 = (j − 1)² − 2 ≥ 9 − 2 > 0; logo 2^(j+1) ≥ (j + 1)². ∎
  (Falha em j = 3: 8 < 9 — por isso a restrição.)
Consequência: para n ≥ 16, j = ⌊lg n⌋ ≥ 4 e n ≥ 2^j ≥ j², donde ⌊lg n⌋ ≤ √n. Então, para
n ≥ 16,
  f(n) = 2⌊lg n⌋ + 3 ≤ 2√n + 3√n = 5√n    (pois √n ≥ 1).
Dado c > 0, tome n₀ = max(16, ⌊25/c²⌋ + 1). Para n ≥ n₀ vale n > 25/c², isto é, √n > 5/c;
multiplicando por c·√n > 0: c·n > 5√n ≥ f(n). Então 0 ≤ f(n) < c·n para todo n ≥ n₀, e
f ∈ o(n). Para o tempo K·f(n), repita com c/K no lugar de c: n₀ = max(16, ⌊25K²/c²⌋ + 1).
Exemplo em n = n₀: c = 1 dá n₀ = 26, f(26) = 11 < 26; c = 1/10 dá n₀ = 2501, f(2501) = 25 <
250,1.
Na versão finita (n ≥ 1), o tempo é ≤ K·f(m) ≤ K·f(n) (f não decrescente, m ≤ n), portanto
também o(n).

**Por que as alternativas óbvias não servem.** A busca linear lê A[1], A[2], … até achar x ou
um valor > x; com x > A[m] ela lê m + 1 posições — Θ(m) no pior caso, que **não** é o(n) (na
leitura n = m, ou na versão finita com m = n). A busca binária direta precisa do extremo direito
do trecho, que é justamente o que não se conhece. O galope descobre um extremo válido: hi = 2^J,
com hi ≤ 2m quando J ≥ 1 (pois 2^(J−1) ≤ m) e hi = 1 quando J = 0 — em no máximo ⌊lg m⌋ + 2
acessos se m ≥ 1, e 1 acesso se m = 0.

## RESPOSTA
(a) Galope + busca binária: teste A[1], A[2], A[4], …, A[2^t], … até achar a primeira posição
    i = 2^J com A[i] ≥ x (as posições com ∞ garantem a parada); então faça busca binária em
    A[⌊i/2⌋ + 1 .. i], lendo A[meio] uma vez por volta. Devolve uma posição com valor x, ou
    "não está".
(b) A fase 1 dá J ≤ ⌊lg m⌋ + 1 dobras (só se dobra enquanto A[i] é finito, isto é, i ≤ m), e a
    fase 2 busca num trecho de 2^(J−1) posições (1 posição se J = 0), com no máximo J leituras
    (1 se J = 0). Total: no máximo 2⌊lg m⌋ + 3 acessos para m ≥ 1 (2 para m = 0); como x maior
    que todos força ⌊lg m⌋ + 2 acessos, o pior caso é Θ(lg m) (c₁ = 1, c₂ = 5, m₀ = 2), com
    m ≤ n. E 2⌊lg n⌋ + 3 < c·n para n ≥ max(16, ⌊25/c²⌋ + 1), qualquer que seja c > 0 — logo o
    tempo é o(n).
