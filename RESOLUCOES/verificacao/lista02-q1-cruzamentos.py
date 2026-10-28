"""Confere os pontos de cruzamento citados na Questao 1 da Lista 2.

O que importa aqui sao as BORDAS: onde ha empate exato. Errar o <= por < muda
a resposta no ponto de fronteira, e foi exatamente isso que um verificador pegou
no rascunho desta lista.
"""

def cruzamento(nome, f, g, pontos, rotf, rotg):
    print(f"\n=== {nome} ===")
    for n in pontos:
        a, b = f(n), g(n)
        rel = "EMPATE EXATO" if a == b else (f"{rotf} menor" if a < b else f"{rotg} menor")
        print(f"  n={n:>12,}  {rotf}={a:>24,}  {rotg}={b:>24,}   -> {rel}")

# 1(a): T_A = n^3 + 10  vs  T_B = 1000 n^2   (ilustra constantes ocultas)
cruzamento("1(a)  n^3+10  vs  1000n^2",
           lambda n: n**3 + 10, lambda n: 1000*n*n,
           [998, 999, 1000, 1001], "A", "B")

# 1(b) razao (iii): T1 = 5000 n^2  vs  T2 = 2 n^3   (cubico ganha ate 2499)
cruzamento("1(b)  2n^3 (cubico)  vs  5000n^2 (quadratico)",
           lambda n: 2*n**3, lambda n: 5000*n*n,
           [2498, 2499, 2500, 2501], "cubico", "quadratico")

# 1(c): T_A = 10^8 n  vs  T_B = 10 n^2   (o enunciado da contagens EXATAS)
cruzamento("1(c)  10^8*n  vs  10*n^2",
           lambda n: 10**8*n, lambda n: 10*n*n,
           [10**6, 10**7 - 1, 10**7, 10**7 + 1, 10**8], "A", "B")

print("\nConclusao 1(c): A so e preferivel para n > 10^7. Em n = 10^7 ha empate exato,")
print("e para n < 10^7 o algoritmo B faz menos instrucoes. Logo A NAO e sempre preferivel.")
