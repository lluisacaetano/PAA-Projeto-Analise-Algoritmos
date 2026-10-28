# -*- coding: utf-8 -*-
"""Lote 7 (onda C): rezende-p10 — com d < 0, T fica negativo para n pequeno e n0 = 1 não satisfaz 0 ≤ T(n)."""
exec(open(__file__.replace("patch7.py","patch1.py")).read().split("# uber-p8")[0])
A = "rezende-unicamp-p-10"
troca(A, "T(0) = d, com d uma constante real qualquer (no caso usual, d = 0, que dá T(1) = 1, T(2) = 2).",
         "T(0) = d, com d ≥ 0 uma constante real (custo de tempo não é negativo; no caso usual, d = 0, que dá T(1) = 1, T(2) = 2).")
troca(A, "com T(0) = d (constante, não depende de n) e T(n)", "com T(0) = d (constante d ≥ 0, não depende de n) e T(n)")
troca(A, "Isso é exatamente a definição de T(n) ∈ O(n). Com d = 0: c = 3, n0 = 1.",
         "Junto com 0 ≤ T(n), que vale para todo n porque d ≥ 0 (indução: T(n) = 2T(⌊n/3⌋) + n com T(⌊n/3⌋) ≥ 0), isso é exatamente a definição de T(n) ∈ O(n). Com d = 0: c = 3, n0 = 1.")
troca(A, "Precisamos 2d + 2 ≤ 2c. Se d ≥ 0: 2d + 2 ≤ 4d + 2 ≤ 2c. Se d < 0: 2d + 2 < 2 ≤ 6 ≤ 2c, pois c ≥ 3. Vale nos dois casos.",
         "Precisamos 2d + 2 ≤ 2c. Como d ≥ 0: 2d + 2 ≤ 4d + 2 ≤ 2c. Vale.")
troca(A, "com T(0) = d0 e T(1) = d1 dados, o mesmo argumento", "com T(0) = d0 ≥ 0 e T(1) = d1 ≥ 0 dados, o mesmo argumento")
troca(A, "Em qualquer escolha de constantes iniciais, a conclusão O(n) não muda; muda só o número c.",
         "Em qualquer escolha de constantes iniciais não negativas, a conclusão O(n) não muda; muda só o número c. (Com d < 0 a cota T(n) ≤ c·n ainda sai da mesma conta, mas T fica negativo para n pequeno — com d = −10, em 118 valores de n, o último n = 129 — e então n0 = 1 não satisfaz o 0 ≤ T(n) da definição; custo negativo não modela tempo, por isso o excluímos.)")
troca(A, "OBSERVAÇÃO (NÃO PEDIDA).\nSe d ≥ 0, então T(n) ≥ 0 para todo n (indução", "OBSERVAÇÃO (NÃO PEDIDA).\nComo d ≥ 0, T(n) ≥ 0 para todo n (indução")
print("fim")
