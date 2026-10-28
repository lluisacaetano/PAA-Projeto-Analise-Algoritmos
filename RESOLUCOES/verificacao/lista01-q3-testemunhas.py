"""Testa os pares (c, n0) da Questao 3 contra a definicao formal do CLRS.

Bater em todos os pontos NAO e demonstracao. Divergir em qualquer ponto E refutacao.
"""
LIM = 200000

def testa_O(nome, f, g, c, n0):
    # definicao: 0 <= f(n) <= c*g(n) para todo n >= n0
    falhas = [n for n in range(n0, LIM) if not (0 <= f(n) <= c*g(n))]
    print(f"  {nome}: c={c}, n0={n0}  ->  {'OK' if not falhas else f'FALHA em n={falhas[:5]}'}")

def testa_Omega(nome, f, g, c, n0):
    # definicao: 0 <= c*g(n) <= f(n) para todo n >= n0
    falhas = [n for n in range(n0, LIM) if not (0 <= c*g(n) <= f(n))]
    print(f"  {nome}: c={c}, n0={n0}  ->  {'OK' if not falhas else f'FALHA em n={falhas[:5]}'}")

def testa_Theta(nome, f, g, c1, c2, n0):
    # definicao: 0 <= c1*g(n) <= f(n) <= c2*g(n) para todo n >= n0
    falhas = [n for n in range(n0, LIM) if not (0 <= c1*g(n) <= f(n) <= c2*g(n))]
    print(f"  {nome}: c1={c1}, c2={c2}, n0={n0}  ->  {'OK' if not falhas else f'FALHA em n={falhas[:5]}'}")

um  = lambda n: 1
n1  = lambda n: n
n2  = lambda n: n*n

print("Questao 3 — testemunhas propostas:")
testa_O    ("(a) f(n)=2^117 em O(1)",         lambda n: 2**117,        um, 2**117, 1)  # 06/10/2026: era 2117 (expoente perdido na extração)
testa_O    ("(b) f(n)=n^2+2n em O(n^2)",      lambda n: n*n + 2*n,     n2, 3,    1)
testa_Theta("(c) f(n)=n^2-2n+3 em Theta(n^2)",lambda n: n*n - 2*n + 3, n2, 0.5, 1, 2)
testa_Omega("(d) f(n)=5n em Omega(n)",        lambda n: 5*n,           n1, 5,    1)
testa_Omega("(e) f(n)=n^2+2n-8 em Omega(n^2)",lambda n: n*n + 2*n - 8, n2, 1,    4)

print("\nBordas que mais derrubam prova (checagem #17 — vale exatamente em n0?):")
print("  (c) n=1: f(1) = 1-2+3 = 2 ; c2*g(1) = 1  ->  2 <= 1 e FALSO, por isso n0=2, nao 1")
print("  (e) n=1: f(1) = 1+2-8 = -5 ->  NEGATIVO, viola 0 <= f(n) da definicao")
print("  (e) n=2: f(2) = 4+4-8 =  0 ;  c*g(2) = 4  ->  4 <= 0 e FALSO")
print("  (e) n=3: f(3) = 9+6-8 =  7 ;  c*g(3) = 9  ->  9 <= 7 e FALSO, por isso n0=4")
print("  (e) n=4: f(4) = 16+8-8= 16 ;  c*g(4) = 16 ->  16 <= 16 OK, o n0=4 e justo")
