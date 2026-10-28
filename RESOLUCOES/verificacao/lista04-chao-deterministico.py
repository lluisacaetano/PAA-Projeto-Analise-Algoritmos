# -*- coding: utf-8 -*-
"""
Lista 4 (PAA / IFMG Formiga, 2026-2) - chao deterministico.
Python puro, sem numpy/sympy. Roda antes de qualquer redacao de prova.

Q1: confere as formas fechadas por avaliacao direta da recorrencia.
Q2: confere o Teorema Mestre na forma de Brassard & Bratley (compara a com b^k)
    contra a recorrencia calculada exatamente em potencias de b.
Q3: exibe o contraexemplo que refuta a proposicao (n=2) e localiza
    exatamente em qual passo k -> k+1 a construcao da "prova" quebra.
"""
import math
from functools import lru_cache

FALHAS = []

def checa(rotulo, ok, detalhe=""):
    print(("  OK   " if ok else "  FALHA") + f"  {rotulo}" + (f"   {detalhe}" if detalhe else ""))
    if not ok:
        FALHAS.append(rotulo)

# ----------------------------------------------------------------------
# QUESTAO 1 - formas fechadas
# ----------------------------------------------------------------------
print("=" * 72)
print("QUESTAO 1 - formas fechadas (medido pela recorrencia vs. formula)")
print("=" * 72)

# (a) 1 + 3 + 5 + ... + (2n-1) = n^2, para todo n >= 1
print("\n(a) soma dos n primeiros impares = n^2")
ok = True
for n in list(range(1, 60)) + [100, 1000, 5000]:
    medido = sum(2 * i - 1 for i in range(1, n + 1))
    formula = n * n
    if medido != formula:
        ok = False
        print(f"    divergencia em n={n}: medido={medido} formula={formula}")
for n in [1, 2, 3]:
    print(f"    n={n}: medido={sum(2*i-1 for i in range(1,n+1))}  formula={n*n}")
checa("1(a)  S(n) = n^2", ok)

# (b) T(1)=2 ; T(n)=2T(n-1)  ->  T(n)=2^n
print("\n(b) T(1)=2, T(n)=2T(n-1)  ->  T(n)=2^n")
def Tb(n):
    t = 2
    for _ in range(2, n + 1):
        t = 2 * t
    return t
ok = all(Tb(n) == 2 ** n for n in range(1, 200))
for n in [1, 2, 3]:
    print(f"    n={n}: recorrencia={Tb(n)}  formula={2**n}")
checa("1(b)  T(n) = 2^n", ok)

# (c) T(1)=1 ; T(n)=T(n-1)+1  ->  T(n)=n
print("\n(c) T(1)=1, T(n)=T(n-1)+1  ->  T(n)=n")
def Tc(n):
    t = 1
    for _ in range(2, n + 1):
        t = t + 1
    return t
ok = all(Tc(n) == n for n in range(1, 400))
for n in [1, 2, 3]:
    print(f"    n={n}: recorrencia={Tc(n)}  formula={n}")
checa("1(c)  T(n) = n", ok)

# (d) T(1)=1 ; T(n)=T(n-1)+3  ->  T(n)=3n-2
print("\n(d) T(1)=1, T(n)=T(n-1)+3  ->  T(n)=3n-2")
def Td(n):
    t = 1
    for _ in range(2, n + 1):
        t = t + 3
    return t
ok = all(Td(n) == 3 * n - 2 for n in range(1, 400))
for n in [1, 2, 3]:
    print(f"    n={n}: recorrencia={Td(n)}  formula={3*n-2}")
checa("1(d)  T(n) = 3n-2", ok)

# (e) T(1)=1 ; T(n)=T(n-1)+2  ->  forma fechada 2n-1, e 2n-1 in Theta(n)
print("\n(e) T(1)=1, T(n)=T(n-1)+2  ->  T(n)=2n-1, e 2n-1 in Theta(n)")
def Te(n):
    t = 1
    for _ in range(2, n + 1):
        t = t + 2
    return t
ok_forma = all(Te(n) == 2 * n - 1 for n in range(1, 400))
for n in [1, 2, 3]:
    print(f"    n={n}: recorrencia={Te(n)}  formula={2*n-1}")
checa("1(e)  T(n) = 2n-1", ok_forma)
# testemunhas de Theta: c1=1, c2=2, n0=1.  Confere EM n=n0 exatamente.
c1, c2, n0 = 1, 2, 1
print(f"    testemunhas Theta: c1={c1}, c2={c2}, n0={n0}")
print(f"    em n=n0={n0} exatamente: {c1}*{n0} = {c1*n0} <= {Te(n0)} <= {c2*n0} = {c2*n0}")
def _theta_ok(limite):
    t = 1                                  # T(1)
    for n in range(1, limite + 1):
        if n > 1:
            t = t + 2
        if not (c1 * n <= t <= c2 * n):
            return False, n
    return True, None
ok_theta, _falha_em = _theta_ok(200000)
if not ok_theta:
    print(f"    primeira violacao em n={_falha_em}")
checa("1(e)  1*n <= 2n-1 <= 2*n para todo n >= 1", ok_theta)

# ----------------------------------------------------------------------
# QUESTAO 2 - Teorema Mestre, forma Brassard & Bratley:
#   T(n) = a T(n/b) + c n^k  ->  a > b^k : Theta(n^(log_b a))
#                                a = b^k : Theta(n^k lg n)
#                                a < b^k : Theta(n^k)
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("QUESTAO 2 - Teorema Mestre (Brassard & Bratley: compara a com b^k)")
print("=" * 72)

CASOS = [
    ("(a)", 2, 3, 0),   # T(n) = 2T(n/3) + 1      -> f(n)=n^0
    ("(b)", 5, 4, 1),   # T(n) = 5T(n/4) + n
    ("(c)", 7, 7, 1),   # T(n) = 7T(n/7) + n
    ("(d)", 9, 3, 2),   # T(n) = 9T(n/3) + n^2
    ("(e)", 8, 2, 3),   # T(n) = 8T(n/2) + n^3
]

def resolve_exato(a, b, k, expoente_max):
    """T(1)=1 ; T(b^m) = a*T(b^(m-1)) + (b^m)^k. Exato em inteiros."""
    T = {0: 1}                       # m = 0  ->  n = 1
    for m in range(1, expoente_max + 1):
        T[m] = a * T[m - 1] + (b ** m) ** k
    return T

def classifica(a, b, k):
    bk = b ** k
    if a > bk:
        return "maior", f"Theta(n^(log_{b} {a}))", math.log(a, b)
    if a == bk:
        return "igual", f"Theta(n^{k} * lg n)", float(k)
    return "menor", f"Theta(n^{k})", float(k)

for rot, a, b, k in CASOS:
    bk = b ** k
    rel, resposta, expo = classifica(a, b, k)
    print(f"\n{rot} T(n) = {a}T(n/{b}) + n^{k}   a={a}, b={b}, k={k}, b^k={bk}  ->  a {'>' if rel=='maior' else ('=' if rel=='igual' else '<')} b^k")
    print(f"    resposta: {resposta}" + (f"   (log_{b} {a} = {expo:.6f})" if rel == "maior" else ""))

    # Confere: a razao T(n)/g(n) tem de estabilizar num intervalo [c1,c2] com c1>0.
    mmax = 14 if b == 2 else (10 if b == 3 else 8)
    T = resolve_exato(a, b, k, mmax)
    if rel == "maior":
        g = lambda n: n ** expo
    elif rel == "igual":
        g = lambda n: (n ** k) * math.log2(n) if n > 1 else 1.0
    else:
        g = lambda n: n ** k
    razoes = []
    for m in range(1, mmax + 1):
        n = b ** m
        razoes.append(T[m] / g(n))
    print(f"    T(n)/g(n) para n={b}^1..{b}^{mmax}:")
    print("      " + ", ".join(f"{r:.4f}" for r in razoes))
    c1, c2 = min(razoes[2:]), max(razoes[2:])   # descarta os 2 primeiros (transiente)
    estavel = c2 / c1 < 3.0 and c1 > 0
    checa(f"2{rot} razao T(n)/g(n) limitada por cima e por baixo",
          estavel, f"c1~{c1:.4f}  c2~{c2:.4f}  c2/c1={c2/c1:.3f}")

# Contraprova: para o caso (c), a resposta ERRADA Theta(n) tem razao que diverge.
print("\n  contraprova (c): se a resposta fosse Theta(n), a razao T(n)/n divergiria")
T = resolve_exato(7, 7, 1, 8)
print("    T(n)/n:      " + ", ".join(f"{T[m]/(7**m):.3f}" for m in range(1, 9)))
print("    T(n)/(n lg n): " + ", ".join(f"{T[m]/((7**m)*math.log2(7**m)):.4f}" for m in range(1, 9)))

# ----------------------------------------------------------------------
# QUESTAO 3 - a proposicao das nacionalidades
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("QUESTAO 3 - contraexemplo e localizacao do passo que quebra")
print("=" * 72)

# P(n): em todo conjunto de n pessoas, se ao menos uma e chinesa, todas sao.
def P_vale(n):
    """Enumera todos os conjuntos de n pessoas com rotulo chines/nao-chines
    e testa a proposicao. Retorna (vale, contraexemplo)."""
    for massa in range(1, 1 << n):          # ao menos uma chinesa
        rotulos = [(massa >> i) & 1 for i in range(n)]
        if any(rotulos) and not all(rotulos):
            return False, rotulos
    return True, None

for n in range(1, 6):
    vale, ce = P_vale(n)
    marca = "VERDADEIRA" if vale else "FALSA"
    extra = "" if vale else f"  contraexemplo: {['chines' if r else 'nao-chines' for r in ce]}"
    print(f"  P({n}) e {marca}{extra}")

checa("3  P(1) e verdadeira", P_vale(1)[0])
checa("3  P(2) e FALSA (logo a cadeia da inducao tem de quebrar em k=1 -> k=2)",
      not P_vale(2)[0])

# O passo construido na "prova": de S={T1..T_{k+1}} com T1 chines, tomar
# A = S \ {T_{k+1}} e B = S \ {T_k}. A h.i. so se aplica a um subconjunto que
# CONTENHA uma pessoa sabidamente chinesa (T1).
print("\n  o passo da 'prova': A = S\\{T_(k+1)},  B = S\\{T_k};  h.i. exige T1 em A e em B")
for k in range(1, 6):
    S = list(range(1, k + 2))            # T1 .. T_{k+1}
    A = [t for t in S if t != k + 1]
    B = [t for t in S if t != k]
    t1_em_A, t1_em_B = (1 in A), (1 in B)
    uniao_cobre = set(A) | set(B) == set(S)
    valido = t1_em_A and t1_em_B and uniao_cobre
    print(f"    k={k} (S com {k+1} pessoas): A={A} B={B}  "
          f"T1 em A? {t1_em_A}  T1 em B? {t1_em_B}  A u B = S? {uniao_cobre}  "
          f"->  passo {'valido' if valido else 'INVALIDO'}")

checa("3  o passo k=1 -> k=2 e invalido (B={T2} nao contem pessoa chinesa conhecida)",
      not (1 in [t for t in [1, 2] if t != 1]))
checa("3  o passo k>=2 e valido (por isso a falha e exatamente em k=1)",
      all(1 in [t for t in range(1, k + 2) if t != k + 1] and
          1 in [t for t in range(1, k + 2) if t != k]
          for k in range(2, 20)))

print()
print("=" * 72)
if FALHAS:
    print(f"FALHAS ({len(FALHAS)}): " + "; ".join(FALHAS))
else:
    print("Nenhuma falha. Chao deterministico consistente.")
print("=" * 72)

import sys
sys.exit(1 if FALHAS else 0)
