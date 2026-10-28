# -*- coding: utf-8 -*-
"""Lote 9 (onda C/D): rezende-p18 — "sem ganho com o heap" é falso com k = 1 (parcela de apagar é nula)."""
exec(open(__file__.replace("patch9.py","patch1.py")).read().split("# uber-p8")[0])
troca("rezende-unicamp-p-18",
 "(Se, em vez de marcar, se apagasse v da lista de cada vizinho percorrendo-a, como na recorrência do texto, cada remoção pagaria até (k − 1)(n − 1) e o total voltaria a O(k n²), sem ganho com o heap.)",
 "(Se, em vez de marcar, se apagasse v da lista de cada vizinho percorrendo-a, como na recorrência do texto, então, para k ≥ 2, cada remoção pagaria até (k − 1)(n − 1) e a cota voltaria a O(k n²), sem ganho na cota com o heap — por exemplo, a estrela K_{1,n−1} com k = 2 custa Θ(n²). Com k = 1 o vértice retirado tem grau 0, a parcela de apagar é nula e o ganho permanece.)")
print("fim")
