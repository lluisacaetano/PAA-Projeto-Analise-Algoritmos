Resposta. Para x, y > 1 fixos, a mudança de base dá log_y n = (log_y x) · log_x n para todo n ≥ 1. Logo f(n) = log_y n é O(log_x n) com as testemunhas c = log_y x = 1/log_x y (real, positiva porque x, y > 1; depende só de x e y, nunca de n) e n0 = 1. Em n = n0 = 1 os dois lados valem 0 e 0 ≤ 0. A recíproca também vale, com c' = log_x y: log_x n é O(log_y n). Por isso log_y n ∈ Θ(log_x n), com c1 = c2 = log_y x e n0 = 1, e a base do logaritmo não muda a classe assintótica. A prova usa x, y > 1 (que o enunciado fixa) para ter c > 0 e log_x n ≥ 0; a hipótese não pode ser simplesmente apagada: com base 1 o logaritmo não está definido, e com x = 1/2, y = 2 tem-se log_2 n NÃO é O(log_(1/2) n) (PASSO 5).

INTERPRETAÇÃO.
Há duas leituras possíveis do enunciado. (A) A afirmação principal: para quaisquer bases fixas x, y > 1, log_y n ∈ O(log_x n), pela definição da p. 7 do Campello: existem c real positiva e n0 inteiro positivo tais que f(n) ≤ c·g(n) para todo n ≥ n0. (B) A paráfrase "ou seja, a base logarítmica não afeta a complexidade assintótica", que só fica justificada se valer também a recíproca, ou seja, Θ. Resolvo (A) com testemunhas explícitas e depois acrescento (B). Em (A), x e y são constantes fixadas antes. A ordem é: para cada par fixo (x, y), ∃c ∃n0 ∀n ≥ n0. Por isso c pode depender de x e de y, mas não de n. O domínio é n inteiro, n ≥ 1, onde log n está definido.

PASSO 1 — MUDANÇA DE BASE, A PARTIR DA DEFINIÇÃO DE LOGARITMO:
Para uma base b > 0 com b ≠ 1 e um real z > 0, log_b z é o único real s tal que b^s = z. Esse s é único porque s ↦ b^s é estritamente monótona: crescente se b > 1, decrescente se 0 < b < 1.
Fixe n ≥ 1 e escreva t = log_x n, isto é, n = x^t. Escreva também s = log_y x, isto é, x = y^s. Então
    n = x^t = (y^s)^t = y^(s·t),
e pela unicidade log_y n = s·t. Ou seja,
    log_y n = (log_y x) · log_x n    para todo n ≥ 1.          (1)
Fazendo n = y em (1): 1 = log_y y = (log_y x)(log_x y). Logo log_y x = 1/log_x y, e as duas formas de escrever c coincidem.

PASSO 2 — O SINAL DA CONSTANTE:
Como y > 1, a função s ↦ y^s é estritamente crescente e y^0 = 1. Como x > 1 = y^0, o expoente s = log_y x satisfaz s > 0. Então c = log_y x é um real positivo, como a definição exige. Pela mesma razão (x > 1 e y > 1), log_x y > 0.

PASSO 3 — AS TESTEMUNHAS PARA O:
Tome
    c = log_y x = 1/log_x y = (ln x)/(ln y)   e   n0 = 1.
Por (1), para todo n ≥ n0 = 1,
    f(n) = log_y n = c · log_x n ≤ c · log_x n.
A desigualdade é na verdade uma igualdade. Logo log_y n ∈ O(log_x n).
Conferência em n = n0 = 1: o lado esquerdo é log_y 1 = 0, o lado direito é c·log_x 1 = c·0 = 0, e 0 ≤ 0 vale. Ao contrário do exemplo da p. 9 (3 log n + 5), aqui não há termo aditivo, então não é preciso fugir de n = 1: n0 = 1 basta. Qualquer c maior e qualquer n0 ≥ 1 também servem, porque log_x n ≥ 0 para n ≥ 1.
Exemplo numérico, com x = 2 e y = 10: c = log_10 2 ≈ 0,30103 e n0 = 1. Em n = 1: 0 ≤ 0. Em n = 8: log_10 8 ≈ 0,90309 e c·log_2 8 = 0,30103·3 ≈ 0,90309, igualdade como (1) prevê. Com x = 10 e y = 2, c = log_2 10 ≈ 3,32.

PASSO 4 — A RECÍPROCA E O Θ:
O mesmo argumento com os papéis de x e y trocados também vale, já que a hipótese é simétrica (x, y > 1). Ele dá log_x n = (log_x y) · log_y n, com c' = log_x y > 0 e n0 = 1. Logo log_x n ∈ O(log_y n): a base nova também não "cresce mais" que a antiga.
Juntando as duas direções na definição de Θ usada na disciplina (CLRS, 3ª ed.: existem c1, c2 > 0 e n0 tais que 0 ≤ c1·g(n) ≤ f(n) ≤ c2·g(n) para todo n ≥ n0), com f(n) = log_y n e g(n) = log_x n, tome
    c1 = c2 = log_y x   e   n0 = 1.
Para n ≥ 1 vale log_x n ≥ 0, então 0 ≤ c1·log_x n, e por (1) c1·log_x n = log_y n = c2·log_x n. Em n = 1, tudo vale 0. Logo log_y n ∈ Θ(log_x n). É isso que justifica a frase "a base logarítmica não afeta a complexidade assintótica": funções não negativas (para n ≥ n0) que diferem por um fator constante positivo estão na mesma classe Θ. Por isso se escreve O(log n) sem base. Só a direção O, sozinha, não bastaria para essa frase: n ∈ O(n²), e mesmo assim n e n² têm complexidades diferentes.

PASSO 5 — ONDE A HIPÓTESE x, y > 1 ENTRA:
O enunciado fixa x, y > 1, e a prova usa isso em dois pontos: c = log_y x > 0 (PASSO 2), que a definição exige, e log_x n ≥ 0 para n ≥ 1 (PASSO 4), que dá o 0 ≤ c1·g(n) do Θ. Não analiso aqui todas as bases fora de (1, ∞), porque o veredito delas depende de qual definição se usa (a do Campello não exige 0 ≤ f; a do CLRS exige) e porque logaritmo negativo não serve como custo de algoritmo. Dois fatos bastam para ver que a hipótese não pode ser simplesmente apagada:
(i) Base 1: 1^s = 1 para todo s, então log_1 n não está definido (para n ≥ 2 não existe s com 1^s = n; para n = 1 todo s serve).
(ii) Contraexemplo concreto, pela definição de O do material: y = 2 e x = 1/2. Então log_x n = −log_2 n. Afirmação: log_2 n NÃO é O(log_(1/2) n). Negação da definição: para toda c > 0 e todo n0 ≥ 1, existe n ≥ n0 com log_2 n > c·log_(1/2) n. Tome n = max(n0, 2). Então log_2 n ≥ 1 > 0 e c·log_(1/2) n = −c·log_2 n < 0. A desigualdade f(n) ≤ c·g(n) falha nesse n, qualquer que seja a escolha de c e n0.

Conferência numérica (Python; não faz parte da prova): para (x, y) = (2, 10), (10, 2), (2, 3), (3, 2) e (1,5; 100), que log_y n ≤ c·log_x n com c = 1/log_x y vale para todo n de 1 a 10⁴, e que em n = 1 os dois lados valem 0. Os valores de c calculados batem com c = log_y x: 0,3010 = log_10 2, 3,3219 = log_2 10, 0,6309 = log_3 2, 1,5850 = log_2 3 e 0,0880 = log_100 1,5. Isso é coerente com a igualdade (1), que torna a desigualdade exata em todo n, e com a escolha n0 = 1.
