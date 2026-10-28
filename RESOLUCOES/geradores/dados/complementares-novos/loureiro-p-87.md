Resposta. 6n³ ∉ Θ(n²). Por contradição: se existissem c₁ > 0, c₂ > 0 e n₀ com 0 ≤ c₁n² ≤ 6n³ ≤ c₂n² para todo n ≥ n₀, então, tomando n* = max(⌈n₀⌉, ⌊c₂/6⌋ + 1), teríamos n* ≥ n₀ e n* > c₂/6, o que dá 6(n*)³ > c₂(n*)², violando a cota superior. Logo não há constantes que satisfaçam a definição. Quem falha é só a cota superior; a inferior vale (por exemplo c₁ = 6, n₀ = 1).

INTERPRETAÇÃO DO ENUNCIADO:

A escrita "6n³ ≠ Θ(n²)" usa o abuso de notação do material (f(n) = Θ(g(n)) significa f pertence ao conjunto Θ(g(n))); portanto "≠" quer dizer "não pertence": 6n³ ∉ Θ(n²). Leituras possíveis: (i) não pertencimento ao conjunto Θ(n²) definido no slide da p. 84; (ii) desigualdade literal entre uma função e um conjunto, que seria trivial e sem conteúdo. Resolvo (i), que é a única que pede "a definição formal de Θ". As funções são f(n) = 6n³ e g(n) = n², com n natural (o conjunto do slide é de funções f : ℕ → ℝ⁺).

PASSO 1 — A DEFINIÇÃO E SUA NEGAÇÃO:

Pelo slide, f(n) = Θ(g(n)) se e só se
    ∃ c₁ > 0, ∃ c₂ > 0, ∃ n₀ tais que ∀ n ≥ n₀: 0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n).
A negação é: para todos c₁ > 0, c₂ > 0 e n₀, existe n ≥ n₀ em que alguma das desigualdades 0 ≤ c₁g(n), c₁g(n) ≤ f(n), f(n) ≤ c₂g(n) falha. Basta mostrar que, quaisquer que sejam c₂ > 0 e n₀, existe n ≥ n₀ (natural) com f(n) > c₂g(n); isso já nega a definição para todo c₁ também, pois c₁ não interfere na desigualdade que falha.

PASSO 2 — SUPOSIÇÃO (PARA CONTRADIÇÃO):

Suponha que existam constantes c₁ > 0, c₂ > 0 e n₀ tais que, para todo natural n ≥ n₀,
    0 ≤ c₁n² ≤ 6n³ ≤ c₂n².      (1)
Em particular, para todo natural n ≥ n₀ vale a cota superior 6n³ ≤ c₂n².

PASSO 3 — O n QUE VIOLA A COTA SUPERIOR (EM FUNÇÃO DE c₂ E n₀):

Defina
    n* = max(⌈n₀⌉, ⌊c₂/6⌋ + 1).
Propriedades de n*:
    (a) n* é natural e n* ≥ ⌈n₀⌉ ≥ n₀, logo (1) deveria valer em n = n*. (Se o material toma n₀ natural, ⌈n₀⌉ = n₀.)
    (b) n* ≥ ⌊c₂/6⌋ + 1 > c₂/6, porque ⌊x⌋ + 1 > x para todo real x. Como c₂ > 0, ⌊c₂/6⌋ ≥ 0, então n* ≥ 1 e, portanto, (n*)² > 0.
Aplicando a cota superior de (1) em n = n*:
    6(n*)³ ≤ c₂(n*)².
Dividindo os dois lados por (n*)² > 0 (o sentido da desigualdade se mantém):
    6n* ≤ c₂, isto é, n* ≤ c₂/6,
o que contradiz (b), n* > c₂/6. Diretamente: 6(n*)³ = 6n*·(n*)² > 6·(c₂/6)·(n*)² = c₂(n*)², a cota superior é violada em n*.

PASSO 4 — CONCLUSÃO:

A suposição (1) é falsa para quaisquer c₁ > 0, c₂ > 0 e n₀: sempre há o natural n* = max(⌈n₀⌉, ⌊c₂/6⌋ + 1) ≥ n₀ com 6(n*)³ > c₂(n*)². Logo não existem constantes como exige a definição, e 6n³ ∉ Θ(n²), ou, na notação do slide, 6n³ ≠ Θ(n²). ∎

OBSERVAÇÃO — SÓ A COTA SUPERIOR FALHA:

A parte inferior de (1) é satisfazível: com c₁ = 6 e n₀ = 1, para todo n ≥ 1 vale 0 ≤ 6n² ≤ 6n³, pois n³ ≥ n² quando n ≥ 1; em n = n₀ = 1 exatamente: 0 ≤ 6 ≤ 6, verdadeiro. Ou seja, 6n³ = Ω(n²), e é apenas o O(n²) que não vale. Por isso a contradição foi construída sobre a cota superior, e o n* depende só de c₂ e n₀, não de c₁.

CONFERÊNCIA DE FRONTEIRA (n EXATAMENTE NO LIMIAR):

O "+1" em ⌊c₂/6⌋ + 1 é necessário: com c₂ = 6 e n = c₂/6 = 1, vale 6·1³ = 6 ≤ 6·1² = 6, sem violação; já n* = ⌊6/6⌋ + 1 = 2 dá 6·8 = 48 > 6·4 = 24, violação. Com c₂ = 12: n* = 3 (para n₀ ≤ 3), 6·27 = 162 > 12·9 = 108.

Conferência numérica (Python; não faz parte da prova): confere a fórmula n* = max(⌈n₀⌉, ⌊c₂/6⌋ + 1) nos três casos testados (com n₀ pequeno): c₂ = 1 dá n* = ⌊1/6⌋ + 1 = 1, e 6·1 = 6 > 1·1 = 1; c₂ = 10 dá n* = ⌊10/6⌋ + 1 = 2, e 6·8 = 48 > 10·4 = 40; c₂ = 1000 dá n* = ⌊1000/6⌋ + 1 = 167, e 6·167 = 1002 > 1000, isto é, 6·167³ > 1000·167². Nos três valores de n a cota superior é violada. As contas numéricas apenas ilustram; a prova é o Passo 3, que vale para todo c₂ > 0 e todo n₀.
