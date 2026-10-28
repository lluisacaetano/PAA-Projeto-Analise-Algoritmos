import math
from functools import lru_cache

print("═══════════ IFMG (Diego Mello) ═══════════")
bad=[n for n in range(1,3000) if sum(i*i for i in range(0,n+1)) != (2*n+1)*(n+1)*n//6]
print(f"  ex1  Σi² (i=0..n) = (2n+1)(n+1)n/6 : {'BATE n=1..2999' if not bad else f'DIVERGE {bad[:3]}'}")
bad=[n for n in range(1,3000) if sum(3*i-2 for i in range(1,n+1)) != n*(3*n-1)//2]
print(f"  ex2  1+4+7+…+(3n−2) = n(3n−1)/2    : {'BATE n=1..2999' if not bad else f'DIVERGE {bad[:3]}'}")

@lru_cache(None)
def hanoi(n): return 1 if n==1 else 2*hanoi(n-1)+1
bad=[n for n in range(1,500) if hanoi(n)!=2**n-1]
print(f"  ex7  Hanoi T(n)=2T(n−1)+1 = 2ⁿ−1   : {'BATE n=1..499' if not bad else f'DIVERGE {bad[:3]}'}")

# ordenacao por selecao: T(j) = T(j-1) + (custo do for, ~j) ; T(1)=c
def selsort_ops(n):
    t=0
    def rec(j):
        nonlocal t
        t+=1                       # teste j=1
        if j==1: return
        t+=1                       # indice<-1
        for i in range(1,j+1): t+=2   # teste + comparacao
        t+=3                       # 3 atribuicoes da troca
        rec(j-1)
    rec(n); return t
print(f"  ex6  ordenacao-por-selecao: T(n)/n² →", end=" ")
print(", ".join(f"n={n}:{selsort_ops(n)/n**2:.3f}" for n in [50,200,800]), "→ Θ(n²)")

print("\n═══════════ Campello ═══════════")
print("  ex1  5n é o(n)?  o() exige que valha para TODO c>0:")
for c in [10, 5, 4, 1]:
    ok = any(5*n < c*n for n in range(1,10000))
    print(f"        c={c:<3} existe n com 5n < {c}n ? {ok}")
print("        → NAO é o(n): falha para todo c ≤ 5.")
print("  ex2  5n² é ω(n²)? ω() exige que valha para TODO c>0:")
for c in [1, 5, 6, 100]:
    ok = any(5*n*n > c*n*n for n in range(1,10000))
    print(f"        c={c:<3} existe n com 5n² > {c}n² ? {ok}")
print("        → NAO é ω(n²): falha para todo c ≥ 5.")

g = lambda n: 3*n*n if n%2==0 else 7*n
print(f"  ex3  f=3n² par / 7n ímpar:  f(n) ≤ 7n² ∀n≥1 ? {all(g(n)<=7*n*n for n in range(1,50000))}")
print(f"                              f(n) ≥ 3n  ∀n≥1 ? {all(g(n)>=3*n for n in range(1,50000))}")
print(f"                              é Ω(n²)? c=1 falha em n ímpar = {[n for n in range(1,200) if not (1*n*n<=g(n))][:3]} → NAO")

print("\n═══════════ Loureiro — Teorema Mestre ═══════════")
def mestre(a,b,fexp,nome):
    crit = math.log(a,b)
    print(f"  {nome}: a={a}, b={b}, n^log_b(a) = n^{crit:.4f}, f(n)=n^{fexp}", end="  → ")
    if fexp < crit - 1e-9:   print(f"CASO 1 → Θ(n^{crit:.4f})")
    elif abs(fexp-crit)<1e-9: print(f"CASO 2 → Θ(n^{crit:.4f} · log n)")
    else:                     print(f"CASO 3 → Θ(n^{fexp})  (checar regularidade)")
mestre(4,2,1,"ex5  T(n)=4T(n/2)+n  ")
mestre(4,2,2,"ex6  T(n)=4T(n/2)+n² ")
mestre(4,2,3,"ex7  T(n)=4T(n/2)+n³ ")
print(f"       regularidade do caso 3 (ex7): 4·(n/2)³ = n³/2 = 0.5·n³ ≤ c·n³ com c=0.5<1 → OK")
print(f"\n  ex8  A: T=7T(n/2)+n² → n^log2(7) = n^{math.log(7,2):.6f}")
print(f"       A': T'=aT'(n/4)+n² → n^log4(a).  A' mais rapido ⟺ log4(a) < log2(7) ⟺ a < 4^log2(7) = {4**math.log(7,2):.4f}")
for a in [47,48,49,50]:
    print(f"         a={a}: log4({a}) = {math.log(a,4):.6f} {'<' if math.log(a,4)<math.log(7,2) else '≥'} {math.log(7,2):.6f}  → {'A0 mais rapido' if math.log(a,4)<math.log(7,2) else 'NAO'}")
print("       → maior inteiro a = 48")

print("\n═══════════ USP — indução ═══════════")
from fractions import Fraction
bad=[n for n in range(1,2000) if sum(Fraction(1,k*(k+1)) for k in range(1,n+1)) != Fraction(n,n+1)]
print(f"  2.1  Σ 1/(k(k+1)) = n/(n+1)        : {'BATE n=1..1999' if not bad else f'DIVERGE {bad[:3]}'}")
print(f"  2.2  2n³ > 3n²+3n+1 para n ≥ 3     :", end=" ")
for n in [1,2,3,4]:
    print(f"n={n}:{2*n**3}>{3*n*n+3*n+1}={2*n**3 > 3*n*n+3*n+1}", end="  ")
print()
F=[0,1]
for i in range(2,700): F.append(F[-1]+F[-2])
bad=[n for n in range(1,130) if F[5*n]%5!=0]
print(f"  2.3  F_5n é múltiplo de 5           : {'BATE n=1..129' if not bad else f'DIVERGE {bad[:3]}'}")
print(f"        F5={F[5]}, F10={F[10]}, F15={F[15]}, F20={F[20]} → todos divisíveis por 5")
print(f"  2.4  PIF ⟹ PBO                      : teorema, sem verificação numérica cabível")
