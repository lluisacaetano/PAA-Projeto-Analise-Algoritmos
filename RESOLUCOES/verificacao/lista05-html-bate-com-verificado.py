# -*- coding: utf-8 -*-
"""
Lista 5: o PDF diz o mesmo que os .md que passaram pelos verificadores?

Na Lista 5 o HTML é GERADO dos .md (geradores/gerar_lista05.py, que já confere linha a linha
que nada caiu nem duplicou). Este script é a conferência independente, no PDF final, no mesmo
molde de lista04-html-bate-com-verificado.py:
  - afirmações decisivas: têm de estar no PDF E nos .md;
  - resíduos das versões refutadas (historico/q*-r*.md): não podem estar em nenhum dos dois;
  - trechos que têm de aparecer exatamente uma vez (teste de duplicação, CLAUDE.md 7.10).
Resíduo é a frase refutada EM USO, longa o bastante para não casar texto legítimo (7.14).

Rodar da raiz do projeto:  python3 RESOLUCOES/verificacao/lista05-html-bate-com-verificado.py
"""
import os
import re
import subprocess
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(RAIZ)
MD = "RESOLUCOES/geradores/dados/lista05/"
PDF = "RESOLUCOES/lista-05-resolucao.pdf"


def norm(s):
    s = re.sub(r"[‐-][ \t]*\n[ \t\f]*", "", s)      # hifenização de fim de linha (7.2b)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    for a, b in [("−", "-"), ("–", "-"), ("—", "-"), ("∗", "*")]:
        s = s.replace(a, b)
    s = s.replace("**", "").replace("_", "").replace("^", "")
    return re.sub(r"\s+", " ", s)


pdf = norm(subprocess.run(["pdftotext", "-layout", PDF, "-"], capture_output=True, text=True).stdout)
mds = {f: norm(open(MD + f, encoding="utf-8").read()) for f in
       ["q1-limpo.md", "q2-limpo.md", "q3-limpo.md", "q4-limpo.md", "q5-limpo.md"]}
md_todo = " || ".join(mds.values())

DECISIVAS = [
    # Q1
    ("Q1 resposta",       "Nenhuma das duas."),
    ("Q1 comparações",    "exatamente o mesmo número de comparações entre elementos"),
    ("Q1 pior caso",      "O vetor estritamente crescente toma o ramo"),
    ("Q1 pilha",          "Profundidade da pilha: 1 + ⌈lg n⌉"),
    ("Q1 cota inferior",  "Nenhuma abordagem pode ser melhor que Θ(n)."),
    ("Q1 lema R",         "a indução não usa o sinal de u nem de v"),
    # Q2
    ("Q2 galope",         "fase 1 (galope)"),
    ("Q2 uma leitura",    "meio ← ⌊(lo + hi)/2⌋;  v ← A[meio]"),
    ("Q2 cota inferior",  "tome x = A[m] + 1"),
    ("Q2 Θ(lg m)",        "c₁ = 1, c₂ = 5, m₀ = 2"),
    ("Q2 o(n)",           "n₀ = max(16, ⌊25/c²⌋ + 1)"),
    ("Q2 f(0)",           "f(0) = 2"),
    # Q3
    ("Q3 resposta",       "O mais eficiente no pior caso é C, com Θ(n² lg n)"),
    ("Q3 ordem",          "C ≺ A ≺ B"),
    ("Q3 hierarquia",     "onde c é uma constante arbitrária inteira ≥ 2"),
    ("Q3 monotonia",      "a partir de algum N"),
    ("Q3 lema",           "Lema. Sejam T e T′ definidas pela mesma recorrência"),
    # Q4
    ("Q4 prova 1",        "Prova 1 — fortalecendo a hipótese"),
    ("Q4 prova 2",        "S(n+1) = 1/2 + S(n)/2"),
    ("Q4 princípio",      "pelo princípio da indução Q(n)"),
    # Q5
    ("Q5 (f)",            "sairia Θ(lg n), que é falso"),
    ("Q5 (h) b=2",        "Simplificando o argumento: 2n/4 = n/2"),
    ("Q5 (i) a=3/2",      "a = 3/2 não é natural"),
    ("Q5 (d) T(16)",      "T(16) = 5 − 16 = −11"),
    ("Q5 (d) C",          "chama-se aqui de C a"),
    ("Q5 (g) base",       "não depende do caso base"),
    ("Q5 ordem linhas",   "na ordem em que o formulário os imprime"),
]

RESIDUOS = [
    # Q1, rodada 1
    "então o custo de uma entrada de tamanho n não depende dos valores",
    "Chamadas recursivas: n.",
    "chamada com n ≥ 2 (linhas 1, 3 e 4)",
    # Q1, rodada 2
    "No nível i da árvore de recursão de MaxB há 2^i chamadas, cada uma",
    # Q1, rodada 3
    "Tomando (d_b, c) = (1, 0) e (0, 1)",
    # Q2, rodada 1
    "se A[meio] < x então lo ← meio + 1",
    "isto é, Θ(lg m) no pior caso",
    "com 2^(J−1) ≤ m, isto é, hi ≤ 2m) em O(lg m) passos",
    # Q3, rodadas 1 e 2
    "≈ Θ(n^2,32)",
    "(H5 do formulário)",
    "Que o custo não diminua com n em todo",
    # Q4, rodada 1
    "a assertiva exata como P(n)",
    "Por que não dá para fazer a indução",
    # Q5, rodadas 1–3
    "em (d), (f), (g) e (i), aplicar a fórmula às cegas",
    "quando o caso base é grande",
    "depende de c > 4·4^(m0)",
    # A normalização põe tudo em minúsculas, então "T(n) = c para n ≤ n0" casaria o texto
    # CORRIGIDO "T(n) = C para n ≤ n0" (7.14). O resíduo é a continuação que só a versão
    # refutada tinha.
    "T(n) = c para n ≤ n0, o limiar muda",
]

UNICOS = [
    "Nenhuma das duas.",
    "O mais eficiente no pior caso é",
    "Prova 2 — a própria assertiva como hipótese de indução",
    "Quadro-resumo",
]

falhas = 0
print("=" * 78)
print("Lista 5: o PDF diz o mesmo que os .md que passaram pelos verificadores?")
print("=" * 78)
for rot, frase in DECISIVAS:
    f = norm(frase)
    no_pdf, no_md = f in pdf, f in md_todo
    ok = no_pdf and no_md
    print(("  OK   " if ok else "  FALHA") + f"  {rot:18s} pdf={no_pdf!s:5s} md={no_md!s:5s}  \"{frase[:48]}\"")
    falhas += 0 if ok else 1

print("\nResíduos das versões refutadas (não podem estar nem no PDF nem nos .md):")
for frase in RESIDUOS:
    f = norm(frase)
    no_pdf, no_md = f in pdf, f in md_todo
    ok = not no_pdf and not no_md
    print(("  OK   " if ok else "  FALHA") + f"  pdf={no_pdf!s:5s} md={no_md!s:5s}  \"{frase[:56]}\"")
    falhas += 0 if ok else 1

# O resíduo tem de ter existido: confere que cada um casa em ALGUMA versão do histórico.
hist = " || ".join(norm(open(os.path.join(MD, "historico", h), encoding="utf-8").read())
                   for h in sorted(os.listdir(MD + "historico")))
print("\nCada resíduo casa em alguma versão refutada (senão o teste é vazio):")
for frase in RESIDUOS:
    ok = norm(frase) in hist
    print(("  OK   " if ok else "  FALHA") + f"  \"{frase[:60]}\"")
    falhas += 0 if ok else 1

print("\nTrechos que têm de aparecer exatamente uma vez (teste de duplicação):")
for frase in UNICOS:
    f = norm(frase)
    n_md, n_pdf = md_todo.count(f), pdf.count(f)
    ok = n_md == 1 and n_pdf == 1
    print(("  OK   " if ok else "  FALHA") + f"  md={n_md} pdf={n_pdf}  \"{frase[:50]}\"")
    falhas += 0 if ok else 1

print()
print("=" * 78)
print("PDF e .md verificados dizem a mesma coisa." if not falhas
      else f"{falhas} FALHAS — o PDF divergiu do texto verificado.")
print("=" * 78)
sys.exit(1 if falhas else 0)
