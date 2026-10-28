# Lista 1 (versão de 09/09/2026) — Questão 1, itens (e) e (f) (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Questão 1. Responda V para os itens que são verdadeiros e F para os itens que são falsos e
justifique suas respostas. Respostas sem justificativas não serão consideradas.
(e) ( ) Se eu provar que um algoritmo leva θ(n²) no pior caso, é possível existir alguma
entrada suficientemente grande para a qual o algoritmo realiza pelo menos 100 ∗ n operações
primitivas?
(f) ( ) Se eu provar que um algoritmo leva O(n²) no pior caso, há obrigatoriamente alguma
entrada suficientemente grande para a qual o algoritmo realiza pelo menos 100 ∗ n operações
primitivas?"

(Contexto dos itens anteriores, que não mudaram: (a) O(n²) no pior caso ⇒ possível O(n) em
algumas entradas? (b) … em todas? (c) Θ(n²) no pior caso ⇒ possível O(n) em algumas
entradas? (d) … em todas?)

## SOLUÇÃO FINAL

### Convenções
Custo medido em operações primitivas (modelo RAM). T(x) = custo na entrada x.
W(n) = máx{T(x) : x entrada de tamanho n} = custo de pior caso.
"W(n) ∈ θ(n²)" significa: existem constantes c₁ > 0, c₂ > 0 e n₀ ≥ 1 tais que
c₁n² ≤ W(n) ≤ c₂n² para todo n ≥ n₀.
"W(n) ∈ O(n²)" significa: existem c > 0 e n₀ ≥ 1 tais que 0 ≤ W(n) ≤ c·n² para todo n ≥ n₀.
"Alguma entrada suficientemente grande para a qual realiza pelo menos 100n operações"
admite duas leituras: (L1) existe ALGUMA entrada x, de tamanho n qualquer, com
T(x) ≥ 100·n; (L2) para TODO n a partir de algum ponto, existe entrada de tamanho n com
T(x) ≥ 100·n. (L2) implica (L1). Em (e) prova-se (L2), logo a resposta vale nas duas
leituras; em (f) refuta-se (L1), logo a resposta também vale nas duas leituras.

### (e) — V
Suponha W(n) ∈ θ(n²), com testemunhas c₁, c₂, n₀. Defina
  N = máx(n₀, ⌊100/c₁⌋ + 1).
Para todo n ≥ N:
- n ≥ ⌊100/c₁⌋ + 1 > 100/c₁, logo c₁·n > 100 e, multiplicando por n > 0, c₁·n² > 100·n;
- n ≥ n₀, logo W(n) ≥ c₁·n².
Encadeando, W(n) > 100·n. Como W(n) é o máximo de T(x) sobre as entradas de tamanho n, ele é
atingido por alguma entrada x_n de tamanho n, e T(x_n) = W(n) > 100·n.
(Se se preferir definir W(n) como supremo, o argumento continua: como sup > 100·n, pela
definição de supremo existe x com T(x) > 100·n.)
Portanto, para TODO n ≥ N existe uma entrada de tamanho n com mais de 100·n operações —
não só "é possível": é obrigatório. É o piso c₁n² do θ que força isso. Resposta: **V**.

Exemplo numérico. Insertion sort, contando só as comparações de chave: no pior caso (vetor
em ordem decrescente) são C(n) = n(n−1)/2 comparações, e C(n) ∈ θ(n²) com c₁ = 1/4,
c₂ = 1/2, n₀ = 2 (para n ≥ 2, n − 1 ≥ n/2, logo n(n−1)/2 ≥ n²/4; e n(n−1)/2 ≤ n²/2 para
todo n ≥ 1). Então N = máx(2, ⌊100/(1/4)⌋ + 1) = máx(2, 401) = 401 e, para n ≥ 401,
C(n) ≥ n²/4 > 100n. Como cada comparação é pelo menos uma operação primitiva, o número de
operações primitivas da entrada de pior caso também passa de 100n. (O limiar N da
demonstração é suficiente, não o menor: as comparações da entrada de pior caso já atingem
100n em n = 201, onde 201·200/2 = 20 100 = 100·201.)
Fencepost: com N = 400, o elo c₁n² > 100n da demonstração falharia, pois
(1/4)·400² = 40 000 = 100·400 — embora neste exemplo C(400) = 79 800 ainda passe de
100·400. É o elo genérico que exige o "+1" em ⌊100/c₁⌋ + 1.

### (f) — F
Agora só se sabe W(n) ∈ O(n²): um teto, sem piso. Um teto não obriga nenhuma entrada a ser
cara. Contraexemplo: o algoritmo que, recebendo um vetor A[1..n] com n ≥ 1, devolve A[1].
Ele executa um número fixo K de operações primitivas em toda entrada, independente de n;
com a convenção de custo unitário, K é pequeno (acessar A[1] e devolver: K ≤ 3). O que o
argumento usa é só que K é uma constante com K < 100, qualquer que seja a convenção. Então:
- W(n) = K ≤ K·n² para todo n ≥ 1, logo W(n) ∈ O(n²) com c = K e n₀ = 1 (e W(n) ≥ 0).
- Para toda entrada x de tamanho n ≥ 1: T(x) = K < 100 ≤ 100·n.
Portanto NENHUMA entrada, de nenhum tamanho, atinge 100·n operações — nem na leitura (L1).
A hipótese "O(n²) no pior caso" é satisfeita e a conclusão falha; logo ela não é obrigatória.
Resposta: **F**.
(O contraexemplo não depende do algoritmo ser constante: qualquer algoritmo que gaste no
máximo a·n + b operações em toda entrada de tamanho n ≥ 1, com constantes a, b ≥ 0 e
a + b < 100, também serve, pois para n ≥ 1 vale a·n + b ≤ (a + b)·n < 100·n, e
a·n + b ≤ (a + b)·n² dá O(n²). É o caso da busca linear em vetor não vazio: na contagem
usual, com laço for, a busca sem sucesso gasta 3n + 3 operações (4n + 3 se o acesso a A[i]
contar à parte), e 4 + 3 < 100.)

### Por que (e) e (f) diferem
Em (e) a hipótese é θ(n²), que tem piso c₁n²; como n² cresce mais que 100n, o piso
ultrapassa 100n para todo n ≥ N = máx(n₀, ⌊100/c₁⌋ + 1). Em (f) a hipótese é O(n²), que é só teto; o teto
é compatível com custo constante. É a mesma distinção dos itens (a)–(d): O é teto, θ é teto
e piso, e os dois falam do máximo W(n).

### Nota sobre a versão original do item (e)
Na versão anterior da lista, o item (e) dizia "O(n²)" (e não θ(n²)) com "é possível existir".
Aquela versão também era V, mas por outro motivo: um algoritmo que faz exatamente 100n
operações em toda entrada é O(n²) (100n ≤ 100n² para n ≥ 1). A versão nova troca O por θ e
mantém "é possível"; o item (f) mantém O e troca "é possível" por "há obrigatoriamente" — e
essa troca inverte a resposta.

## RESPOSTA
(e) **V** — com W(n) ≥ c₁n² para n ≥ n₀, todo n ≥ máx(n₀, ⌊100/c₁⌋ + 1) tem uma entrada de
pior caso com mais de 100n operações; é até obrigatório.
(f) **F** — O(n²) é só teto: o algoritmo que devolve A[1] gasta um número constante K ≤ 3 de
operações, é O(n²) com c = K, n₀ = 1, e nenhuma entrada chega a 100n.
