# -*- coding: utf-8 -*-
"""Lote 2: referências ao chão nas p17/p19/p21 do Rezende (soluções #1)."""
exec(open(__file__.replace("patch2.py","patch1.py")).read().split("# uber-p8")[0])
C = "conferido numericamente em Python (fora da prova)"
troca("rezende-unicamp-p-17", "Conferência: o CHÃO DETERMINÍSTICO confirma a forma fechada do Passo 1 — \"T(n) − T(0) = n(n + 1)/2 + (k − 1)·n(n − 1)/2: True\". Não confere",
      f"Conferência ({C}): a forma fechada do Passo 1, T(n) − T(0) = n(n + 1)/2 + (k − 1)·n(n − 1)/2, confere. A conferência numérica não cobriu")
troca("rezende-unicamp-p-17", "esses foram conferidos à mão nos valores de fronteira (n = 1, 2 para T; n = k + 1 e n = 6 com k = 3 para T'), sem computação.",
      "esses foram conferidos à mão nos valores de fronteira (n = 1, 2 para T; n = k + 1 e n = 6 com k = 3 para T').")
troca("rezende-unicamp-p-19", "Conferência: o chão determinístico confirma a torre", f"Conferência ({C}): conferem a torre")
troca("rezende-unicamp-p-21-exerc-cios-suplementares-item-1", "Conferência: o CHÃO DETERMINÍSTICO (com outro caso base, T(n) = 1 para n ≤ 1000) dá", f"Conferência ({C}): com outro caso base, T(n) = 1 para n ≤ 1000, a recorrência dá")
troca("rezende-unicamp-p-21-exerc-cios-suplementares-item-1", " O chão confirma ainda o domínio:", " Confere ainda o domínio:")
troca("rezende-unicamp-p-21-exerc-cios-suplementares-item-1", " Os números do PASSO 1 e do PASSO 2 foram feitos à mão (sem ferramenta) e estão escritos por extenso para conferência.", " Os números do PASSO 1 e do PASSO 2 estão escritos por extenso para conferência.")
print("fim")
