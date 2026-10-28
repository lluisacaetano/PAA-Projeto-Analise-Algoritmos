Resposta. (1) 100n² = O(n²) é VERDADEIRA (c = 100, n0 = 1). (2) ½n² − 3n = O(n²) é VERDADEIRA (c = ½, n0 = 6; nenhum n0 ≤ 5 serve, porque a definição exige 0 ≤ f(n) e f(n) < 0 para 1 ≤ n ≤ 5 — entre os naturais, 6 é o menor n0). (3) 3n + 20 = O(n²) é VERDADEIRA (c = 23, n0 = 1). (4) 6n³ = O(n²) é FALSA: para quaisquer c > 0 e n0 > 0, o natural n = máx(⌈n0⌉, ⌊c/6⌋ + 1) satisfaz n ≥ n0 e 6n³ > c·n². (5) 720 = O(1) é VERDADEIRA (c = 720, n0 = 1).

INTERPRETAÇÃO.
Leituras possíveis de "f(n) = O(g(n))": (i) como abuso de notação para f(n) ∈ O(g(n)), o conjunto definido no slide 4 do material; (ii) como igualdade literal entre uma função e um conjunto, que não faz sentido. Resolvo a leitura (i), que é a convenção do próprio material ("denotamos por O(g(n)) o conjunto de funções"). O enunciado pede "utilizando a definição", então para cada item verdadeiro exibo constantes numéricas c e n0 e confiro 0 ≤ f(n) ≤ c·g(n) para todo n ≥ n0, inclusive em n = n0 exatamente; para o item falso nego a definição. Tomo n natural (n ≥ 1), domínio usual de tamanho de entrada; os argumentos abaixo valem também para n real nos intervalos indicados.

A definição, com a ordem dos quantificadores explícita: f(n) ∈ O(g(n)) se e somente se existem c > 0 e n0 > 0 tais que, para todo n ≥ n0, 0 ≤ f(n) ≤ c·g(n). Sua negação: para todo c > 0 e todo n0 > 0 existe n ≥ n0 com f(n) < 0 ou f(n) > c·g(n). As constantes c e n0 escolhidas abaixo são números fixos, que não dependem de n.

ITEM 1. 100n² = O(n²): VERDADEIRA.
Testemunhas: c = 100, n0 = 1.
Para todo n ≥ 1: f(n) = 100n² ≥ 0, porque n² > 0; e f(n) = 100n² = 100·n² = c·g(n), logo f(n) ≤ c·g(n) (vale com igualdade).
Conferência em n = n0 = 1: 0 ≤ 100·1² = 100 ≤ 100·1² = 100. Verdadeiro.

ITEM 2. ½n² − 3n = O(n²): VERDADEIRA.
Testemunhas: c = ½, n0 = 6.
Desigualdade da esquerda: f(n) = ½n² − 3n = ½n(n − 6). Para n ≥ 6 os dois fatores n e n − 6 são ≥ 0, logo f(n) ≥ 0.
Desigualdade da direita: para n ≥ 6 (na verdade para todo n ≥ 0), 3n ≥ 0, logo f(n) = ½n² − 3n ≤ ½n² = c·g(n).
Conferência em n = n0 = 6: f(6) = ½·36 − 18 = 18 − 18 = 0, e c·g(6) = ½·36 = 18. Logo 0 ≤ 0 ≤ 18. Verdadeiro.
Por que nenhum n0 ≤ 5 serve (e 6 é o menor n0 natural): a definição do material exige 0 ≤ f(n). Para 1 ≤ n ≤ 5, f(n) = ½n(n − 6) < 0 (n > 0 e n − 6 < 0); por exemplo f(1) = −2,5 e f(5) = 12,5 − 15 = −2,5. Assim nenhum n0 ≤ 5 serve, qualquer que seja c (inclusive com n0 não inteiro: qualquer n0 ≤ 5 deixa n = 5 ≥ n0 com f(5) < 0). Com n0 = 6 a cota inferior vale.
(Qualquer c ≥ ½ também serviria com n0 = 6, pois ½n² ≤ c·n². Escolhi o menor desses.)

ITEM 3. 3n + 20 = O(n²): VERDADEIRA.
Testemunhas: c = 23, n0 = 1.
Para todo n ≥ 1: f(n) = 3n + 20 > 0. Além disso, n ≥ 1 implica n ≤ n² (multiplicando n ≥ 1 por n > 0) e 1 ≤ n². Então 3n + 20 ≤ 3n² + 20n² = 23n² = c·g(n).
Conferência em n = n0 = 1: 0 ≤ 3·1 + 20 = 23 ≤ 23·1² = 23. Verdadeiro (com igualdade à direita).

ITEM 4. 6n³ = O(n²): FALSA.
Negação da definição: devo mostrar que, para todo c > 0 e todo n0 > 0, existe n ≥ n0 com 6n³ > c·n² (a outra metade, f(n) ≥ 0, sempre vale, então a violação tem de ser na cota superior).
Sejam c > 0 e n0 > 0 arbitrários. Tome o natural
    n = máx(⌈n0⌉, ⌊c/6⌋ + 1).
Então n ≥ ⌈n0⌉ ≥ n0, e n ≥ ⌊c/6⌋ + 1 > c/6 (pois ⌊x⌋ + 1 > x para todo real x). De n > c/6 vem 6n > c, e multiplicando por n² > 0 (n ≥ 1): 6n³ = 6n·n² > c·n². Logo a desigualdade f(n) ≤ c·g(n) falha nesse n ≥ n0. Como c e n0 eram arbitrários, não existem constantes que satisfaçam a definição, e 6n³ ∉ O(n²).
Exemplo numérico do argumento: c = 1000, n0 = 1 dá n = máx(1, ⌊166,67⌋ + 1) = 167, e 6·167³ = 6·167·167² = 1002·167² > 1000·167².

ITEM 5. 720 = O(1): VERDADEIRA.
Aqui f(n) = 720 e g(n) = 1 para todo n (funções constantes).
Testemunhas: c = 720, n0 = 1.
Para todo n ≥ 1: 0 ≤ 720 ≤ 720·1 = c·g(n) (igualdade à direita).
Conferência em n = n0 = 1: 0 ≤ 720 ≤ 720. Verdadeiro.
(Também vale com qualquer c ≥ 720; o n0 é irrelevante porque nada depende de n, e n0 = 1 cumpre a exigência de ser positivo.)

OBSERVAÇÃO SOBRE O ALCANCE DAS AFIRMAÇÕES.
As afirmações acima são sobre funções de n, não sobre algoritmos; não há pior ou melhor caso envolvido. Cada desigualdade vale para todo n ≥ n0 indicado, e em nenhum item c ou n0 depende de n.

Conferência numérica (Python; não faz parte da prova): as testemunhas dos itens verdadeiros em todo n de n0 até 20000 — 100n² ≤ 100n² (item 1), 0 ≤ ½n² − 3n ≤ ½n² com falha exatamente em n = 1, …, 5, o que justifica n0 = 6 entre os naturais (item 2), 3n + 20 ≤ 23n² (item 3) e 720 ≤ 720 (item 5) — e, no item 4, que 6n³ ≤ c·n² exige n ≤ c/6, com c = 1000 falhando em n = 167, o mesmo n que a fórmula máx(⌈n0⌉, ⌊c/6⌋ + 1) produz com n0 = 1.
