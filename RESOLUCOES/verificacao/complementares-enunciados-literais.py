# -*- coding: utf-8 -*-
"""Confere que cada enunciado literal dos complementares (geradores/dados/complementares-enunciados-literais.json
 e complementares-novos-enunciados.json)
aparece na página de origem do PDF do professor. Compara por palavras (sem espaços, sem tags, sem expoentes,
que o pdftotext come — 7.21), exigindo que >= 90% das palavras de 3+ letras do enunciado estejam na página.
Sai com código 1 se alguma transcrição não casar (lição de 06/10/2026: conferidor que falha com exit 0 é invisível)."""
import json, os, re, subprocess, sys, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B = os.path.dirname(R)
PDF = {"Campello": "material-complementar/analise-assintotica/analise-de-algoritmos-parte-2-campello.pdf",
       "IFMG": "semana-04-inducao-e-recorrencias/matematica-discreta-recorrencia-e-inducao-diego-mello-ifmg.pdf",
       "USP": "material-complementar/inducao-matematica/principio-de-inducao-finita-usp.pdf",
       "Loureiro": "semana-01-analise-de-algoritmos/slides-analise-de-complexidade-loureiro-ufmg.pdf",
       "Walace (IFMG)": "material-complementar/somatorios/somatorios-walace-rodrigues-ifmg.pdf",
       "Slides UNICAMP MC458": "semana-05-inducao-projeto-recursividade/inducao-no-projeto-de-algoritmos-unicamp-mc458.pdf",
       "Uber (UEM)": "material-complementar/analise-assintotica/crescimento-de-funcoes-uber-uem.pdf",
       "Rezende (UNICAMP)": "semana-04-inducao-e-recorrencias/relacoes-de-recorrencia-rezende-unicamp.pdf"}
import unicodedata
def palavras(s, eh_html=False):
    # o LaTeX dos slides gera "ı́" (i sem ponto + acento combinante) e til decomposto: normaliza os dois lados.
    # Tags só se tiram da TRANSCRIÇÃO (HTML): no texto do PDF, "grau < k, ... >" casaria como tag e comeria
    # a página inteira (7.3). Sub/sobrescrito colam na palavra, como o pdftotext faz ("log<sub>y</sub>" → "logy").
    if eh_html:
        s = re.sub(r"<p>\[Figura:.*?</p>", " ", s, flags=re.S)   # descrição nossa da imagem, não é texto do slide
        s = re.sub(r"</?(sub|sup)>", "", s)
        s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = s.lower().replace("ı", "i")
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
    return [w for w in re.findall(r"[a-z]{3,}", s)]
lit = json.load(open(os.path.join(R, "geradores", "dados", "complementares-enunciados-literais.json"), encoding="utf-8"))
# as 18 questões novas de 06/10/2026 (varredura de filtro duplo), mesmo critério
novos = json.load(open(os.path.join(R, "geradores", "dados", "complementares-novos-enunciados.json"), encoding="utf-8"))
assert len(novos) == 18 and not set(novos) & set(lit), "complementares-novos: esperava 18 entradas sem colisão"
lit.update(novos)
falhas = 0
for fonte, v in lit.items():
    pdf = os.path.join(B, PDF[fonte.split(",")[0]]); p = v["pagina"]
    pag = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), pdf, "-"], capture_output=True, text=True).stdout
    alvo = set(palavras(pag))
    ws = [w for w in palavras(v["html"].split("<p class='orig'>")[0], eh_html=True) if w not in ("sic",)]
    ok = sum(w in alvo for w in ws); taxa = ok / max(1, len(ws))
    marca = "ok " if taxa >= 0.9 else "FALHA"
    if taxa < 0.9: falhas += 1
    print(f"{marca} {fonte:38s} p.{p:<4} {ok}/{len(ws)} palavras ({taxa:.0%})" + ("" if taxa >= 0.9 else "  faltam: " + ", ".join(sorted(set(w for w in ws if w not in alvo)))[:120]))
print("\nRESULTADO:", "OK" if not falhas else f"{falhas} transcrição(ões) sem correspondência")
sys.exit(1 if falhas else 0)
