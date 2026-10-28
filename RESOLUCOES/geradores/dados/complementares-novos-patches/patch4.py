# -*- coding: utf-8 -*-
"""Lote 4 (onda B): loureiro-p185 — frase lateral sobre paralelas/concorrentes falsa ao pé da letra."""
exec(open(__file__.replace("patch4.py","patch1.py")).read().split("# uber-p8")[0])
troca("loureiro-p-185",
 "com retas paralelas ou com três por um ponto, a reta nova acrescenta menos (ex.: três retas por um ponto dão 6, não 7).",
 "se a reta nova é paralela a alguma anterior, ou passa por um ponto onde duas anteriores já se cruzam, ela acrescenta menos que n (ex.: três retas por um ponto dão 6, não 7); e uma configuração com algum par paralelo ou algum trio concorrente tem menos que L_n regiões.")
print("fim")
