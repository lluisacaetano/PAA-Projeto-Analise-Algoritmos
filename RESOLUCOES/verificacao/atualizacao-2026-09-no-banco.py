# -*- coding: utf-8 -*-
"""
Confere que as 5 questoes novas da atualizacao de 09/09/2026 entraram no banco
consolidado, que os rotulos renumerados da Lista 3 estao certos, que o texto
verificado chegou junto -- e que as questoes que ja estavam la continuam.

Mesmo cuidado de lista04-no-banco.py: o banco renderiza a fonte em versalete e o
pdftotext quebra "Lista 3, Q4(a)" em "L ista 3, Q4( a )"; por isso os rotulos sao
comparados com TODO espaco removido.

Rodar da raiz do projeto.
"""
import subprocess, unicodedata, re, sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def norm(s):
    s = re.sub(r"[‐-][ \t]*\n[ \t\f]*", "", s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    for a, b in [("−", "-"), ("–", "-"), ("—", "-"), (" ", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s.replace("_", "").replace("^", ""))

txt = subprocess.run(["pdftotext", "-layout", "RESOLUCOES/banco-de-questoes.pdf", "-"],
                     capture_output=True, text=True).stdout
b_n = norm(txt)
b_v = re.sub(r"\s+", "", b_n)
V = lambda s: re.sub(r"\s+", "", norm(s))

falhas = 0
def linha(ok, t):
    global falhas
    print(("  OK    " if ok else "  FALHA ") + t); falhas += 0 if ok else 1

print("Rotulos novos e renumerados:")
for r in ["Lista 1, Q1(e)", "Lista 3, Q3", "Lista 3, Q4(a)", "Lista 3, Q4(b)",
          "Lista 3, Q4(c)", "Lista 3, Q4(d)", "Lista 3, Q4(e)", "Lista 3, Q5",
          "Lista 4, Q4", "Lista 4, Q5"]:
    linha(V(r) in b_v, f'"{r}"')

print("\nRotulos antigos da Lista 3 nao podem sobrar:")
for r in ["Lista 3, Q3(a)", "Lista 3, Q3(b)", "Lista 3, Q3(c)", "Lista 3, Q3(d)", "Lista 3, Q3(e)"]:
    linha(V(r) not in b_v, f'ausente "{r}"')
linha(V("Lista 1, Q1(f)") not in b_v, 'ausente "Lista 1, Q1(f)" (Q1(f) retirado pelo professor em 13/09/2026)')

print("\nTexto verificado das questoes novas chegou junto:")
for c in ["20 100 = 100·201", "p - q > 0", "(n - 3) + 2 = n - 1",
          "¬P(n) → ¬P(n+1)", "(n+2)(2n+3)", "duas arestas disjuntas",
          "Construir não é, por si só, inválido"]:
    linha(norm(c) in b_n, f'"{c}"')

print("\nResiduos das versoes refutadas:")
for r in ["com no maximo 3n + 2 operacoes", "exige a formula exata do lema",
          "o passo vai na direcao errada: comeca"]:
    linha(norm(r) not in b_n, f'ausente "{r}"')

print("\nQuestoes anteriores continuam la (amostra) e o apendice veio junto:")
for r in ["Lista 1, Q3(a)", "Lista 1, Q2 — código 5", "Lista 2, Q3(d)", "Lista 3, Q1", "Lista 3, Q2",
          "Lista 4, Q3", "Slides UNICAMP MC458, Exemplo 3", "Prova 2025, Q1", "Walace (IFMG), ex. 1"]:
    linha(V(r) in b_v, f'"{r}"')
linha(norm("21 quadros") in b_n and norm("split perfeito") in b_n,
      "apendice do slide (21 quadros, split perfeito) apontado pelos indices novos")
linha(norm("Código 1") in b_n and norm("O tamanho da constante não importa") in b_n,  # 06/10/2026: Q3(a) é 2^117
      "blocos da Lista 1 deslocados em +1 ainda casam (codigo 1, Q3(a))")

m = re.search(r"sao (\d+) questoes com resolucao completa", b_n)
# 14/09/2026: a Lista 5 acrescentou 5 questões (verificacao/lista05-no-banco.py confere quais).
# 13/09/2026: o professor retirou o Q1(f) da Lista 1 → 94.
# 06/10/2026: + 18 questões novas dos complementares (varredura de filtro duplo) → 112.
linha(bool(m) and m.group(1) == "112", f"contagem do banco = {m.group(1) if m else '?'} (esperado 112 = 85 + 5 de 09/09 + 5 da Lista 5 − Q1(f) retirado em 13/09 + 18 complementares novas de 06/10)")

print()
print("Banco consolidado consistente." if not falhas else f"{falhas} FALHAS.")
sys.exit(1 if falhas else 0)
