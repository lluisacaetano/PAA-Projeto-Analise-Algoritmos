Resposta. Com a recorrência (4) lida como T(n) = 2T(⌊n/2⌋) + n para n ≥ 2 e T(1) = 1 (o que dá T(2) = 4 e T(3) = 5, os valores que o texto calcula), vale T(n) ≥ (1/2)·n lg n para todo n ≥ 1. Logo T(n) ∈ Ω(n lg n), com testemunhas c = 1/2 e n0 = 1. A prova é por indução forte (método da substituição): os casos base são n = 1 e n = 2, e o passo vale para todo n ≥ 3. A constante c = 1 não serve: T(7) = 17 < 7 lg 7 ≈ 19,65. A mesma prova vale para qualquer T(1) ≥ 0.

INTERPRETAÇÃO DO ENUNCIADO:
Há três leituras possíveis. (a) A equação (4) com piso, T(n) = 2T(⌊n/2⌋) + n. O texto diz que "a única diferença da expressão (4) e da expressão (3) é o fato de estarmos usando o piso de n/2", e a dedução da p. 8 usa ⌊n/2⌋. Na transcrição, a equação (4) aparece impressa como "T(n) = 2T(n/2) + n, T(1) = ?", sem o símbolo de piso. (b) A fração pura n/2. Essa leitura é a recorrência (3), que só fica definida em potências de 2, e não é o exercício. (c) T(1) indeterminado ("T(1) = ?"). Resolvo a leitura (a), com T(1) = 1. É a "intuição comum" citada na p. 9 e o único valor compatível com T(2) = 4 e T(3) = 5: T(2) = 2T(1) + 2 = 4 e T(3) = 2T(⌊3/2⌋) + 3 = 2T(1) + 3 = 5. No fim, uma observação mostra que o resultado vale para qualquer T(1) ≥ 0, o que também cobre a leitura (c) com T(1) ≥ 0. Uso lg = log₂ (na recorrência (3), T(2^k) = n lg n + n). A classe Ω(n log n) não depende da base do logaritmo. Só a constante c depende dela.

DEFINIÇÃO USADA:
T(n) ∈ Ω(g(n)) se existem constantes reais c > 0 e n0 tais que, para todo n ≥ n0, 0 ≤ c·g(n) ≤ T(n). A ordem dos quantificadores é ∃c ∃n0 ∀n ≥ n0. O texto, para a cota O, pede c ∈ ℕ. Para a cota inferior isso não funciona em base 2, porque c = 1 falha (ver abaixo), e por isso uso c real positivo, como no CLRS. Se o leitor exigir c natural, a mesma prova dá c = 1 com logaritmo na base 4: (1/2)·n lg n = n log₄ n.

AFIRMAÇÃO P(n):
P(n): T(n) ≥ (1/2)·n lg n.
Provo P(n) para todo n ≥ 1 por indução forte em n.

CASOS BASE (n = 1 e n = 2):
n = 1: T(1) = 1 e (1/2)·1·lg 1 = 0. Como 1 ≥ 0, P(1) vale.
n = 2: T(2) = 4 e (1/2)·2·lg 2 = 1. Como 4 ≥ 1, P(2) vale.
O caso n = 2 precisa ser base porque o passo abaixo exige n ≥ 3. Com n = 2, a cota (n−1)/2 = 1/2 fica menor que 1 e o logaritmo dela é negativo.

HIPÓTESE DE INDUÇÃO:
Seja n ≥ 3 e suponha P(k) para todo k com 1 ≤ k < n, ou seja, T(k) ≥ (1/2)·k lg k. Uso essa hipótese exatamente uma vez, em k = ⌊n/2⌋. Esse k está no intervalo, porque para n ≥ 3 vale 1 ≤ ⌊n/2⌋ ≤ n/2 < n.

PASSO INDUTIVO (n ≥ 3):
Passo 1 (definição e hipótese). T(n) = 2T(⌊n/2⌋) + n ≥ 2·(1/2)·⌊n/2⌋·lg⌊n/2⌋ + n = ⌊n/2⌋·lg⌊n/2⌋ + n.

Passo 2 (tirar o piso). Para todo n vale ⌊n/2⌋ ≥ (n−1)/2: a igualdade vale com n ímpar, e com n par ⌊n/2⌋ = n/2 > (n−1)/2. Com n ≥ 3, temos (n−1)/2 ≥ 1. A função x ↦ x lg x é crescente para x ≥ 1, porque os dois fatores, x e lg x, são não negativos e não decrescentes nesse intervalo. Então
    ⌊n/2⌋·lg⌊n/2⌋ ≥ ((n−1)/2)·lg((n−1)/2) = ((n−1)/2)·(lg(n−1) − 1).
Portanto T(n) ≥ ((n−1)/2)·(lg(n−1) − 1) + n.

Passo 3 (comparar com o alvo). Quero T(n) − (1/2)·n lg n ≥ 0. Pelo passo 2,
    T(n) − (1/2)·n lg n ≥ n − (n−1)/2 − (1/2)·[n lg n − (n−1) lg(n−1)].
Seja m = n − 1 ≥ 2. Então
    n lg n − (n−1) lg(n−1) = lg n + m·(lg n − lg m) = lg n + lg((1 + 1/m)^m).
Como ln(1 + x) < x para x > 0, vale m·ln(1 + 1/m) < 1, ou seja, (1 + 1/m)^m < e < 4. Logo lg((1 + 1/m)^m) < 2, e
    n lg n − (n−1) lg(n−1) < lg n + 2.
Substituindo:
    T(n) − (1/2)·n lg n > n − (n−1)/2 − (1/2)·(lg n + 2) = (n − lg n − 1)/2.

Passo 4 (n − lg n − 1 ≥ 0 para todo n ≥ 1). Isso equivale a 2^(n−1) ≥ n, que se prova por indução simples. Em n = 1: 2^0 = 1 ≥ 1. Se 2^(n−1) ≥ n, então 2^n = 2·2^(n−1) ≥ 2n ≥ n + 1. Logo T(n) − (1/2)·n lg n > 0, e P(n) vale.

Com P(1), P(2) e o passo para todo n ≥ 3, P(n) vale para todo n ≥ 1.

TESTEMUNHAS E CONFERÊNCIA EM n = n0:
c = 1/2 e n0 = 1. Em n = n0 = 1: c·g(1) = (1/2)·1·lg 1 = 0 e T(1) = 1, logo 0 ≤ 0 ≤ 1. Para todo n ≥ 1, 0 ≤ (1/2)·n lg n ≤ T(n). A cota vale para toda entrada n ≥ 1, porque T é uma função de n e não há pior ou melhor caso a distinguir. Portanto T(n) ∈ Ω(n lg n). Com a prova da cota O(n lg n) feita no texto, T(n) ∈ Θ(n lg n).

POR QUE c = 1 NÃO FECHA:
Com c = 1, a mesma conta do passo 3 dá a cota inferior n − (n−1) − (lg n + 2) = −1 − lg n, que é negativa. Isso não é só falha da técnica: a afirmação T(n) ≥ n lg n é falsa. T(7) = 2T(3) + 7 = 17, mas 7 lg 7 ≈ 19,65. O piso ⌊n/2⌋ < n/2 com n ímpar faz T ficar abaixo de n lg n em vários n (7, 11, 13, 14, 15, ...). Por isso c precisa ficar abaixo de 1. O valor 1/2 deixa folga suficiente para absorver tanto o piso quanto o termo lg n + 2.

OBSERVAÇÃO (T(1) arbitrário não negativo):
O passo indutivo não usa o valor de T(1). Os casos base valem para qualquer T(1) ≥ 0: P(1) é 0 ≤ T(1), e P(2) é T(2) = 2T(1) + 2 ≥ 2 ≥ 1. Logo T(n) ≥ (1/2)·n lg n para todo n ≥ 1 sempre que T(1) ≥ 0, com as mesmas testemunhas c = 1/2 e n0 = 1. Não afirmo nada para T(1) < 0.

Conferência numérica (Python; não faz parte da prova): T(2) = 4 e T(3) = 5, os valores que o texto calcula; e T(n) ≥ 0,5·n lg n para n = 2, …, 2·10⁵, o que é coerente com a prova (que também cobre n = 1, onde a desigualdade é 0 ≤ 1). Confirma ainda que T(n) ≥ n lg n é falsa, com n = 7 como primeiro contraexemplo, que é o motivo de c = 1 falhar. A razão mínima T(n)/(n lg n) ≈ 0,8361 nesse intervalo mostra que a folga entre 1/2 e a melhor constante empírica é grande. Isso é conferência numérica, não faz parte da prova.
