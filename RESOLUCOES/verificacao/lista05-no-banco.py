# -*- coding: utf-8 -*-
"""
As 5 questões da Lista 5 entraram no banco-de-questoes.pdf, com a resolução certa, e as 90
anteriores continuam lá?

Cuidados herdados (CLAUDE.md 7.2b e 7.13):
  - o banco renderiza a fonte em versalete e o pdftotext quebra isso em "L ista 5, Q1";
    a comparação de rótulos remove TODO espaço;
  - o extrator do banco só enxerga <div class="item">: por isso se procura, para cada questão,
    uma frase do QUADRO "Resposta" (o último bloco), que é o que sumiria primeiro.

Rodar da raiz do projeto:  python3 RESOLUCOES/verificacao/lista05-no-banco.py
"""
import os
import re
import subprocess
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(RAIZ)
sys.path.insert(0, "RESOLUCOES/geradores")
import catalogo as C  # noqa: E402


def norm(s, sem_espaco=False):
    s = re.sub(r"[‐-][ \t]*\n[ \t\f]*", "", s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = s.replace("−", "-")
    return re.sub(r"\s+", "" if sem_espaco else " ", s)


txt = subprocess.run(["pdftotext", "-layout", "RESOLUCOES/banco-de-questoes.pdf", "-"],
                     capture_output=True, text=True).stdout
junto, espacado = norm(txt, True), norm(txt)
falhas = 0


def checa(rot, ok, det=""):
    global falhas
    print(("  OK   " if ok else "  FALHA") + f"  {rot}" + (f"   {det}" if det else ""))
    falhas += 0 if ok else 1


print("=" * 72)
print("Lista 5 no banco de questões")
print("=" * 72)
n_l5 = sum(1 for q in C.Q if q["res"][0] == "L5")
checa("catálogo tem 112 questões (94 + 18 complementares novas de 06/10/2026), 5 da Lista 5", len(C.Q) == 112 and n_l5 == 5, f"{len(C.Q)} / {n_l5}")

# cada rótulo aparece 2× (Parte I, enunciados; Parte II, resoluções)
for q in (1, 2, 3, 4, 5):
    rot = norm(f"Lista 5, Q{q}", True)
    k = junto.count(rot)
    checa(f"rótulo 'Lista 5, Q{q}' na Parte I e na Parte II", k >= 2, f"{k} ocorrências")

# uma frase do quadro Resposta de cada questão (o bloco final)
RESPOSTAS = [
    ("Q1", "Nenhuma é assintoticamente mais eficiente"),
    ("Q2", "Galope + busca binária"),
    ("Q3", "O mais eficiente no pior caso é"),
    ("Q4", "prova-se a forma mais forte"),
    ("Q5", "Não se aplica: a = 3/2 não é natural"),
]
for q, frase in RESPOSTAS:
    checa(f"{q}: quadro Resposta presente no banco", norm(frase) in espacado, frase)

# as questões anteriores continuam lá (amostra de rótulos de cada fonte)
for rot in ["Lista 1, Q3(a)", "Lista 2, Q3(d)", "Lista 3, Q5", "Lista 4, Q5", "Prova 2025, Q1",
            "Slides UNICAMP MC458, Exemplo 3"]:
    checa(f"continua no banco: {rot}", norm(rot, True) in junto)

m = re.search(r"(\d+)\s*quest[oõ]es com resolu", espacado)
checa("capa anuncia 112 questões com resolução (94 + 18 complementares novas de 06/10/2026)", bool(m) and m.group(1) == "112", m.group(1) if m else "?")

print()
print("=" * 72)
print("Banco OK." if not falhas else f"{falhas} FALHA(S).")
print("=" * 72)
sys.exit(1 if falhas else 0)
