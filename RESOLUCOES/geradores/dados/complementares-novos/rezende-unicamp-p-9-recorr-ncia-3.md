Resposta. Para n potência de 2 e caso base T(1) = d com d ≥ 0 (por exemplo T(1) = 1), a recorrência T(n) = 2T(n/2) + n satisfaz T(n) ≥ n lg n para toda potência de 2 n ≥ 1, provado pelo método da substituição (indução em k, n = 2ᵏ) com a mesma constante c = 1 na hipótese e na conclusão. Logo T(n) ∈ Ω(n lg n) com testemunhas c = 1 e n₀ = 1. Se o leitor adotar T(1) = d < 0, a conclusão continua valendo: prova-se por substituição a hipótese reforçada T(n) ≥ n lg n + d·n, e daí T(n) ≥ (1/2)·n lg n para n ≥ n₀ = 2^⌈−2d⌉ (testemunhas c = 1/2, n₀ = 2^⌈−2d⌉). Como log_b n = lg n / lg b, o resultado vale para qualquer base b > 1 do "log" do enunciado.

LEITURA DO ENUNCIADO (INTERPRETAÇÃO):
O exercício pede provar que a recorrência (3), T(n) = 2T(n/2) + n com T(1) = ?, pertence a Ω(n log n). Há três pontos em aberto no texto. (i) O caso base não é dado ("T(1) = ?"); a resposta assintótica não deve depender dele, então adoto T(1) = d e trato separadamente d ≥ 0 (caso principal; inclui o natural T(1) = 1) e d < 0 (observação final). (ii) A recorrência escreve n/2 sem piso nem teto, e a Figura 1 (árvore de recorrência) divide n ao meio em todos os níveis; a única leitura em que T(n/2) é sempre um argumento inteiro definido é n = 2ᵏ, k = 0, 1, 2, …. Por isso o domínio desta prova é o conjunto das potências de 2, e a afirmação Ω vale sobre esse domínio; não afirmo nada sobre n que não sejam potências de 2 (estender exigiria saber que T é não decrescente, o que o enunciado não dá). (iii) "log" sem base: uso lg = log₂ e no fim mostro que a base não importa. A pergunta é sobre uma função T definida pela recorrência, não sobre pior/melhor caso de um algoritmo: a afirmação vale para todo n do domínio.

DEFINIÇÃO USADA:
T(n) ∈ Ω(g(n)) se existem constantes c > 0 e n₀ > 0 tais que, para todo n ≥ n₀ (no domínio), 0 ≤ c·g(n) ≤ T(n). Ordem dos quantificadores: ∃c ∃n₀ ∀n ≥ n₀; c e n₀ abaixo são números fixos, que não dependem de n.

PASSO 1 — A AFIRMAÇÃO A PROVAR POR INDUÇÃO (CASO d ≥ 0):
Seja d = T(1) ≥ 0. Para k ≥ 0, seja
    P(k): T(2ᵏ) ≥ 2ᵏ · k,
isto é, T(n) ≥ 1 · n lg n para n = 2ᵏ (pois lg 2ᵏ = k). A constante da substituição é c = 1.

PASSO 2 — BASE (k = 0, n = 1):
T(1) = d ≥ 0 = 1 · 1 · lg 1, pois lg 1 = 0. Logo P(0) vale. (A base é exatamente n = 1; não é preciso nenhuma base extra, porque o passo abaixo só usa o valor em n/2 ≥ 1.)

PASSO 3 — PASSO INDUTIVO (k ≥ 1, n = 2ᵏ ≥ 2):
Hipótese de indução, exatamente como enunciada: P(k − 1), isto é, T(2ᵏ⁻¹) ≥ 2ᵏ⁻¹ · (k − 1), ou seja, T(n/2) ≥ (n/2)·lg(n/2) = (n/2)(lg n − 1).
Como n = 2ᵏ com k ≥ 1, n/2 = 2ᵏ⁻¹ é potência de 2 maior ou igual a 1, e a recorrência se aplica:
    T(n) = 2T(n/2) + n
         ≥ 2 · (n/2)(lg n − 1) + n        (hipótese de indução, multiplicada por 2 > 0)
         = n lg n − n + n
         = n lg n
         = 1 · 2ᵏ · k.
Logo P(k) vale. A constante c = 1 da hipótese reaparece intacta na conclusão (não "cresceu" no meio), e nenhum termo foi descartado: a desigualdade usa só a hipótese.

PASSO 4 — CONCLUSÃO Ω COM TESTEMUNHAS (d ≥ 0):
Por indução, T(n) ≥ n lg n para toda potência de 2 n ≥ 1. Tome c = 1 e n₀ = 1. Para todo n ≥ n₀ potência de 2: 0 ≤ 1 · n lg n (pois n ≥ 1 implica lg n ≥ 0) e 1 · n lg n ≤ T(n) (Passo 3). Conferência em n = n₀ = 1 exatamente: c · 1 · lg 1 = 0 e T(1) = d ≥ 0, então 0 ≤ 0 ≤ d. Em n = 2: 1 · 2 · lg 2 = 2 e T(2) = 2d + 2 ≥ 2. Portanto T(n) ∈ Ω(n lg n) sobre as potências de 2.

PASSO 5 — A BASE DO LOGARITMO NÃO IMPORTA:
Para qualquer base b > 1, log_b n = lg n / lg b, então n lg n = (lg b) · n log_b n. Logo T(n) ≥ (lg b) · n log_b n para n ≥ 1 potência de 2, e T(n) ∈ Ω(n log_b n) com testemunhas c = lg b > 0 e n₀ = 1. Em particular vale para o "log" do enunciado, qualquer que seja a base usada pelo material.

OBSERVAÇÃO — SE O CASO BASE ADOTADO FOR NEGATIVO (d < 0):
A hipótese P(k) acima falha já na base (T(1) = d < 0 = 1 lg 1), então é preciso reforçá-la com um termo de ordem menor, como é usual no método da substituição. Seja
    Q(k): T(2ᵏ) ≥ 2ᵏ · k + d · 2ᵏ, isto é, T(n) ≥ n lg n + d·n para n = 2ᵏ.
Base (k = 0): T(1) = d = 1 · 0 + d · 1, vale com igualdade.
Passo (k ≥ 1): pela hipótese Q(k − 1), T(n/2) ≥ (n/2)(lg n − 1) + d·(n/2); então
    T(n) = 2T(n/2) + n ≥ n(lg n − 1) + d·n + n = n lg n + d·n,
que é Q(k), com as mesmas constantes (1 e d) da hipótese.
Agora, para n potência de 2 com lg n ≥ −2d: d·n ≥ −(1/2)·n lg n (pois −d ≤ (1/2) lg n e n > 0), logo T(n) ≥ n lg n − (1/2) n lg n = (1/2) n lg n. Tome c = 1/2 e n₀ = 2^⌈−2d⌉ (um número fixo que depende só da constante d, não de n). Para n ≥ n₀ potência de 2, lg n ≥ ⌈−2d⌉ ≥ −2d, e como d < 0 temos ⌈−2d⌉ ≥ 1, logo lg n ≥ 1 > 0 e 0 ≤ (1/2) n lg n ≤ T(n). Conferência em n = n₀ exatamente: lg n₀ = ⌈−2d⌉ ≥ −2d, que é a condição usada. Assim T(n) ∈ Ω(n lg n) também neste caso. (Este argumento também cobre d ≥ 0, mas lá a prova mais simples dos Passos 1–4 já basta.)

Conferência numérica (Python; não faz parte da prova): para a recorrência (3) com T(1) = 1 e n = 2ᵏ, a forma fechada T(2ᵏ) = n lg n + n, que é exatamente o caso d = 1 da igualdade T(n) = n lg n + d·n obtida na observação (a desigualdade Q(k) vale ali com igualdade); em particular T(n) ≥ n lg n, coerente com as testemunhas c = 1, n₀ = 1.
