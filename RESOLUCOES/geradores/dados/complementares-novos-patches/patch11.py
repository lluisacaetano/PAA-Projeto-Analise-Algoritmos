# -*- coding: utf-8 -*-
"""Lote 11 (onda E): p21 base 'precisa' (suficiente vendida como necessária); p18 estrela Θ(n²) só no pior caso
(frase que EU escrevi no lote 9 — 7.15 de novo); p17 frase falsa sobre onde está a análise da matriz; k = n − d, d ≥ 1."""
exec(open(__file__.replace("patch11.py","patch1.py")).read().split("# uber-p8")[0])
troca("rezende-unicamp-p-21-exerc-cios-suplementares-item-1",
 "Portanto o caso base precisa cobrir pelo menos 1 ≤ n ≤ 189. Declaro:",
 "Por isso declaro o caso base em toda a faixa 1 ≤ n ≤ 189 — é uma escolha de conveniência (não a única possível), que garante que, para n ≥ 190, a recorrência só chame argumentos menores que n. Declaro:")
troca("rezende-unicamp-p-18",
 "por exemplo, a estrela K_{1,n−1} com k = 2 custa Θ(n²).",
 "por exemplo, a estrela K_{1,n−1} com k = 2 pode custar Θ(n²): no pior caso sobre a ordem das listas, cada folha retirada está no fim da lista do centro, e apagar custa (n − 1) + (n − 2) + … + 1; com a ordem favorável custaria só Θ(n).")
troca("rezende-unicamp-p-17",
 "A matriz de adjacências é mencionada, mas sua análise está no trecho omitido ([...]); não a trato.",
 "No material, o Exercício vem logo depois da análise por lista de adjacências; a análise por matriz de adjacências vem depois dele (T(n) = T(n − 1) + n + n, isto é, T(n) = T(0) + n(n + 1), também Θ(n²) e quadrática), então a resposta não depende da representação.")
troca("rezende-unicamp-p-17", "Com k perto de n (k = n − O(1))", "Com k perto de n (k = n − d, d ≥ 1 constante)")
print("fim")
