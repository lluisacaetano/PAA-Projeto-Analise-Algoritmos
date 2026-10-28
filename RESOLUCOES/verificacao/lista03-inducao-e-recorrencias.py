from functools import lru_cache
import math

print("=== Q2: f(n) = n se impar, n^2 se par ===")
f = lambda n: n if n % 2 else n*n
print("  n:      ", "".join(f"{n:>7}" for n in range(1,11)))
print("  f(n):   ", "".join(f"{f(n):>7}" for n in range(1,11)))

print("\n  f(n) <= 1*n^2 para todo n>=1?  ", all(0 <= f(n) <= n*n for n in range(1,200000)))
print("  f(n) >= c*n^2 para algum c>0 (ou seja, e Omega(n^2))?")
for c in [1, 0.5, 0.01, 0.0001]:
    falha = [n for n in range(1,100000) if not (c*n*n <= f(n))]
    print(f"     c={c:<8} falha em n={falha[:3]} ... total de falhas={len(falha)}  -> {'NAO e Omega(n^2)' if falha else 'seria Omega'}")
print("  f(n) <= c*n para algum c (ou seja, e O(n))?")
for c in [1, 10, 1000]:
    falha = [n for n in range(1,100000) if not (f(n) <= c*n)]
    print(f"     c={c:<8} falha a partir de n={falha[0] if falha else '-'}  -> {'NAO e O(n)' if falha else 'seria O(n)'}")
print("  f(n) >= 1*n para todo n>=1 (Omega(n))? ", all(n <= f(n) for n in range(1,100000)))

print("\n=== Q4(d): T(1)=1, T(n)=T(n-1)+n  ->  n(n+1)/2 ? ===")
@lru_cache(None)
def Td(n): return 1 if n==1 else Td(n-1)+n
bad=[n for n in range(1,3000) if Td(n)!=n*(n+1)//2]
print("  bate em n=1..2999" if not bad else f"  DIVERGE em {bad[:5]}")
print("  primeiros:", [Td(n) for n in range(1,9)], " formula:", [n*(n+1)//2 for n in range(1,9)])

print("\n=== Q4(e): T(1)=1, T(n)=2T(n-1)+1  ->  2^n - 1 ? ===")
@lru_cache(None)
def Te(n): return 1 if n==1 else 2*Te(n-1)+1
bad=[n for n in range(1,600) if Te(n)!=2**n-1]
print("  bate em n=1..599" if not bad else f"  DIVERGE em {bad[:5]}")
print("  primeiros:", [Te(n) for n in range(1,9)], " formula:", [2**n-1 for n in range(1,9)])

print("\n=== Q4(a): n! > 2^n para n>=4 ? (e falha antes?) ===")
for n in range(1,9):
    fat=math.factorial(n); p=2**n
    print(f"  n={n}: {n}!={fat:>8}  2^{n}={p:>6}  n!>2^n ? {fat>p}")

print("\n=== Q4(b): 2+4+...+2n = n^2+n ? ===")
bad=[n for n in range(1,5000) if sum(2*i for i in range(1,n+1)) != n*n+n]
print("  bate em n=1..4999" if not bad else f"  DIVERGE em {bad[:5]}")

print("\n=== Q4(c): 1+2+...+n = n(n+1)/2 ? ===")
bad=[n for n in range(1,5000) if sum(range(1,n+1)) != n*(n+1)//2]
print("  bate em n=1..4999" if not bad else f"  DIVERGE em {bad[:5]}")


# ---------------------------------------------------------------------------
# Q1 — calibracao das constantes (Alice vs Bob)
#
# ARMADILHA: a primeira calibracao usava T_A(n) = 15*n*lg(n), SEM termo constante.
# Como lg(1) = 0, isso da T_A(1) = 0 e Alice "vence" em n=1 com tempo zero,
# contradizendo o enunciado (que diz que Bob vence para TODO n < 100).
# O erro so aparece testando n=1 — que e exatamente o caso que nao foi testado.
# ---------------------------------------------------------------------------
print("\n=== Q1: varredura COMPLETA de n=1 a 200 ===")
B = lambda n: n*n
for nome, A in [
    ("15 n lg n        (QUEBRADO em n=1)", lambda n: 15*n*math.log2(n)),
    ("15 n lg n + 20   (correto)",         lambda n: 15*n*math.log2(n) + 20),
]:
    ganha = [n for n in range(1, 200) if A(n) < B(n)]
    prim = ganha[0] if ganha else None
    contiguo = ganha == list(range(prim, 200)) if prim else False
    print(f"  {nome}")
    print(f"    Alice vence a partir de n={prim}, sem furos? {contiguo}")
    print(f"    -> {'reproduz o enunciado' if prim == 100 and contiguo else 'NAO reproduz'}")

A = lambda n: 15*n*math.log2(n) + 20
lo, hi = 50.0, 150.0
for _ in range(200):
    mid = (lo + hi) / 2
    if (A(lo) - B(lo)) * (A(mid) - B(mid)) <= 0: hi = mid
    else: lo = mid
print(f"\n  cruzamento real em n = {(lo+hi)/2:.4f}  (entre 99 e 100 — nao 'exatamente 100')")
print(f"  primeiro inteiro em que Alice vence: 100")
