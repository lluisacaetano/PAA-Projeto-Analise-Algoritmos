# -*- coding: utf-8 -*-
"""
O PDF e montado a partir de HTML escrito a mao; os textos que passaram pelos
verificadores adversariais sao os .md em geradores/dados/lista04/.
Este script confere que o PDF diz a MESMA COISA que os .md verificados:
toda afirmacao decisiva tem de aparecer nos dois, e nenhum residuo das versoes
refutadas pode ter sobrevivido em nenhum dos dois.

Rodar da raiz do projeto:  python3 RESOLUCOES/verificacao/lista04-html-bate-com-verificado.py
"""
import subprocess, unicodedata, re, sys, os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(RAIZ)
MD = "RESOLUCOES/geradores/dados/lista04/"
PDF = "RESOLUCOES/lista-04-resolucao.pdf"

def norm(s):
    # Hifenizacao de fim de linha, com DOIS detalhes que custaram tempo:
    #  (1) o pdftotext -layout preenche a linha com espacos ANTES da quebra;
    #  (2) quando a palavra quebra numa mudanca de PAGINA, entre a quebra e o
    #      resto da palavra vem um form feed (\x0c).
    # O caso real que expos os dois: "concluir o conse\u2010\n\x0cquente".
    s = re.sub(r"[\u2010-][ \t]*\n[ \t\f]*", "", s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    for a, b in [("−","-"), ("–","-"), ("—","-"), ("∗","*")]:
        s = s.replace(a, b)
    s = s.replace("_", "")          # log_3 (markdown) == log3 (subscrito no HTML)
    s = s.replace("^", "")          # 2^n (markdown) == 2n com sobrescrito no HTML
    return re.sub(r"\s+", " ", s)

pdf = norm(subprocess.run(["pdftotext","-layout",PDF,"-"],capture_output=True,text=True).stdout)
mds = {f: norm(open(MD+f, encoding="utf-8").read())
       for f in ["q1-limpo.md","q2-limpo.md","q3-limpo.md","q4-slide-limpo.md"]}
md_todo = " || ".join(mds.values())

# --- afirmacoes decisivas: tem de estar no PDF E no .md verificado ----------
DECISIVAS = [
 # Questao 1
 ("Q1(a) base",        "1 + 3 + 5"),
 ("Q1(b) resposta",    "t(n) = 2^n"),
 ("Q1(d) resposta",    "3n - 2"),
 ("Q1(e) forma",       "2n - 1"),
 ("Q1(e) testemunhas", "c1 = 1, c2 = 2, n0 = 1"),
 ("Q1(e) desenrolar",  "t(1) + 2(n-1)"),
 # Questao 2 - as cinco respostas e as testemunhas
 ("Q2(a)", "log3 2"),
 ("Q2(b)", "log4 5"),
 ("Q2(c)", "n(log7 n + 1)"),
 ("Q2(d)", "n2(log3 n + 1)"),
 ("Q2(e)", "n3(lg n + 1)"),
 ("Q2 n0=7", "n0 = 7"),
 ("Q2 n0=3", "n0 = 3"),
 ("Q2 n0=2", "n0 = 2"),
 ("Q2 fencepost", "lg 1 = 0"),
 ("Q2 testemunha c",  "c1 = c/lg b"),
 # Questao 3
 ("Q3 criterio",   "a ∩ b ≠ ∅"),
 ("Q3 cardinalid", "|a ∩ b| = k - 1"),
 ("Q3 elo",        "p(1) → p(2)"),
 ("Q3 termo",      "concluir o consequente"),
 ("Q3 cohen",      "joel e. cohen"),
 ("Q3 polya 1954", "1954"),
 # Apendice
 ("Ap. 2n+1",      "2n + 1"),
 ("Ap. alfa/beta", "α"),
 ("Ap. pilha",     "21 quadros"),
 ("Ap. split",     "split perfeito"),
 ("Q2 ordem",      "mesma ordem em que"),   # a tabela segue a ordem do formulário
 ("Q2 hipotese",   "assintoticamente não decrescente"),
 ("Q2 caso (a)",   "terceiro caso"),
 ("Ap. slide",     "abreviado, não errado"),
 # 14/09/2026: o HTML tinha "com uma pessoa chinesa e não-chinesas em pelo menos uma
 # não-chinesa" — um patch de 31/08 casado pela metade. Achado pelo conferente do banco.
 ("Q3 contramodelo", "pelo menos uma pessoa chinesa e pelo menos uma não-chinesa"),
]

# --- residuos das versoes REFUTADAS: nao podem estar em lugar nenhum -------
RESIDUOS = [
 "afirmar o consequente sem",
 "descarregar o consequente",
 "asseverar o consequente",
 "primeiro caso",
 "o passo do meio é que não os liga",
 "nenhuma das duas se aplica",
 "isso equivale a exigir",
 "apenas se reescalam por c",
 "so reescala c1 e c2",
 "~22 quadros",
 "tem pelo menos dois termos",
 "\"todos os cavalos tem a mesma cor\", de polya",
 "nao-chinesas em pelo menos uma",
]

# Estes residuos so fazem sentido no arquivo do apendice: la houve colisao entre
# as constantes de custo (a, b) e os parametros do teorema. Na Q2 nao ha colisao,
# e "T(n) = a*T(n/b) + c*n^k" e o enunciado legitimo do teorema.
RESIDUOS_APENDICE = [
 "t(n) = a·t(n/b) + c·n^k",
 "potencia exata de b e estendido",
 "parametros: a = 2",
]

falhas = 0
print("=" * 78)
print("O PDF diz o mesmo que os .md que passaram pelos verificadores?")
print("=" * 78)
for rot, frase in DECISIVAS:
    f = norm(frase)
    no_pdf, no_md = f in pdf, f in md_todo
    ok = no_pdf and no_md
    print(("  OK   " if ok else "  FALHA") + f"  {rot:16s} pdf={no_pdf!s:5s} md={no_md!s:5s}  \"{frase}\"")
    falhas += 0 if ok else 1

print()
print("Residuos das versoes refutadas (nao podem estar nem no PDF nem nos .md):")
for frase in RESIDUOS:
    f = norm(frase)
    no_pdf, no_md = f in pdf, f in md_todo
    ok = not no_pdf and not no_md
    print(("  OK   " if ok else "  FALHA") + f"  pdf={no_pdf!s:5s} md={no_md!s:5s}  \"{frase[:52]}\"")
    falhas += 0 if ok else 1

# ---------------------------------------------------------------------------
# Trechos que tem de aparecer EXATAMENTE UMA VEZ. A conferencia original so
# testava presenca, e por isso um patch que duplicou um paragrafo OITO vezes
# passou despercebido (ver CLAUDE.md 7.10).
# ---------------------------------------------------------------------------
UNICOS = [
 "Soma-se a isso um defeito",              # RESPOSTA da Q3 - o que duplicou
 "A prova está errada.",                   # abertura da RESPOSTA da Q3
 "Não há ganho algum de complexidade",     # abertura da RESPOSTA do apendice
 "toda árvore binária A com n ≥ 0 nós",    # enunciado do teorema do apendice
]
print()
print("Trechos que tem de aparecer exatamente uma vez (teste de duplicacao):")
for frase in UNICOS:
    f = norm(frase)
    n_md, n_pdf = md_todo.count(f), pdf.count(f)
    ok = n_md == 1 and n_pdf <= 1     # no pdf pode nao aparecer por quebra de linha
    print(("  OK   " if ok else "  FALHA") + f"  md={n_md} pdf={n_pdf}  \"{frase[:44]}\"")
    falhas += 0 if ok else 1

print()
print("Residuos especificos do apendice (colisao de simbolos a/b vs alfa/beta):")
ap = mds["q4-slide-limpo.md"]
for frase in RESIDUOS_APENDICE:
    f = norm(frase)
    ok = f not in ap
    print(("  OK   " if ok else "  FALHA") + f"  q4-slide-limpo.md  \"{frase[:52]}\"")
    falhas += 0 if ok else 1

print()
print("=" * 78)
print("PDF e .md verificados dizem a mesma coisa." if not falhas
      else f"{falhas} FALHAS - o PDF divergiu do texto verificado.")
print("=" * 78)
sys.exit(1 if falhas else 0)
