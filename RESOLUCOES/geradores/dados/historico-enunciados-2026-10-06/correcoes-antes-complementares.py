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
