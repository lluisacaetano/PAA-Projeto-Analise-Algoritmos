# -*- coding: utf-8 -*-
"""Lote 5 (onda B): campello-p11 — PASSO 5 misturava O do Campello com Θ do CLRS; enxugado ao que o enunciado
fixa (x, y > 1). rezende-p21 — faixa 27,5–48,3 valia só nas potências de 10."""
import re
exec(open(__file__.replace("patch5.py","patch1.py")).read().split("# uber-p8")[0])
p = f"{D}/campello-p-11.md"; t = open(p, encoding="utf-8").read()
ini = t.index("PASSO 5 — O PAPEL DA HIPÓTESE") if "PASSO 5 — O PAPEL DA HIPÓTESE" in t else None
if ini is None: print("  já: PASSO 5")
else:
  fim = t.index("\n\nConferência numérica", ini)
if ini is not None:
  velho = t[ini:fim]
novo = """PASSO 5 — ONDE A HIPÓTESE x, y > 1 ENTRA:
O enunciado fixa x, y > 1, e a prova usa isso em dois pontos: c = log_y x > 0 (PASSO 2), que a definição exige, e log_x n ≥ 0 para n ≥ 1 (PASSO 4), que dá o 0 ≤ c1·g(n) do Θ. Não analiso aqui todas as bases fora de (1, ∞), porque o veredito delas depende de qual definição se usa (a do Campello não exige 0 ≤ f; a do CLRS exige) e porque logaritmo negativo não serve como custo de algoritmo. Dois fatos bastam para ver que a hipótese não pode ser simplesmente apagada:
(i) Base 1: 1^s = 1 para todo s, então log_1 n não está definido (para n ≥ 2 não existe s com 1^s = n; para n = 1 todo s serve).
(ii) Contraexemplo concreto, pela definição de O do material: y = 2 e x = 1/2. Então log_x n = −log_2 n. Afirmação: log_2 n NÃO é O(log_(1/2) n). Negação da definição: para toda c > 0 e todo n0 ≥ 1, existe n ≥ n0 com log_2 n > c·log_(1/2) n. Tome n = max(n0, 2). Então log_2 n ≥ 1 > 0 e c·log_(1/2) n = −c·log_2 n < 0. A desigualdade f(n) ≤ c·g(n) falha nesse n, qualquer que seja a escolha de c e n0."""
if ini is not None and velho != novo:
    if "ONDE A HIPÓTESE x, y > 1 ENTRA" in velho: raise SystemExit("estado inesperado")
    t = t[:ini] + novo + t[fim:]; open(p, "w", encoding="utf-8").write(t); print("  ok: PASSO 5")
troca("campello-p-11", "A hipótese x, y > 1 é suficiente, e é a que interessa para custo de algoritmo; ela não é necessária para o O sozinho. Com base 1 o logaritmo não está definido. Com as duas bases em (0, 1), c = log_y x continua positiva e o O vale do mesmo jeito; com x > 1 e y ∈ (0, 1), o O vale trivialmente (log_y n ≤ 0 ≤ log_x n), mas o Θ falha. O O falha só com x ∈ (0, 1) e y > 1: por exemplo, log_2 n NÃO é O(log_(1/2) n).",
      "A prova usa x, y > 1 (que o enunciado fixa) para ter c > 0 e log_x n ≥ 0; a hipótese não pode ser simplesmente apagada: com base 1 o logaritmo não está definido, e com x = 1/2, y = 2 tem-se log_2 n NÃO é O(log_(1/2) n) (PASSO 5).")
troca("campello-p-11", "funções que diferem por um fator constante positivo estão na mesma classe Θ.",
      "funções não negativas (para n ≥ n0) que diferem por um fator constante positivo estão na mesma classe Θ.")
troca("rezende-unicamp-p-21-exerc-cios-suplementares-item-1", "a recorrência dá T(n)/(n lg n) entre 27,5 e 48,3 para n de 10⁴ a 10⁹",
      "a recorrência dá T(n)/(n lg n) entre 27,5 e 48,3 nas potências de 10 de 10⁴ a 10⁹ (numa amostra densa do mesmo intervalo, entre cerca de 23,9 e 52,2)")
print("fim")
# rezende-p18 (onda C): k = 0 é constante e O(k n²) = O(0) — a comparação só vale com k ≥ 1
for a, b in [("que para k constante é O(m + n log n), melhor que", "que para k constante, k ≥ 1, é O(m + n log n), melhor que"),
             ("Essa é a frase literal do texto,", "Essa é a soma das cotas que o texto dá,"),
             ("n₀ = 2. Isso é melhor que o O(k n²) da lista sem heap sempre que m ∈ o(n²);", "n₀ = 2. Para k ≥ 1, isso é melhor que o O(k n²) da lista sem heap sempre que m ∈ o(n²) (com k = 0 nada é retirado e a comparação não se aplica);")]:
    troca("rezende-unicamp-p-18", a, b)
print("fim2")
