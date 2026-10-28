# -*- coding: utf-8 -*-
"""Correções aplicadas às saídas dos workflows, derivadas dos achados dos verificadores
e conferidas numericamente. Cada entrada é (fonte, item, trecho_antigo, trecho_novo)."""

PATCHES = [
# ── IFMG (3): o lema F_n >= 2^((n-1)/2) e FALSO em n = 2 ──────────────────────
("IFMG","(3)",
 "Testemunhas para a cota inferior exponencial (forma simples de exibir): prova-se por inducao que F_n >= 2^((n-1)/2) para todo n >= 1, portanto C(n) >= 2*2^((n-1)/2) - 1 >= 2^(n/2) para n >= 2; isto e, C(n) = Omega(2^(n/2)) com c = 1 e n0 = 2. Em palavras: o tempo cresce exponencialmente.",
 "Testemunhas para a cota inferior exponencial. Usa-se o lema F_m >= 2^((m-2)/2), valido para todo m >= 1 (o lema com expoente (m-1)/2 seria FALSO em m = 2, pois F_2 = 1 < 2^(1/2) = 1,414). Dele vem F_(n+1) >= 2^((n-1)/2), logo C(n) = 2*F_(n+1) - 1 >= 2*2^((n-1)/2) - 1 = 2^((n+1)/2) - 1. Como 2^((n+1)/2) - 1 >= 2^(n/2) equivale a 2^(n/2)*(raiz(2) - 1) >= 1, isto e n >= 2,54, a desigualdade vale a partir de n = 3. Portanto C(n) = Omega(2^(n/2)) com c = 1 e n0 = 3. Em palavras: o tempo cresce exponencialmente."),

# ── IFMG (4): altura misturava nos e arestas ─────────────────────────────────
("IFMG","(4)",
 "A altura da arvore e 6 (o caminho mais longo, F(6) -> F(5) -> F(4) -> F(3) -> F(2) -> F(1), desce sempre pela esquerda); o caminho mais curto ate uma folha tem comprimento 3 (descendo sempre pela direita)",
 "Contando ARESTAS (convencao padrao para altura), a altura da arvore e 5: o caminho mais longo, F(6) -> F(5) -> F(4) -> F(3) -> F(2) -> F(1), desce sempre pela esquerda e tem 6 nos, portanto 5 arestas. O caminho mais curto ate uma folha, F(6) -> F(4) -> F(2) -> F(0), desce sempre pela direita e tem 4 nos, portanto 3 arestas"),

# ── IFMG (5): a "conferencia" nao batia com a formula exibida ────────────────
("IFMG","(5)",
 "CONFERENCIA. A contagem de operacoes feita executando a recorrencia da 1, 6, 12 para n = 1, 2, 3, e a razao entre o numero de operacoes contadas e n^2 estabiliza (n = 50: 0,569; n = 200: 0,517; n = 800: 0,504), convergindo para a constante a/2 = 1/2 prevista pela forma fechada",
 "CONFERENCIA. Com o custo unitario a = b = c = 1 adotado acima, a forma fechada T(n) = (n^2 + 3n - 2)/2 da T(1) = 1, T(2) = 4, T(3) = 8 e T(4) = 13. A razao T(n)/n^2 estabiliza (n = 50: 0,5296; n = 200: 0,5075; n = 800: 0,5019), convergindo para a constante a/2 = 1/2 prevista pela forma fechada"),

# ── CAMPELLO (4): "ilimitado" e falso — existe maximo finito ─────────────────
("CAMPELLO","(4)",
 "  log n     | ilimitado (*) | ilimitado (*)  | ilimitado (*)      | ilimitado (*)",
 "  log n     | 2^(10^6)      | 2^(3,6*10^9)   | 2^(2,592*10^12)    | 2^(3,1536*10^15)"),
("CAMPELLO","(4)",
 "Por isso a resposta honesta é 'praticamente ilimitado', e não um número.",
 "Ou seja: o maior n existe e vale exatamente 2^t, com t medido em microssegundos — mas e um numero com da ordem de 3*10^5 a 9*10^14 algarismos decimais. O limite pratico deixa de ser o tempo e passa a ser a representacao de n."),

# ── CAMPELLO (5): direcao da desigualdade invertida na prosa ─────────────────
("CAMPELLO","(5)",
 "Cada iteração reduz o intervalo a NO MÁXIMO metade dele: n_{k+1} >= piso((n_k - 1)/2)",
 "Cada iteração DESCARTA no máximo metade do intervalo — equivalentemente, SOBRA pelo menos cerca de metade: n_{k+1} >= piso((n_k - 1)/2)"),
]

def aplica(sol):
    """sol: dict {fonte: {item: {...}}}. Devolve (n_aplicados, n_falhos)."""
    ok = falho = 0
    for fonte, item, velho, novo in PATCHES:
        it = sol.get(fonte, {}).get(item)
        if it and velho in it["justificativa"]:
            it["justificativa"] = it["justificativa"].replace(velho, novo)
            ok += 1
        elif fonte in sol:
            falho += 1
            print(f"  !! patch NAO aplicado: {fonte} {item} — trecho nao encontrado")
    return ok, falho

# ── PROVA-A (1): detector nunca acionado na origem ───────────────────────────
PATCHES += [
("PROVA-A","1",
 "  i <- 0\n  repita",
 "  se o detector acusar ja na origem, PARE (a mina esta a um passo)\n  i <- 0\n  repita"),
("PROVA-A","1",
 "Ponto essencial: o detector tem alcance 1, então NÃO se pode apenas testar no ponto final do salto de 2^i passos — a mina seria simplesmente ultrapassada sem ser vista.",
 "Dois pontos essenciais. Primeiro, e preciso SONDAR A ORIGEM antes de entrar no laco: sem isso, com m = 1 o agente nao consulta o detector estando a um passo da mina e acaba PISANDO nela (para a mina em -1 ele gasta 3 passos e pisa; para +1, gasta 1 e pisa). Com a sondagem inicial, m = 1 e resolvido em 0 passos. Segundo, o detector tem alcance 1, então NÃO se pode apenas testar no ponto final do salto de 2^i passos — a mina seria simplesmente ultrapassada sem ser vista."),
("PROVA-A","1",
 "Confirindo em m = m0 = 1 exatamente: com m = 1 tem-se k = 0 e o algoritmo acusa a mina já no primeiro passo (na verdade a mina está a um passo da origem, então T(1) = 0 ou 1), e 1 <= 14·1. A desigualdade vale.",
 "Conferindo em m = m0 = 1 exatamente: com a sondagem inicial, T(1) = 0 (a mina esta a um passo da origem e e acusada antes de qualquer movimento), e 0 <= 14*1. Sem a sondagem inicial o pior caso seria T(1) = 3 (mina em -1), e 3 <= 14*1 tambem vale. A desigualdade e satisfeita em m0 nos dois casos. Simulando m = 1 ate 299, a maior razao T(m)/m observada foi 12,888 (em m = 258), sempre abaixo de 14."),
("PROVA-A","1",
 "já que qualquer algoritmo precisa de pelo menos m-1 passos para chegar à vizinhança da mina.",
 "ja que qualquer algoritmo precisa de pelo menos m-1 passos para chegar a vizinhanca da mina — e isso se justifica assim: para acusar a mina, que esta a distancia m, o agente precisa ocupar alguma posicao a distancia no maximo 1 dela, e partindo da origem isso exige no minimo m-1 movimentos."),
]

# ── IFMG (4): o campo RESPOSTA contradizia o corpo (altura 6 vs 5) ───────────
# Este erro foi introduzido pelo patch anterior, que corrigiu o corpo e esqueceu
# a linha de resposta. Dois verificadores independentes o classificaram como ALTA.
PATCHES_RESPOSTA = [
("IFMG","(4)",
 "25 nos no total (= 2*F_7 - 1 = 2*13 - 1), altura 6.",
 "25 nos no total (= 2*F_7 - 1 = 2*13 - 1), altura 5 arestas (6 niveis de nos)."),
]

def aplica_resposta(sol):
    ok = falho = 0
    for fonte, item, velho, novo in PATCHES_RESPOSTA:
        it = sol.get(fonte, {}).get(item)
        if it and velho in it["resposta"]:
            it["resposta"] = it["resposta"].replace(velho, novo); ok += 1
        elif fonte in sol:
            falho += 1
            print(f"  !! patch de resposta NAO aplicado: {fonte} {item}")
    return ok, falho

# ══════════ LOTE 4 — Campello (gravidade baixa) ══════════
# Duas destas são consequência dos patches anteriores: a nota do log n ficou com
# frase duplicada, e o "descarta no máximo metade" continuou falso mesmo após o
# primeiro remendo. Todas conferidas em python3 antes de escrever.
PATCHES += [

# #1/#9 — nota do log n: frase duplicada e sem acento (herdada do patch anterior)
("CAMPELLO","(4)",
 "Ou seja, para uma entrada logarítmica o gargalo deixa de ser o tempo e passa a ser a própria representação/armazenamento de n. Ou seja: o maior n existe e vale exatamente 2^t, com t medido em microssegundos — mas e um numero com da ordem de 3*10^5 a 9*10^14 algarismos decimais. O limite pratico deixa de ser o tempo e passa a ser a representacao de n.",
 "Ou seja: o maior n existe e vale exatamente 2^t, com t medido em microssegundos — mas é um número com da ordem de 3·10^5 a 9,5·10^14 algarismos decimais. Para uma entrada logarítmica, portanto, o gargalo deixa de ser o tempo e passa a ser a própria representação de n."),

# #2/#7 — a conta impressa refuta a propria celula (62.746 x 15,94 > 10^6)
("CAMPELLO","(4)",
 "Ex.: 62.746 * lg(62.746) ~ 62.746 * 15,94 ~ 9,9998 * 10^5 <= 10^6, e 62.747 já ultrapassa.",
 "Ex.: lg(62.746) = 15,9372, logo 62.746 * 15,9372 = 999.997,8 <= 10^6; ja 62.747 * lg(62.747) = 1.000.015,2 > 10^6, o que confirma 62.746 como o maior. (Cuidado ao arredondar: com lg ~ 15,94 o produto daria 1.000.171, acima do limite — o arredondamento para cima inverteria a conclusao.)"),

# #3/#6 — "descarta no maximo metade" e FALSO (n=4 descarta 75%)
("CAMPELLO","(5)",
 "Cada iteração DESCARTA no máximo metade do intervalo — equivalentemente, SOBRA pelo menos cerca de metade: n_{k+1} >= piso((n_k - 1)/2), de modo que são necessárias pelo menos piso(lg n) iterações para esvaziar o intervalo.",
 "Cada iteracao deixa pelo menos piso((n_k - 1)/2) elementos, pois os dois ramos tem tamanhos piso((n_k-1)/2) e piso(n_k/2). (Nao vale dizer 'descarta no maximo metade': com n_k = 4 o ramo esquerdo deixa 1 de 4, isto e, descarta 75%.) Dessa recorrencia segue n_k >= n/2^k - 1, de modo que o intervalo so se esvazia quando 2^k > n, isto e, apos pelo menos piso(lg n) iteracoes."),

# #5 — colisao de simbolo c entre o Passo 3 e o Passo 4
("CAMPELLO","(5)",
 "Tome n0 = 2 e c = 2a + b.",
 "Tome n0 = 2 e c2 = 2a + b (o indice evita colisao com a constante da cota inferior, no Passo 4)."),
("CAMPELLO","(5)",
 "Testemunhas: c = a'/2 e n0 = 2, logo T_pior(n) = Omega(lg n).",
 "Testemunhas: c1 = a'/2 e n0 = 2, logo T_pior(n) = Omega(lg n)."),

# #4/#8 — nem todo x ausente forca o maximo de iteracoes
("CAMPELLO","(7)",
 "Pelo item (5), quando x não está no vetor o algoritmo executa piso(lg n) + 1 iterações, e seu custo é Theta(lg n), que cresce sem limite.",
 "Pelo item (5), existe entrada com x ausente que forca piso(lg n) + 1 iteracoes, e nela o custo e Theta(lg n), que cresce sem limite. (Nem todo x ausente forca o maximo: com n = 4 e x menor que todos os elementos sao apenas 2 iteracoes — o que importa aqui e que ALGUMA entrada o forca.)"),

# #10 — "reciproca" e na verdade a cota inferior
("CAMPELLO","(6)",
 "2. Vale também a recíproca: f(n) = d >= d*1 com c = d e n0 = 1",
 "2. Vale também a cota inferior: f(n) = d >= d*1 com c = d e n0 = 1"),
]

# ══════════ LOTE 5 — Prova 2025, Q1 e Q2 (gravidade baixa) ══════════
# Uma delas (a linha Resposta sem a sondagem inicial) e o MESMO padrao que gerou
# o "altura 6": patch aplicado no corpo e esquecido no campo resposta.
PATCHES += [

# #1 — o agente NAO passa pela posicao da mina; ele para em m-1 (simulado m=1..2999)
("PROVA-A","1",
 "como m <= 2^k, ele passa pela própria posição da mina (e, antes disso, pela posição m-1, a um passo dela). Como o detector é acionado a cada passo, a mina é acusada o mais tardar nessa iteração.",
 "como m <= 2^k, o agente alcanca a posicao m-1 ainda nessa iteracao. Como o detector e acionado a cada passo e tem alcance 1, ele acusa a mina ali e o agente PARA — sem nunca ocupar a posicao m. (Simulando o pseudocodigo para m = 1 ate 2999 nos dois lados, o agente jamais pisa na mina: ele para em m-1, ou na propria origem quando m = 1.)"),

# #2 — sem sondar a cada passo o agente PISA na mina, nao a ultrapassa
("PROVA-A","1",
 "a mina seria simplesmente ultrapassada sem ser vista.",
 "a mina estaria em alguma posicao intermediaria do trajeto e o agente PISARIA nela antes de qualquer sondagem — o passo e o movimento de uma unidade, entao ele percorre fisicamente todas as posicoes do caminho."),

# #3 — em m = 1 o detector acusa mas nao distingue o lado
("PROVA-A","1",
 "Com a sondagem inicial, m = 1 e resolvido em 0 passos.",
 "Com a sondagem inicial, m = 1 e resolvido em 0 passos. Ressalva honesta: na origem o detector acusa se e so se m = 1, mas nao informa se a mina esta em +1 ou em -1. Nenhum algoritmo que nao pise na mina consegue distinguir os dois casos, entao 'encontrar' aqui significa detectar a presenca a um passo, que e o maximo que o detector permite."),

# #7 — o somatorio da estrategia alternativa conta so as idas de um lado
("PROVA-A","1",
 "mas custa da ordem de 1 + 2 + ... + m = m(m+1)/2 = Theta(m^2) passos",
 "mas custa 4*(1 + 2 + ... + m) = 2m(m+1) = Theta(m^2) passos — o fator 4 vem de ida e volta em cada um dos dois lados, e o somatorio 1+2+...+m sozinho contaria apenas as idas de um lado"),

# #8 — o item (b) provou UMA direcao, nao a equivalencia
("PROVA-A","2c",
 "por (b), g = O(f) equivale a f = Omega(g)",
 "por (b), aplicado com os papeis trocados (f := g, g := f), g = O(f) implica f = Omega(g) — note que (b) demonstra so essa direcao, e e exatamente a de que precisamos aqui"),
]

# ── linha RESPOSTA dos mesmos itens (o campo que ja me escapou duas vezes) ──
PATCHES_RESPOSTA += [
("PROVA-A","1",
 "Busca por duplicação (exponential search) alternando os dois lados: para i = 0, 1, 2, ...",
 "Busca por duplicação (exponential search): sonda-se o detector na origem ANTES de tudo e, em seguida, alternando os dois lados, para i = 0, 1, 2, ..."),
("PROVA-A","2c",
 'VERDADEIRA (é o Teorema 3.1 do CLRS, na direção "O e Omega implicam Theta").',
 'VERDADEIRA (é o Teorema 3.1 do CLRS, depois de reescrever g = O(f) como f = Omega(g) usando o item (b) com os papéis trocados).'),
]

# ══════════ LOTE 6 — IFMG / Diego Mello (gravidade baixa) ══════════
PATCHES += [

# #2/#5 — (1/2)n^3 NAO e cota superior de Σi²: falha em n = 1, 2, 3
("IFMG","(1)",
 "pois n(n+1)(2n+1)/6 esta entre (1/3)n^3 e (1/2)n^3 * (1+o(1)); testemunhas: c1 = 1/3, c2 = 1, n0 = 1 satisfazem",
 "com as testemunhas c1 = 1/3, c2 = 1 e n0 = 1, que satisfazem"),

# #6 — o lema de Fibonacci era invocado sem prova; a inducao cabe em duas linhas
("IFMG","(3)",
 "Usa-se o lema F_m >= 2^((m-2)/2), valido para todo m >= 1 (o lema com expoente (m-1)/2 seria FALSO em m = 2, pois F_2 = 1 < 2^(1/2) = 1,414).",
 "Usa-se o lema F_m >= 2^((m-2)/2), valido para todo m >= 1 (o lema com expoente (m-1)/2 seria FALSO em m = 2, pois F_2 = 1 < 2^(1/2) = 1,414). Prova do lema, por inducao com DUAS bases (o passo usa F_(m-1) e F_(m-2), entao uma base so nao basta): m = 1 da F_1 = 1 >= 2^(-1/2) = 0,707; m = 2 da F_2 = 1 >= 2^0 = 1. Passo, para m >= 3: F_m = F_(m-1) + F_(m-2) >= 2^((m-3)/2) + 2^((m-4)/2) = 2^((m-4)/2)*(raiz(2) + 1) >= 2^((m-4)/2)*2 = 2^((m-2)/2), pois raiz(2) + 1 = 2,414 > 2.",),

# #8 — 3n - 2 >= 0 equivale a n >= 2/3, nao a n >= 1
("IFMG","(5)",
 "cota inferior: (n^2 + 3n - 2)/2 >= (1/2)*n^2  <=>  3n - 2 >= 0  <=>  n >= 1. Vale para todo n >= 1.",
 "cota inferior: (n^2 + 3n - 2)/2 >= (1/2)*n^2  <=>  3n - 2 >= 0  <=>  n >= 2/3; como n e inteiro, isso equivale a n >= 1. Vale para todo n >= 1."),

# #1/#8 — no caso geral o n0 era apenas afirmado existir, nunca construido
("IFMG","(5)",
 "No caso geral (a, b, c quaisquer positivos), as testemunhas sao c1 = a/4 e c2 = a, com n0 escolhido grande o bastante para absorver os termos de grau 1 e 0 — o argumento e o mesmo, pois o termo (a/2)n^2 domina os demais.",
 "No caso geral (a, b, c quaisquer positivos), a forma fechada e T(n) = (a/2)n^2 + (a/2 + b)n + (c - a - b). Tome c1 = a/4, c2 = a e construa n0 explicitamente: n0 = max(1, 4(a/2 + b)/a, 4|c - a - b|/a). Com esse n0 cada termo de grau menor fica limitado por (a/4)n^2 em modulo, de modo que (a/4)n^2 <= T(n) <= a*n^2 para todo n >= n0. O ponto e que n0 sai de a, b, c por uma formula, e nao e apenas declarado existir."),

# #7 — o custo do laco nao e a*j com um unico a valido para toda entrada
("IFMG","(5)",
 "cada iteracao faz uma comparacao (linha 6) e, no maximo, uma atribuicao (linha 7) — custo O(1) por iteracao. Total do laco: a*j operacoes, para alguma constante a > 0;",
 "cada iteracao faz uma comparacao (linha 6) e, no maximo, uma atribuicao (linha 7) — custo O(1) por iteracao. O numero de vezes que a linha 7 executa depende do vetor (para n = 5 ela roda 10 vezes num vetor crescente, 4 num decrescente e 0 num de elementos iguais), entao o custo do laco nao e uma expressao unica a*j: e a1*j <= custo <= a2*j, com 0 < a1 <= a2 constantes. O que vale para toda entrada e que o laco custa Theta(j);"),

# #3 — o pseudo-codigo numerado nunca e reproduzido, tornando a contagem inauditavel
("IFMG","(5)",
 "CONTAGEM DE CUSTO DE UMA CHAMADA. Considere a chamada ORDENACAO-POR-SELECAO(V, j) e conte o trabalho feito fora da recursao:",
 "CONTAGEM DE CUSTO DE UMA CHAMADA. Para que a contagem linha a linha possa ser conferida, o pseudo-codigo do enunciado:\n\n   1: if (j = 1) then\n   2:     return V\n   3: else\n   4:     indice <- 1\n   5:     for (i <- 1 to j) do\n   6:         if (V[i] > V[indice]) then\n   7:             indice <- i\n   8:         end if\n   9:     end for\n  10:     aux <- V[j]\n  11:     V[j] <- V[indice]\n  12:     V[indice] <- aux\n  13:     ORDENACAO-POR-SELECAO(V, j-1)\n  14: end if\n\nConsidere a chamada ORDENACAO-POR-SELECAO(V, j) e conte o trabalho feito fora da recursao:"),
]


# ══════════ LOTE 7 — Prova 2025, auditoria de 06/10/2026 ══════════
PATCHES += [

# 3(c) — "domina assintoticamente" foi lido como o(g); nos slides do Loureiro é |f| <= c|g| (um O).
# A resposta V não muda (a dominância não é usada); muda a observação lateral, que ficava falsa.
("PROVA-B","3c",
 "a hipótese de que g DOMINA assintoticamente f (isto é, f(n) = o(g(n)), ou f(n)/g(n) -> 0) NÃO foi utilizada",
 "a hipótese de que g DOMINA assintoticamente f (nos slides do Loureiro: existem constantes positivas C e m tais que |f(n)| <= C*|g(n)| para todo n >= m — isto é, f(n) = O(g(n)), e NÃO f(n) = o(g(n)); a letra C, maiúscula, para não colidir com a testemunha c = 1 acima) NÃO foi utilizada"),
("PROVA-B","3c",
 "como f(n) <= g(n) a partir de certo ponto, tem-se g(n) <= f(n) + g(n) <= 2g(n).",
 "como f(n) <= C*g(n) para n >= m (a constante C da definição, que pode ser maior que 1), tem-se, para todo n >= max(N, m) — faixa em que f e g são positivas, de modo que o módulo pode ser retirado —, g(n) <= f(n) + g(n) <= (1 + C)*g(n)."),

# 4(b) — o mesmo erro de definição, e a mesma conta com a constante errada
("PROVA-B","4b",
 "a hipótese de que g DOMINA assintoticamente f (f(n) = o(g(n))) NÃO foi usada",
 "a hipótese de que g DOMINA assintoticamente f (nos slides do Loureiro: |f(n)| <= C*|g(n)| para todo n >= m, com C e m constantes positivas — ou seja, f(n) = O(g(n)); C maiúscula para não colidir com a testemunha c = 1) NÃO foi usada"),
("PROVA-B","4b",
 "como f(n) = o(g(n)) implica f(n) <= g(n) a partir de certo ponto N', temos, para n >= max(N, N'),\n  1*g(n) <= f(n) + g(n) <= 2*g(n),",
 "como a dominância dá f(n) <= C*g(n) para todo n >= m, temos, para n >= max(N, m),\n  1*g(n) <= f(n) + g(n) <= (1 + C)*g(n),"),
("PROVA-B","4b",
 "Isso, aliás, também dá Omega(f(n)), já que g(n) >= f(n) nessa faixa.",
 "Isso, aliás, também dá Omega(f(n)) por outro caminho, já que f(n) + g(n) >= g(n) >= (1/C)*f(n) nessa faixa."),

# 4(a) — 99,82 é a raiz de 15 n lg n + 20 = n², não da equação n/lg n = 15 que o texto escreve (raiz 99,56)
("PROVA-B","4a",
 "ou seja, o cruzamento ocorre em n ~ 99,82, ENTRE 99 e 100 — não 'exatamente em 100'.",
 "ou seja, a raiz de n / lg n = 15 está em n ~ 99,56, ENTRE 99 e 100 — não 'exatamente em 100'. (Com o termo +20 incluído, isto é, resolvendo 15*n*lg n + 20 = n^2, o cruzamento exato das duas funções do exemplo fica em n ~ 99,82 — também entre 99 e 100.)"),

# 5(a) — o formulário exige f(n) = c*n^k exatamente; o enunciado dá Θ(n). Faltava a ponte.
("PROVA-B","5a",
 "  T_A(n) = Theta(n^k) = Theta(n).\n\nIntuição / verificação",
 "  T_A(n) = Theta(n^k) = Theta(n).\n\nHIPÓTESE DO FORMULÁRIO. O teorema impresso na prova exige f(n) = c*n^k EXATAMENTE, e o enunciado só diz que combinar custa Theta(n). SUPOSIÇÃO (declarada, como a instrução 2 da prova pede quando o enunciado é omisso): o custo de combinar é positivo em todo n >= 1 — toda combinação executa ao menos uma operação. A ponte: como esse custo é Theta(n) e positivo, existem constantes 0 < c1 <= c2 com c1*n <= f(n) <= c2*n para todo n >= 1 (os finitos n abaixo do n0 do Theta são absorvidos ajustando c1 e c2). Defina T_inf(n) = T_inf(n/5) + c1*n e T_sup(n) = T_sup(n/5) + c2*n, com o mesmo caso base T_A(1). Por indução sobre n = 5^j, T_inf(n) <= T_A(n) <= T_sup(n): na base as três são iguais, e no passo T_A(n) = T_A(n/5) + f(n) fica entre T_inf(n/5) + c1*n e T_sup(n/5) + c2*n. As duas recorrências extremas já têm a forma exata do formulário (a = 1, b = 5, k = 1, c = c1 ou c2), com n potência exata de 5, e expandindo dão T_sup(n) = T_A(1) + c2*(5n - 5)/4, que é não decrescente; o mesmo para T_inf. Logo ambas são Theta(n), e T_A, presa entre elas, também é — para n potência exata de 5, que é exatamente o domínio que o formulário supõe. Testemunhas explícitas, das formas fechadas: para n potência de 5 com n >= 5, T_A(n) >= T_inf(n) = T_A(1) + c1*(5n - 5)/4 >= c1*n (pois 5n - 5 >= 4n quando n >= 5), e T_A(n) <= T_sup(n) = T_A(1) + c2*(5n - 5)/4 <= (T_A(1) + 5*c2/4)*n. Logo c1' = c1, c2' = T_A(1) + 5*c2/4 e n0 = 5 (em n = 5: T_inf(5) = T_A(1) + 5*c1 >= 5*c1, e T_sup(5) = T_A(1) + 5*c2 <= 5*T_A(1) + 25*c2/4).\n\nIntuição / verificação"),
("PROVA-B","5a",
 "No caso geral T_B(n) = c*n + d com d >= 0, valem c1 = c e c2 = c + d com n0 = 1, já que c*n <= c*n + d <= (c+d)*n para n >= 1 (conferindo em n = 1: c <= c + d <= c + d, correto).",
 "No caso geral T_B(n) = c*n + d, o sinal de d = T_B(1) - c é qualquer (o caso base pode custar menos que uma combinação), mas c + d = T_B(1) > 0. Escreva T_B(n)/n = c*(n-1)/n + T_B(1)/n: é uma média ponderada de c e T_B(1), com pesos (n-1)/n e 1/n. Logo, para todo n >= 1, min(c, T_B(1))*n <= T_B(n) <= max(c, T_B(1))*n, e as testemunhas são c1 = min(c, T_B(1)), c2 = max(c, T_B(1)), n0 = 1 (conferindo em n = 1: T_B(1) está entre min e max de {c, T_B(1)}, correto). Se o custo de combinar variar com n entre duas constantes 0 < c' <= c'' (é o que Theta(1) garante a partir de algum n0; os finitos n abaixo dele são absorvidos como em A, pela mesma SUPOSIÇÃO de positividade, que vale também para o custo constante de combinar de B), o mesmo argumento, feito com c' e com c'', prende T_B entre duas funções lineares."),

# 5(b) — 1,25 vs 1,00 comparava constantes de naturezas diferentes
("PROVA-B","5b",
 "1) CONSTANTES MULTIPLICATIVAS: o custo total de A é aproximadamente 5n/4 = 1,25n unidades de trabalho de combinação, enquanto o de B é aproximadamente 1,00n. Na mesma unidade de medida, B tem constante ligeiramente menor. Mas a notação Theta descarta constantes, então isso não muda a resposta assintótica.",
 "1) CONSTANTES MULTIPLICATIVAS: A gasta cerca de (5/4)*c_A*n, onde c_A é o custo POR ELEMENTO da combinação linear de A; B gasta cerca de c_B*n, onde c_B é o custo de UMA combinação de B. São constantes de naturezas diferentes, que dependem da implementação — o enunciado não permite dizer qual algoritmo tem a menor. E a notação Theta descarta constantes, então isso não muda a resposta assintótica."),
]
for _f, _i, _a, _n in PATCHES[-9:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")

# ══════════ LOTE 8 — Prova 2025, achados da reverificação de 06/10/2026 ══════════
PATCHES += [
# 5(a) — a soma infinita é cota superior da soma finita da árvore
("PROVA-B","5a",
 "  c*n * SOMA_{i>=0} (1/5)^i = c*n * 1/(1 - 1/5) = c*n * 5/4 = 1,25*c*n.\nÉ uma série geométrica DECRESCENTE: o termo do topo domina e a soma total é apenas uma constante (5/4) vezes o custo da raiz.",
 "  c*n * SOMA_{i>=0} (1/5)^i = c*n * 1/(1 - 1/5) = c*n * 5/4 = 1,25*c*n,\nque é uma COTA SUPERIOR: a árvore é finita, e a soma exata dos níveis é c*(5n - 5)/4, mais o caso base. É uma série geométrica DECRESCENTE: o termo do topo, c*n, domina: para n potência de 5 com n >= 5, a soma dos níveis fica entre c*n e no máximo 5/4 disso, fora o caso base (em n = 1 não há nível de combinação, e a soma é 0)."),
# 5(a) — a conclusão herda o domínio (7.1: corpo E resposta)
("PROVA-B","5a",
 "CONCLUSÃO DE (a): T_A(n) = Theta(n) e T_B(n) = Theta(n).",
 "CONCLUSÃO DE (a): T_A(n) = Theta(n), para n potência exata de 5 (o domínio do formulário), e T_B(n) = Theta(n), para todo n >= 1."),
]
PATCHES_RESPOSTA += [
("PROVA-B","5a",
 "Algoritmo A: Theta(n). Algoritmo B: Theta(n).",
 "Algoritmo A: Theta(n) (n potência exata de 5, como supõe o formulário). Algoritmo B: Theta(n)."),
]
for _f, _i, _a, _n in PATCHES[-2:] + PATCHES_RESPOSTA[-1:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")

# ══════════ LOTE 9 — Complementares, auditoria de 06/10/2026 ══════════
# SUBSTITUIÇÃO INTEGRAL de item (não é patch de trecho): o enunciado literal do Campello ex. 7 pergunta
# "Pode-se então concluir que esse algoritmo é Ω(1)?" — a paráfrase antiga dizia Θ(1), e a resolução
# antiga provava "não é Θ(1)", isto é, respondia a OUTRA pergunta. Nova resolução: 3 solvers
# independentes concordaram; custos 6 e 5⌊lg n⌋ + 9 conferidos por força bruta para n = 1..299.
# Guarda de identidade: só substitui se a resposta antiga for a da pergunta Θ(1) (ou já for a nova).
SUBSTITUICOES = {
("CAMPELLO","(7)"): dict(
 assinatura_antiga="Mas NÃO se pode concluir que 'o algoritmo é Theta(1)'",
 resposta="Melhor caso O(1): para todo n ≥ 1 há uma entrada (x na primeira posição consultada) que custa uma constante, 6 operações, com c = 6 e n0 = 1. Quanto à pergunta: SIM, o algoritmo é Ω(1), para toda entrada (c = 1, n0 = 1) — mas NÃO \"por ser O(1)\": O é cota superior e não implica cota inferior (1/n é O(1) e não é Ω(1)). O Ω(1) do algoritmo vem de o custo do melhor caso ser também ≥ uma constante e ser o MÍNIMO sobre todas as entradas, de modo que toda execução custa pelo menos isso. E o algoritmo NÃO é O(1): o pior caso é Θ(lg n).",
 justificativa="""MODELO DE CUSTO. Busca binária iterativa sobre A[1..n] ordenado, procurando x, cada linha executada custando 1 (um teste e a atribuição que ele dispara contam separados):
  1 esq ← 1
  2 dir ← n
  3 enquanto esq ≤ dir
  4    meio ← ⌊(esq+dir)/2⌋
  5    se A[meio] = x devolva meio
  6    senão se x < A[meio] então dir ← meio − 1
  7    senão esq ← meio + 1
  8 devolva "não encontrado"
Custos: inicialização 2; iteração que devolve (teste do laço, linha 4, teste da linha 5, retorno) 4; iteração que não devolve (teste do laço, linha 4, teste 5, teste 6, uma atribuição) 5; saída por "não encontrado" (teste falho do laço, retorno) 2. Para uma entrada I = (A, x) de tamanho n, T(I) é o custo da execução; T_melhor(n) = mín{T(I) : |I| = n} e T_pior(n) = máx{T(I) : |I| = n}. Por definição, T_melhor(n) ≤ T(I) ≤ T_pior(n) para toda I com |I| = n.

PARTE 1 — POR QUE O MELHOR CASO É O(1). Seja n ≥ 1. Como esq = 1 ≤ n = dir, toda execução entra no laço ao menos uma vez. Se a primeira iteração devolve, o custo é 2 + 4 = 6; se não devolve, é pelo menos 2 + 5 + 2 = 9 > 6. E o custo 6 é atingido para todo n ≥ 1: basta qualquer A ordenado com x = A[⌊(1+n)/2⌋], que é o primeiro meio. "Melhor caso" é a melhor composição da entrada com n fixo — não "n pequeno". Logo T_melhor(n) = 6 para todo n ≥ 1, valor que não depende de n.
  O(1): c = 6, n0 = 1, pois 0 ≤ 6 ≤ 6·1 para todo n ≥ 1; em n = n0 = 1: 6 ≤ 6.
  Também Ω(1): c = 6, n0 = 1 (0 ≤ 6·1 ≤ 6). Portanto T_melhor ∈ Θ(1), com c1 = c2 = 6, n0 = 1.
  Vale para: as entradas de melhor caso (x na posição central). Contando só comparações com elementos do vetor, o melhor caso faz 1 comparação, e as testemunhas passam a c = 1, n0 = 1; o modelo muda a constante, não a conclusão.

CONTRAPONTO — O PIOR CASO (o que NÃO se transfere). Seja m = dir − esq + 1 o tamanho do intervalo; então meio = esq + ⌊(m−1)/2⌋. Indo para a direita, o novo tamanho é dir − meio = m − 1 − ⌊(m−1)/2⌋ = ⌊m/2⌋; indo para a esquerda, é meio − esq = ⌊(m−1)/2⌋ ≤ ⌊m/2⌋. Após j iterações que não devolvem, o tamanho é no máximo ⌊n/2^j⌋ (pois ⌊⌊n/2^j⌋/2⌋ = ⌊n/2^(j+1)⌋), e uma nova iteração exige tamanho ≥ 1: há no máximo ⌊lg n⌋ + 1 iterações. A entrada com x > A[n] atinge exatamente esse número (vai sempre para a direita, com tamanhos ⌊n/2^j⌋ exatos), com custo 2 + 5(⌊lg n⌋ + 1) + 2 = 5⌊lg n⌋ + 9; nenhuma execução custa mais, porque uma iteração final que devolve custa 4 < 5 + 2. Logo T_pior(n) = 5⌊lg n⌋ + 9.
  Cota de baixo: ⌊lg n⌋ > lg n − 1 dá T_pior(n) > 5 lg n + 4 ≥ 5 lg n para n ≥ 1.
  Cota de cima: T_pior(n) ≤ 5 lg n + 9 ≤ 14 lg n quando 9 ≤ 9 lg n, isto é, n ≥ 2.
  Portanto T_pior ∈ Θ(lg n), com c1 = 5, c2 = 14, n0 = 2; em n = 2: 5 ≤ 14 ≤ 14.
  T_pior ∉ O(1): se T_pior(n) ≤ c para todo n ≥ n0, tome n ≥ máx(n0, 2^⌈c⌉); então T_pior(n) ≥ 5 lg n ≥ 5c > c — contradição.

PARTE 2 — "PODE-SE ENTÃO CONCLUIR QUE ESSE ALGORITMO É Ω(1)?" "O algoritmo é Ω(g)" significa: existem c > 0 e n0 > 0 tais que, para todo n ≥ n0 e TODA entrada I de tamanho n, T(I) ≥ c·g(n). Pela cadeia T_melhor(n) ≤ T(I) ≤ T_pior(n), isso equivale a T_melhor ∈ Ω(g); do mesmo modo, "o algoritmo é O(g)" equivale a T_pior ∈ O(g). Ou seja: uma cota INFERIOR do melhor caso vale para toda entrada; uma cota SUPERIOR do melhor caso, em geral, NÃO se transfere para as outras entradas (só quando ela também limita o pior caso).

A pergunta admite três leituras, e as três têm resposta:

(A) A inferência "o melhor caso é O(1), LOGO o algoritmo é Ω(1)" é válida? NÃO. O é cota superior e não fornece cota inferior. Contraexemplo dentro das definições do curso: f(n) = 1/n está em O(1) (c = 1, n0 = 1, pois 0 ≤ 1/n ≤ 1), mas não em Ω(1): para qualquer c > 0, todo n > 1/c dá 1/n < c. A conclusão é verdadeira por um fato ADICIONAL: T_melhor(n) = 6 > 0 — toda execução faz ao menos as linhas 1 a 4. Esse fato é a parte Ω do Θ(1) do melhor caso, não a parte O.

(B) O algoritmo (em toda entrada) é Ω(1)? SIM — é a leitura pretendida. Para todo n ≥ 1 e toda I com |I| = n, T(I) ≥ T_melhor(n) = 6 ≥ 1·1. Testemunhas c = 1 (ou c = 6), n0 = 1; em n = 1: 1 ≤ 6. Vale para toda entrada. A justificativa é que o melhor caso é limite inferior de todas as execuções: o que se transfere é a cota inferior do melhor caso, não o "O(1)".

(C) O pior caso é Ω(1)? Sim, mas é uma afirmação fraca: T_pior(n) ≥ 6 ≥ 1 (c = 1, n0 = 1); a cota justa é Ω(lg n), com c = 5, n0 = 1.

O que a pergunta testa: saber QUAL cota do melhor caso "sobe" para o algoritmo inteiro. A resposta é "sim, é Ω(1), porque nenhuma entrada custa menos que o melhor caso" — com dois complementos: NÃO se pode concluir que o algoritmo é O(1) (o pior caso é Θ(lg n)), e, pelo mesmo motivo, também NÃO se pode dizer que ele é Ω(lg n) (a entrada de melhor caso custa 6).

RESUMO
  T_melhor ∈ Θ(1)       c1 = c2 = 6, n0 = 1     entradas de melhor caso
  algoritmo ∈ Ω(1)      c = 1, n0 = 1           toda entrada
  algoritmo ∈ O(1)      FALSO                   falha no pior caso
  T_pior ∈ Θ(lg n)      c1 = 5, c2 = 14, n0 = 2 pior caso (ex.: x > A[n])
  algoritmo ∈ O(lg n)   c = 14, n0 = 2          toda entrada

Conferência: o modelo acima foi executado por força bruta para n = 1..299 com todos os x possíveis (presentes e ausentes, entre e fora dos elementos): o mínimo foi 6 e o máximo 5⌊lg n⌋ + 9 em todos os n, e x > A[n] sempre atinge o máximo. O caso n = 0 fica fora por n0 = 1 (nele o custo seria 4, o que não altera nada)."""),
}

def substitui(sol):
    """Substituição integral de itens (ver LOTE 9). Devolve quantos substituiu; aborta se a guarda falhar."""
    n = 0
    for (fonte, item), s in SUBSTITUICOES.items():
        it = sol.get(fonte, {}).get(item)
        if it is None:
            continue
        if it["justificativa"] == s["justificativa"] and it["resposta"] == s["resposta"]:
            continue
        if s["assinatura_antiga"] not in it["resposta"] + it["justificativa"]:
            raise SystemExit(f"correcoes.py: {fonte} {item} não é o item esperado — substituição recusada")
        it["resposta"], it["justificativa"] = s["resposta"], s["justificativa"]
        n += 1
    return n

# ══════════ LOTE 9b — Complementares, onda A de 06/10/2026 (achados [matemático/lógico], baixa) ══════════
PATCHES += [
# Loureiro ex. 5 — a árvore tem lg n + 1 níveis, e a soma dos lg n internos (n² − n) deixa de fora as
# folhas, que são justamente o nível que domina. Conferido: (n² − n) + n²·T(1) = T(n) para n = 2^0..2^11.
("LOUREIRO","(5)",
 "A arvore tem log_2 n niveis, o nivel i tem 4^i subproblemas de tamanho n/2^i com custo n/2^i cada, ou seja 2^i * n por nivel; a soma geometrica e dominada pelo ultimo nivel, que vale Theta(n^2).",
 "A arvore tem log_2 n + 1 niveis (profundidades 0..log_2 n). Cada nivel interno i < log_2 n tem 4^i subproblemas de tamanho n/2^i com custo n/2^i cada, ou seja 2^i * n por nivel, e esses niveis somam n + 2n + ... + (n/2)*n = n^2 - n. O nivel das folhas tem 4^(log_2 n) = n^2 nos de custo T(1) cada, ou seja n^2 * T(1). A soma geometrica e dominada pelo fundo da arvore: o total e n^2 - n + n^2 * T(1) = Theta(n^2), com T(1) > 0 constante (com T(1) = 1, T(n) = 2n^2 - n)."),
# Campello ex. 4 — com o lg impresso (15,9372) o produto é 999.995,55, não 999.997,8: a conta impressa não fechava.
("CAMPELLO","(4)",
 "Ex.: lg(62.746) = 15,9372, logo 62.746 * 15,9372 = 999.997,8 <= 10^6;",
 "Ex.: lg(62.746) ~ 15,937236, logo 62.746 * lg(62.746) ~ 999.997,8 <= 10^6;"),
]
for _f, _i, _a, _n in PATCHES[-2:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")

# IFMG ex. 5 (onda A, 06/10/2026): (i) "custo unitário (cada operação custa 1)" é falso — contando 1 por
# operação, T(1) = 2 e uma chamada custa ~2j + 7; a = b = c = 1 é escolha ilustrativa. (ii) a recorrência
# EXATA com um único a não vale para toda entrada (a linha 7 roda 0..j−1 vezes): vale o PAR de cotas, e a
# forma Θ. Corpo E linha Resposta (7.1).
PATCHES += [
("IFMG","(5)",
 "Agrupando as parcelas constantes numa constante b > 0, o trabalho local e a*j + b.",
 "Agrupando as parcelas constantes numa constante b > 0, o trabalho local fica entre a1*j + b e a2*j + b. Abaixo escrevo a*j + b, com a valendo a1 (para a cota inferior) ou a2 (para a cota superior): a conta e a mesma nos dois casos, e os dois resultados sao Theta(n^2)."),
("IFMG","(5)",
 "Portanto a recorrencia acima vale para TODA entrada, e o resultado assintotico e o mesmo em todos os casos.",
 "Portanto, para TODA entrada, T(j) - T(j-1) fica entre a1*j + b e a2*j + b: o custo EXATO depende do vetor (pela linha 7), mas a forma T(n) = T(n-1) + Theta(n) vale para toda entrada, e o resultado assintotico e o mesmo em todos os casos."),
("IFMG","(5)",
 "TESTEMUNHAS EXPLICITAS. Tomando o custo unitario a = b = c = 1 (cada operacao elementar custa 1), a expressao acima da",
 "TESTEMUNHAS EXPLICITAS. Tomando, para ilustrar, a = b = c = 1 (valores escolhidos para simplificar a conta, e NAO o custo de contar 1 por operacao elementar: com essa contagem, o caso base ja custa 2 — teste e return — e uma chamada custa cerca de 2j + 7), a expressao acima da"),
("IFMG","(5)",
 "CONFERENCIA. Com o custo unitario a = b = c = 1 adotado acima,",
 "CONFERENCIA. Com a = b = c = 1, os valores ilustrativos adotados acima,"),
]
PATCHES_RESPOSTA += [
("IFMG","(5)",
 "no melhor e no pior caso (o custo nao depende do conteudo do vetor).",
 "no melhor e no pior caso (a ORDEM de crescimento nao depende do conteudo do vetor: o laco sempre faz j iteracoes e j comparacoes; so o numero de execucoes da linha 7 varia, e com ele a constante a, entre a1 e a2)."),
]
for _f, _i, _a, _n in PATCHES[-4:] + PATCHES_RESPOSTA[-1:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")

# Campello ex. 5 (onda A, 06/10/2026): "n_k >= n/2^k - 1" é FALSO no ramo esquerdo (n = 6: n_2 = 0 < 0,5)
# e "só esvazia quando 2^k > n" também (n = 4 esvazia em k = 2). A conclusão (⌊lg n⌋ + 1 iterações no pior
# caso) era verdadeira; troca-se a derivação pela entrada x > A[n], que faz exatamente ⌊lg n⌋ + 1
# iterações (conferido para n = 1..10^5). A linha Resposta (Θ(lg n)) não muda.
PATCHES += [
("CAMPELLO","(5)",
 "Considere a entrada em que x não pertence a A. Cada iteracao deixa pelo menos piso((n_k - 1)/2) elementos, pois os dois ramos tem tamanhos piso((n_k-1)/2) e piso(n_k/2). (Nao vale dizer 'descarta no maximo metade': com n_k = 4 o ramo esquerdo deixa 1 de 4, isto e, descarta 75%.) Dessa recorrencia segue n_k >= n/2^k - 1, de modo que o intervalo so se esvazia quando 2^k > n, isto e, apos pelo menos piso(lg n) iteracoes. Como cada iteração custa pelo menos a' > 0, temos T_pior(n) >= a'*piso(lg n) >= (a'/2)*lg n para n >= 2 (pois piso(lg n) >= lg(n)/2 quando n >= 2). Testemunhas: c1 = a'/2 e n0 = 2, logo T_pior(n) = Omega(lg n).",
 "Para a cota inferior do PIOR caso basta exibir UMA entrada cara: tome x > A[n] (x maior que todos os elementos). Entao toda comparacao manda a busca para a direita, e o novo intervalo tem tamanho piso(n_k/2); como piso(piso(n/2^k)/2) = piso(n/2^(k+1)), apos k iteracoes o tamanho e exatamente piso(n/2^k), que e >= 1 se e somente se 2^k <= n. Logo essa entrada faz exatamente piso(lg n) + 1 iteracoes (conferido para n = 1..10^5). Pelo ramo esquerdo, de tamanho piso((n_k - 1)/2), o intervalo pode esvaziar antes (com n = 4, em 2 iteracoes); por isso a cota usa a entrada x > A[n], e nao 'qualquer x ausente'. Como cada iteracao custa pelo menos a' > 0, temos T_pior(n) >= a'*(piso(lg n) + 1) >= a'*lg n para todo n >= 1 (pois piso(lg n) + 1 > lg n). Testemunhas: c1 = a' e n0 = 1 (em n = 1: a'*1 >= a'*0), logo T_pior(n) = Omega(lg n)."),
]
if PATCHES[-1][2] in PATCHES[-1][3]:
    raise SystemExit("correcoes.py: `antigo` é substring de `novo` em CAMPELLO (5) — duplicaria (7.10)")

# ══════════ LOTE 9c — Complementares, onda B de 06/10/2026: FRASES LATERAIS (7.15 de novo) ══════════
# Nenhuma conta mudou; as quatro correções são de afirmações gerais falsas em comentários.
PATCHES += [
# Loureiro ex. 5 — "folhas dominam => Caso 1" é necessária, não suficiente (contraexemplo f = n^2/lg^2 n:
# as folhas dominam, mas f não é O(n^(2−eps))). E a forma fechada 2n^2 − n só vale para n potência de 2.
("LOUREIRO","(5)",
 "O teorema compara os dois: se as folhas dominam, vale Caso 1; se empatam, Caso 2 (aparece o fator lg n, que conta os niveis); se a raiz domina (e o domínio e 'estavel', o que a regularidade garante), Caso 3.",
 "O teorema compara os dois, mas exige folga POLINOMIAL: se f(n) fica abaixo de n^E por um fator n^eps, vale o Caso 1; se f(n) = Theta(n^E), o Caso 2 (aparece o fator lg n, que conta os niveis); se f(n) fica acima de n^E por um fator n^eps e vale a regularidade, o Caso 3. Entre os casos ha lacunas em que o teorema nao se aplica, por exemplo f(n) = n^E / lg n ou f(n) = n^E * lg n: nao basta 'as folhas dominarem'."),
("LOUREIRO","(5)",
 "com T(1) > 0 constante (com T(1) = 1, T(n) = 2n^2 - n).",
 "com T(1) > 0 constante (para n potencia de 2 e T(1) = 1, T(n) = 2n^2 - n; fora das potencias de 2, com piso ou teto, a forma fechada muda, mas a classe Theta(n^2) nao)."),
# Campello ex. 8 — duas afirmações laterais falsas.
("CAMPELLO","(8)",
 "Só é exponencial de verdade quando o expoente é proporcional a n, não a log n.",
 "Quando o expoente é c·lg n, a função é polinomial (2^(c lg n) = n^c); para crescer como uma exponencial b^n, o expoente precisa crescer pelo menos linearmente em n."),
("CAMPELLO","(8)",
 "confirmam a monotonia da ordem (por exemplo, (n log n)/n^2 decrescente para 0; 27^n/2^n = 13,5^n explodindo)",
 "confirmam a ordem assintótica (por exemplo, (n log n)/n^2 tende a 0, decrescente só a partir de n = 3; 27^n/2^n = 13,5^n explodindo). Para n pequeno a ordem pode se inverter: n^3 > 2^n para n = 2..9"),
# Campello ex. 4 — confundia o VALOR de n com o TAMANHO de n (2^(10^6) + 1 ocupa ~125 KB).
("CAMPELLO","(4)",
 "Para uma entrada logarítmica, portanto, o gargalo deixa de ser o tempo e passa a ser a própria representação de n.",
 "Escrever o número n ainda é possível (2^(10^6) ocupa cerca de 125 KB); o que é fisicamente impossível é uma ENTRADA com n elementos. Para f(n) = lg n, portanto, nenhuma entrada que se possa de fato armazenar chega perto do limite: o gargalo passa a ser armazenar ou ler a entrada, não o tempo de f(n)."),
]
PATCHES_RESPOSTA += [
("CAMPELLO","(4)",
 "para f(n) = log n o limite não é o tempo (qualquer n representável cabe já em 1 segundo)",
 "para f(n) = log n o limite não é o tempo (nenhuma entrada com n elementos que se possa de fato armazenar chega perto do maior n, que é 2^t)"),
("CAMPELLO","(8)",
 "(Os sinais '=' indicam funções que são Theta uma da outra, isto é, empatadas.)",
 "(Os sinais '=' indicam funções Theta uma da outra, isto é, empatadas; log na base 2, como no material. Em base b > 2, como 10 ou e, 2^(log_b n) = n^(log_b 2) sai do empate com 4n e fica estritamente entre 2^10 e 4n.)"),
]
for _f, _i, _a, _n in PATCHES[-5:] + PATCHES_RESPOSTA[-2:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")
# Walace ex. 1 — o cancelamento NÃO é "o coração do método": na soma geométrica S_n reaparece e é isolado
# (é assim que o próprio slide resolve). E "devolve a fórmula" de expoente k−1 só vale conhecendo as menores.
PATCHES += [
("SOMATORIOS","1",
 "Esse cancelamento e o coracao do metodo: ele nao resolve a propria soma, ele a REDUZ a somas de grau inferior.",
 "O objetivo geral do metodo e fazer S_n reaparecer do lado direito e isola-lo: e assim que se resolve a soma geometrica: com S_n = soma de x^i para i = 0 ate n, a perturbacao da S_n + x^(n+1) = 1 + x*S_n, e dai S_n = (x^(n+1) - 1)/(x - 1) para x diferente de 1. Quando, como aqui, a_{i+1} = a_i + termos de ordem menor, o S_n CANCELA: o metodo entao nao fornece S_n, mas uma relacao entre somas de grau inferior."),
("SOMATORIOS","1",
 "Em geral, perturbar a soma das potencias de expoente k devolve a formula da soma das potencias de expoente k-1.",
 "Em geral, perturbar a soma das potencias de expoente k devolve uma equacao para a soma de expoente k-1, que se resolve usando as somas de expoente menor ja conhecidas."),
]
for _f, _i, _a, _n in PATCHES[-2:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")
# USP ex. 2.4 (onda B): "Não há como construir esse mínimo diretamente por indução" é FALSO — há prova
# direta: Q(n) = "todo S ⊆ Z+ com S ∩ {1..n} ≠ ∅ tem mínimo" (conferida nos 1023 subconjuntos de {1..10}).
PATCHES += [
("USP","2.4",
 "Nao ha como construir esse minimo diretamente por inducao, porque inducao percorre os inteiros de baixo para cima, e nao os elementos de S. O truque e inverter:",
 "Uma forma natural de prova-lo, a adotada aqui, e inverter:"),
("USP","2.4",
 "e mostrar que a ausencia de minimo obriga cada um desses inteiros a ficar de fora de S.",
 "e mostrar que a ausencia de minimo obriga cada um desses inteiros a ficar de fora de S. (Ha tambem uma prova direta, sem absurdo: com Q(n) = 'todo S contido em Z+ que tem algum elemento em {1, ..., n} possui minimo', a base vale porque, se 1 esta em S, 1 e o minimo; no passo, se S tem elemento em {1, ..., n} aplica-se a hipotese, e senao n+1 esta em S e e o minimo. Como S e nao-vazio, contem algum k, e Q(k) da o minimo. Nas duas provas, 'minimo' (menor que todos) implica 'minimal' (nenhum menor), que e o que o enunciado pede; em Z+, ordem total, os dois coincidem.)"),
]
for _f, _i, _a, _n in PATCHES[-2:]:
    if _a in _n and _f == "USP" and _a.startswith("Nao ha"):
        raise SystemExit("correcoes.py: `antigo` ⊂ `novo` em USP 2.4 — duplicaria (7.10)")
# Campello ex. 4 (onda C): "acrescenta lg k" só vale para 2^n; para b^n o ganho é log_b k
# (conferido: 1 s -> 1 século dá +32 para 2^n, +20 para 3^n, +9 para 10^n).
PATCHES += [
("CAMPELLO","(4)",
 "Num algoritmo exponencial, o mesmo fator k só acrescenta lg k ao tamanho tratável",
 "Num algoritmo exponencial b^n, o mesmo fator k só acrescenta cerca de log_b k ao tamanho tratável (lg k para 2^n)"),
]
if PATCHES[-1][2] in PATCHES[-1][3]:
    raise SystemExit("correcoes.py: `antigo` ⊂ `novo` em CAMPELLO (4) — duplicaria (7.10)")

# ══════════ LOTE 9d — Complementares, onda D de 06/10/2026: remissões internas e Θ com expoente arredondado ══════════
# "item (5)" apontava para a questão errada: nos complementares o Loureiro ex. 5 é a questão 1, e a 5 é do
# Campello; no banco, é a 75. Troca-se por rótulos de fonte. E Θ(n^2,807355) ≠ Θ(n^(log_2 7)), porque
# log_2 7 = 2,80735492... < 2,807355: igualdade de classe com expoente arredondado é literalmente falsa.
PATCHES += [
("LOUREIRO","(6)", "Mesmo Teorema Mestre enunciado no item (5).", "Mesmo Teorema Mestre (forma do CLRS, a do slide) enunciado na resolucao do Loureiro, ex. 5."),
("LOUREIRO","(7)", "Mesmo Teorema Mestre enunciado no item (5).", "Mesmo Teorema Mestre (forma do CLRS, a do slide) enunciado na resolucao do Loureiro, ex. 5."),
("LOUREIRO","(8)", "Mesmo Teorema Mestre enunciado no item (5).", "Mesmo Teorema Mestre (forma do CLRS, a do slide) enunciado na resolucao do Loureiro, ex. 5."),
("LOUREIRO","(6)", "ele nao aparece nos itens (5) e (7).", "ele nao aparece nos exercicios 5 e 7 do Loureiro."),
("IFMG","(3)", "(ver o item (4))", "(ver o IFMG, ex. 4)"),
("IFMG","(4)", "do item (3)", "do IFMG, ex. 3"),
("LOUREIRO","(8)",
 "E, de fato, para a = 48: T'(n) = Theta(n^2,792481) e T(n) = Theta(n^2,807355); a razao T'(n)/T(n) = Theta(n^(-0,014874)) -> 0",
 "E, de fato, para a = 48: T'(n) = Theta(n^(log_4 48)) e T(n) = Theta(n^(log_2 7)), com log_4 48 ~ 2,792481 e log_2 7 ~ 2,807355; a razao T'(n)/T(n) = Theta(n^(log_4 48 - log_2 7)), com expoente ~ -0,014874 < 0, logo -> 0"),
]
for _f, _i, _a, _n in PATCHES[-7:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")

# ══════════ LOTE 9e — Complementares, onda E: coerência de símbolos e regra geral (7.4, 7.16) ══════════
PATCHES += [
# Campello ex. 4 — k^(1/grau) só é exato (a menos de pisos) para n^grau puro; a linha log n é analítica, não
# busca binária; e raiz(3*10^9) = 54.772, não 56.000 (56.157 é raiz de 3,1536*10^9, o fator de fato).
("CAMPELLO","(4)",
 "aumenta o tamanho tratável por um fator k^(1/grau) — um ganho MULTIPLICATIVO",
 "aumenta o tamanho tratável por um fator de cerca de k^(1/grau) (exato, a menos de pisos, para f(n) = n^grau; para um polinômio com termos de ordem menor, só para t grande) — um ganho MULTIPLICATIVO"),
("CAMPELLO","(4)",
 "Conferência: todas as células foram obtidas por busca binária sobre n verificando f(n) <= t",
 "Conferência: a linha log n é analítica (n = 2^t); as demais células foram obtidas por busca binária sobre n verificando f(n) <= t"),
("CAMPELLO","(4)", "multiplicado por raiz(3*10^9) ~ 56.000", "multiplicado por raiz(3,1536*10^9) ~ 56.157"),
("CAMPELLO","(4)", "multiplicado por (3*10^9)^(1/3) ~ 1.466", "multiplicado por (3,1536*10^9)^(1/3) ~ 1.466"),
# Campello ex. 5 — c2 declarado e nunca usado (7.4); n_0 = tamanho inicial colidia com o n0 da definição
# (7.16); b era custo fixo e base do log ao mesmo tempo.
("CAMPELLO","(5)",
 "Tome n0 = 2 e c2 = 2a + b (o indice evita colisao com a constante da cota inferior, no Passo 4).",
 "Tome n0 = 2 e c = 2a + b (a cota inferior, no Passo 4, usa outra letra: c1)."),
("CAMPELLO","(5)", "(portanto n_0 = n)", "(portanto, no início, o tamanho é n)"),
("CAMPELLO","(5)", "(Base: n_0 = n = n/2^0.", "(Base: com k = 0, o tamanho é n = n/2^0."),
("CAMPELLO","(5)",
 "log_b n = lg n / lg b, e 1/lg b é constante positiva",
 "log_B n = lg n / lg B, e 1/lg B é constante positiva para toda base B > 1"),
]
for _f, _i, _a, _n in PATCHES[-8:]:
    if _a in _n:
        raise SystemExit(f"correcoes.py: `antigo` é substring de `novo` em {_f} {_i} — duplicaria (7.10)")
