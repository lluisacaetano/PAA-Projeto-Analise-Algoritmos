Resposta. (1) 100n² = Ω(n²) é VERDADEIRA (c = 100, n0 = 1). (2) (1/2)n² − 3n = Ω(n²) é VERDADEIRA (c = 1/4, n0 = 12). (3) 3n² + 20 = Ω(n) é VERDADEIRA (c = 3, n0 = 1). (4) 6n = Ω(n²) é FALSA: para quaisquer c > 0 e n0 > 0, o natural n = ⌈máx(n0, 6/c + 1)⌉ satisfaz n ≥ n0 e c·n² > 6n. (5) 720 = Ω(1) é VERDADEIRA (c = 720, n0 = 1).

LEITURA DO ENUNCIADO.
Leituras possíveis: (i) "f(n) = Ω(g(n))" como abuso de notação para "f(n) ∈ Ω(g(n))", conjunto definido no material (p. 10); (ii) "=" como igualdade de conjuntos, o que não faz sentido, pois o lado esquerdo é uma função. Adoto (i), que é a convenção do próprio material ("denotamos por Ω(g(n)) o conjunto de funções"). O enunciado pede para responder "utilizando a definição", então cada item usa exatamente a definição dada:

    f(n) ∈ Ω(g(n)) ⟺ existem constantes positivas c e n0 tais que 0 ≤ c·g(n) ≤ f(n) para todo n ≥ n0.

A ordem dos quantificadores é ∃c ∃n0 ∀n ≥ n0: c e n0 são fixados antes e não podem depender de n. Para VERDADEIRO exibo c e n0 numéricos e provo a desigualdade para todo n ≥ n0, conferindo em n = n0. Para FALSO nego a definição: para todo c > 0 e todo n0 > 0 existe n ≥ n0 com c·g(n) > f(n) (a parte 0 ≤ c·g(n) vale sempre aqui, já que g(n) ≥ 0, logo a única desigualdade que pode falhar é c·g(n) ≤ f(n)). Os itens tratam de funções de n (n natural, n ≥ 1), não de algoritmos, de modo que não há distinção de pior ou melhor caso a fazer.

ITEM 1. 100n² = Ω(n²): VERDADEIRA.
Testemunhas: c = 100, n0 = 1. Para todo n ≥ 1: c·g(n) = 100n² ≥ 0 e 100n² ≤ 100n² (igualdade). Logo 0 ≤ 100n² ≤ 100n² para todo n ≥ 1.
Conferência em n = n0 = 1: 0 ≤ 100·1 = 100 ≤ 100. Vale.

ITEM 2. (1/2)n² − 3n = Ω(n²): VERDADEIRA.
Testemunhas: c = 1/4, n0 = 12.
Desigualdade da direita: (1/4)n² ≤ (1/2)n² − 3n ⟺ 3n ≤ (1/2)n² − (1/4)n² = (1/4)n² ⟺ 12n ≤ n² ⟺ 12 ≤ n (dividindo por n > 0). Logo vale para todo n ≥ 12.
Desigualdade da esquerda: 0 ≤ (1/4)n² vale para todo n.
Logo 0 ≤ (1/4)n² ≤ (1/2)n² − 3n para todo n ≥ 12.
Conferência em n = n0 = 12: c·g(12) = 144/4 = 36; f(12) = 144/2 − 36 = 72 − 36 = 36. Então 0 ≤ 36 ≤ 36. Vale (com igualdade).
Observação: com c = 1/4 o n0 = 12 é o menor possível, pois para 1 ≤ n ≤ 11 tem-se n² < 12n, isto é, (1/4)n² > (1/2)n² − 3n. Note também que f(n) é negativa para 1 ≤ n ≤ 5 e nula em n = 6; isso não atrapalha, porque a definição só exige a desigualdade a partir de n0.

ITEM 3. 3n² + 20 = Ω(n): VERDADEIRA.
Testemunhas: c = 3, n0 = 1. Para todo n ≥ 1 vale n ≤ n² (multiplicando 1 ≤ n por n > 0), logo 3n ≤ 3n² < 3n² + 20. E 0 ≤ 3n. Portanto 0 ≤ 3n ≤ 3n² + 20 para todo n ≥ 1.
Conferência em n = n0 = 1: 0 ≤ 3 ≤ 3 + 20 = 23. Vale.

ITEM 4. 6n = Ω(n²): FALSA.
Negação da definição: para todo c > 0 e todo n0 > 0 existe n ≥ n0 com c·n² > 6n.
Sejam c > 0 e n0 > 0 arbitrários. Tome n = ⌈máx(n0, 6/c + 1)⌉, que é natural. Então:
    n ≥ máx(n0, 6/c + 1) ≥ n0, logo n ≥ n0;
    n ≥ 6/c + 1 > 6/c, logo c·n > 6 (multiplicando por c > 0);
    como n > 0, multiplicando c·n > 6 por n: c·n² > 6n.
Assim a desigualdade c·n² ≤ 6n falha em um n ≥ n0. Como c e n0 eram arbitrários, não existem constantes positivas c e n0 que satisfaçam a definição, e 6n ∉ Ω(n²).
Exemplo concreto (não é a prova, só ilustra): c = 0,01 e n0 = 1 dão n = ⌈máx(1, 601)⌉ = 601, e 0,01·601² = 3612,01 > 3606 = 6·601.

ITEM 5. 720 = Ω(1): VERDADEIRA.
Aqui f(n) = 720 e g(n) = 1 para todo n. Testemunhas: c = 720, n0 = 1. Para todo n ≥ 1: 0 ≤ 720·1 = 720 ≤ 720. (Qualquer c com 0 < c ≤ 720 também serve, por exemplo c = 1.)
Conferência em n = n0 = 1: 0 ≤ 720 ≤ 720. Vale.

Conferência numérica (Python; não faz parte da prova): no item 2, (1/4)n² ≤ (1/2)n² − 3n vale de 12 a 20000 e falha exatamente em n = 1, …, 11, o que bate com n0 = 12 ser o menor possível para c = 1/4 entre os naturais; no item 3, 3n ≤ 3n² + 20 vale de n0 = 1 a 20000 sem falhas; no item 4, para c = 0,01 a desigualdade c·n² ≤ 6n falha em n = 601, exatamente o n = ⌈6/c + 1⌉ = 601 dado pela fórmula do item 4. Os itens 1 e 5 são as igualdades 100n² = 100n² e 720 = 720.
