# -*- coding: utf-8 -*-
"""Lote 8 (onda C): p21 — resumo usava lg n onde a prova usa lg n − 8 (com lg n, 2^19 é falso); p17 — c₀ ≥ 0 não declarado."""
exec(open(__file__.replace("patch8.py","patch1.py")).read().split("# uber-p8")[0])
troca("rezende-unicamp-p-21-exerc-cios-suplementares-item-1",
 "O preço do deslocamento é a parcela c·127008·lg m ≤ c·127008·lg n, que é o(n)",
 "O preço do deslocamento é a parcela c·127008·lg m ≤ c·127008·(lg n − 8), que é o(n)")
troca("rezende-unicamp-p-17",
 "    T'(m) = c₀                                   para m ≤ k,",
 "    T'(m) = c₀ (constante, c₀ ≥ 0)               para m ≤ k,")
print("fim")
