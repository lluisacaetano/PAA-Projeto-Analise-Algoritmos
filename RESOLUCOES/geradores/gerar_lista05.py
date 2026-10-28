# -*- coding: utf-8 -*-
"""
Gera fontes-html/lista-05-resolucao.html a partir dos .md que passaram pelos verificadores
(dados/lista05/q{1..5}-limpo.md).

Diferença deliberada em relação às listas 1-4, cujo HTML é editado à mão: aqui o HTML é
DERIVADO do texto verificado, sem redigitação. É o remédio para os problemas das seções 7.3
(extração corrompendo texto) e 7.13 (texto fora de <div class="item">) do CLAUDE.md: não há
segunda cópia para divergir. Mesmo assim, três invariantes são checadas no fim:
  1. toda linha de texto de cada .md aparece no HTML (nada caiu na montagem);
  2. nenhuma linha longa aparece mais vezes no HTML do que no .md (nada duplicou — 7.10);
  3. as <div> estão balanceadas e todo texto de solução está dentro de <div class="item">.

Rodar de qualquer lugar:  python3 RESOLUCOES/geradores/gerar_lista05.py
"""
import html
import os
import re
import sys

BASE = os.path.expanduser("~/DEV/PAA-Projeto-Analise-Algoritmos")
DADOS = BASE + "/RESOLUCOES/geradores/dados/lista05"
OUT = BASE + "/RESOLUCOES/fontes-html/lista-05-resolucao.html"

TITULOS = {
    1: "Questão 1 — máximo por divisão e conquista",
    2: "Questão 2 — busca num vetor sem fim",
    3: "Questão 3 — qual dos algoritmos A, B, C",
    4: "Questão 4 — prova por indução",
    5: "Questão 5 — Teorema Mestre em dez recorrências",
}

# Preenchido ao fim do fluxo (seção 5 do CLAUDE.md). Texto do rodapé, fora dos blocos .item.
RODAPE = """<strong>Sobre esta resolução.</strong> Fluxo da seção 5 do <code>CLAUDE.md</code>: chão
determinístico em Python puro antes de qualquer redação (<code>verificacao/lista05-chao-deterministico.py</code>);
redação; verificadores adversariais em contexto limpo, quatro por questão e por rodada, cegos ao
raciocínio e uns aos outros, com Bash para conferir as contas; voto assimétrico (4 HOLDS confirma,
2 HOLE refuta); correções; e reverificação da versão corrigida, até a confirmação.
{rodadas}<br>
<strong>Texto-fonte.</strong> Este HTML é gerado por <code>geradores/gerar_lista05.py</code> a partir
dos arquivos <code>geradores/dados/lista05/q*-limpo.md</code> — os mesmos que os verificadores leram —,
e o gerador confere que nenhuma linha deles caiu ou duplicou. Registro das correções, com o motivo
e quem achou: <code>geradores/dados/lista05/correcoes-lista05.md</code>.<br>
<strong>Enunciados.</strong> Transcritos literalmente do PDF do professor, com os erros de
digitação marcados com <em>[sic]</em> e nunca corrigidos.<br>
Lista avaliada — IFMG Campus Formiga, 2026/2."""

RODADAS = ""   # preenchido por estado_verificacao() abaixo


def estado_verificacao():
    arq = DADOS + "/estado-verificacao.txt"
    if os.path.exists(arq):
        return open(arq, encoding="utf-8").read().strip()
    return "<strong>Estado da verificação.</strong> (ver correcoes-lista05.md)"


CSS = open(BASE + "/RESOLUCOES/fontes-html/lista-04-resolucao.html", encoding="utf-8").read()
CSS = CSS[CSS.index("<style>") + len("<style>"): CSS.index("</style>")]
CSS += """
  pre.cod { font-family: "SF Mono", "Menlo", "Consolas", monospace; font-size: 7.5pt;
            line-height: 1.3; background: var(--caixa); border: 0.4pt solid var(--linha);
            padding: 1.2mm 2mm; margin: 1.2mm 0; white-space: pre-wrap; break-inside: avoid; }
  .recuo { display: inline-block; padding-left: 4mm; }
  .recuo2 { display: inline-block; padding-left: 8mm; }
  .caixa-resposta { border: 0.8pt solid var(--realce); padding: 1.6mm 2.4mm; background: #f6f8fb; }
  .caixa-resposta h3 { margin-top: 0.5mm; }
"""


# ─────────────────────────── conversão de texto ───────────────────────────
def sup(s):
    """^(...) -> <sup>...</sup> (parênteses balanceados) e ^token -> <sup>token</sup>."""
    out, i = [], 0
    while i < len(s):
        if s[i] == "^" and i + 1 < len(s):
            if s[i + 1] == "{":
                j = s.index("}", i)
                out.append("<sup>" + s[i + 2: j] + "</sup>")
                i = j + 1
                continue
            if s[i + 1] == "(":
                d, j = 0, i + 1
                while j < len(s):
                    if s[j] == "(":
                        d += 1
                    elif s[j] == ")":
                        d -= 1
                        if d == 0:
                            break
                    j += 1
                if j >= len(s):
                    raise SystemExit("parêntese sem par em: " + s)
                out.append("<sup>" + sup(s[i + 2: j]) + "</sup>")
                i = j + 1
                continue
            m = re.match(r"[\w₀-₉′″]+(?:,\d+)?", s[i + 1:])
            if m:
                out.append("<sup>" + m.group() + "</sup>")
                i += 1 + len(m.group())
                continue
        out.append(s[i])
        i += 1
    return "".join(out)


def sub_(s):
    """_{...} e x_token -> <sub>: d_a, c″_b, T_a, log_b, C_b."""
    s = re.sub(r"_\{([^}]*)\}", r"<sub>\1</sub>", s)
    return re.sub(r"(?<=[\w′″)])_([A-Za-z0-9]+)", r"<sub>\1</sub>", s)


def negrito(h):
    """**…** -> <strong>, também quando atravessa quebra de linha; aborta se cruzar um <span>."""
    h = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", h, flags=re.S)
    for m in re.finditer(r"<strong>(.*?)</strong>", h, flags=re.S):
        if "<span" in m.group(1) or "</span>" in m.group(1):
            raise SystemExit("negrito atravessa uma linha recuada: " + m.group(1)[:60])
    if "**" in h:
        raise SystemExit("** sem par: " + h[h.index("**") - 40: h.index("**") + 40])
    return h


def inline(s, com_negrito=True):
    s = sup(sub_(html.escape(s, quote=False)))
    return negrito(s) if com_negrito else s


INICIA_LINHA = re.compile(r"^(\([a-j]\) |[A-C]: |\|)")


def paragrafo(linhas):
    """Junta as linhas de um bloco: quebra de linha é mantida quando a linha é recuada,
    começa um item (a)…(j) / A: B: C:, ou quando a anterior era curta (fim de frase)."""
    partes = []
    for k, ln in enumerate(linhas):
        recuo = len(ln) - len(ln.lstrip(" "))
        txt = inline(ln.strip(), com_negrito=False)
        if recuo >= 4:
            txt = f'<span class="recuo2">{txt}</span>'
        elif recuo >= 2:
            txt = f'<span class="recuo">{txt}</span>'
        if k == 0:
            partes.append(txt)
            continue
        anterior = linhas[k - 1]
        junta = recuo == 0 and not INICIA_LINHA.match(ln) and len(anterior.rstrip()) >= 78
        partes.append((" " if junta else "<br>\n") + txt)
    return negrito("<p>" + "".join(partes) + "</p>")


def tabela(linhas):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in linhas]
    h = ["<table>"]
    for r, cols in enumerate(rows):
        tag = "th" if r == 0 else "td"
        h.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cols) + "</tr>")
    h.append("</table>")
    return "\n".join(h)


def blocos(texto):
    """Divide um trecho em blocos: parágrafos, código (```) e tabelas (|)."""
    out, buf, cod, em_cod = [], [], [], False
    for ln in texto.split("\n"):
        if ln.strip().startswith("```"):
            if em_cod:
                out.append(("cod", cod))
                cod, em_cod = [], False
            else:
                if buf:
                    out.append(("par", buf))
                    buf = []
                em_cod = True
            continue
        if em_cod:
            cod.append(ln)
            continue
        if not ln.strip():
            if buf:
                out.append(("par", buf))
                buf = []
            continue
        buf.append(ln)
    if em_cod:
        raise SystemExit("bloco de código sem fechamento")
    if buf:
        out.append(("par", buf))
    html_out = []
    for tipo, ls in out:
        if tipo == "cod":
            html_out.append('<pre class="cod">' + html.escape("\n".join(ls), quote=False) + "</pre>")
        elif all(x.strip().startswith("|") for x in ls):
            html_out.append(tabela(ls))
        else:
            html_out.append(paragrafo(ls))
    return "\n".join(html_out)


# ─────────────────────────── montagem ───────────────────────────
def questao(n):
    md = open(f"{DADOS}/q{n}-limpo.md", encoding="utf-8").read()
    corpo = md.split("\n", 1)[1]                       # descarta o título "# Lista 5 — Questão n (...)"
    m = re.search(r"## ENUNCIADO \(literal\)\n(.*?)\n## SOLUÇÃO FINAL\n(.*?)\n## RESPOSTA\n(.*)$", corpo, re.S)
    if not m:
        raise SystemExit(f"q{n}: seções ENUNCIADO / SOLUÇÃO FINAL / RESPOSTA não encontradas")
    enun, sol, resp = m.groups()
    H = [f"<!-- ══════════════════════ QUESTÃO {n} ══════════════════════ -->",
         f"<h2>{TITULOS[n]}</h2>",
         '<div class="enunciado">\n  <span class="rot">Enunciado</span>\n' + blocos(enun) + "\n</div>"]
    secoes = re.split(r"^### (.+)$", sol, flags=re.M)
    if secoes[0].strip():
        raise SystemExit(f"q{n}: texto solto antes da primeira seção ### (ficaria fora de .item)")
    for tit, txt in zip(secoes[1::2], secoes[2::2]):
        H.append('<div class="item">\n<h3>' + inline(tit.strip()) + "</h3>\n" + blocos(txt) + "\n</div>")
    # A caixa da resposta é uma <div> INTERNA: o extrator do banco (gerar_banco.py) só reconhece
    # '<div class="item">' literal — com class="item resposta" o bloco sumiria do banco sem erro.
    H.append('<div class="item">\n<div class="caixa-resposta">\n<h3>Resposta</h3>\n' + blocos(resp)
             + "\n</div>\n</div>")
    return "\n".join(H), md



# 06/10/2026 — anexo "Informações que podem ser úteis" da lista, transcrito literalmente,
# para o documento trazer o enunciado completo (o formulário também aparece nas Q1, Q3 e Q5).
ANEXO_LISTA = """<h2>Informações que podem ser úteis</h2>
<div class="enunciado" id="informacoes-lista">
  <span class="rot">Anexo da lista (transcrição literal)</span>
  <p><strong>Somatórios e Logaritmos:</strong></p>
  <ul>
    <li>Σ<sub>i=1</sub><sup>n</sup> (i) = n(n + 1)/2</li>
    <li>Σ<sub>i=1</sub><sup>n</sup> (a<sup>i</sup>) = a(a<sup>n</sup> − 1)/(a − 1)</li>
    <li>log (a ∗ b) = log a + log b</li>
    <li>log (a/b) = log a − log b</li>
    <li>log<sub>b</sub> a = log<sub>c</sub> a/ log<sub>c</sub> b</li>
    <li>log<sub>b</sub> a<sup>c</sup> = c ∗ log<sub>b</sub> a</li>
    <li>lg a = log<sub>2</sub> a</li>
  </ul>
  <p><strong>Hierarquia de funções:</strong></p>
  <p>A seguinte hierarquia de funções pode ser definida do ponto de vista assintótico:</p>
  <p class="centro">1 ≺ log(n) ≺ √n ≺ n ≺ n ∗ log(n) ≺ n<sup>c</sup> ≺ c<sup>n</sup> ≺ n! ≺ n<sup>n</sup></p>
  <p>onde c é uma constante arbitrária inteira ≥ 2.</p>
  <p><strong>Teorema mestre:</strong></p>
  <p>Sejam as constantes naturais a ≥ 1, b ≥ 2 e k ≥ 0. Considere a função f(n) da forma c ∗ n<sup>k</sup>,
  na qual c &gt; 0 e ∈ R, seja a equação de recorrência dada por T(n) = aT(n/b) + f(n) e suponha n uma
  potência exata de b. Considere ainda que T é uma função que leva números naturais em números reais
  positivos e que T é assintoticamente não decrescente, Nessas condições, [BRASSARD and BRATLEY, 1996]
  indicam que a solução dessa recorrência é limitada assintoticamente por</p>
  <p class="centro">T(n) = θ(n<sup>k</sup>) se a &lt; b<sup>k</sup>; &nbsp; θ(n<sup>k</sup> ∗ lg n) se a = b<sup>k</sup>;
  &nbsp; θ(n<sup>log<sub>b</sub> a</sup>) se a &gt; b<sup>k</sup></p>
  <p><strong>Referências</strong></p>
  <ul><li>[BRASSARD and BRATLEY, 1996] BRASSARD, G. and BRATLEY, P. (1996). Fundamentals of Algorithms.
  Prentice-Hall.</li></ul>
  <p style="font-size:7.6pt;color:#5b6068;">O PDF da lista não tem folha de rosto nem bloco de instruções:
  começa na Questão 1, com numeração de página a partir de 2.</p>
</div>"""

def monta():
    partes, mds = [], {}
    for n in range(1, 6):
        h, md = questao(n)
        partes.append(h)
        mds[n] = md
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>PAA — Lista de Exercícios V — Resolução</title>
<style>{CSS}</style>
</head>
<body>

<div class="cabecalho">
  <h1>Projeto e Análise de Algoritmos — Lista de Exercícios V</h1>
  <div class="meta">
    Instituto Federal de Minas Gerais, Campus Formiga · Bacharelado em Ciência da Computação · 2026/2 · Lista avaliada (5 pontos), entrega em 24/09/2026<br>
    Professor: Mário Luiz Rodrigues Oliveira · Aluna: Luisa Caetano
  </div>
</div>

<div class="nota">
<strong>Como ler esta resolução.</strong> Cada questão traz o enunciado literal, a solução em seções
e, no fim, um quadro <em>Resposta</em>. Toda afirmação de Θ vem com <span class="mat">c<sub>1</sub>,
c<sub>2</sub>, n<sub>0</sub></span> numéricos, conferidos em <span class="mat">n = n<sub>0</sub></span>
exatamente. Ao citar o Teorema Mestre, “primeira/segunda/terceira linha” segue a ordem impressa no
formulário da lista: <span class="mat">a &lt; b<sup>k</sup></span>, <span class="mat">a = b<sup>k</sup></span>,
<span class="mat">a &gt; b<sup>k</sup></span>.
</div>

{chr(10).join(partes)}

{ANEXO_LISTA}

<div class="rodape">
{RODAPE.format(rodadas=estado_verificacao())}
</div>

</body>
</html>
"""
    return doc, mds


# ─────────────────────────── invariantes ───────────────────────────
def texto_de(h):
    h = re.sub(r"<style>.*?</style>", " ", h, flags=re.S)
    h = re.sub(r"</?(?:strong|sub|sup|span|b|i|em|code)\b[^>]*>", "", h)   # inline: sem espaço
    h = re.sub(r"<[^>]+>", " ", h)                                          # bloco: vira espaço
    h = html.unescape(h)
    return re.sub(r"\s+", " ", h)


def norm_md_linha(ln):
    t = ln.strip().replace("**", "")               # negrito pode atravessar a quebra de linha
    t = texto_de(inline(t))                             # mesma conversão que o HTML sofreu
    return re.sub(r"\s+", " ", t).strip()


def confere(doc, mds):
    falhas = []
    if doc.count("<div") != doc.count("</div>"):
        falhas.append(f"<div> desbalanceado: {doc.count('<div')} abre, {doc.count('</div>')} fecha")
    corpo_html = texto_de(doc)
    # O anexo literal da lista (06/10/2026) repete o Teorema Mestre de propósito: a contagem de
    # duplicação ignora o anexo — removido por id, e a remoção tem de ter achado o bloco.
    sem_anexo = re.sub(r'<h2>Informações que podem ser úteis</h2>\s*<div class="enunciado" id="informacoes-lista">.*?</div>', '', doc, flags=re.S)
    if sem_anexo == doc:
        falhas.append("anexo 'Informações que podem ser úteis' não encontrado")
    corpo_dup = texto_de(sem_anexo)
    total = 0
    # A contagem de referência é sobre TODOS os .md: o formulário do Teorema Mestre aparece, de
    # propósito, nos enunciados da Q1 e da Q3 — no HTML ele sai duas vezes, e isso é correto.
    todas = [norm_md_linha(x) for md in mds.values() for x in md.split("\n")[1:] if x.strip()]
    for n, md in mds.items():
        linhas = [l for l in md.split("\n")[1:]
                  if l.strip() and not l.startswith("#") and not l.strip().startswith("```")]
        for ln in linhas:
            if ln.strip().startswith("|"):
                cels = [c for c in ln.strip().strip("|").split("|")]
                alvos = [norm_md_linha(c) for c in cels if c.strip()]
            else:
                alvos = [norm_md_linha(ln)]
            for a in alvos:
                total += 1
                if a not in corpo_html:
                    falhas.append(f"q{n}: linha ausente do HTML: {a[:90]}")
                elif len(a) >= 40:
                    na = corpo_dup.count(a)
                    nm = sum(x.count(a) for x in todas)
                    if na > max(nm, 1):
                        falhas.append(f"q{n}: linha duplicada no HTML ({na}×, md {nm}×): {a[:70]}")
    # todo texto de solução dentro de .item: entre </div> de um item e o <h2>/<div> seguinte não pode
    # haver <p> solto
    soltos = re.findall(r'</div>\s*<p>', doc)
    if soltos:
        falhas.append(f"{len(soltos)} parágrafo(s) fora de <div class=\"item\">")
    return falhas, total


if __name__ == "__main__":
    doc, mds = monta()
    falhas, total = confere(doc, mds)
    itens = re.findall(r'<div class="item">\s*(?:<div class="caixa-resposta">\s*)?<h3>(.*?)</h3>', doc)
    if len(itens) != doc.count('<div class="item">'):
        raise SystemExit("há <div class=\"item\"> sem <h3> logo em seguida")
    print(f"{len(itens)} blocos .item:")
    q, k = 0, 0
    for i, t in enumerate(itens):
        print(f"  [{i:2d}] {re.sub('<[^>]+>', '', t)}")
    if falhas:
        print(f"\n{len(falhas)} FALHA(S) nas invariantes:")
        for f in falhas:
            print("  -", f)
        sys.exit(1)
    open(OUT, "w", encoding="utf-8").write(doc)
    print(f"\nOK: {total} linhas/células do texto verificado conferidas no HTML; nada caiu, nada duplicou.")
    print(f"HTML gerado: {OUT} ({len(doc) // 1024} KB)")
