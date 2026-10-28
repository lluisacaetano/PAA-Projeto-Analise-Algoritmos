# -*- coding: utf-8 -*-
"""
Confere que as 12 questoes da Lista 4 entraram no banco consolidado E que a
entrada delas nao mexeu nas 73 questoes que ja estavam la.

Cuidado: o banco renderiza a fonte em versalete (font-variant: small-caps), e o
pdftotext quebra isso em "L ista 4, Q1( a )". A normalizacao abaixo remove os
espacos espurios antes de comparar -- foi assim que uma primeira conferencia
deu 12 falsos negativos.

Rodar da raiz do projeto.
"""
import subprocess, unicodedata, re, sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def texto(pdf):
    return subprocess.run(["pdftotext","-layout",pdf,"-"],
                          capture_output=True, text=True).stdout.replace("‐\n","").replace("-\n","")

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    for a,b in [("−","-"),("–","-"),("—","-")]: s = s.replace(a,b)
    s = s.replace("_","").replace("^","")
    s = re.sub(r"\s+", " ", s)
    return s

def norm_versalete(s):
    """Alem do normal, colapsa TODO espaco -- desfaz a quebra do versalete."""
    return re.sub(r"\s+", "", norm(s))

banco = texto("RESOLUCOES/banco-de-questoes.pdf")
b_v = norm_versalete(banco)
b_n = norm(banco)

falhas = 0
print("=" * 72)
print("As 12 questoes da Lista 4 estao no banco?")
print("=" * 72)
rotulos = [f"Lista 4, Q1({c})" for c in "abcde"] + \
          [f"Lista 4, Q2({c})" for c in "abcde"] + \
          ["Lista 4, Q3", "Slides UNICAMP MC458, Exemplo 3"]
for r in rotulos:
    ok = norm_versalete(r) in b_v
    print(("  OK   " if ok else "  FALHA") + f'  "{r}"'); falhas += 0 if ok else 1

print()
print("O conteudo verificado chegou junto?")
conteudo = [
 "c1 = 1, c2 = 2, n0 = 1",          # Q1(e) testemunhas
 "T(1) + 2(n-1)",                    # Q1(e) desenrolar
 "n0 = 7", "n0 = 3", "n0 = 2",       # Q2 testemunhas dos casos de igualdade
 "lg 1 = 0",                         # Q2 fencepost
 "c1 = c/lg b",                      # Q2 testemunhas para c != 1
 "T1 ∈ A  e  A ∩ B ≠ ∅",             # Q3 criterio corrigido
 "|A ∩ B| = k - 1",
 "concluir o consequente",           # Q3 termo corrigido
 "Joel E. Cohen",                    # Q3 atribuicao corrigida
 "split perfeito",                   # apendice
 "21 quadros",
]
for c in conteudo:
    ok = norm(c) in b_n
    print(("  OK   " if ok else "  FALHA") + f'  "{c}"'); falhas += 0 if ok else 1

print()
print("Residuos das versoes refutadas nao podem ter entrado:")
for r in ["afirmar o consequente sem", "asseverar o consequente", "~22 quadros",
          "nenhuma das duas se aplica", "apenas se reescalam por c",
          "tem pelo menos dois termos"]:
    # "primeiro caso" NAO entra nesta lista: no banco ele aparece duas vezes,
    # nas resolucoes da prova de 2025, referindo-se a a < b^k -- que e mesmo o
    # primeiro caso na ordem do professor. O residuo a evitar era "primeiro caso"
    # apontando para a > b^k, e isso e coberto por lista04-html-bate-com-verificado.py,
    # que confere os arquivos da lista 4 especificamente.
    ok = norm(r) not in b_n
    print(("  OK   " if ok else "  FALHA") + f'  "{r}"'); falhas += 0 if ok else 1

print()
print("As 73 questoes anteriores continuam la? (amostra de rotulos)")
for r in ["Lista 1, Q3(a)", "Lista 2, Q3(d)", "Lista 3, Q1", "Prova 2025, Q1",
          "Campello, ex. 1", "Loureiro, ex. 8", "Walace (IFMG), ex. 1"]:
    ok = norm_versalete(r) in b_v
    print(("  OK   " if ok else "  FALHA") + f'  "{r}"'); falhas += 0 if ok else 1

print()
print("=" * 72)
print("Banco consolidado consistente." if not falhas else f"{falhas} FALHAS.")
print("=" * 72)
sys.exit(1 if falhas else 0)
