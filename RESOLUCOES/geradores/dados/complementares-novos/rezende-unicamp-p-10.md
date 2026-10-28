Resposta. T(n) = 2T(⌊n/3⌋) + n pertence a O(n). Como o texto não dá o caso base, adotamos: a recorrência vale para todo n ≥ 1 e T(0) = d, com d ≥ 0 uma constante real (custo de tempo não é negativo; no caso usual, d = 0, que dá T(1) = 1, T(2) = 2). Testemunhas: c = máx(3, 2d + 1) e n0 = 1; com d = 0, c = 3 e n0 = 1. Prova por indução forte em n (método da substituição): T(n) ≤ c·n para todo n ≥ 1. No passo, para n ≥ 3, a hipótese aplicada a ⌊n/3⌋ (que é ≥ 1 e < n) dá T(n) ≤ 2c⌊n/3⌋ + n ≤ (2c/3)n + n ≤ c·n, e a última desigualdade vale exatamente porque c ≥ 3: a constante sai do passo igual à que entrou.

INTERPRETAÇÃO.
O enunciado ("Convidamos o leitor a provar que a solução dessa relação de recorrência pertence a O(n)") admite duas leituras: (i) provar a cota superior O(n) formalmente, com testemunhas; (ii) apenas justificar pela árvore da figura 3 que a soma dos níveis é limitada. A leitura (i) é a que a disciplina exige (testemunhas numéricas), e é a que resolvemos; a árvore aparece só como motivação para a escolha de c. O texto também não fixa o caso base nem a partir de que n a recorrência vale; por isso o declaramos explicitamente e mostramos, no fim, que outra escolha razoável só muda o valor numérico de c, não a conclusão. O pedido é só O(n) (cota superior); não é pedido Ω nem Θ.

CASO BASE ADOTADO.
T está definida nos naturais n ≥ 0, com T(0) = d (constante d ≥ 0, não depende de n) e T(n) = 2T(⌊n/3⌋) + n para todo n ≥ 1. Note que ⌊n/3⌋ < n para todo n ≥ 1, então a recorrência define T(n) para todo n a partir de T(0). Em particular, como ⌊1/3⌋ = ⌊2/3⌋ = 0:
    T(1) = 2d + 1,
    T(2) = 2d + 2.
A afirmação "T(n) ∈ O(n)" é sobre n ≥ n0 = 1; o ponto n = 0 fica de fora (se d > 0, T(0) = d > c·0, e não há nada a provar ali, pois a definição só exige n ≥ n0).

DE ONDE VEM O 3 (MOTIVAÇÃO, NÃO É PROVA).
Pela árvore, o nível i tem 2^i nós, cada um com custo no máximo n/3^i, logo o nível custa no máximo (2/3)^i·n. Somando a série geométrica, n·Σ_{i≥0} (2/3)^i = n·1/(1 − 2/3) = 3n. Isso sugere c = 3. Essa conta ignora os pisos e o caso base; a prova abaixo é a que vale.

AFIRMAÇÃO A PROVAR.
Seja c = máx(3, 2d + 1). Para todo n ≥ 1, P(n): T(n) ≤ c·n.
Ordem dos quantificadores: existe c (= máx(3, 2d + 1), número fixo, que depende só da constante d do caso base e não de n), existe n0 = 1, tal que para todo n ≥ n0 vale T(n) ≤ c·n. Junto com 0 ≤ T(n), que vale para todo n porque d ≥ 0 (indução: T(n) = 2T(⌊n/3⌋) + n com T(⌊n/3⌋) ≥ 0), isso é exatamente a definição de T(n) ∈ O(n). Com d = 0: c = 3, n0 = 1.

BASE (n = 1 e n = 2).
São os valores de n ≥ 1 para os quais ⌊n/3⌋ = 0, isto é, em que a recorrência cai em T(0), onde a hipótese P não está disponível (P só fala de n ≥ 1). Por isso são tratados à parte.
    n = 1 (que é n0 exatamente): T(1) = 2d + 1 ≤ c = c·1, porque c ≥ 2d + 1. Vale.
    n = 2: T(2) = 2d + 2. Como c ≥ 2d + 1, temos 2c ≥ 4d + 2. Precisamos 2d + 2 ≤ 2c. Como d ≥ 0: 2d + 2 ≤ 4d + 2 ≤ 2c. Vale.
Com d = 0: T(1) = 1 ≤ 3 e T(2) = 2 ≤ 6.

HIPÓTESE DE INDUÇÃO (FORTE).
Seja n ≥ 3 e suponha P(k) verdadeira para todo k com 1 ≤ k < n, isto é, T(k) ≤ c·k para esses k, com o MESMO c.

PASSO (n ≥ 3).
Como n ≥ 3, k = ⌊n/3⌋ satisfaz k ≥ 1; e k ≤ n/3 < n. Logo a hipótese se aplica a k: T(⌊n/3⌋) ≤ c·⌊n/3⌋. Então
    T(n) = 2T(⌊n/3⌋) + n
         ≤ 2c·⌊n/3⌋ + n          (hipótese em k = ⌊n/3⌋)
         ≤ 2c·(n/3) + n          (⌊n/3⌋ ≤ n/3 e c > 0)
         = c·n − (c/3)·n + n
         = c·n − (c/3 − 1)·n
         ≤ c·n,
pois c ≥ 3 dá c/3 − 1 ≥ 0 e n > 0. Isso é P(n).
A constante não cresce: a hipótese foi usada com c e a conclusão saiu com o mesmo c, sem nenhuma sobra positiva do tipo "c·n + n". O termo extra n foi absorvido pela folga (c/3)·n, que é ≥ n justamente porque c ≥ 3. Com c < 3 o passo não fecharia por esse argumento (a folga (c/3)·n seria menor que n).
Fencepost do passo, n = 3 exatamente: k = ⌊3/3⌋ = 1, e T(3) = 2T(1) + 3 = 2(2d + 1) + 3 ≤ 2c + 3 ≤ 2c + c = 3c, usando T(1) ≤ c (base) e 3 ≤ c. Com d = 0: T(3) = 5 ≤ 9.

CONCLUSÃO.
Por indução forte, T(n) ≤ c·n para todo n ≥ 1, com c = máx(3, 2d + 1). Portanto T(n) ∈ O(n), com testemunhas c = máx(3, 2d + 1) e n0 = 1 (c = 3, n0 = 1 no caso T(0) = 0). Note que T(n) não é custo de "pior caso" ou "melhor caso" de nada: é uma função de n bem definida pela recorrência e pelo caso base, e a cota vale para todo n ≥ 1.

SE O CASO BASE FOR OUTRO.
Se, em vez disso, a recorrência valer só para n ≥ 2, com T(0) = d0 ≥ 0 e T(1) = d1 ≥ 0 dados, o mesmo argumento funciona com c = máx(3, d1, d0 + 1) e n0 = 1: a base é n = 1 (T(1) = d1 ≤ c) e n = 2 (T(2) = 2d0 + 2 ≤ 2c porque c ≥ d0 + 1); o passo para n ≥ 3 é idêntico, palavra por palavra. Por exemplo, T(0) = 1, T(1) = 1 dá c = máx(3, 1, 2) = 3. Em qualquer escolha de constantes iniciais não negativas, a conclusão O(n) não muda; muda só o número c. (Com d < 0 a cota T(n) ≤ c·n ainda sai da mesma conta, mas T fica negativo para n pequeno — com d = −10, em 118 valores de n, o último n = 129 — e então n0 = 1 não satisfaz o 0 ≤ T(n) da definição; custo negativo não modela tempo, por isso o excluímos.)

OBSERVAÇÃO (NÃO PEDIDA).
Como d ≥ 0, T(n) ≥ 0 para todo n (indução: T(n) = 2T(⌊n/3⌋) + n com T(⌊n/3⌋) ≥ 0), logo T(n) ≥ n para n ≥ 1, e portanto T(n) ∈ Θ(n) com c1 = 1, c2 = c, n0 = 1. O contraste com o texto do material: lá a = b dá n por nível e Θ(n lg n); aqui a = 2 < b = 3, os níveis decrescem geometricamente e o total é linear.

Conferência numérica (Python; não faz parte da prova): calculei T(n)/n para n = 1 até 2·10^5 com T(0) = 0, T(1) = 1 (o nosso caso d = 0) e obteve máximo 2,9769 < 3, e T(n) ≤ 3n em todo o intervalo, de acordo com c = 3; com T(0) = 1, T(1) = 1 (o caso "SE O CASO BASE FOR OUTRO", c = 3) obteve máximo 2,9827 < 3, também de acordo. Isso só confere a prova num intervalo finito; a prova é a indução acima.
