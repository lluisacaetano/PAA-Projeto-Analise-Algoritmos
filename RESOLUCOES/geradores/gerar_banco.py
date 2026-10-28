# -*- coding: utf-8 -*-
import re, os, json, glob, html, sys
SCR = "/Users/luisacaetano/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores"
sys.path.insert(0, SCR)
import catalogo as C
import correcoes

BASE = os.path.expanduser("~/DEV/PAA-Projeto-Analise-Algoritmos")
RES  = BASE + "/RESOLUCOES/fontes-html"

TASK = os.path.expanduser("~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores/dados")

# ─────────── 1. resoluções das listas (HTML já pronto) ───────────
LISTAS = {}

def extrai_itens(s):
    """Extrai cada <div class="item"> casando o </div> correspondente por
    contagem de aninhamento.

    A versão anterior usava um lookahead com a lista do que pode vir DEPOIS do
    bloco. Isso funcionava para as listas 1-3 por acidente do que elas contêm, e
    truncava 9 dos 26 blocos da lista 4, que usa <p class="nota"> genérico entre
    seções. Contar aninhamento é imune ao que vem depois. Conferido: reproduz os
    15 + 18 + 13 blocos das listas 1-3 exatamente como o padrão antigo.
    """
    itens, i, abre = [], 0, '<div class="item">'
    while True:
        ini = s.find(abre, i)
        if ini < 0:
            return itens
        j, prof = ini + len(abre), 1
        while prof:
            m = re.compile(r'<div\b|</div>').search(s, j)
            if not m:
                raise ValueError("div class=item sem fechamento")
            prof += 1 if m.group().startswith("<div") else -1
            j = m.end()
        itens.append(s[ini + len(abre): j - len("</div>")])
        i = j

for sig, arq in [("L1","lista-01-resolucao.html"), ("L2","lista-02-resolucao.html"),
                 ("L3","lista-03-resolucao.html"), ("L4","lista-04-resolucao.html"),
                 ("L5","lista-05-resolucao.html")]:
    s = open(os.path.join(RES,arq),encoding="utf-8").read()
    itens = extrai_itens(s)
    for i, it in enumerate(itens):
        if it.count("<div") != it.count("</div>"):
            raise SystemExit(f"{arq}: bloco {i} desbalanceado")
    LISTAS[sig] = {"itens": itens, "html": s}

def bloco_lista(sig, chave):
    d = LISTAS[sig]
    if isinstance(chave, int):
        return d["itens"][chave]
    if isinstance(chave, tuple):
        return "\n".join(d["itens"][i] for i in chave)
    if isinstance(chave, str) and chave.startswith("H3:"):
        alvo = chave[3:]
        m = re.search(re.escape(alvo) + r'(.*?)(?=<h2|<h3|<div class="rodape">)', d["html"], re.S)
        return (alvo + m.group(1)) if m else ""
    # chave string tipo "Q4": pega a seção e remove o enunciado
    m = re.search(rf'<h2[^>]*>Questão {chave[1:]}</h2>(.*?)(?=<h2|<div class="rodape">)', d["html"], re.S)
    corpo = m.group(1) if m else ""
    corpo = re.sub(r'<div class="enunciado">.*?</div>\s*', '', corpo, flags=re.S)
    return corpo

# ─────────── 2. resoluções dos workflows ───────────
def carrega(taskid):
    p = f"{TASK}/{taskid}.output"
    if not os.path.exists(p) or os.path.getsize(p)==0: return {}
    d = json.load(open(p))
    out = {}
    for b in d.get("result", []):
        k = b.get("fonte") or b.get("bloco")
        sol = b.get("solucao") or b.get("solucaoPrincipal")
        if sol:
            out[k] = {i["id"]: i for i in sol["itens"]}
    return out

WF = carrega("wlnpkedmu")   # complementares
PV = carrega("w6i8uhkbj")   # prova 2025 + somatórios
_a, _b = correcoes.aplica(WF); _c, _d = correcoes.aplica(PV)
_e, _f = correcoes.aplica_resposta(WF); _g, _h = correcoes.aplica_resposta(PV)
_sub = correcoes.substitui(WF) + correcoes.substitui(PV)   # LOTE 9: substituições integrais
_a += _e + _g; _b += _f + _h
print(f"correções aplicadas: {_a + _c} (falhas: {_b + _d})")

def txt2html(t):
    """converte o texto plano das soluções dos agentes em HTML legível"""
    t = html.escape(t)
    blocos = re.split(r'\n\s*\n', t)
    out = []
    for b in blocos:
        b = b.strip()
        if not b: continue
        # bloco de código / pseudocódigo: linhas numeradas ou muito indentadas
        if re.match(r'^\s*\d+:', b) or b.count("\n") > 2 and re.search(r'^\s{4,}\S', b, re.M):
            out.append('<pre class="cod">' + b + '</pre>')
        else:
            b = re.sub(r'^([A-ZÁÉÍÓÚÂÊÔÃÕÇ][A-ZÁÉÍÓÚÂÊÔÃÕÇ \(\)\.\-,0-9]{3,60}[\.:])',
                       r'<b>\1</b>', b)
            out.append("<p>" + b.replace("\n"," ") + "</p>")
    return "\n".join(out)

def resolucao(q):
    r = q["res"]
    if r[0] in ("L1","L2","L3","L4","L5"):
        return bloco_lista(r[0], r[1])
    if r[0] == "NV":
        # questões novas dos complementares (06/10/2026): o .md verificado é a fonte de verdade.
        # Formato: 1º parágrafo começa com "Resposta." ; o resto é a justificativa. Aborta se faltar (7.7).
        p = os.path.join(SCR, "dados", "complementares-novos", r[1] + ".md")
        if not os.path.exists(p):
            raise SystemExit(f"gerar_banco: resolução nova ausente: {p}")
        t = open(p, encoding="utf-8").read().strip()
        resp, _, resto = t.partition("\n\n")
        if not resp.startswith("Resposta."):
            raise SystemExit(f"gerar_banco: {p} não começa com 'Resposta.'")
        return (f'<p><b>Resposta.</b> {html.escape(resp[len("Resposta."):].strip())}</p>\n' + txt2html(resto))
    fonte = WF if r[0]=="WF" else PV
    it = fonte.get(r[1], {}).get(r[2])
    if not it:
        return '<p class="pend"><b>Resolução pendente</b> — o bloco correspondente ainda não foi processado.</p>'
    return (f'<p><b>Resposta.</b> {html.escape(it["resposta"])}</p>\n' + txt2html(it["justificativa"]))

# ─────────── 3. inventário das imagens dos materiais ───────────
INV = json.load(open(f"{SCR}/inventario.json"))
NOMES = {k: v["nome"] for k,v in INV.items()}

# ═══════════════════════ RENDERIZAÇÃO ═══════════════════════
OUT = BASE + "/RESOLUCOES"
IMGDIR = OUT + "/banco-img"

CSS = """
@page { size: A4; margin: 9mm 11mm 11mm 11mm; }
:root { --tinta:#16181d; --fraco:#5b6068; --linha:#c8ccd2; --caixa:#f2f3f5; --realce:#1a4a7a; --caiu:#a3400f; }
* { box-sizing:border-box; }
body { font-family:"Charter","Georgia","Times New Roman",serif; font-size:9.1pt; line-height:1.34;
       color:var(--tinta); margin:0; text-align:justify; hyphens:auto; }
h1 { font-size:15pt; margin:0 0 1mm 0; letter-spacing:-0.2pt; }
h2 { font-size:11.5pt; margin:6mm 0 2mm 0; padding-bottom:1mm; border-bottom:1pt solid var(--tinta); break-after:avoid; }
h3 { font-size:9.6pt; margin:4mm 0 1.5mm 0; color:var(--realce); break-after:avoid;
     border-bottom:0.4pt solid var(--linha); padding-bottom:0.6mm; }
h4 { font-size:9.2pt; margin:2.5mm 0 1mm 0; break-after:avoid; }
p { margin:0 0 1.5mm 0; }
.capa { border-bottom:1.5pt solid var(--tinta); padding-bottom:3mm; margin-bottom:4mm; }
.capa .meta { font-size:8pt; color:var(--fraco); line-height:1.45; }
.parte { break-before:page; text-align:center; padding:6mm 0 3mm 0; border-bottom:1.5pt solid var(--tinta); margin-bottom:4mm; }
.parte .n { font-size:8pt; letter-spacing:2pt; color:var(--fraco); font-variant:small-caps; }
.parte h1 { font-size:17pt; margin:1mm 0 1mm 0; }
.parte .sub { font-size:8.4pt; color:var(--fraco); }
.q { margin:0 0 2.6mm 0; break-inside:avoid; }
.q .cab { margin-bottom:0.8mm; }
.q .fonte { margin-right:2mm; }
.q .num { font-weight:700; color:var(--realce); font-size:9.4pt; white-space:nowrap; margin-right:2mm; }
.q .fonte { font-size:7.5pt; color:var(--fraco); font-variant:small-caps; letter-spacing:0.3pt; }
.tag { font-size:7pt; font-variant:small-caps; letter-spacing:0.5pt; padding:0.2mm 1.1mm;
       border:0.5pt solid var(--caiu); color:var(--caiu); border-radius:1mm; white-space:nowrap; }
.tag.pv { border-color:var(--realce); color:var(--realce); }
.dica { font-size:7.8pt; color:var(--fraco); font-style:italic; }
.cod2 { font-family:"SF Mono","Menlo","Consolas",monospace; font-size:7.5pt; line-height:1.3;
        background:var(--caixa); border:0.4pt solid var(--linha); padding:1.2mm 2mm; margin:1mm 0; }
pre.cod { font-family:"SF Mono","Menlo","Consolas",monospace; font-size:7.4pt; line-height:1.28;
          background:var(--caixa); border:0.4pt solid var(--linha); padding:1.2mm 2mm; margin:1.2mm 0;
          white-space:pre-wrap; break-inside:avoid; }
code { font-family:"SF Mono","Menlo","Consolas",monospace; font-size:7.6pt; }
.mat { font-family:"Cambria Math","Georgia",serif; font-style:italic; }
.centro { text-align:center; margin:1.4mm 0; font-family:"Cambria Math","Georgia",serif; }
.resp { font-weight:700; color:var(--realce); }
table { width:100%; border-collapse:collapse; font-size:8pt; margin:1.4mm 0 2mm 0; break-inside:avoid; }
th,td { border:0.4pt solid var(--linha); padding:0.8mm 1.4mm; text-align:left; vertical-align:top; }
th { background:var(--caixa); font-weight:700; font-size:7.7pt; }
td.n { text-align:center; white-space:nowrap; }
.nota { font-size:7.9pt; color:var(--fraco); border-left:1.2pt solid var(--linha); padding-left:2mm; margin:1.4mm 0; }
.item { margin-bottom:2mm; }
.passo { margin:1.2mm 0; padding-left:2.5mm; border-left:1pt solid var(--linha); }
.passo .rot2 { font-weight:700; font-style:normal; color:var(--tinta); }
.enunciado { background:var(--caixa); border-left:2pt solid var(--fraco); padding:1.6mm 2mm;
             margin:0 0 2mm 0; font-size:8.5pt; }
.enunciado .rot { font-variant:small-caps; letter-spacing:0.4pt; color:var(--fraco); font-size:7.4pt;
                  display:block; margin-bottom:0.6mm; }
sub,sup { font-size:68%; line-height:0; position:relative; font-style:normal; }
sub { bottom:-0.25em; } sup { top:-0.32em; }
.ex img { width:70%; border:0.5pt solid var(--linha); margin:0.8mm auto; display:block; }
.ex { break-inside:avoid; margin-bottom:2mm; }
.indice td { border:none; padding:0.5mm 1mm; }
.indice .t { font-weight:700; }
.rodape { margin-top:6mm; padding-top:2mm; border-top:0.6pt solid var(--linha); font-size:7.5pt; color:var(--fraco); }
"""

def conta_exemplos():
    tot = 0
    for sig, d in INV.items():
        tot += len(set(e for pg in d["paginas"] for e in pg["exemplos"]))
    return tot

def render():
    NEX = conta_exemplos()
    H = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
         '<title>PAA — Banco de Questões</title>', f'<style>{CSS}</style></head><body>']

    # numeração
    numeros = {}
    porTema = {}
    for t,_ in C.TEMAS: porTema[t] = [q for q in C.Q if q["tema"]==t]
    n = 0
    for t,_ in C.TEMAS:
        for q in porTema[t]:
            n += 1; numeros[id(q)] = n

    nblocos = 0
    for sig in ["PAA1","SHE","SHE2","CAM2","LOU","LOU2","CAV","UES","IFM2","REZ","REZ2","WAL","USP2"]:
        if sig not in INV: continue
        gs = []; ult = None; ultt = None
        for pg in INV[sig]["paginas"]:
            exs = tuple(pg["exemplos"]); tit = pg.get("titulo","")
            consec = ult is not None and pg["pag"] == ult + 1
            mesmo = gs and ((exs and gs[-1] == exs) or (tit and ultt == tit))
            if consec and (mesmo or (not exs and not tit)): pass
            else: gs.append(exs or (tit,))
            ult = pg["pag"]; ultt = tit
        nblocos += sum(1 for g in gs if g)

    # ── capa ──
    H.append('<div class="capa"><h1>Projeto e Análise de Algoritmos — Banco de Questões</h1>'
             '<div class="meta">IFMG, Campus Formiga · Bacharelado em Ciência da Computação · 2026/2<br>'
             'Professor: Mário Luiz Rodrigues Oliveira · Aluna: Luisa Caetano</div></div>')
    H.append(f'''<p><b>O que é este documento.</b> Reúne num só lugar todas as questões disponíveis da
disciplina: as listas de exercícios 1 a 5, os exercícios dos materiais complementares, a prova de 2025
e os exemplos resolvidos dos slides. São <b>{n} questões com resolução completa</b> mais
<b>{nblocos} exemplos resolvidos</b> extraídos dos slides.</p>
<p><b>Como usar.</b> A Parte I traz só os enunciados, agrupados por assunto — dá para resolver no papel
sem ver a resposta. A Parte II traz as resoluções, na mesma numeração. A Parte III reúne os exemplos
já resolvidos nos slides, reproduzidos como imagem do material original.</p>
<p><b>As marcas.</b> <span class="tag">caiu em 2025</span> indica questão que apareceu, literalmente ou
quase, na prova de 2025. <span class="tag pv">prova 2025</span> indica questão que <i>é</i> da prova de
2025. O professor reaproveita as listas na prova — essas marcas mostram onde investir tempo.</p>''')

    # ── índice ──
    H.append('<h2>Índice</h2><table class="indice">')
    for t,nome in C.TEMAS:
        qs = porTema[t]
        if not qs: continue
        a, b = numeros[id(qs[0])], numeros[id(qs[-1])]
        H.append(f'<tr><td class="t">{nome}</td><td class="n">questões {a}–{b}</td><td class="n">{len(qs)}</td></tr>')
    H.append(f'<tr><td class="t">Exemplos resolvidos dos materiais (Parte III)</td><td class="n">E1–E{nblocos}</td><td class="n">{nblocos}</td></tr>')
    H.append('</table>')

    def tags(q):
        if q["marcador"]=="caiu":  return ' <span class="tag">caiu em 2025</span>'
        if q["marcador"]=="prova": return ' <span class="tag pv">prova 2025</span>'
        return ''

    # ── PARTE I ──
    H.append('<div class="parte"><div class="n">Parte I</div><h1>Enunciados</h1>'
             f'<div class="sub">{n} questões agrupadas por assunto</div></div>')
    for t,nome in C.TEMAS:
        qs = porTema[t]
        if not qs: continue
        H.append(f'<h3>{nome}</h3>')
        for q in qs:
            H.append(f'<div class="q"><div class="cab"><span class="num">{numeros[id(q)]}.</span>'
                     f'<span class="fonte">{q["fonte"]}</span>{tags(q)}</div>{q["enunciado"]}</div>')

    # ── PARTE II ──
    H.append('<div class="parte"><div class="n">Parte II</div><h1>Resoluções</h1>'
             '<div class="sub">mesma numeração da Parte I</div></div>')
    for t,nome in C.TEMAS:
        qs = porTema[t]
        if not qs: continue
        H.append(f'<h3>{nome}</h3>')
        for q in qs:
            H.append(f'<div class="q"><div class="cab"><span class="num">{numeros[id(q)]}.</span>'
                     f'<span class="fonte">{q["fonte"]}</span>{tags(q)}</div>')
            H.append('<div class="enunciado"><span class="rot">Enunciado</span>' + q["enunciado"] + '</div>')
            H.append(resolucao(q))
            H.append('</div>')

    # ── PARTE III ──
    H.append('<div class="parte"><div class="n">Parte III</div><h1>Exemplos resolvidos dos materiais</h1>'
             f'<div class="sub">{nblocos} exemplos, reproduzidos do material original — enunciado e prova juntos</div></div>')
    H.append('''<p class="nota">Estes exemplos já vêm resolvidos nos slides. Estão aqui como
    <b>exercício para praticar</b>: tape a parte de baixo, tente resolver, depois confira. As páginas
    são reproduções fiéis do material original, para não haver risco de erro de transcrição.</p>''')
    ordem = ["PAA1","SHE","SHE2","CAM2","LOU","LOU2","CAV","UES","IFM2","REZ","REZ2","WAL","USP2"]
    e = 0
    for sig in ordem:
        if sig not in INV: continue
        H.append(f'<h3>{INV[sig]["nome"]}</h3>')
        # agrupa paginas consecutivas que pertencem ao mesmo exemplo
        grupos = []
        for pg in INV[sig]["paginas"]:
            exs = tuple(pg["exemplos"])
            tit = pg.get("titulo", "")
            consec = grupos and (pg["pag"] == grupos[-1]["pags"][-1] + 1)
            mesmo = grupos and ((exs and grupos[-1]["exs"] == exs) or
                                (tit and grupos[-1].get("titulo") == tit))
            if consec and mesmo:
                grupos[-1]["pags"].append(pg["pag"])
            elif consec and not exs and not tit:
                grupos[-1]["pags"].append(pg["pag"])
            else:
                grupos.append({"exs": exs, "pags": [pg["pag"]], "titulo": tit})
        for g in grupos:
            if not g["exs"] and not g.get("titulo"):
                continue
            e += 1
            if g["exs"]:
                lista = ", ".join(str(x) for x in g["exs"])
                rot = ("Exemplos " if len(g["exs"]) > 1 else "Exemplo ") + lista
            else:
                rot = g["titulo"]
            pp = g["pags"]
            faixa = f"p. {pp[0]}" if len(pp) == 1 else f"p. {pp[0]}–{pp[-1]}"
            H.append(f'<div class="ex"><div class="cab"><span class="num">E{e}.</span>'
                     f'<span class="fonte">{rot} — {faixa}</span></div>')
            for pag in pp:
                cand = glob.glob(f'{IMGDIR}/{sig}-{pag:03d}-*.png')
                if cand: H.append(f'<img src="file://{cand[0]}">')
            H.append('</div>')

    H.append('''<div class="rodape"><b>Sobre este banco.</b> As resoluções de todas as questões foram
produzidas com verificação adversarial em contexto isolado — verificadores independentes que receberam
apenas o enunciado e a prova final, com a missão de derrubá-la — e conferidas numericamente por scripts
em <code>resolucoes/verificacao/</code>. Os exemplos da Parte III são reproduções do material original e não
foram refeitos. Pendências (livros do Rosen e do Gersting, livro do OBMEP) estão em
<code>resolucoes/PENDENTE.md</code>. IFMG Campus Formiga, 2026/2.</div></body></html>''')
    return "\n".join(H), n, e

html_out, nq, nex = render()
open(f"{OUT}/fontes-html/banco-de-questoes.html","w",encoding="utf-8").write(html_out)
print(f"HTML gerado: {nq} questões + {nex} exemplos | {len(html_out)/1024:.0f} KB")
