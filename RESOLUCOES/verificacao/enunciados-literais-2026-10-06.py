# -*- coding: utf-8 -*-
"""Confere que TODO o texto de cada lista do professor (listas 1–5) aparece no PDF da resolução.
Compara linha a linha do pdftotext da lista, depois de normalizar: sem espaços, ∗→*, Θ→θ
(a fonte do professor alterna os dois) e sem as caixas '( )' do V/F. Linhas de fórmula 2D
(Σ, chaves de casos, frações empilhadas) quebram no pdftotext e são listadas à parte para
conferência visual; não contam como falha."""
import subprocess, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = os.path.join(os.path.dirname(R), "listas-de-exercicios")
def txt(p): return subprocess.run(["pdftotext", p, "-"], capture_output=True, text=True).stdout
import re
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹ⁿᵏ₀₁₂₃", "0123456789nk0123")
def norm(s):
    # U+2126 (ohm, no PDF do professor) e U+03A9 são o mesmo Ω
    s = s.translate(SUP).replace("\u2126", "\u03a9").replace("…", "...").replace("··· ", "···").replace("ℕ", "N")
    s = s.replace("∗", "*").replace("Θ", "θ").replace("( )", "").replace("‐", "-").replace("−", "-")
    s = re.sub(r"^\s*Questão \d+\.\s*", "", s)            # o rótulo vira título da seção
    s = re.sub(r"^\s*(\([a-z]+\)|[a-z]\)|\d\.|•)\s*", "", s)  # (a), a), 1., • viram lista HTML
    return "".join(s.split())
FORMULA = set("ΣPn√≺{}")
tot_falha = 0
ALVOS = [(i, f"{L}/lista-0{i}-2026-2.pdf", f"{R}/lista-0{i}-resolucao.pdf", f"Lista {i}") for i in range(1, 6)]
ALVOS.append(("P", os.path.join(os.path.dirname(R), "provas", "prova-01-2025-exemplo.pdf"),
              f"{R}/prova-01-resolucao.pdf", "Prova 2025"))
for i, p_orig, p_res, nome in ALVOS:
    orig = txt(p_orig)
    # Chrome hifeniza com U+2010 no fim da linha ("algorit‐\nmo"): junta antes de normalizar.
    # "[sic]" é marca editorial da resolução dentro da citação literal; sai da comparação.
    res = txt(p_res).replace("‐\n", "").replace("[sic]", "")
    res = norm(res.replace("\n", " "))
    falhas, visuais, expo, n = [], [], [], 0
    res_sem_exp = re.sub(r"[0-9nk]", "", res)
    for ln in orig.split("\n"):
        s = ln.strip()
        if not s or s.isdigit(): continue
        n += 1
        if norm(s) in res: continue
        # 2º nível: o <sup> do HTML sai fora da linha no pdftotext (2ⁿ → "2"). Tira de AMBOS os
        # lados os caracteres que podem ser expoente e compara de novo; conta à parte.
        # Conferidas na imagem renderizada em 06/10/2026: fórmulas 2D que o pdftotext embaralha na
        # lista do professor (frações empilhadas da L5 Q4; quadro de casos do Teorema Mestre).
        # Σ aⁱ = a(aⁿ − 1)/(a − 1) do anexo: o pdftotext come os DOIS expoentes ("a(a − 1)/(a − 1)");
        # conferida na imagem da p. 4 da Lista 1 em 06/10/2026 — vale para todas as listas e a prova.
        if s.startswith("i=1 (a ) = a(a − 1)/(a − 1)") or \
           (i == 5 and (s.startswith("a) 12 + 14 + 81") or s.startswith("assintoticamente por T (n) = θ(nk"))) or \
           (i == "P" and ("BRATLEY, 1996] indicam" in s
                          or s.startswith("que a solução dessa recorrência é limitada assintoticamente por T (n) = θ(nk"))):
            visuais.append(s); continue
        if len(norm(s)) > 12 and re.sub(r"[0-9nk]", "", norm(s)) in res_sem_exp:
            expo.append(s); continue
        (visuais if (len(norm(s)) <= 12 or any(ch in s for ch in "Σ√≺") or s.startswith(("(", "Pn", "•"))) else falhas).append(s)
    tot_falha += len(falhas)
    print(f"{nome}: {n} linhas; {n-len(falhas)-len(visuais)-len(expo)} casam; {len(expo)} casam com expoente deslocado; {len(visuais)} p/ conferência visual; {len(falhas)} FALHAS")
    for e in expo: print("   expoente:", e)
    for f in falhas: print("   FALHA:", f)
    for v in visuais: print("   visual:", v)
print("\nRESULTADO:", "OK" if tot_falha == 0 else f"{tot_falha} linha(s) sem correspondência")
sys.exit(1 if tot_falha else 0)
