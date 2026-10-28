Resposta. No modelo de custo M declarado abaixo (cada operação primitiva custa 1), Prefix1 executa exatamente T1(n) = 3n² + 13n + 4 operações e Prefix2 executa exatamente T2(n) = 10n + 5 operações, para todo n ≥ 0 e para todo vetor X de tamanho n. Pela definição: T1(n) ≤ 20·n² para todo n ≥ 1 (c = 20, n0 = 1), logo Prefix1 é O(n²); T2(n) ≤ 15·n para todo n ≥ 1 (c = 15, n0 = 1), logo Prefix2 é O(n). As cotas são justas: T1 ∈ Θ(n²) (c1 = 3, c2 = 20, n0 = 1), T2 ∈ Θ(n) (c1 = 10, c2 = 15, n0 = 1), e T1 não é O(n). Não há diferença entre pior caso, melhor caso e caso médio: em cada algoritmo, os laços têm limites que dependem só de n e não há desvio condicional que dependa do conteúdo de X, de modo que todas as entradas de mesmo tamanho n executam exatamente a mesma sequência de operações; os três casos coincidem com T1(n) e com T2(n), respectivamente.

INTERPRETAÇÃO DO ENUNCIADO.
"Os algoritmos anteriores para cálculo da média de prefixo" são Prefix1 (p. 19) e Prefix2 (p. 21). O enunciado pede quatro coisas: (i) uma análise detalhada, linha a linha, do número de operações primitivas; (ii) o número EXATO de operações de cada algoritmo; (iii) prova pela definição de que Prefix1 é O(n²) e Prefix2 é O(n); (iv) discussão de pior caso, melhor caso e caso médio, com justificativa. Leituras possíveis de (ii): (a) contar só quantas vezes cada linha executa, como faz a coluna "#operações" do slide; (b) contar operações primitivas com um modelo de custo explícito. Como o enunciado diz "número exato de operações", e a coluna do slide usa "~" (aproximado), resolvo a leitura (b), mas parto da (a): primeiro conto quantas vezes cada linha executa (isso não depende de modelo), depois multiplico pelo custo de cada linha no modelo declarado. O material presente não traz a regra de contagem de operações primitivas (a p. 15 só diz "encontra-se o no. de operações primitivas ... no pior caso"), então o modelo precisa ser declarado; com outro modelo as constantes mudam, mas as contagens de execução por linha da seção seguinte não mudam.

MODELO DE CUSTO M (declarado).
Custa 1 cada: atribuição, operação aritmética (+, /), comparação, acesso indexado a vetor (X[j], A[i]), retorno, e a alocação "A ← novo vetor de n inteiros" (a linha inteira custa 1). Um laço "para v ← a até b faça" custa: 1 pela inicialização v ← a; 1 por teste v ≤ b (o limite b é tratado como valor já disponível, e o teste custa 1); e 2 por incremento v ← v + 1 (uma soma e uma atribuição). Se o corpo executa k = b − a + 1 vezes (k ≥ 0), o laço faz k incrementos e k + 1 testes (o último teste é o que falha), logo o controle do laço custa 1 + (k + 1) + 2k = 3k + 2.
Custo de cada linha de corpo nesse modelo:
    s ← 0                : 1 (atribuição)
    s ← s + X[j]         : 3 (acesso X[j], soma, atribuição)
    s ← s + X[i]         : 3 (acesso X[i], soma, atribuição)
    A[i] ← s / (i + 1)   : 4 (soma i + 1, divisão, acesso indexado A[i], atribuição)
    retorne A            : 1

PASSO 1 — DE ONDE VEM CADA "~" DA TABELA DE PREFIX1 (quantas vezes cada linha executa).
    1: A ← novo vetor de n inteiros          executa 1 vez
    2: para i ← 0 até n − 1 faça             corpo executa n vezes; n + 1 testes; n incrementos
    3:     s ← 0                             executa n vezes (uma por valor de i)
    4:     para j ← 0 até i faça             para cada i, corpo executa i + 1 vezes; i + 2 testes
    5:         s ← s + X[j]                  executa Σ_{i=0}^{n−1} (i + 1) = 1 + 2 + … + n vezes
    6:     A[i] ← s / (i + 1)                executa n vezes
    7: retorne A                             executa 1 vez
O "~ n" da linha 2 é porque o teste do laço externo acontece n + 1 vezes, não n: o slide despreza o teste final. O "~ n" das linhas 3 e 6 é na verdade exato em número de execuções (n vezes cada); o "~" esconde só o custo de cada execução (1 e 4 operações em M). O "~ 1 + 2 + … + n" da linha 5 é exato em execuções; o da linha 4 é aproximado, porque o laço interno, para um i fixo, testa i + 2 vezes, e no total testa Σ_{i=0}^{n−1} (i + 2) = (1 + 2 + … + n) + n vezes. Pela progressão aritmética (p. 20), 1 + 2 + … + n = n(n + 1)/2; a "área em laranja" n²/2 + n·½ do slide é exatamente esse valor.

PASSO 2 — PREFIX1 EXATO NO MODELO M.
Linha 1: 1.
Linha 2 (controle do laço externo, k = n): 3n + 2.
Linha 3: n execuções × 1 = n.
Linha 4 (controle do laço interno, para cada i com k = i + 1): 3(i + 1) + 2 = 3i + 5; somando em i = 0, …, n − 1: 3·Σ_{i=0}^{n−1} i + 5n = 3·n(n − 1)/2 + 5n.
Linha 5: n(n + 1)/2 execuções × 3 = 3·n(n + 1)/2.
Linha 6: n execuções × 4 = 4n.
Linha 7: 1.
Total:
    T1(n) = 1 + (3n + 2) + n + [3n(n − 1)/2 + 5n] + 3n(n + 1)/2 + 4n + 1.
As duas frações somam 3n(n − 1)/2 + 3n(n + 1)/2 = (3/2)·(n² − n + n² + n) = 3n². Os termos lineares somam 3n + n + 5n + 4n = 13n. As constantes somam 1 + 2 + 1 = 4. Logo
    T1(n) = 3n² + 13n + 4,  para todo n ≥ 0.
Checagem em n = 0 (laço externo não executa): alocação 1 + inicialização i ← 0 1 + teste que falha 1 + retorno 1 = 4 = T1(0). Checagem em n = 1: linha 1: 1; linha 2: 3·1 + 2 = 5; linha 3: 1; linha 4 (i = 0): 5; linha 5: 3; linha 6: 4; linha 7: 1; soma 20 = 3 + 13 + 4 = T1(1).

PASSO 3 — DE ONDE VEM CADA "~" DA TABELA DE PREFIX2, E A CONTAGEM EXATA.
    1: A ← novo vetor de n inteiros          executa 1 vez                      custo 1
    2: s ← 0                                 executa 1 vez                      custo 1
    3: para i ← 0 até n − 1 faça             corpo n vezes; n + 1 testes        custo 3n + 2
    4:     s ← s + X[i]                      executa n vezes                    custo 3n
    5:     A[i] ← s / (i + 1)                executa n vezes                    custo 4n
    6: retorne A                             executa 1 vez                      custo 1
O "~ n" da linha 3 esconde de novo o teste final (n + 1 testes) e os incrementos; os "~ n" das linhas 4 e 5 são exatos em execuções e escondem o custo por execução (3 e 4). Total:
    T2(n) = 1 + 1 + (3n + 2) + 3n + 4n + 1 = 10n + 5,  para todo n ≥ 0.
Checagem: n = 0 dá 1 + 1 + 2 + 1 = 5 = T2(0); n = 1 dá 1 + 1 + 5 + 3 + 4 + 1 = 15 = T2(1).
A diferença essencial está na linha 5 de Prefix1: ela refaz, para cada i, a soma X[0] + … + X[i] desde o início, o que dá 1 + 2 + … + n execuções; Prefix2 mantém em s a soma do prefixo anterior e faz uma única soma por i.

PASSO 4 — PREFIX1 É O(n²), PELA DEFINIÇÃO.
Definição (Campello): f(n) é O(g(n)) se existem uma constante real c > 0 e um inteiro n0 ≥ 1 tais que f(n) ≤ c·g(n) para todo n ≥ n0. Ordem dos quantificadores: ∃c ∃n0 ∀n ≥ n0.
Tome c = 20 e n0 = 1 (escolhidos antes de n, sem depender de n). Para todo inteiro n ≥ 1 vale n ≤ n² e 1 ≤ n², logo 13n ≤ 13n² e 4 ≤ 4n². Somando a 3n² ≤ 3n²:
    T1(n) = 3n² + 13n + 4 ≤ 3n² + 13n² + 4n² = 20n²,  para todo n ≥ 1.
Em n = n0 = 1 exatamente: T1(1) = 20 e 20·1² = 20; 20 ≤ 20 vale (com igualdade). Portanto Prefix1 é O(n²).

PASSO 5 — PREFIX2 É O(n), PELA DEFINIÇÃO.
Tome c = 15 e n0 = 1. Para todo inteiro n ≥ 1 vale 5 ≤ 5n, logo
    T2(n) = 10n + 5 ≤ 10n + 5n = 15n,  para todo n ≥ 1.
Em n = n0 = 1 exatamente: T2(1) = 15 e 15·1 = 15; 15 ≤ 15 vale. Portanto Prefix2 é O(n).

PASSO 6 — AS COTAS SÃO JUSTAS (Θ) E PREFIX1 NÃO É O(n).
O enunciado só pede O, mas O é cota superior e não diz que Prefix1 é pior que Prefix2; para isso é preciso a cota inferior.
Prefix1 ∈ Θ(n²): para todo n ≥ 1, 13n + 4 ≥ 0, logo T1(n) ≥ 3n². Com c1 = 3, c2 = 20, n0 = 1: 3n² ≤ T1(n) ≤ 20n² para todo n ≥ 1. Em n = 1: 3 ≤ 20 ≤ 20.
Prefix2 ∈ Θ(n): para todo n ≥ 1, 10n ≤ 10n + 5 ≤ 15n. Com c1 = 10, c2 = 15, n0 = 1. Em n = 1: 10 ≤ 15 ≤ 15.
Prefix1 não é O(n). Negação da definição: para toda constante c > 0 e todo inteiro n0 ≥ 1, existe n ≥ n0 com T1(n) > c·n. Dados c e n0 quaisquer, tome n = max(n0, ⌈c/3⌉ + 1). Então n ≥ n0 e n > c/3 (pois n ≥ ⌈c/3⌉ + 1 > c/3), logo 3n > c, e como n ≥ 1:
    T1(n) = 3n² + 13n + 4 > 3n² = (3n)·n > c·n.
Exemplo: c = 100, n0 = 1 dá n = max(1, 34 + 1) = 35, e T1(35) = 3·1225 + 455 + 4 = 4134 > 3500 = 100·35. Assim nenhuma escolha de c e n0 serve, e Prefix1 está em Θ(n²) mas não em O(n): sua contagem cresce estritamente mais rápido que a de Prefix2.

PASSO 7 — PIOR CASO, MELHOR CASO E CASO MÉDIO.
Fixe n. Em Prefix1, o laço externo executa exatamente n vezes e, para cada i, o laço interno executa exatamente i + 1 vezes: esses números dependem só de n e de i, nunca dos valores X[0], …, X[n − 1]. Não há nenhum "se" nos algoritmos, e nenhuma linha é pulada ou repetida conforme o conteúdo de X. O mesmo vale para Prefix2, cujo único laço executa exatamente n vezes. Logo, para cada n, todas as entradas de tamanho n produzem exatamente a mesma sequência de operações, e no modelo M (custo 1 por operação, independente do valor dos operandos):
    pior caso de Prefix1 = melhor caso = caso médio = 3n² + 13n + 4;
    pior caso de Prefix2 = melhor caso = caso médio = 10n + 5.
O caso médio coincide com os outros dois para qualquer distribuição de probabilidade sobre as entradas, porque a média de uma quantidade constante é essa constante. Em consequência, as afirmações dos PASSOS 4 a 6 valem para toda entrada, não só para o pior caso: Prefix1 é Θ(n²) e Prefix2 é Θ(n) em pior, melhor e caso médio. Ressalva de escopo: essa igualdade dos três casos é afirmada dentro do modelo de custo unitário M (o da disciplina); num modelo que cobrasse aritmética pelo número de bits dos operandos, o custo de cada soma passaria a depender dos valores de X, e a discussão teria de ser refeita.

Conferência numérica (Python; não faz parte da prova): uma implementação instrumentada no mesmo modelo M contou T1(n) = 3n² + 13n + 4 e T2(n) = 10n + 5 para n = 0, …, 300, com 3 vetores diferentes para cada n, e obteve a mesma contagem independentemente do conteúdo — o que bate com as fórmulas dos PASSOS 2 e 3 e com a igualdade dos três casos do PASSO 7. Confirmou também as testemunhas: 3n² + 13n + 4 ≤ 20n² para n ≥ 1, com igualdade 20 ≤ 20 em n = 1, e 10n + 5 ≤ 15n para n ≥ 1, com 15 ≤ 15 em n = 1. A cota inferior (Θ) e a refutação de "Prefix1 é O(n)" não entram nessa contagem; estão provadas algebricamente no PASSO 6.
