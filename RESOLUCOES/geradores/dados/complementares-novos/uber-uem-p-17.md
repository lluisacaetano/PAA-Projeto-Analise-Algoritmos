Resposta. (1) 100n² = Θ(n²) é VERDADEIRA: c₁ = c₂ = 100, n₀ = 1. (2) (1/2)n² − 3n = Θ(n²) é VERDADEIRA: c₁ = 1/4, c₂ = 1/2, n₀ = 12. (3) 3n² + 20 = Θ(n) é FALSA: falha a cota superior f(n) ≤ c₂·n; para quaisquer c₁, c₂, n₀ positivos, n = max(⌈n₀⌉, ⌊c₂/3⌋ + 1) a viola. (4) 6n = Θ(n²) é FALSA: falha a cota inferior c₁·n² ≤ f(n); para quaisquer c₁, c₂, n₀ positivos, n = max(⌈n₀⌉, ⌊6/c₁⌋ + 1) a viola. (5) 720 = Θ(1) é VERDADEIRA: c₁ = c₂ = 720, n₀ = 1.

INTERPRETAÇÃO.
Leituras possíveis de "f(n) = Θ(g(n))": (i) como igualdade de conjuntos, o que não faz sentido (à esquerda há uma função); (ii) como pertinência f(n) ∈ Θ(g(n)), que é a convenção do material (CLRS, 3ª ed., seção 3.1, adotada no slide 10/33). Resolvo a leitura (ii). O enunciado pede "utilizando a definição na notação Θ", então cada item é decidido diretamente pela definição do slide 10/33, sem usar limites nem o Teorema 3.1 como atalho:

    Θ(g(n)) = {f(n): existem constantes positivas c₁, c₂ e n₀ tais que 0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n) para todo n ≥ n₀}.

A ordem dos quantificadores é ∃c₁ ∃c₂ ∃n₀ ∀n ≥ n₀. O domínio é n natural, n ≥ 1. Não há algoritmo nem entradas: cada f é uma função fixa de n, então não cabe falar em pior ou melhor caso. A negação da definição, usada nos itens falsos, é: para TODAS as constantes positivas c₁, c₂, n₀ existe n ≥ n₀ tal que alguma das desigualdades 0 ≤ c₁g(n), c₁g(n) ≤ f(n), f(n) ≤ c₂g(n) é falsa. Em cada item falso exibo esse n em função das constantes e digo qual desigualdade falha.

ITEM 1 — 100n² = Θ(n²): VERDADEIRA.
Testemunhas: c₁ = 100, c₂ = 100, n₀ = 1. Para todo n ≥ 1: 0 ≤ 100n² (n² > 0), 100n² ≤ 100n² e 100n² ≤ 100n² (igualdades). Conferência em n = n₀ = 1: 0 ≤ 100·1 = 100 ≤ 100 ≤ 100. Vale.

ITEM 2 — (1/2)n² − 3n = Θ(n²): VERDADEIRA.
Seja f(n) = n²/2 − 3n. Testemunhas: c₁ = 1/4, c₂ = 1/2, n₀ = 12.
Cota inferior: para n > 0, n²/4 ≤ n²/2 − 3n ⟺ 3n ≤ n²/4 ⟺ 12 ≤ n. Logo vale para todo n ≥ 12 (e falha para 1 ≤ n ≤ 11, por isso n₀ = 12 e não menor).
Cota superior: n²/2 − 3n ≤ n²/2 ⟺ 0 ≤ 3n, verdadeiro para todo n ≥ 1.
Não negatividade: c₁n² = n²/4 ≥ 0.
Conferência em n = n₀ = 12: c₁g(12) = 144/4 = 36; f(12) = 72 − 36 = 36; c₂g(12) = 72. Então 0 ≤ 36 ≤ 36 ≤ 72. Vale (com igualdade na cota inferior).

ITEM 3 — 3n² + 20 = Θ(n): FALSA. A desigualdade que falha é a SUPERIOR, f(n) ≤ c₂·n.
Sejam c₁, c₂, n₀ constantes positivas arbitrárias. Tome n = max(⌈n₀⌉, ⌊c₂/3⌋ + 1). Então n ≥ n₀ e n > c₂/3 (porque ⌊x⌋ + 1 > x), isto é, 3n > c₂. Multiplicando por n > 0: 3n² > c₂n, e portanto f(n) = 3n² + 20 > 3n² > c₂n. Assim, para quaisquer c₁, c₂, n₀ há n ≥ n₀ com f(n) > c₂g(n); a definição é negada e 3n² + 20 ∉ Θ(n).
Exemplo numérico: c₂ = 300, n₀ = 1 dá n = max(1, 101) = 101: f(101) = 30623 > 300·101 = 30300. (A cota inferior, por outro lado, vale: com c₁ = 3, 3n ≤ 3n² + 20 para todo n ≥ 1; a função é Ω(n), mas não O(n), e por isso não é Θ(n).)

ITEM 4 — 6n = Θ(n²): FALSA. A desigualdade que falha é a INFERIOR, c₁·n² ≤ f(n).
Sejam c₁, c₂, n₀ constantes positivas arbitrárias. Tome n = max(⌈n₀⌉, ⌊6/c₁⌋ + 1). Então n ≥ n₀ e n > 6/c₁, isto é, c₁n > 6. Multiplicando por n > 0: c₁n² > 6n = f(n). Assim, para quaisquer c₁, c₂, n₀ há n ≥ n₀ com c₁g(n) > f(n); a definição é negada e 6n ∉ Θ(n²).
Exemplo numérico: c₁ = 0,01, n₀ = 1 dá n = max(1, 601) = 601: c₁n² = 0,01·361201 = 3612,01 > 6·601 = 3606. (A cota superior, por outro lado, vale: 6n ≤ 6n² para n ≥ 1; a função é O(n²), mas não Ω(n²).)

ITEM 5 — 720 = Θ(1): VERDADEIRA.
Aqui f(n) = 720 e g(n) = 1 são funções constantes de n. Testemunhas: c₁ = 720, c₂ = 720, n₀ = 1. Para todo n ≥ 1: 0 ≤ 720·1 ≤ 720 ≤ 720·1 (igualdades). Conferência em n = n₀ = 1: 0 ≤ 720 ≤ 720 ≤ 720. Vale. (Qualquer c₁ ≤ 720 ≤ c₂ positivos também servem.)

Conferência numérica (Python; não faz parte da prova): item 1, 100n² ≤ 100n² em todo n ≥ 1; item 2, n²/4 ≤ n²/2 − 3n ≤ n²/2 vale de 12 a 20000 e falha exatamente em n = 1, …, 11, o que justifica n₀ = 12 entre os naturais com c₁ = 1/4; item 5, 720 ≤ 720; item 3, 3n ≤ 3n² + 20 em todo n ≥ 1 (cota inferior) e, com c₂ = 300, a cota superior falha já em n = 100, onde 30020 > 30000, e o n = 101 da fórmula também falha; item 4, com c₁ = 0,01 a cota inferior falha em n = 601, o mesmo n da fórmula.
