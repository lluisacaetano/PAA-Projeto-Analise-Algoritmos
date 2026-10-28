# -*- coding: utf-8 -*-
"""Lote 10 (onda D): rezende-p17 — "custo modelado é Θ(k·n²)" e "k da ordem de n ⇒ Θ(n³)" são falsos para T' com k = n − O(1)."""
exec(open(__file__.replace("patch10.py","patch1.py")).read().split("# uber-p8")[0])
A = "rezende-unicamp-p-17"
troca(A, "Se k é uma entrada que pode crescer junto com n, o custo modelado é Θ(k·n²), que vai de quadrático (k constante) a cúbico (k proporcional a n, por exemplo k = ⌊n/2⌋), e o teto é O(n³) porque k útil é no máximo n − 1.",
      "Se k é uma entrada que pode crescer junto com n, a recorrência literal dá Θ(k·n²); o modelo T' dá O(k·n²) ⊆ O(n³), que vai de quadrático (k constante) a cúbico (k = ⌊αn⌋ com 0 < α < 1 fixo, por exemplo k = ⌊n/2⌋), e o teto é O(n³) porque k útil é no máximo n − 1. Com k perto de n (k = n − O(1)) restam só O(1) passos de custo Θ(k·n) e T' volta a Θ(n²): com k = n − 1, T'(n) = c₀ + n + (n − 2)(n − 1).")
troca(A, "Se k crescer com n, a dependência em k aparece: com k da ordem de n o custo modelado chega a Θ(n³), e nunca passa de O(n³)",
      "Se k crescer com n, a dependência em k aparece: com k proporcional a n e longe de n (k = ⌊αn⌋, 0 < α < 1; por exemplo k = ⌊n/2⌋) o custo modelado chega a Θ(n³), e nunca passa de O(n³)")
print("fim")
