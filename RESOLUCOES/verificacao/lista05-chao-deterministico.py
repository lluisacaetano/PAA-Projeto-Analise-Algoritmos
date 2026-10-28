# -*- coding: utf-8 -*-
"""
Lista 5 (PAA / IFMG Formiga, 2026-2) - chao deterministico.
Python puro, sem numpy/sympy. Roda antes de qualquer redacao de prova.

Q1: implementa os dois algoritmos de maximo (n-1 e n/2+n/2), confere que acertam,
    conta comparacoes, chamadas e profundidade de pilha, e mostra que o custo
    nao depende dos dados (pior caso = todo caso).
Q2: busca "galopante" (dobra o indice, depois busca binaria) num vetor sem fim;
    confere correcao para todo x, conta acessos e testa a cota 2*floor(lg m)+3;
    testa as testemunhas do o(n).
Q3: as tres recorrencias em aritmetica exata; formas fechadas; testemunhas; ordem.
Q4: 1/2 + ... + 1/2^n < 1 com Fraction; os dois passos indutivos.
Q5: os dez itens: identificacao (a, b, k, c), formas fechadas exatas, testemunhas
    nos itens aplicaveis e o comportamento real nos nao aplicaveis.
"""
import math
import random
import sys
from fractions import Fraction as F
from functools import lru_cache

sys.setrecursionlimit(20000)
FALHAS = []


def checa(rotulo, ok, detalhe=""):
    print(("  OK   " if ok else "  FALHA") + f"  {rotulo}" + (f"   {detalhe}" if detalhe else ""))
    if not ok:
        FALHAS.append(rotulo)


def floor_lg(n):
    """floor(log2 n) em aritmetica inteira (n >= 1)."""
    return n.bit_length() - 1


def titulo(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


# ----------------------------------------------------------------------
# QUESTAO 1 - maximo por divisao e conquista
# ----------------------------------------------------------------------
titulo("QUESTAO 1 - maximo: subproblema n-1  vs  dois subproblemas n/2")


class Cont:
    def __init__(self):
        self.comp = 0
        self.cham = 0
        self.prof = 0
        self.prof_max = 0


def max_a(A, n, c):
    """MaxA(A, n): maximo de A[1..n] (aqui A[0..n-1])."""
    c.cham += 1
    c.prof += 1
    c.prof_max = max(c.prof_max, c.prof)
    if n == 1:
        r = A[0]
    else:
        m = max_a(A, n - 1, c)
        c.comp += 1
        r = m if m >= A[n - 1] else A[n - 1]
    c.prof -= 1
    return r


def max_b(A, i, j, c):
    """MaxB(A, i, j): maximo de A[i..j], dividindo ao meio."""
    c.cham += 1
    c.prof += 1
    c.prof_max = max(c.prof_max, c.prof)
    if i == j:
        r = A[i]
    else:
        m = (i + j) // 2
        e = max_b(A, i, m, c)
        d = max_b(A, m + 1, j, c)
        c.comp += 1
        r = e if e >= d else d
    c.prof -= 1
    return r


random.seed(2026)
ok_corr = ok_comp = ok_cham = ok_prof = True
for n in list(range(1, 301)) + [512, 1000, 1023, 1024, 1025]:
    for _ in range(3):
        A = [random.uniform(-1e6, 1e6) for _ in range(n)]
        ca, cb = Cont(), Cont()
        ra, rb = max_a(A, n, ca), max_b(A, 0, n - 1, cb)
        if not (ra == rb == max(A)):
            ok_corr = False
        if not (ca.comp == cb.comp == n - 1):
            ok_comp = False
            print(f"    n={n}: comp a={ca.comp} b={cb.comp}")
        if not (ca.cham == n and cb.cham == 2 * n - 1):
            ok_cham = False
        # profundidade: n em (a); 1 + ceil(lg n) em (b)
        ceil_lg = (n - 1).bit_length()
        if not (ca.prof_max == n and cb.prof_max == 1 + ceil_lg):
            ok_prof = False
            print(f"    n={n}: prof a={ca.prof_max} b={cb.prof_max} esperado {n},{1+ceil_lg}")
for n in [1, 2, 3, 4]:
    A = list(range(n))
    ca, cb = Cont(), Cont()
    max_a(A, n, ca); max_b(A, 0, n - 1, cb)
    print(f"    n={n}: comparacoes a={ca.comp} b={cb.comp} | chamadas a={ca.cham} b={cb.cham}"
          f" | pilha a={ca.prof_max} b={cb.prof_max}")
checa("1  os dois algoritmos devolvem max(A) (n = 1..300 e potencias/vizinhas de 2)", ok_corr)
checa("1  comparacoes entre elementos = n - 1 nos DOIS", ok_comp)
checa("1  chamadas: n em (a), 2n - 1 em (b)", ok_cham)
checa("1  pilha: n em (a), 1 + ceil(lg n) em (b)", ok_prof)

# pior caso = todo caso: varre todas as permutacoes para n <= 7
from itertools import permutations
ok_indep = True
for n in range(1, 8):
    ja, jb = set(), set()
    for p in permutations(range(n)):
        ca, cb = Cont(), Cont()
        max_a(list(p), n, ca); max_b(list(p), 0, n - 1, cb)
        ja.add((ca.comp, ca.cham)); jb.add((cb.comp, cb.cham))
    if len(ja) != 1 or len(jb) != 1:
        ok_indep = False
checa("1  custo identico em TODAS as permutacoes, n = 1..7 (pior caso = todo caso)", ok_indep)

# modelo de custo: T_a(n) = T_a(n-1) + c, T_a(1) = d ; T_b(n) = T_b(ceil)+T_b(floor)+c, T_b(1)=d
ok_ta = ok_tb = True
for c_, d_ in [(1, 1), (3, 5), (7, 2), (F(1, 3), F(9, 4))]:
    ta = {1: d_}
    for n in range(2, 3000):
        ta[n] = ta[n - 1] + c_
        if ta[n] != d_ + c_ * (n - 1):
            ok_ta = False

    @lru_cache(None)
    def tb(n, c_=c_, d_=d_):
        if n == 1:
            return d_
        return tb((n + 1) // 2) + tb(n // 2) + c_
    for n in range(1, 3000):
        if tb(n) != d_ * n + c_ * (n - 1):
            ok_tb = False
checa("1  T_a(n) = d + c(n-1)  para todo n = 1..2999", ok_ta)
checa("1  T_b(n) = d*n + c(n-1) para todo n = 1..2999 (qualquer divisao ceil/floor)", ok_tb)

# ----------------------------------------------------------------------
# QUESTAO 2 - busca num vetor sem fim
# ----------------------------------------------------------------------
titulo("QUESTAO 2 - busca galopante (dobra, depois busca binaria)")

INF = float("inf")


class VetorSemFim:
    """A[1..m] inteiros crescentes, A[i] = INF para i > m. Conta acessos."""
    def __init__(self, vals, comprimento=None):
        self.v = vals
        self.n = comprimento          # None = infinito
        self.acessos = 0

    def __getitem__(self, i):
        assert i >= 1
        self.acessos += 1
        if self.n is not None and i > self.n:
            return INF                # a "mensagem de erro infinito" do enunciado
        return self.v[i - 1] if i <= len(self.v) else INF


def busca(A, x):
    i = 1
    while A[i] < x:                   # para quando A[i] >= x (INF >= x sempre)
        i = 2 * i
    lo = i // 2 + 1                   # i = 1  ->  lo = 1
    hi = i
    while lo <= hi:
        meio = (lo + hi) // 2
        v = A[meio]
        if v == x:
            return meio
        if v < x:
            lo = meio + 1
        else:
            hi = meio - 1
    return None


ok_corr = ok_cota = True
pior = {}
for m in range(0, 700):
    for estrito in (True, False):
        if estrito:
            vals = sorted(random.sample(range(-3 * m - 5, 3 * m + 5), m))
        else:
            vals = sorted(random.randint(-m - 2, m + 2) for _ in range(m))
        candidatos = set(vals) | {v + 1 for v in vals} | {v - 1 for v in vals} | {-10**9, 10**9, 0}
        for x in candidatos:
            for comp in (None, m, m + 3, 2 * m + 7):       # infinito, ou comprimento finito n >= m
                A = VetorSemFim(vals, comp)
                p = busca(A, x)
                presente = x in vals
                if presente:
                    if p is None or not (1 <= p <= m) or vals[p - 1] != x:
                        ok_corr = False
                else:
                    if p is not None:
                        ok_corr = False
                pior[m] = max(pior.get(m, 0), A.acessos)
                cota = 2 * floor_lg(m) + 3 if m >= 1 else 2
                if A.acessos > cota:
                    ok_cota = False
                    print(f"    m={m} x={x} acessos={A.acessos} > cota {cota}")
checa("2  devolve posicao com A[p] = x quando existe, None quando nao (m = 0..699, com e sem repeticao)", ok_corr)
checa("2  acessos <= 2*floor(lg m) + 3 (m >= 1); <= 2 para m = 0", ok_cota)
print("    pior numero de acessos observado vs. cota, alguns m:")
for m in [0, 1, 2, 3, 4, 5, 7, 8, 15, 16, 100, 255, 256, 511, 512, 699]:
    cota = 2 * floor_lg(m) + 3 if m >= 1 else 2
    print(f"      m={m:4d}  pior={pior[m]:3d}  cota={cota:3d}")
atinge = [m for m in range(1, 700) if pior[m] == 2 * floor_lg(m) + 3]
print(f"    a cota e atingida em {len(atinge)} valores de m em 1..699 (ex.: {atinge[:8]})")

# Lema: 2^j >= j^2 para j >= 4; logo floor(lg n) <= sqrt(n) para n >= 16
ok = all(2 ** j >= j * j for j in range(4, 2000))
checa("2  2^j >= j^2 para j = 4..1999", ok)
print("    e falha em j = 3:", 2 ** 3, "<", 9)
ok = all(floor_lg(n) ** 2 <= n for n in range(16, 300000))
checa("2  floor(lg n)^2 <= n para n = 16..299999", ok)
print("    valores pequenos com floor(lg n)^2 > n:", [n for n in range(1, 16) if floor_lg(n) ** 2 > n])
# o(n): f(n) = 2 floor(lg n) + 3 <= 5 sqrt(n) para n >= 16  ->  f(n) < c n para n > 25/c^2
ok = all(2 * floor_lg(n) + 3 <= 5 * math.isqrt(n) for n in range(16, 300000))
checa("2  2 floor(lg n) + 3 <= 5 isqrt(n) <= 5 sqrt(n) para n = 16..299999", ok)
ok_on = True
for c in [F(1), F(1, 2), F(1, 10), F(1, 100), F(1, 1000)]:
    n0 = max(16, int(25 / (c * c)) + 1)
    for n in list(range(n0, n0 + 5000)) + [n0 * 10, n0 * 1000]:
        if not (2 * floor_lg(n) + 3 < c * n):
            ok_on = False
            print(f"    c={c} n0={n0} falha em n={n}")
    print(f"    c = {str(c):>6}: n0 = max(16, floor(25/c^2)+1) = {n0};  f(n0) = {2*floor_lg(n0)+3}  <  c*n0 = {float(c*n0):.2f}")
checa("2  para cada c testado, f(n) < c*n para todo n >= n0 testado", ok_on)

# ----------------------------------------------------------------------
# QUESTAO 3 - A, B, C
# ----------------------------------------------------------------------
titulo("QUESTAO 3 - A: 5T(n/2)+n  B: 2T(n-1)+1  C: 9T(n/3)+n^2  (T(1)=1)")
lg5, lg3 = math.log2(5), math.log2(3)
TA = {0: F(1)}
for j in range(1, 40):
    TA[j] = 5 * TA[j - 1] + 2 ** j
ok = all(TA[j] == F(5, 3) * 5 ** j - F(2, 3) * 2 ** j for j in range(40))
checa("3  T_A(2^j) = (5/3) n^(lg 5) - (2/3) n", ok)
ok = all(5 ** j <= TA[j] <= F(5, 3) * 5 ** j for j in range(40))
checa("3  A: c1 = 1, c2 = 5/3, n0 = 1  (n^(lg5) = 5^j)", ok, f"em n=1: 1 <= {TA[0]} <= 5/3")
TB = {1: 1}
for n in range(2, 300):
    TB[n] = 2 * TB[n - 1] + 1
ok = all(TB[n] == 2 ** n - 1 for n in range(1, 300))
checa("3  T_B(n) = 2^n - 1", ok)
ok = all(F(1, 2) * 2 ** n <= TB[n] <= 2 ** n for n in range(1, 300))
checa("3  B: c1 = 1/2, c2 = 1, n0 = 1", ok, f"em n=1: 1 <= {TB[1]} <= 2")
TC = {0: 1}
for j in range(1, 40):
    TC[j] = 9 * TC[j - 1] + 9 ** j
ok = all(TC[j] == 9 ** j * (j + 1) for j in range(40))
checa("3  T_C(3^j) = n^2 (log_3 n + 1)", ok)
# c1 = 1/lg3, c2 = 2/lg3, n0 = 3 : n^2 lg n = 9^j * j*lg3  ->  c1*... = 9^j j ; c2*... = 2*9^j j
ok = all(9 ** j * j <= TC[j] <= 2 * 9 ** j * j for j in range(1, 40))
checa("3  C: c1 = 1/lg3, c2 = 2/lg3, n0 = 3  (em n=3: 9 <= 18 <= 18)", ok)
print("    razao T_C / T_A em n = 2^j nao e potencia de 3; compara-se as classes:")
for n in [2 ** 4, 2 ** 10, 2 ** 20, 2 ** 40, 2 ** 80]:
    r = (n ** 2 * math.log2(n)) / (n ** lg5)
    print(f"      n = 2^{floor_lg(n):2d}:  n^2 lg n / n^(lg 5) = {r:.4g}")
print("    n^(lg5) / 2^n:", ", ".join(f"n={n}: {n**lg5/2**n:.3g}" for n in [10, 20, 30, 40, 60]))
print(f"    expoente de A: lg 5 = {lg5:.6f} > 2 ; logo n^2 lg n = o(n^(lg5))  (lg n = o(n^0.3219))")

# ----------------------------------------------------------------------
# QUESTAO 4 - 1/2 + ... + 1/2^n < 1
# ----------------------------------------------------------------------
titulo("QUESTAO 4 - soma geometrica 1/2 + ... + 1/2^n < 1")
ok_fech = ok_lt = ok_passo = True
S = F(0)
for n in range(1, 400):
    S += F(1, 2 ** n)
    if S != 1 - F(1, 2 ** n):
        ok_fech = False
    if not S < 1:
        ok_lt = False
    # passo "tira o primeiro termo": S(n+1) = 1/2 + S(n)/2
    Sn1 = S + F(1, 2 ** (n + 1))
    if Sn1 != F(1, 2) + S / 2:
        ok_passo = False
checa("4  S(n) = 1 - 1/2^n para n = 1..399", ok_fech)
checa("4  S(n) < 1 para n = 1..399", ok_lt)
checa("4  S(n+1) = 1/2 + S(n)/2 para n = 1..399", ok_passo)
print("    n=1: S=1/2 ; n=2: S=3/4 ; n=3: S=7/8")
# a hipotese fraca 'S(n) < 1' nao basta pelo ultimo termo: s < 1 com s + 1/2^(n+1) >= 1
n = 3
s = 1 - F(1, 2 ** (n + 2))
print(f"    passo ingenuo: s = {s} < 1 mas s + 1/2^{n+1} = {s + F(1, 2**(n+1))} >= 1  -> o passo 'soma o ultimo' nao fecha so com S(n) < 1")

# ----------------------------------------------------------------------
# QUESTAO 5 - Teorema Mestre (Brassard & Bratley)
# ----------------------------------------------------------------------
titulo("QUESTAO 5 - dez recorrencias")


def serie(a, b, f, t, J):
    """T(b^0) = t ; T(b^j) = a T(b^(j-1)) + f(b^j), aritmetica exata."""
    T = [F(t)]
    for j in range(1, J + 1):
        T.append(a * T[-1] + f(F(b) ** j))
    return T


# (a) T(n) = T(n/3) + 1 : a=1 b=3 k=0 c=1, a = b^k  -> Theta(lg n)
T = serie(1, 3, lambda n: 1, 1, 60)
checa("5(a) T(3^j) = j + 1 = log_3 n + 1", all(T[j] == j + 1 for j in range(61)))
# testemunhas c1 = 1/lg3, c2 = 2/lg3, n0 = 3 :  lg n = j lg3 -> c1 lg n = j, c2 lg n = 2j
checa("5(a) c1=1/lg3, c2=2/lg3, n0=3: j <= j+1 <= 2j para j >= 1", all(j <= T[j] <= 2 * j for j in range(1, 61)),
      "em n=3: 1 <= 2 <= 2")
checa("5(a) n0 = 1 NAO serve (lg 1 = 0 e T(1) = 1)", not (T[0] <= 0))
checa("5(a) T nao decrescente nas potencias de 3", all(T[j] < T[j + 1] for j in range(60)))

# (b) 2T(n/2) + n lg n : fora da forma c n^k. Fora do teorema: n(1 + lg n (lg n + 1)/2)
T = serie(2, 2, lambda n: n * (n.numerator.bit_length() - 1), 1, 60)
checa("5(b) [fora do teorema] T(2^j) = n (1 + j(j+1)/2)", all(T[j] == 2 ** j * (1 + F(j * (j + 1), 2)) for j in range(61)))
checa("5(b) [fora] c1=1/2, c2=2, n0=2 contra n lg^2 n", all(F(1, 2) * 2 ** j * j * j <= T[j] <= 2 * 2 ** j * j * j for j in range(1, 61)),
      "em n=2: 1 <= 4 <= 4")
# e nao e da forma c n^k: T(n)/(n lg n) diverge e T/(n^(1+e)) -> 0
print("    (b) f(n)/n = lg n nao e constante; f(n)/n^(1.1) em n=2^10,2^40,2^200:",
      ", ".join(f"{j * 2**j / 2**(1.1*j):.3g}" for j in [10, 40, 200]))

# (c) T(2n/3) + n : b = 3/2 nao e natural. Fora: T(n) = T(floor(2n/3)) + n, T(1) = 1
@lru_cache(None)
def Tc(n):
    return 1 if n <= 1 else Tc((2 * n) // 3) + n
checa("5(c) [fora, com piso] n <= T(n) <= 3n para n = 1..200000",
      all(n <= Tc(n) <= 3 * n for n in range(1, 200001)))

# (d) 5T(n/4) - n : c = -1 < 0.  T(4^j) = (t-4) 5^j + 4*4^j
ok = True
for t in [F(1), F(2), F(4), F(5), F(100), F(7, 2)]:
    T = serie(5, 4, lambda n: -n, t, 40)
    if not all(T[j] == (t - 4) * 5 ** j + 4 * 4 ** j for j in range(41)):
        ok = False
checa("5(d) T(4^j) = (T(1) - 4) n^(log_4 5) + 4n  (varios T(1))", ok)
T = serie(5, 4, lambda n: -n, 1, 10)
print("    (d) com T(1) = 1:", [str(x) for x in T[:5]], "-> negativo ja em n = 16")
checa("5(d) com T(1)=1 fica negativo (T(16) = -11)", T[2] == -11 and all(T[j] < 0 for j in range(2, 11)))

# (e) T(n-1) + 3 : 3n - 2
Te = [None, 1]
for n in range(2, 500):
    Te.append(Te[-1] + 3)
checa("5(e) [fora] T(n) = 3n - 2", all(Te[n] == 3 * n - 2 for n in range(1, 500)))

# (f) T(n/3) + 0 : T constante
T = serie(1, 3, lambda n: 0, 1, 50)
checa("5(f) T(3^j) = T(1) = 1 para todo j (Theta(1), e NAO Theta(lg n))", all(x == 1 for x in T))

# (g) 5T(n/4) - n^2 : T(4^j) = (t + 16/11) 5^j - (16/11) 16^j
ok = True
primeiro_neg = {}
for t in [F(1), F(10), F(1000), F(10 ** 6)]:
    T = serie(5, 4, lambda n: -n * n, t, 60)
    if not all(T[j] == (t + F(16, 11)) * 5 ** j - F(16, 11) * 16 ** j for j in range(61)):
        ok = False
    primeiro_neg[t] = next(j for j in range(61) if T[j] < 0)
checa("5(g) T(4^j) = (T(1) + 16/11) n^(log_4 5) - (16/11) n^2", ok)
print("    (g) primeiro j com T(4^j) < 0, por T(1):", {str(k): v for k, v in primeiro_neg.items()})

# (h) T(2n/4) + n = T(n/2) + n : a=1 b=2 k=1 ; T = 2n - 1
T = serie(1, 2, lambda n: n, 1, 60)
checa("5(h) T(2^j) = 2n - 1", all(T[j] == 2 * 2 ** j - 1 for j in range(61)))
checa("5(h) c1=1, c2=2, n0=1", all(2 ** j <= T[j] <= 2 * 2 ** j for j in range(61)), "em n=1: 1 <= 1 <= 2")

# (i) (3/2) T(n/4) - n^2 : a = 3/2 nao natural, c < 0.
ok = True
for t in [F(1), F(1000)]:
    T = serie(F(3, 2), 4, lambda n: -n * n, t, 40)
    if not all(T[j] == (t + F(32, 29)) * F(3, 2) ** j - F(32, 29) * 16 ** j for j in range(41)):
        ok = False
checa("5(i) T(4^j) = (T(1) + 32/29)(3/2)^j - (32/29) n^2", ok)
T = serie(F(3, 2), 4, lambda n: -n * n, 1, 3)
print("    (i) com T(1)=1:", [str(x) for x in T])

# (j) 3T(n/2) + n : a=3 b=2 k=1, a > b^k ; T = 3 n^(lg 3) - 2n
T = serie(3, 2, lambda n: n, 1, 60)
checa("5(j) T(2^j) = 3 n^(lg3) - 2n", all(T[j] == 3 * 3 ** j - 2 * 2 ** j for j in range(61)))
checa("5(j) c1=1, c2=3, n0=1", all(3 ** j <= T[j] <= 3 * 3 ** j for j in range(61)), "em n=1: 1 <= 1 <= 3")

# caso base generico T(1) = t nos itens aplicaveis
ok = True
for t in [F(1), F(1, 3), F(2), F(7), F(1000)]:
    Ta = serie(1, 3, lambda n: 1, t, 40)
    Th = serie(1, 2, lambda n: n, t, 40)
    Tj = serie(3, 2, lambda n: n, t, 40)
    if not all(Ta[j] == j + t for j in range(41)):
        ok = False
    if not all(Th[j] == 2 * 2 ** j - 2 + t for j in range(41)):
        ok = False
    if not all(Tj[j] == (t + 2) * 3 ** j - 2 * 2 ** j for j in range(41)):
        ok = False
checa("5    T(1)=t: (a) log_3 n + t ; (h) 2n - 2 + t ; (j) (t+2) n^(lg3) - 2n", ok)
# (b) nao e c n^k: n=2 e n=4 forcam k=2, c=1/2; n=8 refuta
checa("5(b) n lg n = c n^k em n=2,4 forca (c,k)=(1/2,2), e n=8 refuta (32 != 24)",
      F(1, 2) * 2 ** 2 == 2 and F(1, 2) * 4 ** 2 == 8 and F(1, 2) * 8 ** 2 == 32 and 8 * 3 == 24)

# Identificacao pedida pelo teorema, item a item
print()
print("    item | a    | b    | f(n)      | forma c n^k? | a,b naturais? | veredito")
tab = [
    ("(a)", "1", "3", "1", "sim c=1,k=0", "sim", "APLICA: a = b^k = 1 -> Theta(lg n)"),
    ("(b)", "2", "2", "n lg n", "NAO", "sim", "nao aplica"),
    ("(c)", "1", "3/2", "n", "sim", "NAO (b)", "nao aplica"),
    ("(d)", "5", "4", "-n", "NAO (c<0)", "sim", "nao aplica"),
    ("(e)", "-", "-", "3", "-", "nao e aT(n/b)", "nao aplica"),
    ("(f)", "1", "3", "0", "NAO (c=0)", "sim", "nao aplica"),
    ("(g)", "5", "4", "-n^2", "NAO (c<0)", "sim", "nao aplica"),
    ("(h)", "1", "2", "n", "sim c=1,k=1", "sim", "APLICA: a=1 < b^k=2 -> Theta(n)"),
    ("(i)", "3/2", "4", "-n^2", "NAO (c<0)", "NAO (a)", "nao aplica"),
    ("(j)", "3", "2", "n", "sim c=1,k=1", "sim", "APLICA: a=3 > b^k=2 -> Theta(n^lg3)"),
]
for r in tab:
    print("    " + " | ".join(f"{x:<12}" for x in r))

# ----------------------------------------------------------------------
# RODADA 2 - conferencias acrescentadas depois da verificacao adversarial
# ----------------------------------------------------------------------
titulo("RODADA 2 - o que as correcoes passaram a afirmar")

# Q1: modelo de custo por linha executada (base: 1 linha; n >= 2: linhas 1-3 em MaxA,
# 1-5 em MaxB, mais a linha do 'senao' quando tomado). Pior caso = vetor estritamente crescente.
def linhas_a(A):
    tot, m = 1, A[0]                        # chamada de tamanho 1: linha 1
    for k in range(1, len(A)):
        tot += 3                            # linhas 1, 2, 3
        if not (m >= A[k]):
            tot += 1                        # linha 4
            m = A[k]
    return tot


def linhas_b(A, i, j):
    if i == j:
        return 1, A[i]
    q = (i + j) // 2
    ce, e = linhas_b(A, i, q)
    cd, d = linhas_b(A, q + 1, j)
    tot = ce + cd + 5                       # linhas 1-5
    if e >= d:
        return tot, e
    return tot + 1, d                       # linha 6


ok_a = ok_b = True
for n in range(1, 8):
    ca = [linhas_a(list(p)) for p in permutations(range(n))]
    cb = [linhas_b(list(p), 0, n - 1)[0] for p in permutations(range(n))]
    cresc = list(range(n))
    if not (max(ca) == linhas_a(cresc) == 1 + 4 * (n - 1) and min(ca) == 1 + 3 * (n - 1)):
        ok_a = False
    if not (max(cb) == linhas_b(cresc, 0, n - 1)[0] == n + 6 * (n - 1) and min(cb) == n + 5 * (n - 1)):
        ok_b = False
    if n in (2, 4, 6):
        print(f"    n={n}: MaxA linhas min={min(ca)} max={max(ca)} | MaxB linhas min={min(cb)} max={max(cb)}")
checa("1  MaxA: pior caso = vetor crescente = d + c''(n-1) (d=1, c''=4); melhor = d + c'(n-1) (c'=3)", ok_a)
checa("1  MaxB: pior caso = vetor crescente = d n + c''(n-1) (d=1, c''=6); melhor = d n + c'(n-1) (c'=5)", ok_b)
ok = all(math.log2(n) <= 1 + (n - 1).bit_length() <= 2 * math.log2(n) for n in range(2, 10 ** 6))
checa("1  lg n <= 1 + ceil(lg n) <= 2 lg n para n = 2..999999 (pilha de MaxB)", ok)

# Q2: cota inferior do pior caso (x = A[m] + 1) e testemunhas de Theta(lg m)
ok_inf = ok_w = True
for m in range(1, 3000):
    vals = list(range(1, m + 1))
    A = VetorSemFim(vals)
    busca(A, m + 1)
    if A.acessos < floor_lg(m) + 2:
        ok_inf = False
for m in range(2, 10 ** 6):
    L = floor_lg(m)
    if not (math.log2(m) <= L + 2 and 2 * L + 3 <= 5 * math.log2(m)):
        ok_w = False
        break
checa("2  x = A[m]+1 forca >= floor(lg m) + 2 acessos (m = 1..2999)", ok_inf)
checa("2  lg m <= floor(lg m)+2  e  2 floor(lg m)+3 <= 5 lg m  (m = 2..999999)", ok_w)
checa("2  W(2) = 4 (pior caso observado em m = 2)", pior[2] == 4)
checa("2  f(0)=2 <= f(1)=3 e f nao decrescente em m = 1..10^5",
      all(2 * floor_lg(m) + 3 <= 2 * floor_lg(m + 1) + 3 for m in range(1, 10 ** 5)))

# Q3: formas fechadas e testemunhas para t, c quaisquer
ok = True
for t in [F(1), F(1, 3), F(7)]:
    for c in [F(1), F(1, 10), F(10)]:
        TA = [t]
        TC = [t]
        for j in range(1, 30):
            TA.append(5 * TA[-1] + c * 2 ** j)
            TC.append(9 * TC[-1] + c * 9 ** j)
        for j in range(30):
            if TA[j] != (t + 2 * c / 3) * 5 ** j - (2 * c / 3) * 2 ** j:
                ok = False
            if not (t * 5 ** j <= TA[j] <= (t + 2 * c / 3) * 5 ** j):
                ok = False
            if TC[j] != 9 ** j * (t + c * j):
                ok = False
            # c1 = c/lg3, c2 = (t+c)/lg3 contra n^2 lg n = 9^j * j * lg3
            if j >= 1 and not (c * 9 ** j * j <= TC[j] <= (t + c) * 9 ** j * j):
                ok = False
        if not (all(TA[j] < TA[j + 1] for j in range(29)) and all(TC[j] < TC[j + 1] for j in range(29))):
            ok = False
checa("3  A: (t+2c/3) n^lg5 - (2c/3) n, c1=t, c2=t+2c/3 ; C: n^2 (t + c log3 n), c1=c/lg3, c2=(t+c)/lg3", ok)

# Q5: caso base T(n) = c para n <= n0 (b^m0 = maior potencia de b <= n0)
ok = True
for m0 in range(0, 4):
    for c in [F(1), F(10), F(17), F(1000)]:
        # (d) 5T(n/4) - n
        Td = {m0: c}
        for m in range(m0 + 1, m0 + 40):
            Td[m] = 5 * Td[m - 1] - 4 ** m
        A_ = (c - 4 * 4 ** m0) / F(5) ** m0
        if not all(Td[m] == A_ * 5 ** m + 4 * 4 ** m for m in Td):
            ok = False
        neg = any(Td[m] < 0 for m in Td)
        if (c > 4 * 4 ** m0) == neg and c != 4 * 4 ** m0:
            ok = False
        # (a), (h), (j)
        Ta, Th, Tj = {m0: c}, {m0: c}, {m0: c}
        for m in range(m0 + 1, m0 + 40):
            Ta[m] = Ta[m - 1] + 1
            Th[m] = Th[m - 1] + 2 ** m
            Tj[m] = 3 * Tj[m - 1] + 2 ** m
        if not all(Ta[m] == c + (m - m0) for m in Ta):
            ok = False
        if not all(Th[m] == 2 * 2 ** m + c - 2 ** (m0 + 1) for m in Th):
            ok = False
        if not all(Tj[m] == (c + 2 * 2 ** m0) / F(3) ** m0 * 3 ** m - 2 * 2 ** m for m in Tj):
            ok = False
checa("5  base T(n)=c, n<=n0: (d) limiar c > 4*4^m0 ; (a) c+(m-m0) ; (h) 2n+c-2^(m0+1) ; (j) coef. (c+2*2^m0)/3^m0", ok)
Td = {1: F(10)}
for m in range(2, 8):
    Td[m] = 5 * Td[m - 1] - 4 ** m
checa("5(d) exemplo do texto: n0 = 4, C = 10 -> T(4^6) < 0", Td[6] < 0, f"T(4^6) = {Td[6]}")

# (g), (i): com T(n) = C para n <= n0, so muda o coeficiente do termo homogeneo;
# o de n^2 (-16/11 em (g), -32/29 em (i)) nao depende do caso base, e T -> -inf.
ok = True
for m0 in range(0, 4):
    for C in [F(1), F(10), F(10 ** 9)]:
        Tg, Ti = {m0: C}, {m0: C}
        for m in range(m0 + 1, m0 + 70):
            Tg[m] = 5 * Tg[m - 1] - 16 ** m
            Ti[m] = F(3, 2) * Ti[m - 1] - 16 ** m
        alfa_g = (C + F(16, 11) * 16 ** m0) / F(5) ** m0
        alfa_i = (C + F(32, 29) * 16 ** m0) / F(3, 2) ** m0
        if not all(Tg[m] == alfa_g * 5 ** m - F(16, 11) * 16 ** m for m in Tg):
            ok = False
        if not all(Ti[m] == alfa_i * F(3, 2) ** m - F(32, 29) * 16 ** m for m in Ti):
            ok = False
        if not (Tg[m0 + 69] < 0 and Ti[m0 + 69] < 0):
            ok = False
checa("5(g)(i) base T(n)=C: coeficiente de n^2 fixo (-16/11, -32/29) e T negativa no fim", ok)

print()
print("=" * 72)
if FALHAS:
    print(f"FALHAS ({len(FALHAS)}): " + "; ".join(FALHAS))
else:
    print("Nenhuma falha. Chao deterministico consistente.")
print("=" * 72)
sys.exit(1 if FALHAS else 0)
