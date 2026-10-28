# -*- coding: utf-8 -*-
"""
Chao deterministico da atualizacao de 09/09/2026 (listas 1, 3 e 4 revisadas pelo
professor). Roda ANTES de qualquer redacao, em Python puro, sem biblioteca.

  Lista 1, Q1(e)  -- theta(n^2) no pior caso => existe entrada com >= 100n?
  Lista 1, Q1(f)  -- O(n^2) no pior caso => existe OBRIGATORIAMENTE entrada com >= 100n?
  Lista 3, Q3     -- 2^n moedas, uma falsa mais leve, n pesagens
  Lista 3, Q5     -- P(n): 1+...+n = n(n+1)/2 + 1  (passo vale, base nunca)
  Lista 4, Q4     -- 1^2 + ... + n^2 = n(n+1)(2n+1)/6
  Lista 4, Q5     -- arvores: n vertices => n-1 arestas; a falacia do "build-up"

Rodar da raiz do projeto:
  python3 RESOLUCOES/verificacao/atualizacao-2026-09-chao-deterministico.py
"""
import itertools, sys
from fractions import Fraction

falhas = 0
def confere(rot, ok):
    global falhas
    print(("  OK    " if ok else "  FALHA ") + rot)
    falhas += 0 if ok else 1

# ---------------------------------------------------------------------------
print("Lista 1, Q1(e) -- piso do theta forca alguma entrada >= 100n")
# Insertion sort, pior caso em comparacoes de chave: W(n) = n(n-1)/2.
# c1 = 1/4, n0 = 2 (testemunhas usadas na resolucao da Q1(c)).
W = lambda n: n * (n - 1) // 2
confere("W(n) >= n^2/4 para 2 <= n <= 10^5", all(4 * W(n) >= n * n for n in range(2, 100001)))
# Com W(n) >= c1 n^2 e n > 100/c1, vem W(n) > 100n. Para c1 = 1/4: n > 400.
confere("W(n) > 100n para 401 <= n <= 10^5", all(W(n) > 100 * n for n in range(401, 100001)))
primeiro = next(n for n in range(1, 10**6) if W(n) >= 100 * n)
confere(f"primeiro n com W(n) >= 100n e {primeiro} (esperado 201)", primeiro == 201)
confere("em n = 201: W = 20100 = 100*201", W(201) == 20100 == 100 * 201)
# O limiar da demonstracao geral (n > 100/c1 = 400) e SUFICIENTE, nao o menor.
confere("n = 400 nao serve na desigualdade estrita c1 n^2 > 100 n (fencepost)",
        not (Fraction(1, 4) * 400**2 > 100 * 400))
confere("n = 401 serve", Fraction(1, 4) * 401**2 > 100 * 401)

print("\nLista 1, Q1(f) -- contraexemplo: custo constante")
# Algoritmo que devolve A[1]: 3 operacoes primitivas em toda entrada (ler, atribuir, devolver),
# numero fixo; qualquer constante K serve.
for K in (1, 3, 99):
    confere(f"K = {K}: K <= K*n^2 para n >= 1 (O(n^2) com c = K, n0 = 1)",
            all(K <= K * n * n for n in range(1, 10001)))
    confere(f"K = {K}: K < 100n para TODO n >= 1 (nunca atinge 100n)",
            all(K < 100 * n for n in range(1, 10001)))
confere("K = 100 ja atinge 100n em n = 1 -- por isso o contraexemplo exige K < 100",
        100 >= 100 * 1)
# Contraexemplo linear que tambem nunca atinge: 99n + 0  (busca linear com < 100 ops/iteracao)
confere("99n < 100n para todo n >= 1", all(99 * n < 100 * n for n in range(1, 10001)))

# ---------------------------------------------------------------------------
print("\nLista 3, Q3 -- moeda falsa por bisseccao")
def bisseccao(moedas):
    """moedas: lista de pesos (uma e mais leve). Devolve (indice_achado, pesagens)."""
    grupo = list(range(len(moedas)))
    pesagens = 0
    while len(grupo) > 1:
        m = len(grupo) // 2
        E, D = grupo[:m], grupo[m:]
        assert len(E) == len(D)
        pE, pD = sum(moedas[i] for i in E), sum(moedas[i] for i in D)
        pesagens += 1
        assert pE != pD, "a balanca nunca equilibra: um prato tem a falsa"
        grupo = E if pE < pD else D
    return grupo[0], pesagens

ok_todos = True
for n in range(0, 13):
    for falsa in range(2**n):
        pesos = [10] * (2**n); pesos[falsa] = 9
        achada, p = bisseccao(pesos)
        if achada != falsa or p != n:
            ok_todos = False
confere("n = 0..12, toda posicao da falsa: acha a moeda certa com exatamente n pesagens", ok_todos)

# Independe de QUAL o peso: so importa ser menor. Testa pesos irracionais-ish.
ok = True
for n in range(1, 9):
    for falsa in range(2**n):
        pesos = [Fraction(7, 3)] * (2**n); pesos[falsa] = Fraction(7, 3) - Fraction(1, 1000)
        ok &= bisseccao(pesos) == (falsa, n)
confere("vale para qualquer diferenca de peso (Fraction 1/1000)", ok)

# n pesagens NAO e o otimo: cota inferior informacional ceil(log3 2^n) e 8 moedas em 2 pesagens.
def ceil_log3(x):
    k, p = 0, 1
    while p < x: p *= 3; k += 1
    return k
print("   n  moedas  bisseccao  cota ceil(log3 2^n)")
for n in range(0, 9):
    print(f"  {n:2d}  {2**n:6d}  {n:9d}  {ceil_log3(2**n):5d}")

def tres_pratos_8(pesos):
    """Estrategia classica para 8 moedas em 2 pesagens: 3 x 3, sobra 2."""
    s = lambda idx: sum(pesos[i] for i in idx)
    A, B, C = [0, 1, 2], [3, 4, 5], [6, 7]
    if s(A) == s(B):
        return (6 if pesos[6] < pesos[7] else 7), 2
    G = A if s(A) < s(B) else B
    if pesos[G[0]] == pesos[G[1]]:
        return G[2], 2
    return (G[0] if pesos[G[0]] < pesos[G[1]] else G[1]), 2
ok = all(tres_pratos_8([10 if i != f else 9 for i in range(8)]) == (f, 2) for f in range(8))
confere("8 moedas (n = 3) resolvidas em 2 pesagens -- n pesagens basta, mas nao e minimo", ok)

def hibrida(pesos):
    """n >= 3: bisseccao ate sobrar um grupo de 8, depois a estrategia 3x3 de 8 moedas."""
    grupo, pes = list(range(len(pesos))), 0
    while len(grupo) > 8:
        m = len(grupo) // 2
        E, D = grupo[:m], grupo[m:]
        pes += 1
        grupo = E if sum(pesos[i] for i in E) < sum(pesos[i] for i in D) else D
    idx, p2 = tres_pratos_8([pesos[i] for i in grupo])
    return grupo[idx], pes + p2
ok = all(hibrida([10 if i != f else 9 for i in range(2**n)]) == (f, n - 1)
         for n in range(3, 12) for f in range(2**n))
confere("n = 3..11, toda posicao: bisseccao ate 8 + 3x3 acha a falsa com n - 1 pesagens", ok)

# ---------------------------------------------------------------------------
print("\nLista 3, Q5 -- P(n): 1+...+n = n(n+1)/2 + 1")
S = lambda n: n * (n + 1) // 2
dir_ = lambda n: Fraction(n * (n + 1), 2) + 1
confere("(i) identidade do passo: [n(n+1)/2 + 1] + (n+1) = (n+1)(n+2)/2 + 1, n = 0..10^4",
        all(dir_(n) + (n + 1) == dir_(n + 1) for n in range(0, 10001)))
confere("(ii) P(n) falsa para n = 0..10^5 (lado esquerdo = direito - 1)",
        all(S(n) == dir_(n) - 1 for n in range(0, 100001)))
confere("P(0): soma vazia 0 vs 0*1/2 + 1 = 1 -> falsa (cobre a convencao 0 in N)", 0 != dir_(0))
confere("P(1): 1 vs 2 -> falsa", 1 != dir_(1))

# ---------------------------------------------------------------------------
print("\nLista 4, Q4 -- soma dos quadrados")
acc, ok = 0, True
for n in range(0, 20001):
    acc += n * n
    ok &= 6 * acc == n * (n + 1) * (2 * n + 1)
confere("1^2+...+n^2 = n(n+1)(2n+1)/6 para n = 0..20000 (inclui soma vazia n = 0)", ok)
confere("n(n+1)(2n+1) divisivel por 6 para n = 0..10^5",
        all(n * (n + 1) * (2 * n + 1) % 6 == 0 for n in range(0, 100001)))
confere("passo: n(n+1)(2n+1)/6 + (n+1)^2 = (n+1)(n+2)(2n+3)/6, n = 0..10^4",
        all(n*(n+1)*(2*n+1) + 6*(n+1)**2 == (n+1)*(n+2)*(2*n+3) for n in range(0, 10001)))
confere("fatoracao do passo: (n+1)[n(2n+1) + 6(n+1)] = (n+1)(2n^2 + 7n + 6)",
        all((n+1)*(n*(2*n+1) + 6*(n+1)) == (n+1)*(2*n*n + 7*n + 6) for n in range(0, 1001)))
confere("2n^2 + 7n + 6 = (n+2)(2n+3)",
        all(2*n*n + 7*n + 6 == (n+2)*(2*n+3) for n in range(-100, 1001)))

# ---------------------------------------------------------------------------
print("\nLista 4, Q5 -- arvores e o erro de 'build-up'")
def conexo(V, E):
    V = list(V)
    if not V: return True
    adj = {v: set() for v in V}
    for a, b in E: adj[a].add(b); adj[b].add(a)
    vis, pilha = {V[0]}, [V[0]]
    while pilha:
        x = pilha.pop()
        for y in adj[x] - vis: vis.add(y); pilha.append(y)
    return len(vis) == len(V)

def aciclico(V, E):
    pai = {v: v for v in V}
    def acha(x):
        while pai[x] != x: pai[x] = pai[pai[x]]; x = pai[x]
        return x
    for a, b in E:
        ra, rb = acha(a), acha(b)
        if ra == rb: return False
        pai[ra] = rb
    return True

def arvores(n):
    """Todas as arvores rotuladas em {0..n-1}, por forca bruta sobre subconjuntos de arestas."""
    V = range(n)
    todas = list(itertools.combinations(V, 2))
    out = []
    for m in range(0, len(todas) + 1):
        for E in itertools.combinations(todas, m):
            if conexo(V, E) and aciclico(V, E):
                out.append(frozenset(E))
    return out

cache = {}
for n in range(1, 7):
    T = arvores(n)
    cache[n] = T
    cayley = 1 if n <= 2 else n ** (n - 2)
    confere(f"n = {n}: {len(T)} arvores rotuladas (Cayley n^(n-2) = {cayley}), "
            f"todas com n-1 = {n-1} arestas", len(T) == cayley and all(len(E) == n - 1 for E in T))

# Toda arvore com >= 2 vertices tem >= 2 folhas; remover uma folha deixa arvore.
ok_folha, ok_remove = True, True
for n in range(2, 7):
    for E in cache[n]:
        grau = {v: 0 for v in range(n)}
        for a, b in E: grau[a] += 1; grau[b] += 1
        folhas = [v for v in grau if grau[v] == 1]
        ok_folha &= len(folhas) >= 2
        for f in folhas:
            V2 = [v for v in range(n) if v != f]
            E2 = [e for e in E if f not in e]
            ok_remove &= conexo(V2, E2) and aciclico(V2, E2) and len(E2) == len(E) - 1
confere("n = 2..6: toda arvore tem >= 2 folhas", ok_folha)
confere("n = 2..6: remover qualquer folha (e sua aresta) deixa arvore com uma aresta a menos", ok_remove)

# Para arvores o build-up ALCANCA todas -- mas isso e justamente o lema que o aluno nao provou.
ok = True
for n in range(1, 6):
    geradas = set()
    for E in cache[n]:
        for u in range(n):
            geradas.add(frozenset(set(E) | {(u, n)}))
    # arvores rotuladas em {0..n} em que o vertice n e folha
    alvo = {E for E in cache[n + 1] if sum(1 for e in E if n in e) == 1}
    ok &= geradas == alvo
confere("n = 1..5: 'pendurar folha' gera exatamente as arvores de n+1 em que o novo vertice e folha", ok)

# Mesma forma de argumento prova coisa FALSA: "todo grafo com n >= 1 vertices e grau minimo
# >= 1 e conexo". Build-up: pendurar um vertice num grafo conexo mantem conexo e grau >= 1.
V4, E4 = range(4), [(0, 1), (2, 3)]
grau4 = [sum(1 for e in E4 if v in e) for v in V4]
confere("contraexemplo: 2 arestas disjuntas, 4 vertices, grau minimo 1, NAO conexo",
        min(grau4) >= 1 and not conexo(V4, E4))
# E o build-up so gera conexos: a partir de todos os grafos conexos de 3 vertices com grau >= 1
ok = True
for m in range(0, 4):
    for E in itertools.combinations(list(itertools.combinations(range(3), 2)), m):
        if conexo(range(3), E) and all(sum(1 for e in E if v in e) >= 1 for v in range(3)):
            for u in range(3):
                ok &= conexo(range(4), list(E) + [(u, 3)])
confere("build-up a partir de grafos conexos de 3 vertices so gera grafos conexos -- nunca o contraexemplo", ok)

print()
print("=" * 72)
print("Chao deterministico OK." if not falhas else f"{falhas} FALHAS.")
print("=" * 72)
sys.exit(1 if falhas else 0)
