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
 ("1","5,0","PROVA-A","1",
  "Você está em um campo minado infinitamente grande. Você tem um detector de minas que só consegue "
  "identificar uma mina localizada no máximo a <b>um passo</b> de distância. Você deve encontrar a primeira "
  "mina do campo, mas a única informação que você tem sobre esta mina é que ela está diretamente à sua "
  "esquerda ou diretamente à sua direita. Entretanto, você não sabe a quantidade <span class='mat'>m</span> "
  "de passos de onde você está até a mina.<br><b>(3,0)</b> Projete um algoritmo para achar a mina em "
  "O(<span class='mat'>f</span>(m)) passos, com <span class='mat'>f</span>(m) polinomial em m."
  "<br><b>(2,0)</b> Argumente que seu algoritmo tem a complexidade requerida.", None),
 ("2(a)","2,0","PROVA-A","2a",
  "Se <span class='mat'>f</span>(n) ∈ O(<span class='mat'>u</span>(n)) e <span class='mat'>g</span>(n) ∈ "
  "O(<span class='mat'>v</span>(n)) então <span class='mat'>f</span>(n) <b>−</b> <span class='mat'>g</span>(n) ∈ "
  "O(<span class='mat'>u</span>(n) <b>−</b> <span class='mat'>v</span>(n)).",
  "Lista 2, Q3(c) — <b>mesma sentença com + trocado por −, e a resposta se inverte</b>"),
 ("2(b)","2,0","PROVA-A","2b",
  "Se <span class='mat'>f</span>(n) ∈ O(<span class='mat'>g</span>(n)) então <span class='mat'>g</span>(n) ∈ "
  "Ω(<span class='mat'>f</span>(n)).",
  "Lista 2, Q3(a) — uma das duas direções do “se e somente se”"),
 ("2(c)","2,0","PROVA-A","2c",
  "Se <span class='mat'>f</span>(n) ∈ O(<span class='mat'>g</span>(n)) e <span class='mat'>g</span>(n) ∈ "
  "O(<span class='mat'>f</span>(n)) então <span class='mat'>f</span>(n) ∈ Θ(<span class='mat'>g</span>(n)).",
  "Lista 2, Q3(d) — <b>idêntica, palavra por palavra</b>"),
 ("3(a)","2,0","PROVA-B","3a",
  "V ou F, com justificativa: a solução da equação de recorrência "
  "<span class='mat'>T</span>(n) = 2<span class='mat'>T</span>(n/7) + n pertence a O(n²).",
  "Loureiro, ex. 5–8 — mesma técnica (Teorema Mestre), recorrência nova"),
 ("3(b)","2,0","PROVA-B","3b",
  "V ou F, com justificativa: se <span class='mat'>f</span>(n) = 3n² − n + 4 então "
  "<span class='mat'>f</span>(n) ∈ Θ(n²).",
  "Lista 1, Q3(c) — mesma técnica, polinômio trocado"),
 ("3(c)","2,0","PROVA-B","3c",
  "V ou F, com justificativa: sejam <span class='mat'>f</span>(n) e <span class='mat'>g</span>(n) "
  "assintoticamente positivas e considere que <span class='mat'>g</span>(n) domina assintoticamente "
  "<span class='mat'>f</span>(n); então <span class='mat'>f</span>(n) + <span class='mat'>g</span>(n) ∈ "
  "Ω(<span class='mat'>f</span>(n)).", "definição de “domina assintoticamente” vem dos slides do Loureiro"),
 ("4(a)","2,0","PROVA-B","4a",
  "Alice afirma que seu algoritmo de ordenação Θ(n·lg n) é melhor que o de Bob, que é Θ(n²). Ao executarem "
  "ambos no mesmo ambiente, descobriram que para n &lt; 100 o Θ(n²) é mais rápido, e apenas para n ≥ 100 o "
  "Θ(n·lg n) é melhor. Explique como essa situação pode ocorrer.",
  "Lista 3, Q1 — <b>idêntica, palavra por palavra</b>"),
 ("4(b)","2,0","PROVA-B","4b",
  "Sejam <span class='mat'>f</span>(n) e <span class='mat'>g</span>(n) assintoticamente positivas e considere "
  "que <span class='mat'>g</span>(n) domina assintoticamente <span class='mat'>f</span>(n). Pode-se afirmar que "
  "<span class='mat'>f</span>(n) + <span class='mat'>g</span>(n) ∈ Ω(<span class='mat'>f</span>(n))? "
  "Justifique formalmente.", "repete a Questão 3(c) desta mesma prova"),
 ("5(a)","3,0","PROVA-B","5a",
  "O algoritmo <b>A</b> resolve o problema dividindo-o em <b>um único</b> subproblema de tamanho n/5, resolve "
  "recursivamente e combina as soluções em tempo Θ(n). O algoritmo <b>B</b> divide em <b>um único</b> "
  "subproblema de tamanho n−1, resolve recursivamente e combina em tempo constante.<br>"
  "Qual o consumo de tempo de cada um? Expresse em notação Θ e justifique.",
  "Lista 3, Q4(d) e (e) — mesma técnica de recorrência, casos novos (antes da atualização de 09/09/2026 era a Q3)"),
 ("5(b)","1,0","PROVA-B","5b",
  "Qual dos dois algoritmos é assintoticamente mais eficiente no pior caso? Justifique.", None),
]

H=['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
   '<title>PAA — Prova I de 2025 — Resolução</title>',f'<style>{CSS}</style></head><body>']
H.append('<div class="capa"><h1>Projeto e Análise de Algoritmos — Prova I de 2025</h1>'
         '<div class="meta">Resolução comentada · IFMG, Campus Formiga · Bacharelado em Ciência da Computação<br>'
         'Professor: Mário Luiz Rodrigues Oliveira · 25 pontos · 120 minutos</div></div>')
H.append('''<p class="nota"><b>Por que esta prova importa.</b> Cinco das onze questões saem direto das listas
de exercícios — duas idênticas palavra por palavra. As tarjas <span class="tag">de onde veio</span> indicam
a origem de cada uma. <b>Atenção à Questão 2(a):</b> ela é a Q3(c) da Lista 2 com o sinal trocado de + para −,
e a resposta inverte de verdadeira para falsa. Decorar o gabarito da lista faz perder os pontos.</p>''')

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

H.append('''<div class="rodape"><b>Sobre esta resolução.</b> Produzida com verificação adversarial em contexto
isolado e conferida numericamente: o algoritmo do campo minado foi simulado (a razão máxima passos/m observada
em m = 1…299 foi 12,888, confirmando a testemunha c = 14), as recorrências da Questão 5 foram resolvidas por
expansão direta, e as testemunhas da Questão 3(b) foram testadas em 300 000 valores de n. Os scripts estão em
<code>RESOLUCOES/verificacao/</code>. IFMG Campus Formiga.</div></body></html>''')

open(f"{OUT}/fontes-html/prova-01-resolucao.html","w",encoding="utf-8").write("\n".join(H))
print(f"HTML da prova gerado ({len('\n'.join(H))/1024:.0f} KB)")
