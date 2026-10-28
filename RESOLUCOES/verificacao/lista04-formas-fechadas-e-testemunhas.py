# -*- coding: utf-8 -*-
"""
Lista 4 - conferencia das FORMAS FECHADAS e das TESTEMUNHAS propostas pelos solvers.
Roda depois do chao deterministico e antes dos verificadores.
Python puro. Aritmetica inteira exata onde possivel.
"""
import math, random

FALHAS = []
def checa(rot, ok, det=""):
    print(("  OK   " if ok else "  FALHA") + f"  {rot}" + (f"   {det}" if det else ""))
    if not ok:
        FALHAS.append(rot)

print("=" * 76)
print("Q2 - forma fechada exata em n = b^m  (T(1)=1)")
print("=" * 76)

def T_exata(a, b, k, m):
    """T(1)=1 ; T(b^i) = a*T(b^(i-1)) + (b^i)^k. Inteiros exatos."""
    t = 1
    for i in range(1, m + 1):
        t = a * t + (b ** i) ** k
    return t

# Lema geral:  T(b^m) = a^m + sum_{i=0}^{m-1} a^i * b^(k*(m-i))
print("\nLema da expansao:  T(b^m) = a^m + soma_{i=0}^{m-1} a^i * b^(k(m-i))")
ok = True
for (a, b, k) in [(2,3,0),(5,4,1),(7,7,1),(9,3,2),(8,2,3),(3,2,1),(1,2,0),(4,2,2),(2,2,5)]:
    for m in range(0, 12):
        lema = a**m + sum(a**i * b**(k*(m-i)) for i in range(0, m))
        if lema != T_exata(a, b, k, m):
            ok = False
            print(f"    divergencia a={a} b={b} k={k} m={m}: lema={lema} exata={T_exata(a,b,k,m)}")
checa("Q2 lema da expansao vale para 9 triplas (a,b,k) e m=0..11", ok)

# (F1) caso a = b^k :  T(n) = (m+1) * n^k
print("\n(F1) caso a = b^k:  T(b^m) = (m+1) * (b^m)^k")
ok = True
for (a, b, k) in [(7,7,1),(9,3,2),(8,2,3),(4,2,2),(2,2,1),(16,2,4),(25,5,2)]:
    assert a == b**k
    for m in range(0, 11):
        f1 = (m + 1) * (b**m)**k
        if f1 != T_exata(a, b, k, m):
            ok = False
            print(f"    divergencia a={a} b={b} k={k} m={m}: F1={f1} exata={T_exata(a,b,k,m)}")
checa("Q2 (F1) vale para 7 triplas com a=b^k, m=0..10", ok)

# (F2) caso a != b^k :  T(n) = A*n^(log_b a) - B*n^k,  A = a/(a-b^k), B = b^k/(a-b^k)
print("\n(F2) caso a != b^k:  T(b^m) = A*a^m - B*b^(km),  A = a/(a-b^k), B = b^k/(a-b^k)")
print("     (aritmetica em fracoes inteiras para evitar erro de ponto flutuante)")
from fractions import Fraction
ok = True
for (a, b, k) in [(2,3,0),(5,4,1),(3,2,1),(2,2,0),(4,3,1),(2,4,1),(1,2,1),(3,3,2)]:
    if a == b**k:
        continue
    A = Fraction(a, a - b**k)
    B = Fraction(b**k, a - b**k)
    for m in range(0, 11):
        f2 = A * a**m - B * b**(k*m)
        ex = T_exata(a, b, k, m)
        if f2 != ex:
            ok = False
            print(f"    divergencia a={a} b={b} k={k} m={m}: F2={f2} exata={ex}")
checa("Q2 (F2) vale exatamente (em fracoes) para 8 triplas com a != b^k, m=0..10", ok)
print("     nota: A - B = (a - b^k)/(a - b^k) = 1  ->  T(1) = A - B = 1, bate com o caso base.")
for (a,b,k) in [(2,3,0),(5,4,1),(3,2,1)]:
    A = Fraction(a, a-b**k); B = Fraction(b**k, a-b**k)
    print(f"       a={a} b={b} k={k}:  A={A}  B={B}  A-B={A-B}")

# --- formas fechadas item a item, como escritas na resolucao -------------
print("\nFormas fechadas item a item (as que vao para o documento):")
casos_forma = [
    ("(a)  T(n) = 2*n^(log_3 2) - 1",       2,3,0, lambda n: 2*n**math.log(2,3) - 1),
    ("(b)  T(n) = 5*n^(log_4 5) - 4n",      5,4,1, lambda n: 5*n**math.log(5,4) - 4*n),
    ("(c)  T(n) = n*(log_7 n + 1)",         7,7,1, lambda n: n*(math.log(n,7) + 1)),
    ("(d)  T(n) = n^2*(log_3 n + 1)",       9,3,2, lambda n: n*n*(math.log(n,3) + 1)),
    ("(e)  T(n) = n^3*(lg n + 1)",          8,2,3, lambda n: n**3*(math.log2(n) + 1)),
]
for rot, a, b, k, f in casos_forma:
    mmax = 12 if b == 2 else (9 if b == 3 else 7)
    pior = 0.0
    for m in range(0, mmax + 1):
        n = b**m
        ex = T_exata(a, b, k, m)
        pior = max(pior, abs(f(n) - ex) / max(1, abs(ex)))
    checa(rot, pior < 1e-12, f"erro relativo maximo = {pior:.2e}  (m=0..{mmax})")

# ------------------------------------------------------------------
# TESTEMUNHAS de Theta - conferindo EM n = n0 exatamente
# ------------------------------------------------------------------
print()
print("=" * 76)
print("Q2 - testemunhas de Theta, conferidas EM n = n0 exatamente e alem")
print("=" * 76)

# caso a > b^k : c1 = 1, c2 = A, n0 = 1
print("\ncaso a > b^k :  c1 = 1, c2 = A = a/(a-b^k), n0 = 1,  g(n) = n^(log_b a)")
for rot, a, b, k in [("(a)",2,3,0), ("(b)",5,4,1)]:
    A = a / (a - b**k)
    c1, c2, n0 = 1.0, A, 1
    g = lambda n: n ** math.log(a, b)
    T1 = T_exata(a, b, k, 0)
    print(f"  {rot} a={a} b={b} k={k}:  A={A}")
    print(f"      em n=n0=1 exatamente: c1*g(1)={c1*g(1):.6f} <= T(1)={T1} <= c2*g(1)={c2*g(1):.6f}")
    mmax = 9 if b == 3 else 7
    ok = all(c1*g(b**m) <= T_exata(a,b,k,m) <= c2*g(b**m) + 1e-9 for m in range(0, mmax+1))
    checa(f"2{rot} c1=1, c2={A:g}, n0=1", ok, f"testado em n=b^0..b^{mmax}")

# caso a = b^k : c1 = 1/lg b, c2 = 2/lg b, n0 = b
print("\ncaso a = b^k :  c1 = 1/lg b, c2 = 2/lg b, n0 = b,  g(n) = n^k * lg n")
print("  (n0 = 1 seria FALSO: lg 1 = 0, logo a cota superior c2*0 = 0 < T(1) = 1)")
for rot, a, b, k in [("(c)",7,7,1), ("(d)",9,3,2), ("(e)",8,2,3)]:
    c1, c2, n0 = 1/math.log2(b), 2/math.log2(b), b
    g = lambda n: (n**k) * math.log2(n)
    # refuta n0 = 1
    ruim = (T_exata(a,b,k,0) <= c2 * g(1))
    checa(f"2{rot} n0=1 e REFUTADO", not ruim,
          f"T(1)={T_exata(a,b,k,0)}  c2*g(1)={c2*g(1):.1f}  ->  {T_exata(a,b,k,0)} <= 0 e falso")
    # confere em n = n0 = b exatamente
    Tb_ = T_exata(a, b, k, 1)
    print(f"      em n=n0={b} exatamente: {c1*g(b):.4f} <= T({b})={Tb_} <= {c2*g(b):.4f}")
    mmax = 12 if b == 2 else (9 if b == 3 else 7)
    ok = all(c1*g(b**m) - 1e-9 <= T_exata(a,b,k,m) <= c2*g(b**m) + 1e-9 for m in range(1, mmax+1))
    checa(f"2{rot} c1=1/lg {b}, c2=2/lg {b}, n0={b}", ok, f"testado em n=b^1..b^{mmax}")

# contraprova (c): nao e Theta(n)
print("\ncontraprova (c): T(n)/n = log_7 n + 1 diverge  ->  T nao e O(n)")
for m in [1,2,4,8,12]:
    n = 7**m
    print(f"    n=7^{m}:  T(n)/n = {T_exata(7,7,1,m)/n:.1f}")
checa("2(c) T(n)/n cresce sem limite (refuta Theta(n))",
      T_exata(7,7,1,12)/7**12 > T_exata(7,7,1,4)/7**4 > T_exata(7,7,1,1)/7)

# ------------------------------------------------------------------
# EXERCICIO DO SLIDE - fatores de balanceamento em arvore binaria
# Afirmacao a conferir: o numero de chamadas de FatorAltura numa arvore
# de n nos e 2n+1, INDEPENDENTE do formato da arvore.
# ------------------------------------------------------------------
print()
print("=" * 76)
print("Exercicio do slide (UNICAMP, Exemplo 3) - o formato da arvore muda algo?")
print("=" * 76)

class No:
    __slots__ = ("e", "d")
    def __init__(self, e=None, d=None):
        self.e, self.d = e, d

chamadas = 0
prof_max = 0
def fator_altura(A, prof=1):
    """Transcricao literal do algoritmo do slide. Conta chamadas e profundidade."""
    global chamadas, prof_max
    chamadas += 1
    prof_max = max(prof_max, prof)
    if A is None:                       # n = 0
        return -1
    he = fator_altura(A.e, prof + 1)
    hd = fator_altura(A.d, prof + 1)
    A_fb = he - hd                      # r.f <- he - hd
    return max(he, hd) + 1

def n_nos(A):
    return 0 if A is None else 1 + n_nos(A.e) + n_nos(A.d)

def cadeia(n):                          # arvore degenerada (so filho esquerdo)
    r = None
    for _ in range(n):
        r = No(r, None)
    return r

def balanceada(n):                      # o mais balanceada possivel
    if n == 0:
        return None
    ne = (n - 1) // 2
    return No(balanceada(ne), balanceada(n - 1 - ne))

def aleatoria(n, rnd):
    if n == 0:
        return None
    ne = rnd.randrange(n)
    return No(aleatoria(ne, rnd), aleatoria(n - 1 - ne, rnd))

print("\n  formato          n     chamadas   2n+1   profundidade max")
rnd = random.Random(20260831)
ok_chamadas = True
linhas = []
for nome, gera in [("cadeia", cadeia), ("balanceada", balanceada)]:
    for n in [0, 1, 2, 3, 7, 15, 100, 500]:
        A = gera(n)
        chamadas = 0; prof_max = 0
        fator_altura(A)
        assert n_nos(A) == n
        linhas.append((nome, n, chamadas, 2*n+1, prof_max))
        if chamadas != 2*n + 1:
            ok_chamadas = False
for i in range(12):                     # arvores aleatorias
    n = rnd.randrange(1, 220)
    A = aleatoria(n, rnd)
    chamadas = 0; prof_max = 0
    fator_altura(A)
    linhas.append(("aleatoria", n, chamadas, 2*n+1, prof_max))
    if chamadas != 2*n + 1:
        ok_chamadas = False
for nome, n, ch, esp, pm in linhas:
    marca = "" if ch == esp else "   <-- DIVERGE"
    print(f"  {nome:12s} {n:5d}   {ch:8d}  {esp:6d}   {pm:6d}{marca}")

checa("slide  numero de chamadas = 2n+1 para TODA arvore testada (cadeia, balanceada, 12 aleatorias)",
      ok_chamadas)

# a profundidade e o que muda
cad = [l for l in linhas if l[0] == "cadeia" and l[1] == 500][0]
bal = [l for l in linhas if l[0] == "balanceada" and l[1] == 500][0]
print(f"\n  n=500:  cadeia -> profundidade {cad[4]};  balanceada -> profundidade {bal[4]}")
print(f"          chamadas: {cad[2]} nos dois casos.")
checa("slide  o tempo (chamadas) NAO muda com o formato", cad[2] == bal[2])
checa("slide  a PROFUNDIDADE muda: cadeia ~ n, balanceada ~ lg n",
      cad[4] > 10 * bal[4] / 2 and bal[4] <= 2*math.log2(501) + 3,
      f"cadeia={cad[4]}  balanceada={bal[4]}  2*lg(501)+3={2*math.log2(501)+3:.1f}")

# a recorrencia balanceada pelo Teorema Mestre: T(n)=2T(n/2)+1 -> a=2,b=2,k=0,b^k=1,a>b^k -> Theta(n^log_2 2)=Theta(n)
print("\n  recorrencia balanceada T(n) = 2T(n/2) + 1:  a=2, b=2, k=0, b^k=1, a>b^k")
print("    -> Theta(n^(log_2 2)) = Theta(n^1) = Theta(n).  Mesma classe do caso cadeia.")
T = {0: 1}
for m in range(1, 15):
    T[m] = 2*T[m-1] + 1
print("    T(2^m)/2^m para m=1..14: " + ", ".join(f"{T[m]/2**m:.4f}" for m in range(1, 15)))
checa("slide  T(n)=2T(n/2)+1 tem T(n)/n limitado (Theta(n), nao Theta(n lg n))",
      all(1.0 <= T[m]/2**m <= 2.0 for m in range(1, 15)),
      "razao em [1,2] para m=1..14; se fosse Theta(n lg n) a razao cresceria como lg n")

print()
print("=" * 76)
print(("FALHAS (%d): " % len(FALHAS)) + "; ".join(FALHAS) if FALHAS
      else "Nenhuma falha. Formas fechadas, testemunhas e contagem do slide conferidas.")
print("=" * 76)


# ======================================================================
# ADENDO (rodada 3) - as testemunhas para c != 1, introduzidas por patch.
# Afirmacao do texto corrigido:
#   T_c(n) = a^m + c*(T_1(n) - a^m)
#   caso a = b^k :  c1 = c/lg b,  c2 = (1+c)/lg b,  n0 = b
#   caso a > b^k :  c1 = 1,       c2 = 1 + c*B,     n0 = 1   (A - B = 1 se preserva)
# ======================================================================
from fractions import Fraction as F

print()
print("=" * 76)
print("ADENDO - testemunhas para c != 1 (afirmacoes introduzidas por patch)")
print("=" * 76)

def T_c(a, b, k, c, m):
    """T(1)=1 ; T(b^i) = a*T(b^(i-1)) + c*(b^i)^k. Exato em Fraction."""
    t = F(1)
    for i in range(1, m + 1):
        t = a * t + F(c) * (b ** i) ** k
    return t

# (1) a identidade T_c = a^m + c*(T_1 - a^m)
print("\n(1) T_c(n) = a^m + c*(T_1(n) - a^m)")
ok = True
for (a, b, k) in [(2,3,0),(5,4,1),(7,7,1),(9,3,2),(8,2,3),(3,2,1),(2,2,2),(1,2,1),(4,3,2)]:
    for c in [F(1,4), F(1,2), F(1), F(2), F(7,3), F(10)]:
        for m in range(0, 9):
            esq = T_c(a, b, k, c, m)
            dir_ = a**m + c * (T_c(a, b, k, 1, m) - a**m)
            if esq != dir_:
                ok = False
                print(f"    divergencia a={a} b={b} k={k} c={c} m={m}: {esq} != {dir_}")
checa("adendo  identidade T_c = a^m + c*(T_1 - a^m)  (9 triplas x 6 valores de c x m=0..8)", ok)
print("    e T_c != c*T_1 em geral (o termo do caso base nao leva o c):")
for (a,b,k,c,m) in [(9,3,2,F(1,2),3), (2,3,0,F(2),4)]:
    print(f"      a={a} b={b} k={k} c={c} m={m}:  T_c={T_c(a,b,k,c,m)}   c*T_1={c*T_c(a,b,k,1,m)}")

# (2) caso a = b^k : c1 = c/lg b, c2 = (1+c)/lg b, n0 = b
print("\n(2) caso a = b^k :  c1 = c/lg b,  c2 = (1+c)/lg b,  n0 = b")
ok = True
for (a, b, k) in [(7,7,1),(9,3,2),(8,2,3),(4,2,2),(16,2,4),(25,5,2)]:
    for c in [0.25, 0.5, 1.0, 2.0, 7/3, 10.0]:
        c1, c2 = c/math.log2(b), (1+c)/math.log2(b)
        for m in range(1, 11):
            n = b**m
            g = (n**k) * math.log2(n)
            T = float(T_c(a, b, k, F(c).limit_denominator(10**6), m))
            if not (c1*g - 1e-9 <= T <= c2*g + 1e-9):
                ok = False
                print(f"    viola a={a} b={b} k={k} c={c} m={m}: {c1*g:.4f} <= {T:.4f} <= {c2*g:.4f}")
checa("adendo  a = b^k: c1 = c/lg b, c2 = (1+c)/lg b, n0 = b  (6 triplas x 6 c x m=1..10)", ok)
# confere em n = n0 = b EXATAMENTE, e mostra que a versao ANTIGA (reescalar por c) falha
print("    em n = n0 = b exatamente, e contraprova da afirmacao antiga (c2 = c*2/lg b):")
for (a,b,k,c) in [(9,3,2,0.5), (7,7,1,0.25), (8,2,3,0.5)]:
    n = b; g = (n**k)*math.log2(n)
    T = float(T_c(a,b,k,F(c).limit_denominator(10**6),1))
    c2_novo, c2_velho = (1+c)/math.log2(b), c*2/math.log2(b)
    print(f"      a={a} b={b} k={k} c={c}:  T({n})={T:g}   c2_novo*g={c2_novo*g:g}  "
          f"c2_velho*g={c2_velho*g:g}  ->  antigo {'FALHA' if T > c2_velho*g + 1e-9 else 'passa'}")
checa("adendo  a formula ANTIGA (reescalar c2 por c) e refutada para 0 < c < 1",
      float(T_c(9,3,2,F(1,2),1)) > (0.5*2/math.log2(3)) * (9*math.log2(3)) + 1e-9,
      "item (d) com c=1/2: T(3)=13,5 > 9,0")

# (3) caso a > b^k : c1 = 1, c2 = 1 + c*B, n0 = 1
print("\n(3) caso a > b^k :  c1 = 1,  c2 = 1 + c*B  com B = b^k/(a-b^k),  n0 = 1")
ok = True
for (a, b, k) in [(2,3,0),(5,4,1),(3,2,1),(4,3,1),(2,2,0),(9,2,2)]:
    B = F(b**k, a - b**k)
    for c in [F(1,4), F(1,2), F(1), F(2), F(10)]:
        c1, c2 = 1.0, float(1 + c*B)
        for m in range(0, 11):
            n = b**m
            g = n ** math.log(a, b)
            T = float(T_c(a, b, k, c, m))
            if not (c1*g - 1e-9 <= T <= c2*g + 1e-9):
                ok = False
                print(f"    viola a={a} b={b} k={k} c={c} m={m}: {c1*g:.4f} <= {T:.4f} <= {c2*g:.4f}")
checa("adendo  a > b^k: c1 = 1, c2 = 1 + c*B, n0 = 1  (6 triplas x 5 c x m=0..10)", ok)
print("    a identidade A - B = 1 se preserva com o c:  A_c = 1 + c*B,  B_c = c*B")
for (a,b,k,c) in [(2,3,0,F(1,2)), (5,4,1,F(2))]:
    B = F(b**k, a-b**k); Ac, Bc = 1 + c*B, c*B
    print(f"      a={a} b={b} k={k} c={c}:  B={B}  A_c={Ac}  B_c={Bc}  A_c-B_c={Ac-Bc}")
checa("adendo  A_c - B_c = 1 para todo c",
      all((1 + c*F(b**k, a-b**k)) - c*F(b**k, a-b**k) == 1
          for (a,b,k) in [(2,3,0),(5,4,1),(3,2,1)] for c in [F(1,4),F(1),F(7,3)]))

print()
print("=" * 76)
print(("ADENDO - FALHAS: " + "; ".join(FALHAS)) if FALHAS else "ADENDO - nenhuma falha.")
print("=" * 76)

import sys
sys.exit(1 if FALHAS else 0)
