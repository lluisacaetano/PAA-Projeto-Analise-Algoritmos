# -*- coding: utf-8 -*-
"""Lote 3 (onda B): walace item 2 — contraste falso com o slide 15; ifmg-23 — frase sem verbo."""
exec(open(__file__.replace("patch3.py","patch1.py")).read().split("# uber-p8")[0])
troca("walace-ifmg-slide-16-item-2",
 "Ao contrário do exemplo do slide 15, aqui a soma perturbada T(n) se cancela por inteiro — não é preciso conhecer T(n), que não tem forma fechada elementar; ela serve só de veículo para chegar a S(n).",
 "Como no exemplo do slide 15 (onde Σ i³ aparece dos dois lados e se cancela), a soma perturbada T(n) se cancela por inteiro: não é preciso conhecer T(n), que serve só de veículo para chegar a S(n). A diferença está no que sobra: no slide 15 sobram as somas auxiliares Σ i e Σ 1, cujas formas fechadas é preciso conhecer, e a incógnita Σ i² aparece com coeficiente 3; aqui não sobra nenhuma soma além de S(n), que aparece com coeficiente 1.")
troca("ifmg-slide-23", "a simulação do Algoritmo 6 com a primeira chamada (V, 10) e confirma", "a simulação do Algoritmo 6 com a primeira chamada (V, 10) confirma")
print("fim")
