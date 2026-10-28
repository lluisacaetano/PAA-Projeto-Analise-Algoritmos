# -*- coding: utf-8 -*-
import sys, os, json, re, html
SCR="/Users/luisacaetano/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores"
sys.path.insert(0,SCR)
exec(open(f"{SCR}/gerar_banco.py").read().split('# ═══════════════════════ RENDERIZAÇÃO')[0])

OUT = os.path.expanduser("~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES")
_src = open(f"{SCR}/gerar_banco.py", encoding="utf-8").read()
CSS = _src[_src.index('CSS = """')+9 : _src.index('"""', _src.index('CSS = """')+9)]
assert len(CSS) > 3000, "CSS não extraído do gerar_banco.py"

Q = [
 # 06/10/2026: enunciados transcritos LITERALMENTE da prova (antes estavam resumidos/parafraseados).
 # Itens que compartilham um enunciado comum (Q2, Q3, Q4, Q5) repetem esse enunciado em cada item.
 ("1","5,0","PROVA-A","1",
  "Você está em um campo minado infinitamente grande. Você tem um detector de minas que só consegue "
  "identificar uma mina localizada no máximo a um passo de distância. Você deve encontrar a primeira mina "
  "do campo, mas a única informação que você tem sobre esta mina é que ela está diretamente a sua esquerda "
  "ou diretamente a sua direita. Entretanto, você não sabe a quantidade <span class='mat'>m</span> de passos "
  "de onde você está até a mina.<br>(3.0 pontos) Projete um algoritmo para achar a mina em "
  "O(<span class='mat'>f</span>(<span class='mat'>m</span>)) passos. A função <span class='mat'>f</span>(<span class='mat'>m</span>) "
  "deve ser polinomial no parâmetro <span class='mat'>m</span>.<br>(2.0 pontos) Argumente que seu algoritmo "
  "tem a complexidade requerida.", None),
]
Q2 = ("Prove que as afirmativas abaixo são verdadeiras ou falsas, usando para isso as definições das notações "
      "assintóticas e/ou contra exemplos. Considere que as funções <span class='mat'>f</span>(n) e "
      "<span class='mat'>g</span>(n) são assintoticamente não negativas.<br>")
Q3 = ("A respeito da análise de algoritmos e propriedades das notações assintóticas, responda <b>V</b> para as "
      "sentenças que julgar verdadeiras e <b>F</b> para as sentenças que julgar falsas. Justifique suas respostas. "
      "Respostas sem justificativas não serão consideradas.<br>")
Q4 = "A respeito da análise de algoritmos e propriedades das notações assintóticas, responda:<br>"
Q5 = ("Suponha que, para resolver um problema com entradas de tamanho n, você tenha que escolher um dentre dois "
      "algoritmos A e B.<br>1. O algoritmo A resolve problemas dividindo-o em um único subproblema de tamanho n/5, "
      "resolve recursivamente o subproblema e então combina as soluções em tempo θ(n).<br>2. O algoritmo B resolve "
      "problemas de tamanho n, dividindo-o em único subproblema de tamanho n − 1, resolve recursivamente o "
      "subproblema e então combina as soluções em tempo constante.<br>Considere essas informações e responda:<br>")
F, G, U, V = ("<span class='mat'>f</span>(n)", "<span class='mat'>g</span>(n)",
              "<span class='mat'>u</span>(n)", "<span class='mat'>v</span>(n)")
Q += [
 ("2(a)","2,0","PROVA-A","2a",
  Q2 + f"a) (2.0 pontos) Se {F} ∈ O({U}) e {G} ∈ O({V}) então {F} − {G} ∈ O({U} − {V}).",
  "Lista 2, Q3(c) — <b>mesma sentença com + trocado por −, e a resposta se inverte</b>"),
 ("2(b)","2,0","PROVA-A","2b",
  Q2 + f"b) (2.0 pontos) Se {F} ∈ O({G}) então {G} ∈ Ω({F}).",
  "Lista 2, Q3(a) — uma das duas direções do “se e somente se”"),
 ("2(c)","2,0","PROVA-A","2c",
  Q2 + f"c) (2.0 pontos) Se {F} ∈ O({G}) e {G} ∈ O({F}) então {F} ∈ θ({G}).",
  "Lista 2, Q3(d) — <b>o item é idêntico, palavra por palavra</b> (o enunciado comum da lista diz “sentenças”; o da prova, “afirmativas”)"),
 ("3(a)","2,0","PROVA-B","3a",
  Q3 + "a) ( ) (2.0 pontos) A solução da equação de recorrência <span class='mat'>T</span>(n) = "
  "2<span class='mat'>T</span>(n/7) + n ∈ O(n<sup>2</sup>).",
  "Loureiro, ex. 5–8 — mesma técnica (Teorema Mestre), recorrência nova"),
 ("3(b)","2,0","PROVA-B","3b",
  Q3 + f"b) ( ) (2.0 pontos) Se {F} = 3 ∗ n<sup>2</sup> − n + 4 então {F} ∈ Θ(n<sup>2</sup>).",
  "Lista 1, Q3(c) — mesma técnica, polinômio trocado"),
 ("3(c)","2,0","PROVA-B","3c",
  Q3 + f"c) ( ) (2.0 pontos) Sejam as funções {F} e {G} assintoticamente positivas e considere que {G} "
  f"domina assintoticamente {F}, então {F} + {G} ∈ Ω({F}).",
  "definição de “domina assintoticamente” vem dos slides do Loureiro"),
 ("4(a)","2,0","PROVA-B","4a",
  Q4 + "(a) (2 pontos) Alice e Bob estão discutindo sobre o desempenho de seus algoritmos de ordenação. Alice "
  "afirma que o seu algoritmo de ordenação executando em tempo θ(n ∗ lgn) é melhor que algoritmo de Bob que "
  "executa em tempo θ(n<sup>2</sup>). Para decidir qual é melhor algoritmo, implementaram e executaram os dois "
  "algoritmos no mesmo ambiente (mesma arquitetura, mesmo sistema operacional, mesma linguagem de programação e "
  "mesmo compilador) em uma série de dados. Para espanto de Alice, descobriram que quando n &lt; 100 o algoritmo "
  "θ(n<sup>2</sup>) é mais rápido e apenas quando n ≥ 100 é que o algoritmo θ(n ∗ lgn) é melhor. Explique como "
  "essa situação pode ocorrer.",
  "Lista 3, Q1 — <b>idêntica, exceto por uma expressão</b>: a lista diz “executaram <i>ambos os</i> algoritmos”, a prova diz “executaram <i>os dois</i> algoritmos”"),
 ("4(b)","2,0","PROVA-B","4b",
  Q4 + f"(b) (2 pontos) Sejam as funções {F} e {G} assintoticamente positivas e considere que {G} domina "
  f"assintoticamente {F}. Pode-se afirmar que {F} + {G} ∈ Ω({F}) ? Justifique formalmente sua resposta.",
  "repete a Questão 3(c) desta mesma prova"),
 ("5(a)","3,0","PROVA-B","5a",
  Q5 + "(a) (3.0 pontos) Qual o consumo de tempo de cada um dos algoritmos? Expresse sua resposta em termos da "
  "notação θ. Justifique sua resposta. Respostas sem justificativas não serão consideradas.",
  "Lista 3, Q4(d) e (e) — mesma técnica de recorrência, casos novos (antes da atualização de 09/09/2026 era a Q3)"),
 ("5(b)","1,0","PROVA-B","5b",
  Q5 + "(b) (1.0 ponto) Qual dos algoritmos é assintoticamente mais eficiente no pior caso? Justifique sua "
  "resposta. Respostas sem justificativas não serão consideradas.", None),
]

CABECALHO_PROVA = """<div class="enunciado" id="instrucoes-prova"><span class="rot">Cabeçalho, código de honra e instruções da prova (transcrição literal)</span>
<p>Instituto Federal de Educação, Ciência e Tecnologia · Curso: Bacharelado em Ciência da Computação ·
Disciplina: Projeto Análise de Algoritmos · Professor: Mário Luiz Rodrigues Oliveira · Atividade: Prova I ·
Formiga, MG, 13 de junho de 2025</p>
<p><b>Código de honra e conduta discente:</b><br>Eu, ______________________, matrícula __________ prometo pela
minha honra que fui honesto(a) e não trapaceei nessa avaliação passando ou recebendo cola.<br>
Formiga, MG, 13 de junho de 2025.</p>
<p><b>Instruções:</b></p>
<ol>
<li>Esta atividade deve, obrigatoriamente, ser resolvida <b>individualmente</b>.</li>
<li>Caso você ache que falta algum detalhe nas especificações, você deverá fazer as suposições que julgar
necessárias e escrevê-las junto à resolução da atividade. Pode acontecer também que a descrição desta atividade
contenha dados e/ou especificações supérfluas para sua solução. Utilize sua capacidade de julgamento para
separar o supérfluo do necessário.</li>
<li>Na(s) folha(s) contendo a solução desta atividade coloque seu nome e matrícula. Na correção desta prova
será considerado apenas e tão somente o conteúdo que estiver na(s) folha(s) de solução.</li>
<li><b>Não basta apresentar apenas o(s) resultado(s). É necessário mostrar a resolução ou o raciocínio
utilizado para responder às questões. Portanto, justifique formalmente todas as suas respostas. Questões sem
respostas ou com respostas sem justificativas não serão consideradas</b>.</li>
<li>É permitido aos discentes consultar materiais impressos, tais como: livros, materiais disponibilizados
pelo professor e anotações produzidas pelo discente.</li>
<li>Não são permitidas consultas a materiais/conteúdos disponíveis na <i>Web</i>.</li>
<li>Durante a realização desta atividade não é permitido o uso de celulares e outros dispositivos
eletrônicos; bem como também conversas e/ou diálogos com colegas.</li>
<li>Seja honesto(a) e lembre-se: você deu sua palavra de honra.</li>
<li><b>Plágio ou a tentativa de plágio implicará em nota 0 (zero) a todos os envolvidos</b>. Sem prejuízo de
demais sanções/pebalidades cabíveis nesta situação.</li>
<li>O valor desta atividade é <b>25 pontos</b> e você terá até 120 minutos para resolvê-la.</li>
</ol></div>"""

ANEXO_PROVA = """<h2>Informações que podem ser úteis</h2>
<div class="enunciado" id="informacoes-prova"><span class="rot">Anexo da prova (transcrição literal)</span>
<p><b>Somatórios e Logaritmos:</b></p>
<ul>
<li>Σ<sub>i=1</sub><sup>n</sup> (i) = n(n + 1)/2</li>
<li>Σ<sub>i=1</sub><sup>n</sup> (a<sup>i</sup>) = a(a<sup>n</sup> − 1)/(a − 1)</li>
<li>log (a ∗ b) = log a + log b</li>
<li>log (a/b) = log a − log b</li>
<li>log<sub>b</sub> a = log<sub>c</sub> a/ log<sub>c</sub> b</li>
<li>log<sub>b</sub> a<sup>c</sup> = c ∗ log<sub>b</sub> a</li>
<li>lg a = log<sub>2</sub> a</li>
</ul>
<p><b>Hierarquia de funções:</b></p>
<p>A seguinte hierarquia de funções pode ser definida do ponto de vista assintótico:
1 ≺ log(n) ≺ √n ≺ n ≺ n ∗ log(n) ≺ n<sup>c</sup> ≺ c<sup>n</sup> ≺ n! ≺ n<sup>n</sup> onde c é uma constante
arbitrária inteira ≥ 2.</p>
<p><b>Teorema mestre:</b></p>
<p>Sejam as constantes naturais a ≥ 1, b ≥ 2 e k ≥ 0. Considere a função f(n) da forma c∗n<sup>k</sup>, na qual
c &gt; 0 e ∈ R, seja a equação de recorrência dada por T(n) = aT(n/b)+f(n) e suponha n uma potência exata de b.
Considere ainda que T é uma função que leva números naturais em números reais positivos e que T é
assintoticamente não decrescente, Nessas condições, [BRASSARD and BRATLEY, 1996] indicam que a solução dessa
recorrência é limitada assintoticamente por</p>
<p style="text-align:center">T(n) = θ(n<sup>k</sup>) se a &lt; b<sup>k</sup>; &nbsp; θ(n<sup>k</sup> ∗ lg n) se a = b<sup>k</sup>;
&nbsp; θ(n<sup>log<sub>b</sub> a</sup>) se a &gt; b<sup>k</sup></p>
<p><b>Referências</b></p>
<p>[BRASSARD and BRATLEY, 1996] BRASSARD, G. and BRATLEY, P. (1996). Fundamentals of Algorithms. Prentice-Hall.</p>
</div>"""


H=['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
   '<title>PAA — Prova I de 2025 — Resolução</title>',f'<style>{CSS}</style></head><body>']
H.append('<div class="capa"><h1>Projeto e Análise de Algoritmos — Prova I de 2025</h1>'
         '<div class="meta">Resolução comentada · IFMG, Campus Formiga · Bacharelado em Ciência da Computação<br>'
         'Professor: Mário Luiz Rodrigues Oliveira · 25 pontos · 120 minutos</div></div>')
H.append('''<p class="nota"><b>Por que esta prova importa.</b> Cinco das onze questões saem direto das listas
de exercícios — uma delas idêntica palavra por palavra (2(c)) e outra a menos de uma expressão (4(a)). As tarjas <span class="tag">de onde veio</span> indicam
a origem de cada uma. <b>Atenção à Questão 2(a):</b> ela é a Q3(c) da Lista 2 com o sinal trocado de + para −,
e a resposta inverte de verdadeira para falsa. Decorar o gabarito da lista faz perder os pontos.</p>''')
H.append(CABECALHO_PROVA)

for num, pts, bloco, chave, enun, origem in Q:
    it = PV.get(bloco,{}).get(chave)
    H.append(f'<div class="q"><h3>Questão {num} <span style="font-weight:400;font-size:8pt;color:#5b6068">({pts} pontos)</span></h3>')
    H.append(f'<div class="enunciado"><span class="rot">Enunciado</span><p>{enun}</p></div>')
    if origem:
        H.append(f'<p style="margin-bottom:1.6mm"><span class="tag">de onde veio</span> &nbsp;{origem}</p>')
    if it:
        H.append(f'<p><b>Resposta.</b> {html.escape(it["resposta"])}</p>')
        H.append(txt2html(it["justificativa"]))
    else:
        H.append('<p class="pend">resolução não encontrada</p>')
    H.append('</div>')

H.append(ANEXO_PROVA)
H.append('''<div class="rodape"><b>Sobre esta resolução.</b> Produzida com verificação adversarial em contexto
isolado e conferida numericamente: o algoritmo do campo minado foi simulado (a razão máxima passos/m observada
em m = 1…299 foi 12,888, confirmando a testemunha c = 14), as recorrências da Questão 5 foram resolvidas por
expansão direta, e as testemunhas da Questão 3(b) foram testadas em 300 000 valores de n. Os scripts estão em
<code>RESOLUCOES/verificacao/</code>.<br><b>Auditoria de 06/10/2026.</b> Enunciados, cabeçalho, instruções e anexo
transcritos literalmente da prova (antes estavam resumidos). Corrigidos, sem mudar nenhuma resposta: a definição de
“domina assintoticamente” nas 3(c) e 4(b) (nos slides do Loureiro é |f| ≤ C|g|, um O, e não um o); o ponto de cruzamento
da 4(a) (a raiz de n/lg n = 15 é 99,56; 99,82 é a do exemplo com +20); as testemunhas de B na 5(a) (caso base mais barato
que uma combinação); a ponte entre Θ(n) e a forma c·n<sup>k</sup> do formulário, com testemunhas numéricas, na 5(a); e a
comparação de constantes da 5(b). Patches no lote 7 e 8 de <code>geradores/correcoes.py</code>. Verificação: 4 rodadas de 4
verificadores independentes; todas deram HOLDS em todas as questões, e os achados de cada rodada (cada vez menores) foram
corrigidos e reverificados. IFMG Campus Formiga.</div></body></html>''')

open(f"{OUT}/fontes-html/prova-01-resolucao.html","w",encoding="utf-8").write("\n".join(H))
print(f"HTML da prova gerado ({len('\n'.join(H))/1024:.0f} KB)")
