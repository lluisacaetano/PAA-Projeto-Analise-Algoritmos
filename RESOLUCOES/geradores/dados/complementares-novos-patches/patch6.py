# -*- coding: utf-8 -*-
"""Lote 6 (onda B): rezende-p17 — rascunho no Passo 4; Resposta cita o modelo T' sem nomeá-lo."""
exec(open(__file__.replace("patch6.py","patch1.py")).read().split("# uber-p8")[0])
troca("rezende-unicamp-p-17", "Em particular nunca é exponencial (pelo mesmo argumento do Passo 3, com n³ no lugar de n²: n³ = 8m³ e m³ ≤ 2^(2m)... prefiro não depender disso: basta notar n³ ≤ n·n² e repetir — ver nota abaixo).",
      "Em particular nunca é exponencial (ver nota abaixo).")
troca("rezende-unicamp-p-17", "Em nenhum caso é exponencial: para k arbitrário o custo do modelo é O(n³).",
      "Em nenhum caso é exponencial: para k arbitrário o custo do modelo T' do Passo 4 (que para quando restam m ≤ k vértices) é O(n³).")
print("fim")
