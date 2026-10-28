import math
# Conta TODAS as operacoes primitivas (guia RAM da lista): 1 por atribuicao, teste e incremento.

def cod1(n):                      # while (i <= n) { soma++; i = i*10 }
    t = 2                         # soma=0 ; i=1
    i = 1; it = 0
    while i <= n:
        t += 1                    # teste verdadeiro
        t += 2                    # soma=soma+1 ; i=i*10
        i *= 10; it += 1
    t += 1                        # teste falso
    return t, it

def cod2(n):                      # i=n; while (i>0) { soma+=i; i=i//2 }
    t = 2
    i = n; it = 0
    while i > 0:
        t += 1
        t += 2
        i //= 2; it += 1
    t += 1
    return t, it

def cod3(n, x):                   # if (i != x) soma+=i ELSE for j=1..i
    t = 2                         # x=escolha(...) ; soma=0
    t += 1                        # i=1
    inner = 0
    for i in range(1, n+1):
        t += 1                    # teste i<=n
        t += 1                    # teste do if
        if i != x:
            t += 1                # soma = soma + i
        else:
            t += 1                # j = 1
            for j in range(1, i+1):
                t += 3            # teste j<=i ; soma=soma+j*x ; j=j+1
                inner += 1
            t += 1                # teste j<=i falso
        t += 1                    # i = i+1
    t += 1                        # teste i<=n falso
    return t, inner

def cod4(n, x):                   # if (i == x) soma+=i ELSE for j=1..i
    t = 3
    inner = 0
    for i in range(1, n+1):
        t += 2
        if i == x:
            t += 1
        else:
            t += 1
            for j in range(1, i+1):
                t += 3; inner += 1
            t += 1
        t += 1
    t += 1
    return t, inner

def cod5(n):                      # for i=1..n { for j=1; j<=i; j*=3 { for k=1..25 } }
    t = 2
    inner = 0
    for i in range(1, n+1):
        t += 2                    # teste i<=n ; j=1
        j = 1
        while j <= i:
            t += 1                # teste j<=i
            t += 1                # k = 1
            for k in range(1, 26):
                t += 3
                inner += 1
            t += 1                # teste k<=25 falso
            t += 1                # j = 3*j
            j *= 3
        t += 1                    # teste j<=i falso
        t += 1                    # i = i+1
    t += 1
    return t, inner

print("=== codigo 1: i = i*10  ->  iteracoes vs floor(log10 n)+1 ===")
for n in [1,9,10,99,100,1000,10**6]:
    t,it = cod1(n); print(f"  n={n:8} ops={t:6} iter={it:3} floor(log10 n)+1={math.floor(math.log10(n))+1}")

print("\n=== codigo 2: i = i//2  ->  iteracoes vs floor(lg n)+1 ===")
for n in [1,2,3,7,8,1000,10**6]:
    t,it = cod2(n); print(f"  n={n:8} ops={t:6} iter={it:3} floor(lg n)+1={math.floor(math.log2(n))+1}")

# Pior caso analitico, conferido por varredura completa em n pequeno:
print("\n=== confirmando QUAL x e o pior caso (varredura completa, n=60) ===")
n=60
b3 = max((cod3(n,x)[0], x) for x in range(1,n+1)); p3 = min((cod3(n,x)[0], x) for x in range(1,n+1))
b4 = max((cod4(n,x)[0], x) for x in range(1,n+1)); p4 = min((cod4(n,x)[0], x) for x in range(1,n+1))
print(f"  codigo 3: pior ops={b3[0]} em x={b3[1]} | melhor ops={p3[0]} em x={p3[1]}")
print(f"  codigo 4: pior ops={b4[0]} em x={b4[1]} | melhor ops={p4[0]} em x={p4[1]}")

print("\n=== codigo 3 (if i != x), pior caso x=n  ->  ops/n ===")
for n in [10,50,200,800,3200,12800]:
    t,inner = cod3(n,n); print(f"  n={n:6} ops={t:9} corpo_interno={inner:6}  ops/n={t/n:8.3f}")

print("\n=== codigo 4 (if i == x), pior caso x=1  ->  ops/n^2 ===")
for n in [10,50,200,800,3200,12800]:
    t,inner = cod4(n,1); print(f"  n={n:6} ops={t:11} corpo_interno={inner:9}  ops/n^2={t/n**2:8.4f}")

print("\n=== codigo 5: j = 3*j  ->  ops/(n lg n) ===")
for n in [10,50,200,800,3200,12800]:
    t,inner = cod5(n); print(f"  n={n:6} ops={t:9} corpo={inner:8}  ops/(n lg n)={t/(n*math.log2(n)):8.3f}")
