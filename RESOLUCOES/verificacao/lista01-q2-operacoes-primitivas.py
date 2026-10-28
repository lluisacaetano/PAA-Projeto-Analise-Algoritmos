import math
# Contador de operacoes primitivas seguindo o guia RAM da lista.
def c1(n,k):
    t=2
    for i in range(1,n+1):
        t+=2
        for j in range(1,n+1): t+=3
        t+=2
    return t+1
def c2(n,k):
    t=2
    for i in range(1,n+1):
        t+=2
        for j in range(1,n+1):
            t+=2; c=j
            while c<=k: t+=3; c+=1
            t+=2
        t+=2
    return t+1
def c3(n,k):
    t=2
    for i in range(1,n+1):
        t+=2
        for j in range(1,i+1): t+=3
        t+=2
    return t+1
def c4(n,k):
    t=2
    for i in range(1,n+1):
        t+=2
        for j in range(i,n+1):
            t+=2; c=1
            while c<=k: t+=3; c*=2
            t+=2
        t+=2
    return t+1
def c5(n,k):
    t=2
    for i in range(1,n+1):
        t+=2
        for j in range(1,n+1):
            t+=2; c=1
            while c<=n: t+=3; c*=5
            t+=2
        t+=2
    return t+1

k=8
print(f"{'n':>6} | {'c1/n^2':>9} {'c2/n^2':>9} {'c3/n^2':>9} {'c4/n^2':>9} {'c5/(n^2 lg n)':>14}")
for n in [50,100,200,400,800,1600]:
    print(f"{n:6} | {c1(n,k)/n**2:9.4f} {c2(n,k)/n**2:9.4f} {c3(n,k)/n**2:9.4f} "
          f"{c4(n,k)/n**2:9.4f} {c5(n,k)/(n*n*math.log2(n)):14.4f}")
print("\nrazoes estabilizando => a classe esta certa; crescendo/indo a zero => errada")

print("\n\n=== CONFERINDO AS FORMULAS EXATAS DO DOCUMENTO ===")
def m_k(k): return math.floor(math.log2(k))+1
def m_n(n): return math.floor(math.log(n,5))+1
F1 = lambda n,k: 3*n*n + 4*n + 3
def F2(n,k):
    K = sum(max(0,k-j+1) for j in range(1,n+1))
    return 4*n*n + (4+3*K)*n + 3
F3 = lambda n,k: 1.5*n*n + 5.5*n + 3
F4 = lambda n,k: (3*m_k(k)+4)*(n*(n+1)/2) + 4*n + 3
F5 = lambda n,k: n*n*(3*m_n(n)+4) + 4*n + 3

for nome,cont,form in [("T1",c1,F1),("T2",c2,F2),("T3",c3,F3),("T4",c4,F4),("T5",c5,F5)]:
    ruins=[]
    for k in [1,2,5,8,20]:
        for n in range(1,120):
            a,b = cont(n,k), form(n,k)
            if abs(a-b) > 1e-9: ruins.append((n,k,a,b))
    print(f"  {nome}: {'BATE em todos os (n,k)' if not ruins else f'DIVERGE {ruins[:4]}'}")
