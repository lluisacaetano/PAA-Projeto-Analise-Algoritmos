# -*- coding: utf-8 -*-
"""
Ajuste de 13/09/2026: o professor retirou o item (f) da Questão 1 da Lista 1.

Confere:
  1. a lista na pasta é o PDF que o professor mandou, e a Q1 dele tem cinco itens;
  2. o HTML e o PDF da resolução não têm mais o bloco do (f) nem frase que o trate como vigente;
  3. INVARIANTE DE ÍNDICE — para toda entrada ("L1", i) do catálogo, o <h3> do i-ésimo bloco de
     lista-01-resolucao.html corresponde ao rótulo da entrada. A retirada do (f) deslocou os
     blocos em −1, e os códigos da Q2 usavam um índice CALCULADO (6 + i) que um ajuste por
     regex de literais não pega: sem este teste, cada código sairia no banco com a resolução
     do seguinte, sem erro nenhum (CLAUDE.md 7.13);
  4. o banco não tem mais "Lista 1, Q1(f)" e cada código da Q2 aparece com a resolução certa.

Rodar da raiz do projeto:  python3 RESOLUCOES/verificacao/lista01-ajuste-2026-09-13.py
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
    s = s.replace("−", "-").replace("—", "-")
    return re.sub(r"\s+", "" if sem_espaco else " ", s)


def txt(pdf):
    return subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout


falhas = 0


def checa(rot, ok, det=""):
    global falhas
    print(("  OK   " if ok else "  FALHA") + f"  {rot}" + (f"   [{det}]" if det else ""))
    falhas += 0 if ok else 1


print("=" * 74)
print("Lista 1 — ajuste de 13/09/2026 (Q1(f) retirado)")
print("=" * 74)

# 1. a lista na pasta
lista = txt("listas-de-exercicios/lista-01-2026-2.pdf")
q1 = lista[lista.find("Questão 1."): lista.find("Questão 2.")]
itens = re.findall(r"\(([a-z])\) \( \)", q1)
checa("Q1 da lista atual tem os itens (a)–(e) e nada mais", itens == list("abcde"), "".join(itens))
checa("a lista atual não tem 'obrigatoriamente'", "obrigatoriamente" not in norm(q1))
checa("versão de 09/09 arquivada", os.path.exists("listas-de-exercicios/versoes-anteriores/lista-01-2026-2-versao-09-09.pdf"))

# 2. a resolução
H = open("RESOLUCOES/fontes-html/lista-01-resolucao.html", encoding="utf-8").read()
secao_q1 = H[H.find("<h2>Questão 1</h2>"): H.find("<h2>Questão 2</h2>")]
checa("HTML: sem bloco <h3>(f)", "<h3>(f)" not in H)
checa("HTML: enunciado da Q1 com 5 <li>", secao_q1.count("<li>") == 5, str(secao_q1.count("<li>")))
R = norm(txt("RESOLUCOES/lista-01-resolucao.pdf"))
for residuo in ["os seis itens", "e em (f) se refuta", "logo, nao ha obrigatoriamente.",
                "levar para o (f) o v do (e) antigo", "em (e) e (f) mudam duas coisas"]:
    checa(f"PDF da resolução sem o resíduo \"{residuo}\"", residuo not in R)
for decisiva in ["os cinco itens giram", "o item (f) retirado", "(l2) implica (l1)", "20 100 = 100·201"]:
    checa(f"PDF da resolução contém \"{decisiva}\"", norm(decisiva) in R)

# 3. invariante de índice: o bloco apontado é o do rótulo
blocos = re.findall(r'<div class="item">\s*<h3>(.*?)</h3>', H, flags=re.S)
blocos = [norm(re.sub(r"<[^>]+>", "", b)) for b in blocos]
checa("lista-01-resolucao.html tem 15 blocos (Q1 5 + Q2 5 + Q3 5)", len(blocos) == 15, str(len(blocos)))
for q in C.Q:
    if q["res"][0] != "L1" or not isinstance(q["res"][1], int):
        continue
    i, fonte = q["res"][1], q["fonte"]
    h3 = blocos[i] if i < len(blocos) else "(fora do intervalo)"
    m1 = re.match(r"Lista 1, Q1\((\w)\)$", fonte)
    m2 = re.match(r"Lista 1, Q2 — código (\d)$", fonte)
    m3 = re.match(r"Lista 1, Q3\((\w)\)$", fonte)
    if m1:
        ok = h3.startswith(f"({m1.group(1)})") and i <= 4
    elif m2:
        ok = h3.startswith(f"codigo {m2.group(1)}")
    elif m3:
        ok = h3.startswith(f"({m3.group(1)}) f(n)")
    else:
        ok = False
    checa(f"{fonte:26s} -> bloco {i:2d}", ok, h3[:40])

# 4. banco
b = txt("RESOLUCOES/banco-de-questoes.pdf")
bj = norm(b, True)
checa("banco sem o rótulo 'Lista 1, Q1(f)'", norm("Lista 1, Q1(f)", True) not in bj)
checa("banco com 'Lista 1, Q1(e)'", norm("Lista 1, Q1(e)", True) in bj)
# na Parte II, cada código da Q2 tem de vir seguido da SUA resolução (h3 "Código k — ...")
parte2 = bj[bj.find(norm("Resoluções", True) + norm("mesma numeração", True)):] or bj
for k in range(1, 6):
    rot = norm(f"Lista 1, Q2 — código {k}", True)
    pos = parte2.find(rot)
    trecho = parte2[pos: pos + 1500] if pos >= 0 else ""
    checa(f"banco: 'código {k}' seguido de 'Código {k} — O(…)'", pos >= 0 and norm(f"Código {k} — O(", True) in trecho)

print()
print("=" * 74)
print("Ajuste de 13/09 consistente." if not falhas else f"{falhas} FALHA(S).")
print("=" * 74)
sys.exit(1 if falhas else 0)
