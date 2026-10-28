# -*- coding: utf-8 -*-
"""
Patches aplicados as saidas dos solvers da Lista 4, com o motivo de cada um.
Cada patch veio de um verificador adversarial em contexto limpo, cego ao raciocinio
do solver e aos demais verificadores. Mesmo formato de RESOLUCOES/geradores/correcoes.py.

Rodar:  python3 correcoes-lista04.py   (a partir deste diretorio)
"""
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PATCHES = []
# Patches da rodada 1 cujo trecho foi REESCRITO por um patch da rodada 2.
# Nesses, nem `antigo` nem `novo` batem com o arquivo atual - e isso e esperado.
SUPERSEDED = {("q3-limpo.md", 4): 11, ("q3-limpo.md", 5): 10, ("q3-limpo.md", 9): 12,
              ("q2-limpo.md", 2): 3, ("q3-limpo.md", 6): 13, ("q4-slide-limpo.md", 1): 6,
              ("q2-limpo.md", 5): 6, ("q2-limpo.md", 6): 7,
              ("q3-limpo.md", 13): 21, ("q3-limpo.md", 14): 22, ("q3-limpo.md", 15): 17,
              ("q3-limpo.md", 11): 18, ("q3-limpo.md", 12): 23,
              ("q3-limpo.md", 1): 24, ("q3-limpo.md", 2): 26,
              ("q3-limpo.md", 17): 27}

def patch(arquivo, motivo, achado_por, gravidade, antigo, novo, superseded_por=None):
    """superseded_por: numero do patch de uma rodada posterior que reescreveu este
    mesmo trecho. Nesses casos nem `antigo` nem `novo` batem com o arquivo atual, e
    isso e esperado, nao falha."""
    PATCHES.append(dict(arquivo=arquivo, motivo=motivo, achado_por=achado_por,
                        gravidade=gravidade, antigo=antigo, novo=novo,
                        superseded_por=superseded_por))

# =====================================================================
# QUESTAO 3 - REFUTADA: dois verificadores independentes deram HOLE_FOUND
# =====================================================================

patch("q3-limpo.md",
      "O criterio 'T1 in A inter B' e SUFICIENTE, nao necessario. Depois de aplicar P(k) a A "
      "(que contem T1), TODO elemento de A passa a ser sabidamente chines; logo basta "
      "A inter B != vazio. Contraexemplo enumerado (k=3): A={T1,T2,T3}, B={T2,T3,T4} funciona "
      "sem T1 em B. Nesta construcao as duas condicoes coincidem (|A inter B| = k-1), entao o "
      "limiar k>=2 e o veredito nao mudam - mas a questao pede justificativa FORMAL e o corpo "
      "vendia o criterio errado como 'formulacao precisa'. Agravante: a secao RESPOSTA ja usava "
      "a formulacao CERTA - corpo e resposta divergiam (armadilha 7.1 do CLAUDE.md, invertida).",
      "verificadores Q3-A e Q3-B (independentes, mesmo achado)", "media",
"""3.2 A condição exata de aplicabilidade da hipótese. P(k) é uma implicação. Aplicá-la a um
conjunto X com |X| = k só produz "todos de X são chineses" se o antecedente estiver verificado
para X, isto é, se soubermos que X contém pelo menos uma pessoa chinesa. Ter |X| = k não basta.
No cenário do passo, a única pessoa de quem se sabe a priori a nacionalidade é T1. Portanto o
passo exige T1 ∈ A e T1 ∈ B, isto é T1 ∈ A ∩ B. E
  A ∩ B = S∖{T_k, T_{k+1}} = {T1, …, T_{k−1}},  com |A ∩ B| = k − 1.
Logo T1 ∈ A ∩ B se e somente se k − 1 ≥ 1, ou seja k ≥ 2.
Formulação precisa do defeito (não a versão genérica "os dois subconjuntos podem não se
intersectar"): o passo requer que cada um dos dois subconjuntos de tamanho k contenha uma pessoa
sabidamente chinesa; como a única testemunha disponível é T1, isso equivale a exigir
T1 ∈ A ∩ B, o que a construção só garante para k ≥ 2.""",
"""3.2 A condição exata de aplicabilidade da hipótese. P(k) é uma implicação. Aplicá-la a um
conjunto X com |X| = k só produz "todos de X são chineses" se o antecedente estiver verificado
para X, isto é, se soubermos que X contém pelo menos uma pessoa chinesa. Ter |X| = k não basta.
A sutileza é que a lista de pessoas sabidamente chinesas CRESCE ao longo do argumento. No início
a única testemunha é T1; mas ao aplicar P(k) a A, que contém T1, todo elemento de A passa a ser
sabidamente chinês — e então qualquer elemento de A ∩ B serve de testemunha para a segunda
aplicação. A condição realmente exigida pelo passo encadeado é, portanto,
  T1 ∈ A   e   A ∩ B ≠ ∅.
(Exigir T1 ∈ A ∩ B também funcionaria, mas é forte demais: para k = 3 o par A = {T1,T2,T3},
B = {T2,T3,T4} fecha o passo sem que T1 esteja em B.)
Na construção do texto as duas condições coincidem, e a conta é imediata:
  A ∩ B = S∖{T_k, T_{k+1}} = {T1, …, T_{k−1}},  com |A ∩ B| = k − 1.
Logo A ∩ B ≠ ∅ se e somente se k − 1 ≥ 1, ou seja k ≥ 2. A cardinalidade nem depende da
rotulação: |A| = |B| = k e |A ∪ B| = k + 1 forçam |A ∩ B| = 2k − (k+1) = k − 1.""")

patch("q3-limpo.md",
      "'tem uma leitura unica' e afirmacao de unicidade sem prova (#40). A secao 3.4 ja fecha "
      "o buraco por exaustao, entao a unicidade nem e necessaria ao argumento.",
      "verificador Q3-A", "baixa",
"""3.1 Reconstrução do passo. O texto não escreve o passo genérico (diz "a generalização … é a
prova desejada"), mas a construção exibida em 3 → 4 tem uma leitura única. Generalizando:""",
"""3.1 Reconstrução do passo. O texto não escreve o passo genérico (diz "a generalização … é a
prova desejada"), mas a construção exibida em 3 → 4 tem uma generalização natural — e a §3.4
mostra que a conclusão não depende de qual generalização se adote. Generalizando:""")

patch("q3-limpo.md",
      "Espelha o patch de 3.2: o criterio certo e disjuncao, nao 'um contem T1 e o outro nao'.",
      "verificador Q3-A", "media",
"""dois elementos distintos de um conjunto de k+1 = 2 elementos, os subconjuntos resultantes são
forçosamente os singletons {T1} e {T2}: um contém T1 e o outro não. Para k = 1 a falha é
estrutural, não um azar de rotulação.""",
"""dois elementos distintos de um conjunto de k+1 = 2 elementos, os subconjuntos resultantes são
forçosamente os singletons {T1} e {T2}, que são disjuntos — e sem interseção não há como
transportar testemunha de um subconjunto para o outro, qualquer que seja a rotulação. Para
k = 1 a falha é estrutural, não um azar de rotulação.""")

patch("q3-limpo.md",
      "'para todo k >= 2, P(k) e falsa' e literalmente FALSA num mundo de populacao finita N: "
      "para k > N nao existe conjunto de k pessoas e P(k) fica vacuamente VERDADEIRA (o "
      "verificador mediu: com N=5, P(6)=P(7)=V). A conclusao sobrevivia, mas pela razao que o "
      "texto nao dava. Como o passo k>=2 e VALIDO (vale em todo modelo), a escolha do mundo e "
      "irrelevante: basta exibir um mundo com um chines e um nao-chines.",
      "verificador Q3-B", "media",
"""Por que "base válida + passo válido para quase todo k" não basta — argumento de contramodelo.
Considere o mundo concreto em que T1 é chinês e todas as demais pessoas não são. Nesse mundo:
 - P(1) é verdadeira (a base vale);
 - para todo k ≥ 2, P(k) é falsa, logo a implicação P(k) → P(k+1) é verdadeira por vacuidade
   (todos os passos a partir de k = 2 valem);
 - e, no entanto, ∀n P(n) é falsa.
Como existe um modelo que satisfaz todas as premissas oferecidas e refuta a conclusão, essas
premissas não implicam a conclusão. E, coerentemente, a única implicação da cadeia que é falsa
nesse modelo é exatamente P(1) → P(2), a que o texto não demonstrou.""",
"""Por que "base válida + passo válido para quase todo k" não basta — argumento de contramodelo.
Tome qualquer mundo com ao menos uma pessoa chinesa e ao menos uma não-chinesa; por exemplo,
T1 chinês e T2 brasileiro. Confira nele as premissas oferecidas, uma a uma:
 - P(1) é verdadeira, logo a base vale (de fato P(1) é verdadeira em todo mundo);
 - P(k) → P(k+1) vale para todo k ≥ 2, logo o passo vale — a derivação da §3.1 é correta
   sempre que k ≥ 2, qualquer que seja o mundo;
 - e, no entanto, ∀n P(n) é falsa, pois P(2) falha pelo contraexemplo da §2.
Como existe um modelo que satisfaz todas as premissas oferecidas e refuta a conclusão, essas
premissas não implicam a conclusão — nenhuma reescrita da prova poderia salvá-la. E,
coerentemente, a única implicação da cadeia que é falsa nesse modelo é exatamente P(1) → P(2),
a que o texto não demonstrou.""")

patch("q3-limpo.md",
      "Vocabulario logico impreciso: descarrega-se HIPOTESE, nunca conclusao. A arbitrariedade "
      "de k autoriza GENERALIZACAO UNIVERSAL; quem produz a implicacao e a descarga da "
      "hipotese. A frase fundia as duas regras, num item que e uma aula sobre rigor de inducao.",
      "verificador Q3-B", "baixa",
""""seja k ≥ n0 arbitrário e suponha P(k)" — a arbitrariedade de k é o que permite descarregar a
conclusão universal ∀k (P(k) → P(k+1)). Fixando n = 3, o máximo que o texto estabelece é a
implicação concreta P(3) → P(4).""",
""""seja k ≥ n0 arbitrário e suponha P(k)". Duas regras trabalham juntas: descarregar a hipótese
P(k) é o que produz a implicação P(k) → P(k+1), e a arbitrariedade de k é o que autoriza a
generalização universal, ∀k (P(k) → P(k+1)). Fixando n = 3, nenhuma das duas se aplica — o
máximo que o texto estabelece é a implicação concreta P(3) → P(4).""")

patch("q3-limpo.md",
      "'descarregar o consequente' nao e nome de regra nenhuma. O que se descreve e AFIRMAR o "
      "consequente sem ter estabelecido o antecedente (modus ponens sem a premissa menor). "
      "A substancia estava certa; o nome, nao.",
      "verificador Q3-B", "baixa",
"""A falácia está em descarregar o consequente: a frase
"Portanto, as quatro pessoas têm nacionalidade chinesa!" é apresentada como fato categórico
quando só vale sob a hipótese não demonstrada P(3).""",
"""A falácia está em afirmar o consequente sem ter estabelecido o
antecedente — modus ponens sem a premissa menor: a frase "Portanto, as quatro pessoas têm
nacionalidade chinesa!" é apresentada como fato categórico quando só vale sob a hipótese não
demonstrada P(3).""")

patch("q3-limpo.md",
      "'O unico fato inferivel' e falso ao pe da letra (inferem-se as proprias premissas, as "
      "tautologias, e P(k)->P(n) para n>k>=2). O que se quer dizer e 'a unica instancia P(n)'.",
      "verificador Q3-B", "baixa",
      "aos outros, mas ninguém empurra o segundo. O único fato inferível dessas premissas é P(1).",
      "aos outros, mas ninguém empurra o segundo. A única instância P(n) inferível dessas\npremissas é P(1).")

patch("q3-limpo.md",
      "Atribuicao historica errada, e aparecia DUAS vezes (secao 6 e RESPOSTA). Polya (1954) "
      "levantou a falacia, mas na forma 'quaisquer n mocas tem olhos da mesma cor'; a "
      "formulacao com cavalos e creditada a Joel E. Cohen (1961). Os dois verificadores "
      "sinalizaram; o segundo confirmou em fonte.",
      "verificadores Q3-A (duvida) e Q3-B (confirmou em fonte)", "baixa",
"""### 6. O nome do padrão
É o disfarce brasileiro de um clássico: o "paradoxo" de que todos os cavalos têm a mesma cor,
popularizado por George Pólya (Induction and Analogy in Mathematics, 1954), cuja formulação
usual é "todo conjunto de n cavalos é monocromático", com base em n = 1 e passo por dois
subconjuntos de tamanho n−1. A anatomia é idêntica, inclusive no ponto de ruptura: os dois
subconjuntos de tamanho n−1 só têm elemento em comum quando n − 1 ≥ 2. Sempre que um passo
indutivo aplica a hipótese a dois subconjuntos e conclui pela união, teste imediatamente o
menor k.""",
"""### 6. O nome do padrão
É o disfarce brasileiro de um clássico. A falácia foi levantada por George Pólya em Induction
and Analogy in Mathematics (1954), na forma "quaisquer n moças têm olhos da mesma cor"; a
formulação que ficou famosa — "todos os cavalos têm a mesma cor" — é creditada a Joel E. Cohen
(1961). A anatomia é idêntica à desta questão: base em n = 1 e passo por dois subconjuntos de
tamanho n−1, que só têm elemento em comum quando n − 1 ≥ 2. Sempre que um passo indutivo aplica
a hipótese a dois subconjuntos e conclui pela união, teste imediatamente o menor k.""")

patch("q3-limpo.md",
      "Espelha na RESPOSTA os dois patches do corpo (criterio de disjuncao e atribuicao "
      "historica). O CLAUDE.md 7.1 registra que corrigir o corpo e esquecer a linha Resposta "
      "aconteceu tres vezes na sessao anterior; aqui os dois patches vao juntos.",
      "verificadores Q3-A e Q3-B", "media",
"""refuta P(2)), e o defeito está em que a hipótese de indução só pode ser aplicada a um
subconjunto que contenha alguém sabidamente chinês — condição que a construção (dois
subconjuntos de tamanho k obtidos removendo dois elementos distintos) satisfaz apenas para
k ≥ 2. Assim o elo P(1) → P(2) nunca é estabelecido e a cadeia indutiva se rompe logo após a
base. É a versão brasileira do paradoxo "todos os cavalos têm a mesma cor", de Pólya.""",
"""refuta P(2)), e o defeito está em que a hipótese de indução só pode ser aplicada a um
subconjunto que contenha alguém já sabidamente chinês. Como aplicá-la ao primeiro subconjunto
certifica todos os seus elementos, a condição para encadear as duas aplicações é A ∩ B ≠ ∅ — e
na construção do texto (dois subconjuntos de tamanho k obtidos removendo dois elementos
distintos) tem-se |A ∩ B| = k − 1, o que só é satisfeito para k ≥ 2. Assim o elo P(1) → P(2)
nunca é estabelecido e a cadeia indutiva se rompe logo após a base. É a versão brasileira da
falácia que Pólya levantou em 1954 e que ficou conhecida como "todos os cavalos têm a mesma
cor".""")

# =====================================================================
# EXERCICIO DO SLIDE - REFUTADO
# =====================================================================

patch("q4-slide-limpo.md",
      "COLISAO DE SIMBOLOS, gravidade media-alta. A secao 0 declara 'a' e 'b' como as "
      "constantes de CUSTO; a secao 1 redeclarava 'a = 2' e 'b = 2' como os PARAMETROS do "
      "Teorema Mestre. No mesmo paragrafo da RESPOSTA conviviam 'a = 2, b = 2' e 'custo "
      "(n+1)a + n*b' - lido ao pe da letra daria 4n+2, contradizendo o '2n+1 chamadas' da "
      "frase ao lado. Renomeados os parametros do teorema para alfa e beta. Nenhuma conta muda.",
      "verificador do exercicio do slide", "media-alta",
"""Parâmetros: a = 2 (linhas 4 e 5: esquerda E direita são visitadas); b = 2 (cada subárvore tem
≈ n/2 nós); k = 0 (o trabalho fora da recursão é constante).
Comparação: b^k = 2^0 = 1, e a = 2. Portanto a > b^k.
Conclusão (primeiro caso): T(n) = Θ(n^(log_b a)) = Θ(n^(log_2 2)) = Θ(n^1) = Θ(n).""",
"""Para não colidir com as constantes de custo a e b da §0, escrevo os parâmetros do teorema como
α (número de chamadas recursivas), β (fator de redução) e k, na forma
T(n) = α·T(n/β) + c·n^k, com o critério α ≷ β^k.
Parâmetros: α = 2 (linhas 4 e 5: esquerda E direita são visitadas); β = 2 (cada subárvore tem
≈ n/2 nós); k = 0 (o trabalho fora da recursão é constante).
Comparação: β^k = 2^0 = 1, e α = 2. Portanto α > β^k.
Conclusão (primeiro caso): T(n) = Θ(n^(log_β α)) = Θ(n^(log_2 2)) = Θ(n^1) = Θ(n).""")

patch("q4-slide-limpo.md",
      "Espelha o patch anterior no paragrafo da busca binaria, onde a mesma colisao ocorria.",
      "verificador do exercicio do slide", "media",
"""Por que não é como a busca binária. A busca binária tem T(n) = T(n/2) + Θ(1), ou seja a = 1,
b = 2, k = 0, b^k = 1; aqui a = b^k, que é o segundo caso do Teorema Mestre, dando
Θ(n^k lg n) = Θ(lg n). A queda para logarítmico vem de a = 1: a busca binária descarta uma das
metades. FatorAltura tem a = 2: desce nas duas metades e não descarta nada, porque precisa do
f.b. de todo mundo.""",
"""Por que não é como a busca binária. A busca binária tem T(n) = T(n/2) + Θ(1), ou seja α = 1,
β = 2, k = 0, β^k = 1; aqui α = β^k, que é o segundo caso do Teorema Mestre, dando
Θ(n^k lg n) = Θ(lg n). A queda para logarítmico vem de α = 1: a busca binária descarta uma das
metades. FatorAltura tem α = 2: desce nas duas metades e não descarta nada, porque precisa do
f.b. de todo mundo.""")

patch("q4-slide-limpo.md",
      "Espelha a correcao da colisao de simbolos na secao RESPOSTA - era ali que a contradicao "
      "ficava visivel (armadilha 7.1 do CLAUDE.md).",
      "verificador do exercicio do slide", "media-alta",
"""Não há ganho algum de complexidade de tempo. Pelo Teorema Mestre (Brassard & Bratley), o caso
balanceado T(n) = 2T(n/2) + Θ(1) tem a = 2, b = 2, k = 0, b^k = 1 e, como a > b^k, resulta
Θ(n^(log_2 2)) = Θ(n) — a mesma classe do caso degenerado. De fato o custo é idêntico, e não
apenas da mesma ordem: toda árvore com n nós gera exatamente 2n+1 chamadas e custo
(n+1)a + n·b, seja qual for sua forma.""",
"""Não há ganho algum de complexidade de tempo. Pelo Teorema Mestre (Brassard & Bratley), o caso
balanceado T(n) = 2T(n/2) + Θ(1) tem α = 2, β = 2, k = 0, β^k = 1 e, como α > β^k, resulta
Θ(n^(log_2 2)) = Θ(n) — a mesma classe do caso degenerado. De fato o custo é idêntico, e não
apenas da mesma ordem: toda árvore com n nós gera exatamente 2n+1 chamadas e custo
(n+1)a + n·b, com a e b as constantes de custo da §0 (no modelo unitário a = b = 1, o que dá
justamente 2n+1), seja qual for sua forma.""")

patch("q4-slide-limpo.md",
      "Off-by-one contra a propria formula do texto: floor(lg 10^6) + 2 = floor(19,9316) + 2 = "
      "21, e o verificador MEDIU 21 quadros em n = 10^6. O '~22' vinha de usar teto em vez de "
      "piso. Num texto cujo argumento central e precisao de fencepost, e o tipo de "
      "inconsistencia que o leitor usa contra o resto.",
      "verificador do exercicio do slide", "baixa",
"""Para n = 10^6 é a diferença entre ~10^6 quadros na pilha (estouro certo na maioria dos
ambientes) e ~22 quadros.""",
"""Para n = 10^6 é a diferença entre 10^6 + 1 quadros na pilha (estouro certo na maioria dos
ambientes) e ⌊lg 10^6⌋ + 2 = 21 quadros.""")

patch("q4-slide-limpo.md",
      "A enumeracao de linhas omitia a linha 1 (o teste 'se n = 0'), que uma chamada nao vazia "
      "tambem executa. A definicao estava certa; so a lista entre parenteses estava incompleta.",
      "verificador do exercicio do slide", "baixa",
      "  b > 0 : custo da parte não recursiva de uma chamada com A não vazia (linhas 3, 7, 8, 9).",
      "  b > 0 : custo da parte não recursiva de uma chamada com A não vazia (linha 1 e linhas\n          3, 7, 8, 9).")

# =====================================================================
# QUESTAO 2 - HOLDS, mas com duas ressalvas que os DOIS verificadores
# levantaram independentemente. Nao sao buracos; sao clareza.
# =====================================================================

patch("q2-limpo.md",
      "Colisao de simbolo n0: o ENUNCIADO usa n0 para o limiar do caso base ('T(n) = c para "
      "todo n <= n0'); a solucao reusa n0 para o limiar das testemunhas de Theta, e depois "
      "volta ao sentido do enunciado nesta frase. Nenhuma conta fica errada, mas os dois "
      "verificadores tropecaram no mesmo ponto. Renomeado para n_base.",
      "verificadores Q2-A e Q2-B (independentes, mesma ressalva)", "baixa",
"""porque vem do número de níveis (log_b n), que independe do caso base. Interromper a recursão em
n ≤ n0 em vez de n = 1 corta apenas log_b n0 = O(1) níveis do topo da soma.""",
"""porque vem do número de níveis (log_b n), que independe do caso base. Interromper a recursão em
n ≤ n_base (o limiar do enunciado, que não deve ser confundido com o n0 das testemunhas de Θ)
em vez de n = 1 corta apenas log_b n_base = O(1) níveis do topo do intervalo de somação — que
são os níveis mais profundos da árvore de recursão.""")

patch("q2-limpo.md",
      "O Lema 0.2 e enunciado so para c = 1, enquanto o teorema em 0.1 admite c*n^k geral. Os "
      "cinco itens tem c = 1, entao nao ha lacuna efetiva - mas o estreitamento nao estava "
      "anunciado, e os dois verificadores registraram.",
      "verificadores Q2-A e Q2-B (independentes, mesma ressalva)", "baixa",
"""### 0.2 Lema da expansão (onde "n é potência exata de b" é usado)
Lema. Seja T(1) = 1 e T(n) = a·T(n/b) + n^k para n > 1. Se n = b^m com m ≥ 0 inteiro, então""",
"""### 0.2 Lema da expansão (onde "n é potência exata de b" é usado)
O lema abaixo é enunciado com c = 1, que é o caso dos cinco itens desta questão. Para c > 0
qualquer, todo o termo motor fica multiplicado por c e as constantes c1, c2 das testemunhas
apenas se reescalam por c — as classes Θ não mudam.
Lema. Seja T(1) = 1 e T(n) = a·T(n/b) + n^k para n > 1. Se n = b^m com m ≥ 0 inteiro, então""")


# =====================================================================
# QUESTAO 1 - CONFIRMADA (4 HOLDS), mas dois verificadores sugeriram
# melhorias reais. Nao sao buracos; sao o que um corretor rigoroso cobraria.
# =====================================================================

patch("q1-limpo.md",
      "O item (e) apresentava a forma fechada 2n-1 ja pronta, sem o desenrolar que a produziu. "
      "Logicamente irrelevante (inducao VERIFICA um palpite, e a verificacao esta completa), "
      "mas o enunciado da lista diz 'e necessario mostrar a resolucao ou o raciocinio "
      "utilizado'. Duas linhas de desenrolar fecham a pergunta 'de onde veio isso?' antes que "
      "ela seja feita.",
      "verificador Q1-D", "baixa",
"""Fase 1 — forma fechada por indução: T(n) = 2n − 1.
P(n): T(n) = 2n − 1.""",
"""Fase 1 — forma fechada por indução: T(n) = 2n − 1.
De onde vem o palpite: desenrolando a recorrência, T(n) = T(n−1) + 2 = T(n−2) + 2·2 = … =
T(1) + 2(n−1) = 1 + 2n − 2 = 2n − 1. O desenrolar é heurística, não demonstração — quem
demonstra é a indução abaixo, que parte da definição recursiva e chega à fórmula.
P(n): T(n) = 2n − 1.""")

patch("q1-limpo.md",
      "Sobre-justificacao: 'ter pelo menos dois termos' e SUFICIENTE, nao necessario - a "
      "separacao do ultimo termo vale ja com a soma vazia. A premissa e verdadeira e a "
      "implicacao e valida, entao nada quebrava; mas num texto que cobra necessidade x "
      "suficiencia na Questao 3, vale ser exato aqui tambem.",
      "verificadores Q1-B (nit) e Q1-C (mesmo achado)", "baixa",
"""Passo: como n ≥ 1, então n+1 ≥ 2, logo o somatório até n+1 tem pelo menos dois termos e
pode ser separado no somatório até n mais o termo k = n+1:""",
"""Passo: separa-se o somatório até n+1 no somatório até n mais o termo k = n+1 — separação
válida para todo n ≥ 0, inclusive quando a soma restante é vazia:""")


# =====================================================================
# RODADA 2 - problemas INTRODUZIDOS pelos patches da rodada 1.
# E exatamente a armadilha 7.2 do CLAUDE.md ("todo lote de correcao deve
# voltar para verificacao"). Achados pela REVERIFICACAO.
# =====================================================================

patch("q3-limpo.md",
      "PROBLEMA INTRODUZIDO PELO PATCH. O patch da rodada 1 inseriu 'Duas regras trabalham "
      "juntas', criando um antecedente para 'nenhuma das duas se aplica' - e essa frase ficou "
      "FALSA e autocontraditoria: com n = 3 fixo, a descarga de hipotese (->-introducao) SE "
      "APLICA normalmente e produz exatamente P(3) -> P(4), que e o que a propria oracao "
      "seguinte afirma. So a generalizacao universal falha. A frase tambem contradizia a §4(b), "
      "que diz que supor P(3) numa prova condicional e legitimo.",
      "REVERIFICACAO Q3-A", "media",
      """Fixando n = 3, nenhuma das duas se aplica — o
máximo que o texto estabelece é a implicação concreta P(3) → P(4).""",
      """Fixando n = 3, a primeira ainda se aplica — assumir P(3), derivar P(4) e
descarregar produz legitimamente a implicação P(3) → P(4) — mas a segunda não: sem k arbitrário
não há generalização universal. É por isso que o texto fica preso a essa única implicação
concreta.""")

patch("q3-limpo.md",
      "'qualquer mundo com ao menos uma chinesa e ao menos uma nao-chinesa' admite o mundo de "
      "exatamente duas pessoas, onde P(3) e VACUAMENTE VERDADEIRA - contradizendo a afirmacao "
      "da §2 de que P(n) e falsa para todo n >= 2. O contramodelo continua valido (so precisa "
      "de P(2) falsa), mas a redacao pressupunha tacitamente um universo grande o bastante.",
      "REVERIFICACAO Q3-A", "baixa",
      """Tome qualquer mundo com ao menos uma pessoa chinesa e ao menos uma não-chinesa; por exemplo,
T1 chinês e T2 brasileiro.""",
      """Tome um mundo com uma pessoa chinesa e não-chinesas em quantidade arbitrária — T1 chinês,
T2 brasileiro, e assim por diante.""")

patch("q3-limpo.md",
      "Referente frouxo na secao RESPOSTA: 'o que' apontava gramaticalmente para a IGUALDADE "
      "|A inter B| = k-1, que vale para todo k (inclusive k=1, com valor 0). O que so vale para "
      "k >= 2 e a condicao A inter B != vazio.",
      "REVERIFICACAO Q3-A", "baixa",
      """distintos) tem-se |A ∩ B| = k − 1, o que só é satisfeito para k ≥ 2.""",
      """distintos) tem-se |A ∩ B| = k − 1, de modo que a condição A ∩ B ≠ ∅ só é satisfeita para
k ≥ 2.""")


# =====================================================================
# RODADA 3 - achados da reverificacao. Dois deles sao problemas que os
# patches da rodada 1 INTRODUZIRAM ou deixaram pela metade.
# =====================================================================

patch("q2-limpo.md",
      "PROBLEMA INTRODUZIDO PELO PATCH. O paragrafo inserido na rodada 1 afirmava que 'as "
      "constantes c1, c2 das testemunhas apenas se reescalam por c'. FALSO para 0 < c < 1, e "
      "DOIS reverificadores independentes acharam com o mesmo contraexemplo. Motivo: o termo do "
      "caso base a^m NAO leva o c, entao T_c = a^m + c*(T_1 - a^m), que nao e c*T_1. Numeros do "
      "verificador, item (d) com c = 1/2: T(3) = 13,5 mas c2 'reescalado' = (1/2)*(2/lg 3) daria "
      "cota 9,0 -- e 13,5 <= 9,0 e falso. As testemunhas corretas estao no texto novo e foram "
      "conferidas em n = n0 exatamente.",
      "REVERIFICACAO Q1+Q2 (dois verificadores, mesmo contraexemplo)", "media",
"""O lema abaixo é enunciado com c = 1, que é o caso dos cinco itens desta questão. Para c > 0
qualquer, todo o termo motor fica multiplicado por c e as constantes c1, c2 das testemunhas
apenas se reescalam por c — as classes Θ não mudam.""",
"""O lema abaixo é enunciado com c = 1, que é o caso dos cinco itens desta questão. Para c > 0
qualquer, o termo motor fica multiplicado por c, mas o termo do caso base a^m não — de modo que
T_c(n) = a^m + c·(T_1(n) − a^m), e não c·T_1(n). As testemunhas mudam por constantes, não por um
simples fator c: no caso a = b^k ficam c1 = c/lg b, c2 = (1+c)/lg b, n0 = b; no caso a > b^k
ficam c1 = 1, c2 = 1 + c·B, n0 = 1 (a identidade A − B = 1 se preserva). Em ambos, as classes Θ
não mudam — que é o que importa aqui.""")

patch("q2-limpo.md",
      "Mesma imprecisao do patch anterior, na secao 'Observacao sobre o caso base': dizer que c "
      "'so reescala c1 e c2' e falso para 0 < c < 1. E a renomeacao n0 -> n_base tinha ficado "
      "pela metade: a primeira frase do MESMO paragrafo ainda usava n0 para o limiar, que e "
      "exatamente a colisao que o patch queria eliminar.",
      "REVERIFICACAO Q1+Q2", "baixa",
"""O enunciado admite T(1) = 1 ou T(n) = c para todo n ≤ n0. Isso não altera nenhuma das classes Θ.""",
"""O enunciado admite T(1) = 1 ou T(n) = c para todo n ≤ n_base. Isso não altera nenhuma das
classes Θ.""")

patch("q2-limpo.md",
      "Fecha a mesma imprecisao na frase final da secao do caso base.",
      "REVERIFICACAO Q1+Q2", "baixa",
"""Em todos, c > 0 constante só reescala c1 e c2; nos casos de igualdade o fator lg n sobrevive""",
"""Em todos, c > 0 constante muda c1 e c2 apenas por constantes (no caso a = b^k, para c/lg b e
(1+c)/lg b); nos casos de igualdade o fator lg n sobrevive""")

patch("q3-limpo.md",
      "TERMO TECNICO TROCADO. 'Afirmar o consequente' e o nome consagrado de OUTRA falacia: de "
      "A->B e B, inferir A. Aqui o erro e o inverso -- de A->B, asseverar B sem ter A. O aposto "
      "'modus ponens sem a premissa menor' descrevia certo, mas o termo que abria a frase "
      "apontava para a falacia errada. Numa questao de logica formal e o tipo de item que o "
      "corretor marca. Os dois reverificadores da Q3 apontaram.",
      "REVERIFICACAO Q3-A (nit) e Q3-B (achado)", "media",
      """A falácia está em afirmar o consequente sem ter estabelecido o""",
      """A falácia está em asseverar o consequente de uma prova condicional sem ter estabelecido o""")

patch("q3-limpo.md",
      "Troca de sujeito nao sinalizada: a §5 credita 'corretamente demonstrado' ao passo, mas o "
      "texto do professor NAO escreve o passo generico -- quem o escreve e a reconstrucao da "
      "§3.1. Sem a marcacao, a §5 parece contradizer a §4(d), que chama a generalizacao de "
      "buraco.",
      "REVERIFICACAO Q3-B", "baixa",
      "  Passo: P(k) → P(k+1) para todo k ≥ 2 — corretamente demonstrado. ✔",
      "  Passo: P(k) → P(k+1) para todo k ≥ 2 — corretamente demonstrado, uma vez escrito\n    explicitamente como na reconstrução da §3.1. ✔")

patch("q3-limpo.md",
      "'P(n) e falsa para todo n >= 2' e contingente ao tamanho da populacao: num mundo com "
      "exatamente 2 pessoas, P(3) em diante e vacuamente VERDADEIRA. Os dois reverificadores "
      "sinalizaram. Nao afeta o argumento (so precisa de P(2) falsa), mas um corretor literalista "
      "pega.",
      "REVERIFICACAO Q3-A e Q3-B", "baixa",
      """O mesmo contraexemplo se estende a qualquer n ≥ 2: C = {T1 chinês, T2, …, Tn não-chineses}.
Portanto P(1) é verdadeira e P(n) é falsa para todo n ≥ 2.""",
      """O mesmo contraexemplo se estende a qualquer n ≥ 2: C = {T1 chinês, T2, …, Tn não-chineses}.
Portanto P(1) é verdadeira, e P(n) é falsa para todo n ≥ 2 — desde que haja pessoas suficientes
para formar um conjunto de tamanho n. (Num universo com menos de n pessoas, P(n) é vacuamente
verdadeira, por falta de conjunto a testar; isso não socorre a prova, que precisaria de P(2).)""")

patch("q3-limpo.md",
      "A critica de §4(c) ao 'fundir hipotese e passo' e fraca: assumir a h.i. DENTRO do passo e "
      "a pratica padrao, e a propria §7 enuncia o PIF com duas condicoes. O defeito real ali e o "
      "k fixo, que a mesma alinea ja aponta. Reescrito para nao cobrar o que nao e erro.",
      "REVERIFICACAO Q3-B", "baixa",
      """(c) O rótulo está trocado. O que o texto chama de "hipótese de indução" é o passo indutivo, e
apenas na instância concreta 3 → 4. Uma prova por indução tem três partes — base, hipótese e
passo — e o texto funde as duas últimas, além de omitir a quantificação universal sobre k.""",
      """(c) O rótulo está trocado. O que o texto chama de "hipótese de indução" é, na verdade, o passo
indutivo — e apenas na instância concreta 3 → 4. Enunciar a hipótese dentro do passo é prática
comum e não seria defeito; o defeito é o rótulo esconder que ali está sendo feita a parte que
precisaria de k arbitrário, e que a quantificação universal sobre k nunca aparece.""")

patch("q4-slide-limpo.md",
      "RENOMEACAO INCOMPLETA. O patch da rodada 1 renomeou os parametros do Teorema Mestre para "
      "alfa/beta, mas deixou 'T(n) = a*T(n/b) + c*n^k' na frase ANTERIOR a renomeacao -- que e "
      "literalmente a colisao que o patch existia para eliminar: o leitor encontra a*T(n/b) a dez "
      "linhas de 'a > 0: custo de uma chamada vazia'. A frase de renomeacao subiu para antes de "
      "qualquer uso.",
      "REVERIFICACAO do exercicio do slide", "media-baixa",
"""Para aplicar o teorema na forma T(n) = a·T(n/b) + c·n^k é preciso um termo motor literalmente
c·n^k. Substituindo o Θ(1) por constantes explícitas: existem d1, d2 > 0 com
d1 ≤ (custo não recursivo de uma chamada) ≤ d2 (basta d1 = min(a,b), d2 = max(a,b)); logo
2T(n/2) + d1 ≤ T(n) ≤ 2T(n/2) + d2, e cada lado é uma recorrência na forma exigida com k = 0,
porque c·n^0 = c é constante.
Para não colidir com as constantes de custo a e b da §0, escrevo os parâmetros do teorema como
α (número de chamadas recursivas), β (fator de redução) e k, na forma
T(n) = α·T(n/β) + c·n^k, com o critério α ≷ β^k.
Parâmetros: α = 2""",
"""As constantes a e b já estão ocupadas pelos custos da §0, então escrevo daqui em diante os
parâmetros do teorema como α (número de chamadas recursivas), β (fator de redução) e k, na forma
T(n) = α·T(n/β) + c·n^k, com o critério α ≷ β^k.
Para aplicar o teorema nessa forma é preciso um termo motor literalmente c·n^k. Substituindo o
Θ(1) por constantes explícitas: existem d1, d2 > 0 com
d1 ≤ (custo não recursivo de uma chamada) ≤ d2 (basta d1 = min(a,b), d2 = max(a,b), com a e b os
custos da §0); logo 2T(n/2) + d1 ≤ T(n) ≤ 2T(n/2) + d2, e cada lado é uma recorrência na forma
exigida com k = 0, porque c·n^0 = c é constante.
Parâmetros: α = 2""")

patch("q4-slide-limpo.md",
      "RESIDUO DA RENOMEACAO, o pior dos dois: esta ressalva vem DEPOIS da declaracao de que os "
      "parametros do teorema sao alfa/beta, entao o unico 'b' ainda em vigor e a constante de "
      "CUSTO. Lido assim, 'n potencia exata de b' com a=b=1 diria 'n potencia exata de 1', isto "
      "e n = 1 -- sem sentido, ja que a mesma secao conclui Theta(n) para todo n.",
      "REVERIFICACAO do exercicio do slide", "media",
      """Ressalva: nessa formulação o resultado é enunciado para n potência exata de b e estendido pela
regularidade de n^k; "n/2" ignora pisos e tetos.""",
      """Ressalva: nessa formulação o resultado é enunciado para n potência exata de β (aqui, potência
de 2) e estendido pela regularidade de n^k; "n/2" ignora pisos e tetos.""")

patch("q4-slide-limpo.md",
      "O valor EXATO floor(lg n) + 2 so vale para o split perfeito. Sob '~ n/2' tomado ao pe da "
      "letra (fracao constante), a profundidade medida e maior -- o verificador mediu 13 quadros "
      "com split 0,45 e 23 com split 0,25, para n = 1000, contra floor(lg 1000) + 2 = 11. A "
      "conclusao assintotica sobrevive (a razao com lg n fica limitada), mas a celula da tabela "
      "prometia exatidao que o cabecalho nao sustenta.",
      "REVERIFICACAO do exercicio do slide", "baixa",
      "| Profundidade máxima da recursão | n + 1 quadros = Θ(n) | ⌊lg n⌋ + 2 quadros = Θ(lg n) | Sim, drasticamente |",
      "| Profundidade máxima da recursão | n + 1 quadros = Θ(n) | ⌊lg n⌋ + 2 quadros no split perfeito, Θ(lg n) em qualquer split de fração constante | Sim, drasticamente |")


# =====================================================================
# RODADA 4 - achado da reverificacao final. De novo um problema
# INTRODUZIDO por um patch anterior (armadilha 7.2 do CLAUDE.md).
# =====================================================================

patch("q2-limpo.md",
      "PROBLEMA INTRODUZIDO PELO PATCH DA RODADA 3. A formula c1 = c/lg b esta CERTA na §0.2, "
      "onde c e o coeficiente do TERMO MOTOR; o patch a copiou para a secao do caso base, onde "
      "c e a constante da BASE (T(1) = c) - e ali ela e FALSA. Sao regimes diferentes: no motor "
      "a razao T/(n^k lg n) e 1/lg n + c/lg b, com infimo c/lg b; na base e 1/lg b + c/lg n, "
      "com infimo 1/lg b, que NAO depende de c. Contraexemplo conferido: item (e) com c = 3, "
      "T(4) = 320 mas a cota afirmada daria 384 -- violada, e nao por fencepost, permanentemente. "
      "168 violacoes medidas em 3 itens x 4 valores de c x m=1..29. Com c <= 1 a cota so fica "
      "frouxa, e por isso passou: o documento inteiro usa c = 1, onde c/lg b = 1/lg b coincidem. "
      "O c2 = (1+c)/lg b do mesmo parenteses estava correto nos dois regimes.",
      "REVERIFICACAO FINAL Q2-A", "media",
"""Em todos, c > 0 constante muda c1 e c2 apenas por constantes (no caso a = b^k, para c/lg b e
(1+c)/lg b); nos casos de igualdade o fator lg n sobrevive""",
"""Aqui c é a constante do caso base, não o coeficiente do termo motor da §0.2 — e os dois papéis
dão testemunhas diferentes. Com T(1) = c a razão T(n)/(n^k lg n) vale 1/lg b + c/lg n, cujo
ínfimo é 1/lg b e não depende de c; no regime do termo motor a razão é 1/lg n + c/lg b, com
ínfimo c/lg b. Portanto, no caso a = b^k com T(1) = c, as testemunhas são c1 = 1/lg b,
c2 = (1+c)/lg b, n0 = b. Em todos os itens, c > 0 constante muda c1 e c2 apenas por constantes;
nos casos de igualdade o fator lg n sobrevive""")

patch("q2-limpo.md",
      "Risco vizinho apontado pelo segundo verificador da rodada final: o 'Em todos' generico "
      "convidava a importar tambem as testemunhas do caso a > b^k (c1 = 1, n0 = 1), que falham "
      "na leitura de caso base com c < 1 -- item (a) com T(1) = 1/4 da T(1) = 0,25 < 1. Deduzi e "
      "conferi as corretas: T_c = T_1 + (c-1)a^m = (A+c-1)n^alfa - B n^k, e como A - B = 1 vem "
      "(A+c-1) - B = c, logo c1 = c, c2 = c + B, n0 = 1. Zero violacoes em 5 triplas x 5 valores "
      "de c x m=0..21. Agora a secao cobre os dois casos explicitamente, em vez de generalizar.",
      "REVERIFICACAO FINAL Q2-B", "media",
"""c2 = (1+c)/lg b, n0 = b. Em todos os itens, c > 0 constante muda c1 e c2 apenas por constantes;
nos casos de igualdade o fator lg n sobrevive""",
"""c2 = (1+c)/lg b, n0 = b. E no caso a > b^k com T(1) = c vale
T_c(n) = T_1(n) + (c−1)·a^m = (A + c − 1)·n^(log_b a) − B·n^k; como A − B = 1, a diferença
(A + c − 1) − B é exatamente c, e as testemunhas ficam c1 = c, c2 = c + B, n0 = 1. Em todos os
casos, portanto, c > 0 muda c1 e c2 apenas por constantes — nunca a classe. Nos casos de
igualdade o fator lg n sobrevive""")

# =====================================================================
# RODADA 5 - Q3. Os dois verificadores da rodada final divergiram no achado
# principal (A deu HOLE_FOUND, B deu HOLDS dizendo que a sinalizacao ja
# existia). Corrijo o que os DOIS apontam, o que e objetivamente verdadeiro,
# e desambiguo o ponto em disputa para que nenhuma leitura fique errada.
# =====================================================================

patch("q3-limpo.md",
      "A ressalva de vacuidade que EU introduzi na rodada 3 foi criticada pelos dois "
      "verificadores. O A: ela nao foi propagada para os dois lugares gemeos (§3.3 e §5), criando "
      "tres pontos de atrito onde nao havia nenhum, e o parenteses nao fecha (num universo com "
      "menos de 2 pessoas, P(2) TAMBEM e vacuamente verdadeira). O B: a condicao dada e "
      "insuficiente - precisa de >=1 chines E >=1 nao-chines, senao num mundo 'todos chineses' "
      "com gente de sobra P(3) e verdadeira. Ambos recomendam remover. O universo do discurso e "
      "'pessoas', nao um mundo finito estipulado. Volto a afirmacao seca.",
      "REVERIFICACAO FINAL Q3-A e Q3-B (ambos)", "baixa",
"""Portanto P(1) é verdadeira, e P(n) é falsa para todo n ≥ 2 — desde que haja pessoas suficientes
para formar um conjunto de tamanho n. (Num universo com menos de n pessoas, P(n) é vacuamente
verdadeira, por falta de conjunto a testar; isso não socorre a prova, que precisaria de P(2).)""",
"""Portanto P(1) é verdadeira e P(n) é falsa para todo n ≥ 2.""")

patch("q3-limpo.md",
      "'nao-chinesas em quantidade arbitraria' admite ZERO, e o verificador rodou: com uma pessoa "
      "so, as tres premissas E a conclusao ficam verdadeiras -- o contramodelo colapsa. E salvo "
      "apenas pela clausula seguinte. Fecho a brecha.",
      "REVERIFICACAO FINAL Q3-A", "baixa",
"""Tome um mundo com uma pessoa chinesa e não-chinesas em quantidade arbitrária — T1 chinês,
T2 brasileiro, e assim por diante.""",
"""Tome um mundo com pelo menos uma pessoa chinesa e pelo menos uma não-chinesa — T1 chinês,
T2 brasileiro, e quantas mais se queira.""")

patch("q3-limpo.md",
      "TEXTO ORFAO do criterio antigo. A §3.2 passou a dizer que exigir T1 em B e 'forte demais', "
      "com contraexemplo; mas a §7 continuava nomeando T1 em B como A hipotese tacita, e a §4(d) "
      "idem. O documento passava a apresentar dois criterios diferentes como 'a' condicao, e a §7 "
      "usava justamente o que ela mesma classificou de forte demais.",
      "REVERIFICACAO FINAL Q3-A", "media",
      """hipótese extra — aqui "k ≥ 2", disfarçada na suposição não declarada de que T1 ∈ B —""",
      """hipótese extra — aqui "k ≥ 2", disfarçada na suposição não declarada de que A ∩ B ≠ ∅ (na
construção do texto, de que T1 ∈ B) —""")

patch("q3-limpo.md",
      "Espelha o patch anterior na §4(d), o outro lugar onde o criterio antigo sobreviveu.",
      "REVERIFICACAO FINAL Q3-A", "baixa",
      """com os quantificadores explícitos, seria obrigado a justificar "T1 ∈ B", e o caso k = 1""",
      """com os quantificadores explícitos, seria obrigado a justificar que A ∩ B ≠ ∅ — na construção
do texto, que T1 ∈ B — e o caso k = 1""")

patch("q3-limpo.md",
      "'Asseverar' e sinonimo de 'afirmar', e 'afirmar o consequente' e o nome consagrado de OUTRA "
      "falacia (de A->B e B, inferir A). Os dois verificadores sinalizaram o risco de o leitor "
      "ativar o nome errado antes de chegar a glosa. Troco por um verbo que nao colide.",
      "REVERIFICACAO FINAL Q3-A e Q3-B (ambos)", "media",
      """A falácia está em asseverar o consequente de uma prova condicional sem ter estabelecido o""",
      """A falácia está em concluir o consequente de uma prova condicional sem ter estabelecido o""")

patch("q3-limpo.md",
      "PONTO EM DISPUTA entre os dois verificadores. O A leu o cabecalho 'O que a construcao "
      "realmente estabelece' como atribuindo o passo ao TEXTO DO PROFESSOR, o que contradiz a "
      "§4(a) e a §4(d); o B leu como atribuindo a reconstrucao, e achou correto. Reescrevo para "
      "que a atribuicao seja explicita e nenhuma das duas leituras fique errada.",
      "REVERIFICACAO FINAL Q3-A (achado) e Q3-B (discordou)", "media",
"""O que a construção realmente estabelece é:
  Base: P(1) — verdadeira. ✔
  Passo: P(k) → P(k+1) para todo k ≥ 2 — corretamente demonstrado, uma vez escrito
    explicitamente como na reconstrução da §3.1. ✔""",
"""O texto do professor não escreve o passo genérico — ele exibe só a instância 3 → 4 e delega o
resto a um "analogamente". Completando-o como na reconstrução da §3.1, com a aplicabilidade da
hipótese verificada como na §3.2, o que fica de pé é:
  Base: P(1) — verdadeira, e provada pelo próprio texto. ✔
  Passo: P(k) → P(k+1) para todo k ≥ 2 — demonstrável, mas pela reconstrução, não pelo texto. ✔""")

patch("q3-limpo.md",
      "Completude da RESPOSTA: ela entregava so o diagnostico do elo k=1, que e um defeito da "
      "RECONSTRUCAO. O defeito imediato do texto COMO ESCRITO -- supor P(3), que nunca foi "
      "derivada de P(1) -- estava no corpo (§4a, §4b) mas nao na resposta. Um corretor que leia so "
      "a resposta perde metade da critica.",
      "REVERIFICACAO FINAL Q3-B", "baixa",
"""nunca é estabelecido e a cadeia indutiva se rompe logo após a base. É a versão brasileira da""",
"""nunca é estabelecido e a cadeia indutiva se rompe logo após a base. Soma-se a isso um defeito
do texto tal como escrito: ele supõe P(3), que nunca foi derivada da base P(1), e apresenta a
conclusão como fato categórico — de modo que, além da base P(1), o máximo que estabelece é a
implicação P(3) → P(4). É a versão brasileira da""")

# =====================================================================
# RODADA 6 - dois achados do verificador A do apendice. NENHUM veio de
# patch: sao defeitos do texto original que sobreviveram a cinco rodadas.
# =====================================================================

patch("q4-slide-limpo.md",
      "CRITICA INJUSTA AO MATERIAL DO PROFESSOR - e a regra da secao 8 do CLAUDE.md diz para nao "
      "fazer isso. Eu afirmava que o passo do meio do slide 'nao liga os extremos'. Falso: "
      "T(1) + (n-1)(T(0)+b) = (2a+b) + (n-1)(a+b) = (n+1)a + n*b, que e EXATAMENTE o lado direito "
      "do slide. Conferi em n=1..25 com a=3, b=7: medido = slide = formula, zero divergencias. "
      "Minha objecao contava PARCELAS, e Theta(1) nao se compromete com constante nenhuma -- cada "
      "Theta(1) da soma e o incremento de um passo do desenrolar, que ja embute o T(0) do filho "
      "vazio. Pior: a propria secao declara tres linhas adiante que 'cada Theta(1) pode esconder "
      "constante diferente', o que torna a contagem de parcelas ilegitima pelo meu proprio "
      "criterio. Reescrito para registrar o que de fato vale a pena registrar (a necessidade da "
      "constante uniforme e a base declarada), sem acusar o slide de erro que ele nao comete.",
      "REVERIFICACAO FINAL apendice-A", "media",
"""(ii) O passo intermediário é impreciso em dois pontos. O slide escreve
T(n) = T(1) + Σ_{i=2}^{n} Θ(1); essa expressão tem n − 1 parcelas além de T(1), e não reproduz
literalmente o total (n+1)Θ(1) + nΘ(1), que tem 2n + 1 parcelas. Além disso, o caso base
declarado na própria recorrência é n = 0, não n = 1: a cadeia só termina ao chegar em
FatorAltura da árvore vazia. O desenrolar honesto é o da §2:
T(n) = T(0) + n·(a + b) = (n+1)a + n·b. Os extremos do slide estão certos; o passo do meio é que
não os liga. Somar um número variável de termos "Θ(1)" é abuso de notação: cada Θ(1) pode
esconder constante diferente, e nada na notação garante uma constante uniforme limitando todas.
O argumento só é válido porque tal constante uniforme existe aqui — max(a, b).""",
"""(ii) O passo intermediário é abreviado, não errado. O slide escreve
T(n) = T(1) + Σ_{i=2}^{n} Θ(1), e isso de fato liga os extremos: cada Θ(1) da soma é o incremento
de um passo do desenrolar, que já embute o T(0) do filho vazio, de modo que
T(1) + (n−1)·(T(0) + b) = (2a + b) + (n−1)(a + b) = (n+1)a + n·b — exatamente o lado direito que
o slide escreve. (Conferido numericamente para n = 1…25.) Objetar que "a soma tem n−1 parcelas e
o total tem 2n+1" seria contar parcelas, e Θ(1) não se compromete com constante nenhuma.
O que vale registrar é outra coisa: somar um número variável de termos Θ(1) só é legítimo porque
existe uma constante uniforme limitando todos eles — aqui max(a, b) —, e essa uniformidade não
está na notação, está no algoritmo. E o caso base declarado na recorrência é n = 0, não n = 1:
parar em T(1) é atalho legítimo, mas é preciso saber que T(1) = 2a + b, e não a.""")

patch("q4-slide-limpo.md",
      "ROTULO DO CASO EM DESACORDO COM O FORMULARIO DA PROVA. Conferi o PDF da prova de 2025: o "
      "Teorema Mestre e impresso na ordem a < b^k (1o), a = b^k (2o), a > b^k (3o). Nossos textos "
      "chamavam a > b^k de 'primeiro caso'. Nenhuma conta muda, mas numa prova em que o teorema "
      "vem impresso, apontar para a linha errada e ponto perdido de graca. O documento irmao "
      "prova-01-resolucao.html ja usava a ordem do professor - eramos nos que estavamos fora de "
      "sintonia. (A hipotese 'T assintoticamente nao decrescente', que o enunciado do professor "
      "exige, foi acrescentada no q2-limpo.md; aqui nao, porque a §3 deste arquivo dispensa o "
      "teorema inteiro e prova o custo exato por inducao.)",
      "REVERIFICACAO FINAL apendice-A", "media",
"""Comparação: β^k = 2^0 = 1, e α = 2. Portanto α > β^k.
Conclusão (primeiro caso): T(n) = Θ(n^(log_β α)) = Θ(n^(log_2 2)) = Θ(n^1) = Θ(n).""",
"""Comparação: β^k = 2^0 = 1, e α = 2. Portanto α > β^k.
Conclusão — é o caso α > β^k, que no formulário entregue na prova aparece como o terceiro dos
três (a ordem impressa é a < b^k, a = b^k, a > b^k):
T(n) = Θ(n^(log_β α)) = Θ(n^(log_2 2)) = Θ(n^1) = Θ(n).""")

patch("q2-limpo.md",
      "Mesmo desacordo de rotulo: o formulario da prova ordena a < b^k, a = b^k, a > b^k. Passo a "
      "listar o teorema na ORDEM DO PROFESSOR, para que 'primeiro/segundo/terceiro caso' aponte "
      "para a linha certa quando a folha estiver na mesa. Acrescento tambem a hipotese "
      "'T assintoticamente nao decrescente', que o enunciado do professor exige.",
      "REVERIFICACAO FINAL apendice-A", "media",
"""### 0.1 Teorema Mestre, forma de Brassard & Bratley
Para T(n) = a·T(n/b) + c·n^k, com a ≥ 1, b > 1, k ≥ 0, c > 0:
  a > b^k  →  T(n) ∈ Θ(n^(log_b a))
  a = b^k  →  T(n) ∈ Θ(n^k · lg n)
  a < b^k  →  T(n) ∈ Θ(n^k)""",
"""### 0.1 Teorema Mestre, forma de Brassard & Bratley
Para T(n) = a·T(n/b) + c·n^k, com a ≥ 1 natural, b ≥ 2 natural, k ≥ 0, c > 0 real, n potência
exata de b, e T assintoticamente não decrescente — listando os casos na MESMA ORDEM em que o
formulário da prova os imprime, para que "primeiro/segundo/terceiro caso" aponte para a linha
certa com a folha na mesa:
  1º  a < b^k  →  T(n) ∈ Θ(n^k)
  2º  a = b^k  →  T(n) ∈ Θ(n^k · lg n)
  3º  a > b^k  →  T(n) ∈ Θ(n^(log_b a))""")

patch("q2-limpo.md",
      "Fecha a incoerencia que o patch anterior criou: a lista do teorema passou para a ordem do "
      "professor (a > b^k e o TERCEIRO), mas os itens (a) e (b) e o quadro-resumo continuavam "
      "dizendo 'primeiro caso'. E exatamente a armadilha 7.4 do CLAUDE.md - o patch que conserta "
      "metade das ocorrencias.",
      "conferencia propria apos o patch da rodada 6", "media",
      """Comparação: b^k = 3^0 = 1. Como 2 > 1, tem-se a > b^k: primeiro caso.""",
      """Comparação: b^k = 3^0 = 1. Como 2 > 1, tem-se a > b^k: terceiro caso.""")

patch("q2-limpo.md",
      "Idem para o item (b).",
      "conferencia propria apos o patch da rodada 6", "media",
      """Comparação: b^k = 4^1 = 4. Como 5 > 4, tem-se a > b^k: primeiro caso.""",
      """Comparação: b^k = 4^1 = 4. Como 5 > 4, tem-se a > b^k: terceiro caso.""")

patch("q2-limpo.md",
      "Idem para as duas linhas do quadro-resumo.",
      "conferencia propria apos o patch da rodada 6", "media",
      """| (a) | 2T(n/3)+1  | 2 | 3 | 0 | 1 | 2 > 1 | 1º | 2n^(log_3 2) − 1 | Θ(n^(log_3 2)) ≈ Θ(n^0,6309) |
| (b) | 5T(n/4)+n  | 5 | 4 | 1 | 4 | 5 > 4 | 1º | 5n^(log_4 5) − 4n | Θ(n^(log_4 5)) ≈ Θ(n^1,1610) |""",
      """| (a) | 2T(n/3)+1  | 2 | 3 | 0 | 1 | 2 > 1 | 3º | 2n^(log_3 2) − 1 | Θ(n^(log_3 2)) ≈ Θ(n^0,6309) |
| (b) | 5T(n/4)+n  | 5 | 4 | 1 | 4 | 5 > 4 | 3º | 5n^(log_4 5) − 4n | Θ(n^(log_4 5)) ≈ Θ(n^1,1610) |""")

patch("q2-limpo.md",
      "Os Corolarios tambem nomeavam o caso pela ordem antiga.",
      "conferencia propria apos o patch da rodada 6", "baixa",
      """Corolário 1 (testemunhas no caso a > b^k).""",
      """Corolário 1 (testemunhas no caso a > b^k, o terceiro).""")

patch("q2-limpo.md",
      "Idem, Corolario 2.",
      "conferencia propria apos o patch da rodada 6", "baixa",
      """Corolário 2 (testemunhas no caso a = b^k).""",
      """Corolário 2 (testemunhas no caso a = b^k, o segundo).""")

# =====================================================================
# RODADA 7 - so o que nao envolve juizo. As demais notas da rodada final
# sao de APRESENTACAO e ficam registradas sem mexer, pelo criterio da
# secao 7.10 do CLAUDE.md.
# =====================================================================

patch("q2-limpo.md",
      "Erro de gramatica: 'teria-se' nao existe; a enclise nao cabe com o 'se' apassivador nessa "
      "construcao. Correcao objetiva, sem juizo editorial.",
      "RODADA FINAL Q2", "baixa",
      """A restrição n ≥ b não é cosmética: em n = 1 teria-se lg 1 = 0 e a cota superior seria""",
      """A restrição n ≥ b não é cosmética: em n = 1 ter-se-ia lg 1 = 0 e a cota superior seria""")

patch("q2-limpo.md",
      "O '[sic]' estava DENTRO das aspas do bloco rotulado 'ENUNCIADO (literal)'. A regra da secao "
      "8 do CLAUDE.md manda nao alterar enunciado; a anotacao editorial fica melhor fora das "
      "aspas, de modo que o que esta entre elas seja transcricao pura do PDF do professor.",
      "RODADA FINAL Q2", "baixa",
      """alguma constante n0. Suponha, também, que n uma potência exata de b. [sic — falta "é" no
original] Escolha o valor adequado
para a constante b conforme a equação de recorrência a ser resolvida. Justifique todas as suas
respostas. Respostas sem justificativas não serão consideradas." """.rstrip() + "\n",
      """alguma constante n0. Suponha, também, que n uma potência exata de b. Escolha o valor adequado
para a constante b conforme a equação de recorrência a ser resolvida. Justifique todas as suas
respostas. Respostas sem justificativas não serão consideradas."
[Nota de transcrição, fora do enunciado: onde se lê "que n uma potência exata de b", o original
do professor não traz o "é". Transcrito como está, sem correção.]\n""")

# =====================================================================
# RODADA 8 - achados de merito da rodada final da Q3.
# =====================================================================

patch("q3-limpo.md",
      "MATEMATICO. A §3.2 chamava 'T1 ∈ A e A ∩ B ≠ ∅' de 'a condicao realmente exigida' -- "
      "alegacao de necessidade E suficiencia. E so suficiente: como A ∪ B = S e T1 ∈ S, T1 esta "
      "sempre em A ou em B, entao chamar de A o primeiro a receber a hipotese e WLOG, nao "
      "exigencia. Contraexemplo enumerado e conferido por mim: k=3, A={T2,T3,T4}, B={T1,T2,T3} -- "
      "T1 nao esta em A e o passo fecha (aplica-se P(3) a B, que contem T1; isso certifica T2 e "
      "T3; T2 esta em A, entao aplica-se P(3) a A e certifica T4). Enumeracao k=1..5: 'A ∩ B ≠ ∅' "
      "coincide EXATAMENTE com 'fecha' (0/6/12/20/30), enquanto o criterio de duas partes deixa "
      "de fora 2/3/4/5 pares que fecham. Agravante: §7, §4(d) e a RESPOSTA ja diziam so "
      "'A ∩ B ≠ ∅' -- era a §3.2, que DEFINE o criterio, a unica fora do passo.",
      "RODADA FINAL Q3", "media",
"""A condição realmente exigida pelo passo encadeado é, portanto,
  T1 ∈ A   e   A ∩ B ≠ ∅.""",
"""Com a rotulação da §3.1 — A é o primeiro subconjunto a receber a hipótese —, o passo encadeado
exige T1 ∈ A e A ∩ B ≠ ∅. Mas T1 ∈ A ∪ B = S sempre vale, de modo que chamar de A aquele que
contém T1 é escolha de rótulo, não exigência: a condição substantiva, a única que pode falhar, é
  A ∩ B ≠ ∅.""")

patch("q3-limpo.md",
      "COERENCIA com aresta matematica. A §5 estipula 'um mundo com pelo menos uma chinesa e pelo "
      "menos uma nao-chinesa -- e quantas mais se queira', o que admite EXATAMENTE duas pessoas. "
      "Nesse mundo P(3) em diante e vacuamente verdadeira, e a licao final ('Aqui isso e "
      "impossivel: P(n) e falsa para todo n >= 2') fica falsa para n >= 3. O contramodelo "
      "sobrevive intacto -- so precisa de P(2) falsa, e conferi em 15 mundos --, mas a licao "
      "dependia da falsidade GLOBAL. Reescrita para depender so do que o argumento precisa.",
      "RODADA FINAL Q3", "media",
"""demonstrado — a menos que se prove independentemente uma nova base acima de m. Aqui isso é
impossível: P(n) é falsa para todo n ≥ 2.""",
"""demonstrado — a menos que se prove independentemente uma nova base acima de m. Aqui não há base
a resgatar: qualquer nova base teria de recuperar P(2) para cobrir n = 2, e P(2) é falsa pelo
contraexemplo da §2.""")

patch("q3-limpo.md",
      "COERENCIA. A §3.1 prometia que a §3.4 mostra independencia 'de qual generalizacao se "
      "adote', mas a §3.4 se escopa a construcoes com DOIS subconjuntos de tamanho k ('Qualquer "
      "versao dessa construcao obtem os dois subconjuntos...'). A conclusao e verdadeira -- "
      "enumerei todas as familias de k-subconjuntos que cobrem S e em k=1 nenhuma fecha --, mas a "
      "§3.4 como escrita nao a demonstra nessa amplitude. Alinho a promessa ao que a secao entrega.",
      "RODADA FINAL Q3", "baixa",
      """prova desejada"), mas a construção exibida em 3 → 4 tem uma generalização natural — e a §3.4
mostra que a conclusão não depende de qual generalização se adote. Generalizando:""",
      """prova desejada"), mas a construção exibida em 3 → 4 tem uma generalização natural — e a §3.4
mostra que a conclusão não depende de qual escolha de elementos removidos se adote.
Generalizando:""")

# =====================================================================
# RODADA 9 - o ultimo achado. Armadilha 7.4: consertei a frase na §5 e
# deixei a gemea na §2.
# =====================================================================

patch("q3-limpo.md",
      "MATEMATICO. 'P(n) e falsa para todo n >= 2' e exatamente a frase que a rodada 8 removeu da "
      "§5 por ser falsa -- e ela sobreviveu na §2. No mundo minimo que a propria §5 admite (T1 "
      "chines, T2 brasileiro, duas pessoas), nao existe conjunto de 3 pessoas, entao P(3) em "
      "diante e VACUAMENTE VERDADEIRA. Conferi por enumeracao. A correcao nao reintroduz a "
      "ressalva de vacuidade que duas rodadas atras foi julgada ruidosa: escopa a afirmacao em "
      "P(2), que e o unico valor que o resto do documento usa (§3.3 e §5 citam a §2 so para P(2)) "
      "e que e falso em TODO mundo com ao menos um chines e ao menos um nao-chines - conferido "
      "por enumeracao exaustiva em populacoes de 2 a 8 pessoas.",
      "VERIFICACAO DE FECHAMENTO Q3-A", "media",
"""O mesmo contraexemplo se estende a qualquer n ≥ 2: C = {T1 chinês, T2, …, Tn não-chineses}.
Portanto P(1) é verdadeira e P(n) é falsa para todo n ≥ 2.""",
"""Portanto P(1) é verdadeira e P(2) é falsa. O mesmo contraexemplo — C = {T1 chinês, T2, …, Tn
não-chineses} — refuta P(n) para qualquer n ≥ 2 para o qual existam n pessoas; e é P(2) que o
resto desta resposta usa.""")

def aplicar():
    from collections import defaultdict
    por_arquivo = defaultdict(list)
    for p in PATCHES:
        por_arquivo[p["arquivo"]].append(p)
    falhas = 0
    for arq in sorted(por_arquivo):
        texto = open(arq, encoding="utf-8").read()
        for i, p in enumerate(por_arquivo[arq], 1):
            n = texto.count(p["antigo"])
            sup = SUPERSEDED.get((arq, i))
            if sup and n == 0:
                print(f"  subst. {arq} patch {i}  -> trecho reescrito pelo patch {sup} (rodada 2)")
                continue
            if n == 0 and p["novo"] in texto and len(p["novo"]) > 40:
                # idempotente: patch ja aplicado numa rodada anterior
                print(f"  ja ok  {arq} patch {i}  [{p['gravidade']:11s}]  {p['achado_por']}")
                continue
            if n != 1:
                print(f"  FALHA  {arq} patch {i}: {n} ocorrencias (esperava 1)")
                print(f"         {p['motivo'][:90]}...")
                falhas += 1
                continue
            # GUARDA (bug real, achado em 31/08/2026): se `antigo` for PREFIXO de
            # `novo`, ele volta a casar a cada execucao e o bloco e anexado de novo.
            # Aconteceu: um patch da Q3 inseriu o mesmo paragrafo OITO vezes ao longo
            # das rodadas, sem nenhuma falha reportada. A guarda abaixo torna isso
            # impossivel de passar despercebido.
            if p["antigo"] in p["novo"]:
                raise SystemExit(
                    f"{arq} patch {i}: `antigo` e substring de `novo` — o patch nao e "
                    f"idempotente e vai duplicar o texto a cada execucao. Reescreva o "
                    f"`antigo` para incluir texto que desapareca na troca.")
            texto = texto.replace(p["antigo"], p["novo"])
            if p["antigo"] in texto:
                raise SystemExit(
                    f"{arq} patch {i}: `antigo` ainda aparece depois da substituicao.")
            print(f"  OK     {arq} patch {i}  [{p['gravidade']:11s}]  {p['achado_por']}")
        open(arq, "w", encoding="utf-8").write(texto)
    print()
    print(f"{len(PATCHES)} patches aplicados, {falhas} falhas.")
    return 1 if falhas else 0

if __name__ == "__main__":
    sys.exit(aplicar())
