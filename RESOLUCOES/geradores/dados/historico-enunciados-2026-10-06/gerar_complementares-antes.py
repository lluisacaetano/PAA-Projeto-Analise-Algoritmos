# -*- coding: utf-8 -*-
import sys, os, json, re, html
SCR="/Users/luisacaetano/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores"
sys.path.insert(0,SCR)
src = open(f"{SCR}/gerar_banco.py").read()
exec(src.split('# ═══════════════════════ RENDERIZAÇÃO')[0])
CSS = src[src.index('CSS = """')+9 : src.index('"""', src.index('CSS = """')+9)]

OUT  = os.path.expanduser("~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES")
IMGDIR = OUT + "/banco-img"
INV = json.load(open(f"{SCR}/inventario.json"))

FORA = ('Lista 1','Lista 2','Lista 3','Prova')
QS = [q for q in C.Q if not q['fonte'].startswith(FORA)]
assert len(QS) == 24, f"esperava 24, veio {len(QS)}"
assert not any('Lista' in q['fonte'] or 'Prova' in q['fonte'] for q in QS), "vazou lista/prova"

# agrupa por material de origem, na ordem em que a disciplina apresenta
ORDEM = ["Loureiro","Campello","IFMG","Walace (IFMG)","USP"]
TITULOS = {
 "Loureiro":     "Loureiro — Análise de Complexidade (UFMG) · semana 1 · Teorema Mestre",
 "Campello":     "Campello — Análise de Algoritmos II · notação assintótica",
 "IFMG":         "Diego Mello — Matemática Discreta (IFMG Formiga) · semana 4",
 "Walace (IFMG)":"Walace Rodrigues — Somatórios (IFMG Formiga)",
 "USP":          "Princípio de Indução Finita (IME-USP)",
}
grupos = {k: [q for q in QS if q['fonte'].split(',')[0] == k] for k in ORDEM}
assert sum(len(v) for v in grupos.values()) == 24, "algum grupo ficou de fora"

EXTRA = """
.q { break-inside:auto; margin-bottom:4mm; padding-bottom:2mm; border-bottom:0.4pt dotted var(--linha); }
.solu { margin-top:1.6mm; padding-left:2.5mm; border-left:2pt solid var(--realce); }
.solu > p:first-child { margin-top:0; }
.rot-sol { font-variant:small-caps; letter-spacing:0.5pt; color:var(--realce);
           font-size:7.6pt; font-weight:700; display:block; margin-bottom:0.8mm; }
.parte { break-before:auto; }
"""

H=['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
   '<title>PAA — Exercícios dos materiais complementares</title>',
   f'<style>{CSS}{EXTRA}</style></head><body>']
H.append('<div class="capa"><h1>PAA — Exercícios dos materiais complementares</h1>'
         '<div class="meta">Resolução logo abaixo de cada enunciado · IFMG, Campus Formiga · 2026/2<br>'
         'Professor: Mário Luiz Rodrigues Oliveira · Aluna: Luisa Caetano</div></div>')
H.append(f'''<p><b>O que é.</b> As <b>{len(QS)} questões</b> que vêm dos PDFs e slides da disciplina —
sem as listas e sem a prova, que estão nos seus próprios documentos. Cada resolução vem
<b>logo abaixo do enunciado</b>, para conferência rápida na tela.</p>
<p><b>Depois delas</b>, os exemplos já resolvidos nos slides, reproduzidos do material original.</p>''')

H.append('<table class="indice">')
for k in ORDEM:
    H.append(f'<tr><td class="t">{TITULOS[k]}</td><td class="n">{len(grupos[k])}</td></tr>')
H.append('</table>')

n = 0
for k in ORDEM:
    H.append(f'<h3>{TITULOS[k]}</h3>')
    for q in grupos[k]:
        n += 1
        H.append(f'<div class="q"><div class="cab"><span class="num">{n}.</span>'
                 f'<span class="fonte">{q["fonte"]}</span></div>')
        H.append(q["enunciado"])
        H.append('<div class="solu"><span class="rot-sol">Resolução</span>')
        H.append(resolucao(q))
        H.append('</div></div>')
assert n == 24, f"renderizou {n} em vez de 24"

# ── exemplos dos slides ──
H.append('<div class="parte" style="break-before:page"><div class="n">Parte II</div>'
         '<h1>Exemplos resolvidos dos slides</h1>'
         '<div class="sub">reproduzidos do material original — enunciado e prova juntos</div></div>')
ordem_img = ["PAA1","SHE","SHE2","CAM2","LOU","LOU2","CAV","UES","IFM2","REZ","REZ2","WAL","USP2"]
import glob
e = 0
for sig in ordem_img:
    if sig not in INV: continue
    H.append(f'<h3>{INV[sig]["nome"]}</h3>')
    grupos_img = []
    for pg in INV[sig]["paginas"]:
        exs = tuple(pg["exemplos"]); tit = pg.get("titulo","")
        consec = grupos_img and (pg["pag"] == grupos_img[-1]["pags"][-1] + 1)
        mesmo = grupos_img and ((exs and grupos_img[-1]["exs"] == exs) or (tit and grupos_img[-1].get("titulo") == tit))
        if consec and mesmo: grupos_img[-1]["pags"].append(pg["pag"])
        elif consec and not exs and not tit: grupos_img[-1]["pags"].append(pg["pag"])
        else: grupos_img.append({"exs":exs,"pags":[pg["pag"]],"titulo":tit})
    for g in grupos_img:
        if not g["exs"] and not g.get("titulo"): continue
        e += 1
        rot = (("Exemplos " if len(g["exs"])>1 else "Exemplo ") + ", ".join(str(x) for x in g["exs"])) if g["exs"] else g["titulo"]
        pp = g["pags"]; faixa = f"p. {pp[0]}" if len(pp)==1 else f"p. {pp[0]}–{pp[-1]}"
        H.append(f'<div class="ex"><div class="cab"><span class="num">E{e}.</span>'
                 f'<span class="fonte">{rot} — {faixa}</span></div>')
        for pag in pp:
            cand = glob.glob(f'{IMGDIR}/{sig}-{pag:03d}-*.png')
            if cand: H.append(f'<img src="file://{cand[0]}">')
        H.append('</div>')

H.append(f'''<div class="rodape"><b>Sobre este documento.</b> Contém as {n} questões dos materiais
complementares e {e} blocos de exemplos dos slides. As listas 1–3 e a prova de 2025 <b>não</b> estão aqui —
cada uma tem seu próprio PDF nesta pasta, e todas juntas estão em <code>banco-de-questoes.pdf</code>.
As resoluções passaram por verificação adversarial em contexto isolado e conferência numérica
(<code>RESOLUCOES/verificacao/</code>). IFMG Campus Formiga, 2026/2.</div></body></html>''')

open(f"{OUT}/fontes-html/complementares.html","w",encoding="utf-8").write("\n".join(H))
print(f"OK — {n} questões (resolução inline) + {e} blocos de exemplos")
