# -*- coding: utf-8 -*-
"""Lote 12 (onda G): p18 — 'No texto, Kₙ...' atribui ao material um exemplo que ele não tem."""
exec(open(__file__.replace("patch12.py","patch1.py")).read().split("# uber-p8")[0])
troca("rezende-unicamp-p-18", "No texto, Kₙ com k = n cai aqui", "Por exemplo, Kₙ com k = n cai aqui")
print("fim")
