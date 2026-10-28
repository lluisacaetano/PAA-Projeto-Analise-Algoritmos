# -*- coding: utf-8 -*-
"""
Atualizacao de 09/09/2026 (listas 1, 3 e 4 revisadas pelo professor).

Os textos que passaram pelos verificadores adversariais sao os .md em
geradores/dados/lista0{1,3,4}/. Os PDFs sao a diagramacao deles. Este script
confere, para cada lista:
  1. toda afirmacao decisiva aparece no PDF E no .md verificado;
  2. nenhum residuo das versoes REFUTADAS sobreviveu (nem no PDF, nem no .md);
  3. trechos que tem de aparecer exatamente uma vez nao duplicaram (CLAUDE.md 7.10);
  4. os rotulos antigos da Lista 3 (Q3(a)..Q3(e)) sumiram do PDF da Lista 3.

Rodar da raiz do projeto:
  python3 RESOLUCOES/verificacao/atualizacao-2026-09-html-bate-com-verificado.py
"""
import subprocess, unicodedata, re, sys, os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(RAIZ)
D = "RESOLUCOES/geradores/dados/"

def norm(s):
    # mesma normalizacao de lista04-html-bate-com-verificado.py (hifenizacao de fim de
    # linha, inclusive a que cruza pagina com \x0c; acentos; sub/sobrescritos via NFKD)
    s = re.sub(r"[‐-][ \t]*\n[ \t\f]*", "", s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    for a, b in [("−", "-"), ("–", "-"), ("—", "-"), ("∗", "*"), (" ", " ")]:
        s = s.replace(a, b)
    s = s.replace("_", "").replace("^", "")
    return re.sub(r"\s+", " ", s)

def pdf(p):
    return norm(subprocess.run(["pdftotext", "-layout", p, "-"],
                               capture_output=True, text=True).stdout)

CASOS = {
 "Lista 1": dict(
   pdf="RESOLUCOES/lista-01-resolucao.pdf",
   md=["lista01/q1ef-limpo.md"],
   # 13/09/2026: o professor retirou o Q1(f). "3n + 3", "4n + 3" e "a + b < 100" eram do bloco
   # do (f) e saíram do PDF; o (e) guarda uma nota curta sobre o (f) ("k < 100", "ha obrigatoriamente").
   decisivas=["20 100 = 100·201", "40 000 = 100·400", "79 800",
              "k < 100", "(l2) implica (l1)", "ha obrigatoriamente"],
   # "3n + 2" sozinho casaria a contagem LEGITIMA do codigo 1 da Q2 ("2n + 2 + n = 3n + 2");
   # o residuo refutado e a cota da busca linear.
   # a ultima e texto ANTIGO (de agosto), falso: (a) e (b) sao ambos V. Achado pelo
   # conferente de diagramacao em 14/09/2026.
   residuos=["com no maximo 3n + 2 operacoes", "97n > 2", "o piso ultrapassa 100n a partir de n > 100/c",
             "e por isso que (a) e (b) diferem",
             # 13/09/2026: resíduos do Q1(f) retirado (o bloco inteiro e as frases que o citavam)
             "logo, nao ha obrigatoriamente.", "os seis itens giram", "e em (f) se refuta (l1)",
             "levar para o (f) o v do (e) antigo"],
   unicos=["Sobre a versão original do item (e)"]),
 "Lista 3": dict(
   pdf="RESOLUCOES/lista-03-resolucao.pdf",
   md=["lista03/q3-moedas-limpo.md", "lista03/q5-passo-sem-base-limpo.md"],
   decisivas=["p - q > 0", "1 + n = n + 1", "(n - 3) + 2 = n - 1",
              "para todo conjunto m", "¬p(n) → ¬p(n+1)", "(n+1)(n+2)/2 + 1",
              "a falha da base, sozinha, nao basta"],
   residuos=["exige a formula exata do lema", "as duas partes da inducao, base e passo, sao indispensaveis"],
   unicos=["O que falta é um ponto de partida", "Nos dois caminhos há base"]),
 "Lista 4": dict(
   pdf="RESOLUCOES/lista-04-resolucao.pdf",
   md=["lista04/questao4-soma-dos-quadrados-limpo.md", "lista04/questao5-arvores-limpo.md"],
   decisivas=["(n+1)(2n² + 7n + 6)/6", "(n+2)(2n+3) = 2n² + 3n + 4n + 6",
              "duas arestas disjuntas", "construir nao e, por si so, invalido",
              "o caminho natural e reduzi-la", "a menos do nome dos vertices",
              "um fato que a prova do estudante nao estabelece"],
   # o rodape CITA a frase removida entre aspas; o residuo e a frase em uso, seguida de ":"
   residuos=["o passo vai na direcao errada: comeca", "e uma coincidencia que a prova"],
   unicos=["Construir não é, por si só, inválido"]),
}

falhas = 0
def linha(ok, txt):
    global falhas
    print(("  OK    " if ok else "  FALHA ") + txt)
    falhas += 0 if ok else 1

for nome, c in CASOS.items():
    print("=" * 78); print(nome); print("=" * 78)
    P = pdf(c["pdf"])
    M = " || ".join(norm(open(D + f, encoding="utf-8").read()) for f in c["md"])
    for frase in c["decisivas"]:
        f = norm(frase)
        linha(f in P and f in M, f"decisiva  pdf={f in P!s:5s} md={f in M!s:5s}  \"{frase}\"")
    for frase in c["residuos"]:
        f = norm(frase)
        linha(f not in P and f not in M, f"residuo   pdf={f in P!s:5s} md={f in M!s:5s}  \"{frase}\"")
    for frase in c["unicos"]:
        f = norm(frase)
        n_md, n_pdf = M.count(f), P.count(f)
        linha(n_md == 1 and n_pdf <= 1, f"unico     md={n_md} pdf={n_pdf}  \"{frase}\"")

print("=" * 78); print("Renumeracao da Lista 3 (a antiga Q3 e a Q4)"); print("=" * 78)
P3 = pdf("RESOLUCOES/lista-03-resolucao.pdf")
for q in ["questao 3", "questao 4", "questao 5"]:
    linha(P3.count(q) >= 1, f"cabecalho \"{q}\" presente")
linha("questao 4(a)" in P3 and "questao 4(c)" in P3, "as remissoes internas apontam para 4(a) e 4(c)")
PROVA = pdf("RESOLUCOES/prova-01-resolucao.pdf")
linha("lista 3, q4(d) e (e)" in PROVA and "lista 3, q3(d)" not in PROVA,
      "mapa da prova de 2025 aponta para Lista 3, Q4(d)(e), nao mais Q3")

print()
print("PDFs e .md verificados dizem a mesma coisa." if not falhas else f"{falhas} FALHAS.")
sys.exit(1 if falhas else 0)
