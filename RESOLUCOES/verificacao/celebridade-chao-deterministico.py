# -*- coding: utf-8 -*-
"""
Problema da celebridade (slides MC458/UNICAMP, Exemplo 4) - chao deterministico.
Python puro, sem biblioteca. Roda da raiz do projeto.

Este script ja derrubou TRES suposicoes minhas na primeira versao:
  - eu achava que a "matriz sem celebridade nenhuma" era o pior caso da 1a
    tentativa; nao e -- ela e o MELHOR (a verificacao aborta no primeiro j);
  - eu achava que o algoritmo do slide custa sempre 3(n-1); nao custa -- o custo
    varia com a matriz, entre n+1 e 3(n-1);
  - e portanto que o custo nao dependia da matriz. Depende.
Os numeros abaixo sao os corretos, todos medidos.
"""
import sys, random
from itertools import product

FALHAS = []
def checa(rot, ok, det=""):
    print(("  OK   " if ok else "  FALHA") + f"  {rot}" + (f"   {det}" if det else ""))
    if not ok: FALHAS.append(rot)

def celebridades(M):
    """Forca bruta pela definicao. M[i][j] = 1  <=>  i conhece j."""
    n = len(M)
    return [k for k in range(n)
            if all(M[i][k] == 1 for i in range(n) if i != k)
            and all(M[k][j] == 0 for j in range(n) if j != k)]

def matrizes(n):
    """Todas as matrizes n x n com diagonal irrelevante fixada em 0."""
    fora = [(i, j) for i in range(n) for j in range(n) if i != j]
    for bits in product([0, 1], repeat=len(fora)):
        M = [[0]*n for _ in range(n)]
        for (i, j), b in zip(fora, bits): M[i][j] = b
        yield M

# ══════════════════ 1. no maximo uma celebridade ══════════════════
print("=" * 76)
print("1. Existe no maximo uma celebridade?")
print("=" * 76)
mais, total = 0, 0
for n in range(1, 5):
    for M in matrizes(n):
        total += 1
        if len(celebridades(M)) > 1: mais += 1
checa("nenhuma matriz com duas ou mais celebridades", mais == 0,
      f"{total} matrizes exaustivas (n=1..4)")
print("  razao: se k e k' fossem ambas celebridades e k != k', entao k' e conhecida")
print("         por todos, logo M[k][k'] = 1; mas k nao conhece ninguem, logo")
print("         M[k][k'] = 0. Contradicao.")

# ══════════════════ 2. solucao ingenua ══════════════════
print()
print("=" * 76)
print("2. A solucao ingenua do slide custa 2n(n-1)?")
print("=" * 76)
def ingenua(M):
    n = len(M); ac = 0
    for k in range(n):
        for i in range(n):
            if i != k: ac += 1          # coluna k
        for j in range(n):
            if j != k: ac += 1          # linha k
    return ac
print("    n   medido   2n(n-1)")
ok = True
for n in [1, 2, 3, 5, 10, 50, 200]:
    ac = ingenua([[0]*n for _ in range(n)])
    print(f"  {n:3d}   {ac:6d}   {2*n*(n-1):7d}")
    if ac != 2*n*(n-1): ok = False
checa("ingenua = 2n(n-1) acessos, exatamente", ok)

# ══════════════════ 3. a 1a tentativa (remover a pessoa n) ══════════════════
print()
print("=" * 76)
print("3. A 1a tentativa e quadratica? Qual o pior caso, de verdade?")
print("=" * 76)
def tentativa1(M):
    """Remove SEMPRE a pessoa n. Conta acessos a M."""
    n = len(M); cont = [0]
    def rec(S):
        if len(S) == 1: return S[0]
        ult, Sl = S[-1], S[:-1]
        k = rec(Sl)
        if k is not None:                                  # caso 1: 2 acessos
            cont[0] += 2
            if M[ult][k] == 1 and M[k][ult] == 0: return k
        for j in Sl:                                       # caso 2: varre linha e coluna
            cont[0] += 2
            if not (M[ult][j] == 0 and M[j][ult] == 1): return None
        return ult
    return rec(list(range(n))), cont[0]

print("  ARMADILHA: a matriz 'todo mundo conhece todo mundo' NAO e o pior caso --")
print("  o laco do caso 2 aborta no primeiro j. E o MELHOR caso.")
for n in [8, 16, 32]:
    M = [[1]*n for _ in range(n)]
    for i in range(n): M[i][i] = 0
    print(f"    n={n:3d}: sem celebridade nenhuma -> {tentativa1(M)[1]:4d} acessos (linear!)")

print("\n  pior caso real, por busca exaustiva:")
exaust = {}
for n in range(2, 6):
    pior = max(tentativa1(M)[1] for M in matrizes(n))
    exaust[n] = pior
    print(f"    n={n}: custo maximo sobre TODAS as {2**(n*n-n)} matrizes = {pior}"
          f"    n^2+n-2 = {n*n+n-2}")
checa("pior caso da 1a tentativa = n^2 + n - 2 (exaustivo, n=2..5)",
      all(exaust[n] == n*n+n-2 for n in exaust))

def ordem_total(n):
    """M[i][j] = 1 se j > i. Atinge o pior caso: a verificacao do caso 2 percorre
    quase toda a lista antes de falhar, em todo nivel da recursao."""
    return [[1 if j > i else 0 for j in range(n)] for i in range(n)]
print("\n  a familia que atinge o pior caso (M[i][j] = 1 se j > i), em n maiores:")
print("    n   medido   n^2+n-2")
ok = True
for n in range(2, 15):
    c = tentativa1(ordem_total(n))[1]
    if n <= 5: print(f"  {n:4d}   {c:6d}   {n*n+n-2:7d}   (bate com o exaustivo: {exaust[n]})")
    elif n % 3 == 0: print(f"  {n:4d}   {c:6d}   {n*n+n-2:7d}")
    if c != n*n+n-2: ok = False
checa("a familia atinge n^2+n-2 para n=2..14", ok)
print("  -> T(n) = T(n-1) + Theta(n)  =>  Theta(n^2).")
print("     A causa: remove-se uma pessoa ARBITRARIA, sobre a qual nada se sabe;")
print("     verificar se ela e celebridade custa varrer linha e coluna, Theta(n).")

# ══════════════════ 4. o algoritmo do slide ══════════════════
print()
print("=" * 76)
print("4. O algoritmo do slide: correto? quanto custa?")
print("=" * 76)
def celebridade(M):
    """Transcricao literal do pseudocodigo. Separa acessos de ELIMINACAO
    (linha 4) dos de VERIFICACAO (linha 8)."""
    n = len(M); elim, ver = [0], [0]
    def rec(S):
        if len(S) == 1: return S[0]                 # linha 1
        i, j = S[0], S[1]                           # linha 3
        elim[0] += 1                                # linha 4: UM acesso
        s = i if M[i][j] == 1 else j
        k = rec([x for x in S if x != s])           # linhas 5-6
        if k is not None:                           # linha 7
            ver[0] += 2                             # linha 8: DOIS acessos
            if M[s][k] != 1 or M[k][s] != 0: k = None
        return k
    return rec(list(range(n))), elim[0], ver[0]

print("\n  correcao, exaustiva:")
ok = True
for n in range(1, 6):
    erros = sum(1 for M in matrizes(n)
                if ([] if celebridade(M)[0] is None else [celebridade(M)[0]]) != celebridades(M))
    tot = 2**(n*n-n)
    print(f"    n={n}: {tot:8d} matrizes, {erros} discordancias da definicao")
    if erros: ok = False
checa("algoritmo do slide correto para TODA matriz com n <= 5", ok)

rnd = random.Random(20260831); erros = 0
for _ in range(400):
    n = rnd.randrange(1, 10)
    M = [[rnd.randrange(2) for _ in range(n)] for _ in range(n)]
    for i in range(n): M[i][i] = 0
    if rnd.random() < 0.5:
        c = rnd.randrange(n)
        for i in range(n):
            if i != c: M[i][c] = 1; M[c][i] = 0
    k = celebridade(M)[0]
    if ([] if k is None else [k]) != celebridades(M): erros += 1
checa("correto em 400 matrizes aleatorias (n<=9, metade com celebridade plantada)", erros == 0)

print("\n  CUSTO -- e aqui esta a sutileza que eu tinha errado:")
print("  a linha 7 ('se k > 0 entao') pula a verificacao depois que o candidato")
print("  ja foi descartado. Entao o custo DEPENDE da matriz.")
print("    n   minimo   maximo   3(n-1)   n+1")
ok_max = True
for n in range(2, 6):
    custos = set()
    for M in matrizes(n):
        _, e, v = celebridade(M); custos.add(e+v)
    print(f"  {n:3d}   {min(custos):6d}   {max(custos):6d}   {3*(n-1):6d}   {n+1:3d}")
    if max(custos) != 3*(n-1) or min(custos) != n+1: ok_max = False
checa("custo varia entre n+1 e 3(n-1); o maximo e 3(n-1)", ok_max)

print("\n  e quando EXISTE celebridade, o custo e sempre o maximo?")
ok = True
for n in range(2, 6):
    com = {celebridade(M)[1] + celebridade(M)[2] for M in matrizes(n) if celebridades(M)}
    print(f"    n={n}: custos observados quando ha celebridade = {sorted(com)}   3(n-1) = {3*(n-1)}")
    if com != {3*(n-1)}: ok = False
checa("havendo celebridade, o custo e EXATAMENTE 3(n-1) = (n-1) eliminacoes + 2(n-1) verificacoes", ok)

print("\n  os dois lados da conta, na matriz com celebridade:")
print("    n   elim   verif   total   3(n-1)")
for n in [2, 3, 5, 10, 50, 200]:
    M = [[0]*n for _ in range(n)]
    for i in range(n):
        if i != 0: M[i][0] = 1        # pessoa 0 e celebridade
    _, e, v = celebridade(M)
    print(f"  {n:3d}   {e:4d}   {v:5d}   {e+v:5d}   {3*(n-1):6d}")

print("\n  comparacao final, em acessos a M:")
print("     n   ingenua 2n(n-1)   1a tentativa (pior) n^2+n-2   slide (pior) 3(n-1)")
for n in [10, 100, 1000, 10000]:
    print(f"  {n:5d}   {2*n*(n-1):16d}   {n*n+n-2:27d}   {3*(n-1):19d}")

print()
print("=" * 76)
print(("FALHAS ate aqui: " + "; ".join(FALHAS)) if FALHAS else
      "Sem falhas ate aqui. Segue o adendo.")
print("=" * 76)


# ══════════════════ 5. ADENDO — as tres afirmacoes que o solver declarou
#                      como NAO medidas. Meco agora.
# ══════════════════
print()
print("=" * 76)
print("5. ADENDO: o que o solver marcou como nao conferido")
print("=" * 76)

# (i) a variante ingenua COM aborto antecipado custa (n-1)(n+4)/2 na ordem total?
def ingenua_aborto(M):
    """Varre linha antes de coluna, j crescente, e para no primeiro elemento violado."""
    n = len(M); ac = 0
    for k in range(n):
        ok = True
        for j in range(n):                       # linha k: tem de ser toda 0
            if j == k: continue
            ac += 1
            if M[k][j] != 0: ok = False; break
        if not ok: continue
        for i in range(n):                       # coluna k: tem de ser toda 1
            if i == k: continue
            ac += 1
            if M[i][k] != 1: ok = False; break
    return ac

def ordem_total2(n):
    return [[1 if j > i else 0 for j in range(n)] for i in range(n)]

print("\n(i) ingenua com aborto, na familia M[i,j]=1 <=> j>i:")
print("     n   medido   (n-1)(n+4)/2")
ok = True
for n in range(2, 13):
    m = ingenua_aborto(ordem_total2(n)); f = (n-1)*(n+4)//2
    if n <= 6 or n == 12: print(f"   {n:3d}   {m:6d}   {f:12d}")
    if m != f: ok = False
checa("(i) ingenua com aborto = (n-1)(n+4)/2 nessa familia, n=2..12", ok)
print("     -> o solver derivou essa formula a mao; agora esta medida.")

# (ii) a cota inferior: todo algoritmo correto le >= n posicoes no pior caso.
# Testo o argumento de adversario concretamente: se uma coluna p nao e lida,
# existe matriz M1 indistinguivel de M0 onde p E celebridade.
print("\n(ii) cota inferior: se uma coluna nunca e lida, o algoritmo erra")
def le_colunas(M, alg):
    """Roda o algoritmo do slide instrumentado e devolve quais colunas foram lidas."""
    n = len(M); lidas = set()
    def get(x, y):
        lidas.add(y); return M[x][y]
    def rec(S):
        if len(S) == 1: return S[0]
        i, j = S[0], S[1]
        s = i if get(i, j) == 1 else j
        k = rec([x for x in S if x != s])
        if k is not None:
            a, b = get(s, k), get(k, s)
            if a != 1 or b != 0: k = None
        return k
    r = rec(list(range(n)))
    return r, lidas
ok = True
for n in range(2, 8):
    M0 = [[0]*n for _ in range(n)]              # ninguem conhece ninguem: sem celebridade
    r, lidas = le_colunas(M0, None)
    if r is not None: ok = False
    faltando = set(range(n)) - lidas
    print(f"   n={n}: resposta em M0 = {r}, colunas lidas = {len(lidas)}/{n}, nao lidas = {sorted(faltando)}")
    if faltando: ok = False
checa("(ii) o algoritmo do slide le ao menos uma posicao de CADA coluna (n=2..7)", ok)
print("     -> consistente com a cota inferior de n acessos: se ele pulasse uma")
print("        coluna p, a matriz M1 (coluna p toda 1) seria indistinguivel e ele erraria.")

# demonstra o adversario na pratica, para o algoritmo INGENUO com aborto,
# que de fato pode pular colunas -- e por isso precisa de mais acessos.
print("\n(iii) o argumento do adversario, exibido concretamente:")
n = 4
M0 = [[0]*n for _ in range(n)]
r0, lidas0 = le_colunas(M0, None)
p = 2
M1 = [r[:] for r in M0]
for x in range(n):
    if x != p: M1[x][p] = 1
r1, _ = le_colunas(M1, None)
print(f"   M0 (tudo 0): resposta {r0} (correto: sem celebridade -> {celebridades(M0)})")
print(f"   M1 (coluna {p} toda 1): celebridade real = {celebridades(M1)}, algoritmo devolve {r1}")
checa("(iii) o algoritmo acerta em M1 porque LE a coluna p",
      r1 == p and celebridades(M1) == [p],
      f"le a coluna {p}? {'sim' if p in lidas0 else 'nao'}")

# (iv) a convencao da linha 8: sem curto-circuito reproduz os custos medidos?
print("\n(iv) convencao de contagem da linha 8 (2 acessos, sem curto-circuito):")
def celeb_curto(M):
    """Variante COM curto-circuito, para comparar."""
    n = len(M); ac = [0]
    def rec(S):
        if len(S) == 1: return S[0]
        i, j = S[0], S[1]; ac[0] += 1
        s = i if M[i][j] == 1 else j
        k = rec([x for x in S if x != s])
        if k is not None:
            ac[0] += 1
            if M[s][k] != 1: k = None
            else:
                ac[0] += 1
                if M[k][s] != 0: k = None
        return k
    return rec(list(range(n))), ac[0]
print("     n   min/max SEM curto-circuito   min/max COM curto-circuito")
for n in range(2, 6):
    sem = set(); com = set()
    for M in matrizes(n):
        _, e, v = celebridade(M); sem.add(e+v)
        com.add(celeb_curto(M)[1])
    print(f"   {n:3d}   {min(sem)}/{max(sem):-3d}                      {min(com)}/{max(com)}")
checa("(iv) a convencao sem curto-circuito da min=n+1 e max=3(n-1)",
      all((lambda s: min(s) == n+1 and max(s) == 3*(n-1))
          ({celebridade(M)[1]+celebridade(M)[2] for M in matrizes(n)}) for n in range(2, 6)))
print("     -> o solver declarou essa convencao explicitamente; ela e a que reproduz")
print("        os numeros medidos. Com curto-circuito o MELHOR caso cairia para n.")

print()
print("=" * 76)
print(("ADENDO - FALHAS: " + "; ".join(FALHAS)) if FALHAS else "ADENDO - nenhuma falha.")
print("=" * 76)
sys.exit(1 if FALHAS else 0)
