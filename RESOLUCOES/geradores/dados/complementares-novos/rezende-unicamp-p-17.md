Resposta. Na representação por lista de adjacências, a recorrência do texto, T(n) = T(n − 1) + n + (k − 1)(n − 1), tem forma fechada T(n) = T(0) + n(n + 1)/2 + (k − 1)·n(n − 1)/2 = T(0) + (k·n² − (k − 2)·n)/2. Para todo k ≥ 1 e todo n ≥ 2 vale (1/4)·k·n² ≤ T(n) ≤ ((3 + T(0))/4)·k·n², com constantes que não dependem nem de n nem de k; logo T(n) ∈ Θ(k·n²), o que confirma o O(kn²) do texto. Com k constante (k ≥ 1), o algoritmo é QUADRÁTICO em n: T(n) ∈ Θ(n²) (c₁ = k/4, c₂ = (3 + T(0))·k/4, n₀ = 2), não é linear (T ∉ O(n)) e não é exponencial (T ∉ Ω(2ⁿ)). Se k puder crescer com n, a classificação só vale com ressalva: k útil vai no máximo até n − 1 (com k ≥ n o passo para de imediato), e com k = ⌊n/2⌋ o custo da recorrência é Θ(n³) — nem linear, nem quadrático. Em nenhum caso é exponencial: para k arbitrário o custo do modelo T' do Passo 4 (que para quando restam m ≤ k vértices) é O(n³). Todas as afirmações são sobre o custo de pior caso que a recorrência do texto modela (é uma cota superior para o tempo do algoritmo).

INTERPRETATION CHECK.

Leitura 1, "o algoritmo acima": o algoritmo indutivo do Subgrafo Induzido Maximal (retirar um vértice de grau < k e recorrer em n − 1 vértices), analisado na representação por lista de adjacências — a única cuja análise está no trecho, com a recorrência T(n) = T(n − 1) + n + (k − 1)(n − 1). No material, o Exercício vem logo depois da análise por lista de adjacências; a análise por matriz de adjacências vem depois dele (T(n) = T(n − 1) + n + n, isto é, T(n) = T(0) + n(n + 1), também Θ(n²) e quadrática), então a resposta não depende da representação. Esta é a leitura que resolvo.

Leitura 2, "linear, quadrática ou exponencial" em função de quê: do parâmetro da indução, n = |V|. O texto escreve O(kn²) e diz que "k é uma entrada do problema"; então há duas sub-leituras: (a) k fixo (constante independente de n) — a pergunta de múltipla escolha só tem resposta exata aqui, e a resposta é "quadrática"; (b) k livre, podendo crescer com n — trato também, porque muda a resposta (passa a cúbica no pior caso de k), e mostro que nem assim fica exponencial.

Leitura 3, "complexidade": custo de pior caso, como o próprio texto modela (busca do vértice em tempo n no pior caso; graus g(vᵢ) = n − 1 no pior caso). A recorrência é uma cota superior do tempo do algoritmo; os Θ abaixo são do valor T(n) da recorrência. Não afirmo que toda entrada gaste isso: o algoritmo pode parar antes (por exemplo, se todos os vértices já têm grau ≥ k na primeira verificação).

Hipótese sobre k: tomo k ≥ 1. Com k ≤ 0 todo vértice tem grau ≥ k, o algoritmo devolve H = G na primeira verificação, e a recorrência nem se aplica (o termo (k − 1)(n − 1) seria negativo, um "custo" sem sentido).

PASSO 1 — FORMA FECHADA DA RECORRÊNCIA LITERAL:

A recorrência vale para n ≥ 1, com T(0) = t₀ ≥ 0 uma constante. Desenrolando (telescópio), T(n) − T(0) = Σ_{j=1}^{n} [T(j) − T(j − 1)] = Σ_{j=1}^{n} [j + (k − 1)(j − 1)].

Fechando as duas somas: Σ_{j=1}^{n} j = n(n + 1)/2 e Σ_{j=1}^{n} (j − 1) = Σ_{i=0}^{n−1} i = n(n − 1)/2. Logo

    T(n) = t₀ + n(n + 1)/2 + (k − 1)·n(n − 1)/2
         = t₀ + [n² + n + (k − 1)n² − (k − 1)n]/2
         = t₀ + (k·n² − (k − 2)·n)/2.

Conferência à mão nos primeiros valores. n = 1: pela recorrência, T(1) = t₀ + 1 + (k − 1)·0 = t₀ + 1; pela fórmula, t₀ + (k − k + 2)/2 = t₀ + 1. n = 2: pela recorrência, T(2) = T(1) + 2 + (k − 1)·1 = t₀ + k + 2; pela fórmula, t₀ + (4k − 2k + 4)/2 = t₀ + k + 2. Batem.

PASSO 2 — T(n) ∈ Θ(k·n²) COM CONSTANTES UNIFORMES EM k:

Afirmação: para todo k ≥ 1 e todo n ≥ 2, (1/4)·k·n² ≤ T(n) ≤ ((3 + t₀)/4)·k·n².

Cota inferior. Como t₀ ≥ 0 e −(k − 2) ≥ −k, T(n) ≥ (k·n² − k·n)/2 = k·n(n − 1)/2. Para n ≥ 2, n − 1 ≥ n/2, logo T(n) ≥ k·n·(n/2)/2 = k·n²/4. Em n = n₀ = 2 exatamente: T(2) = t₀ + k + 2 ≥ k = (1/4)·k·4. Vale.

Cota superior. −(k − 2)·n/2 = −k·n/2 + n ≤ n/2 quando k ≥ 1 (pois −k·n/2 + n ≤ −n/2 + n = n/2). Então T(n) ≤ t₀ + k·n²/2 + n/2. Para n ≥ 2: n/2 ≤ n²/4 ≤ k·n²/4 (pois k ≥ 1); e t₀ ≤ t₀·k·n²/4, porque k·n²/4 ≥ 1·4/4 = 1. Somando, T(n) ≤ k·n²/2 + k·n²/4 + t₀·k·n²/4 = ((3 + t₀)/4)·k·n². Em n = n₀ = 2 com k = 1 (o caso mais apertado): T(2) = t₀ + 3 e ((3 + t₀)/4)·1·4 = 3 + t₀ — igualdade, a desigualdade vale.

As constantes c₁ = 1/4, c₂ = (3 + t₀)/4 e n₀ = 2 são escolhidas antes de n e não dependem de n nem de k. Isso confirma o O(kn²) do texto e mostra que ele é justo (também Ω(kn²)) para a recorrência.

PASSO 3 — k CONSTANTE: QUADRÁTICA.

Fixado k ≥ 1 (constante), o Passo 2 dá, para todo n ≥ n₀ = 2, c₁·n² ≤ T(n) ≤ c₂·n² com c₁ = k/4 > 0 e c₂ = (3 + t₀)·k/4. Logo T(n) ∈ Θ(n²): quadrática. Em n = 2: c₁·4 = k ≤ t₀ + k + 2 = T(2) ≤ (3 + t₀)·k = c₂·4, pois t₀ + k + 2 ≤ (3 + t₀)k equivale a t₀(k − 1) + 2(k − 1) ≥ 0, verdadeiro para k ≥ 1.

Não é linear: T ∉ O(n). Negando a definição: para todo c > 0 e todo n₀ ≥ 1, tome n = max(n₀, 2, ⌊4c/k⌋ + 1). Então n ≥ n₀, n ≥ 2 e n > 4c/k, logo T(n) ≥ k·n²/4 = (k·n/4)·n > c·n. Isso viola T(n) ≤ c·n nesse n ≥ n₀.

Não é exponencial: T ∉ Ω(2ⁿ). Primeiro, m² ≤ 2^m para todo inteiro m ≥ 4 (indução: P(m): m² ≤ 2^m. Base m = 4: 16 ≤ 16. Passo: se m ≥ 4 e m² ≤ 2^m, então (m + 1)² = m² + 2m + 1 ≤ 2m² porque m² − 2m − 1 = (m − 1)² − 2 ≥ 9 − 2 > 0; logo (m + 1)² ≤ 2·m² ≤ 2·2^m = 2^(m+1)). Para n = 2m par com m ≥ 4: n² = 4m² ≤ 4·2^m = 4·2^(n/2). Agora a negação: para todo c > 0 e todo n₀, tome m inteiro com m ≥ max(4, n₀) e 2^m > 4c₂/c (existe, pois 2^m cresce sem limite), e n = 2m ≥ n₀. Então T(n) ≤ c₂·n² ≤ 4c₂·2^m < c·2^m·2^m = c·2ⁿ. Isso viola T(n) ≥ c·2ⁿ nesse n ≥ n₀. Como aⁿ ≥ 2ⁿ para a ≥ 2, também T ∉ Ω(aⁿ) para toda base a ≥ 2.

PASSO 4 — k CRESCENDO COM n: ATÉ ONDE, E O QUE MUDA.

Até onde k pode ir. O passo do algoritmo diz: se |V| < k + 1, não há subgrafo com a propriedade, e para. Então com k ≥ n o algoritmo termina na primeira verificação, em tempo constante; o único k que gera trabalho é 1 ≤ k ≤ n − 1. Além disso, como k é fixo durante toda a recursão e o número de vértices cai de um em um, a recursão só continua enquanto o grafo corrente tem m ≥ k + 1 vértices. Um modelo mais fiel ao passo é, portanto,

    T'(m) = c₀ (constante, c₀ ≥ 0)               para m ≤ k,
    T'(m) = T'(m − 1) + m + (k − 1)(m − 1)       para m ≥ k + 1,

cuja forma fechada, para n ≥ k, é T'(n) = c₀ + Σ_{m=k+1}^{n} [m + (k − 1)(m − 1)] = c₀ + [n(n + 1) − k(k + 1)]/2 + (k − 1)·[n(n − 1) − k(k − 1)]/2. Conferência em n = k + 1: a soma tem um termo, (k + 1) + (k − 1)k; a fórmula dá [(k + 1)(k + 2) − k(k + 1)]/2 + (k − 1)[(k + 1)k − k(k − 1)]/2 = (k + 1) + (k − 1)k. Bate.

Cota superior em função só de n. As parcelas somadas em T'(n) − c₀ são parte das parcelas (todas ≥ 0) de T(n) − t₀ do Passo 1, logo T'(n) − c₀ ≤ (k·n² − (k − 2)·n)/2 ≤ (3/4)·k·n² para n ≥ 2 (Passo 2 com t₀ = 0). Com k ≤ n − 1 < n: T'(n) ≤ c₀ + (3/4)·n³. Então, qualquer que seja k, o custo modelado é O(n³): para n ≥ 1, T'(n) ≤ (3/4 + c₀)·n³ (pois c₀ ≤ c₀·n³). Em particular nunca é exponencial (ver nota abaixo).

Nota sobre "nunca exponencial" com cota n³: para m ≥ 10, m³ ≤ 2^m (P(m): m³ ≤ 2^m; base m = 10: 1000 ≤ 1024; passo: (m + 1)³ ≤ 2m³ porque ((m + 1)/m)³ ≤ (1,1)³ = 1,331 ≤ 2 para m ≥ 10). Para n = 3m com m ≥ 10: n³ = 27m³ ≤ 27·2^m = 27·2^(n/3). Dado c > 0 e n₀, tome m ≥ max(10, n₀) com 2^(2m) > 27·(3/4 + c₀)/c e n = 3m: T'(n) ≤ (3/4 + c₀)·27·2^m < c·2^(2m)·2^m = c·2ⁿ. Logo T' ∉ Ω(2ⁿ).

Com k = ⌊n/2⌋ o custo é cúbico, não quadrático. Tome k = ⌊n/2⌋ e n ≥ 6 (então k ≥ 3 ≥ 1 e k ≤ n/2). Pelo fechamento de T', T'(n) − c₀ ≥ (k − 1)·[n(n − 1) − k(k − 1)]/2, já que a outra parcela, [n(n + 1) − k(k + 1)]/2, é ≥ 0 (n ≥ k). Com k ≤ n/2: k(k − 1) ≤ (n/2)(n/2 − 1) = n²/4 − n/2, logo n(n − 1) − k(k − 1) ≥ n² − n − n²/4 + n/2 = 3n²/4 − n/2 ≥ n²/2 para n ≥ 2. E k − 1 ≥ (n − 1)/2 − 1 = (n − 3)/2 ≥ n/4 para n ≥ 6. Portanto T'(n) ≥ (n/4)·(n²/2)/2 = n³/16 para n ≥ 6. Em n = n₀ = 6 exatamente: k = 3, T'(6) − c₀ = Σ_{m=4}^{6} [m + 2(m − 1)] = 10 + 13 + 16 = 39 ≥ 216/16 = 13,5. Vale. Do lado de cima, T'(n) ≤ c₀ + (3/4)·k·n² ≤ c₀ + (3/8)·n³. Logo, com k = ⌊n/2⌋, T'(n) ∈ Θ(n³) (c₁ = 1/16, c₂ = 3/8 + c₀, n₀ = 6; em n = 6: 13,5 ≤ 39 + c₀ ≤ (3/8 + c₀)·216 = 81 + 216c₀).

Não é quadrático nesse regime: para todo c > 0 e n₀, tome n = max(n₀, 6, ⌊16c⌋ + 1); então T'(n) ≥ n³/16 = (n/16)·n² > c·n², violando T'(n) ≤ c·n². O mesmo vale para a recorrência literal do texto: com k = ⌊n/2⌋ ≥ n/4 (n ≥ 2), o Passo 2 dá T(n) ≥ k·n²/4 ≥ n³/16.

Resumo do Passo 4: a resposta "quadrática" pressupõe k constante (ou, mais geralmente, k limitado por uma constante). Se k é uma entrada que pode crescer junto com n, a recorrência literal dá Θ(k·n²); o modelo T' dá O(k·n²) ⊆ O(n³), que vai de quadrático (k constante) a cúbico (k = ⌊αn⌋ com 0 < α < 1 fixo, por exemplo k = ⌊n/2⌋), e o teto é O(n³) porque k útil é no máximo n − 1. Com k perto de n (k = n − d, d ≥ 1 constante) restam só O(1) passos de custo Θ(k·n) e T' volta a Θ(n²): com k = n − 1, T'(n) = c₀ + n + (n − 2)(n − 1). Em nenhum regime é exponencial nem, para k ≥ 1 com a recorrência dada, linear.

CONCLUSÃO.

Pela recorrência do texto (lista de adjacências, pior caso), o algoritmo tem custo Θ(k·n²). Como a pergunta é em função de n e oferece "linear, quadrática ou exponencial", a resposta é: quadrática, desde que k seja tratado como constante. Ela não é linear (T ∉ O(n)) nem exponencial (T ∉ Ω(2ⁿ)); o algoritmo é polinomial. Se k crescer com n, a dependência em k aparece: com k proporcional a n e longe de n (k = ⌊αn⌋, 0 < α < 1; por exemplo k = ⌊n/2⌋) o custo modelado chega a Θ(n³), e nunca passa de O(n³), porque com k ≥ n o algoritmo para na primeira verificação.

Conferência numérica (Python; não faz parte da prova): a forma fechada do Passo 1, T(n) − T(0) = n(n + 1)/2 + (k − 1)·n(n − 1)/2, confere. A conferência numérica não cobriu as testemunhas c₁ = 1/4, c₂ = (3 + t₀)/4, n₀ = 2, a forma fechada de T' nem o regime k = ⌊n/2⌋; esses foram conferidos à mão nos valores de fronteira (n = 1, 2 para T; n = k + 1 e n = 6 com k = 3 para T').
