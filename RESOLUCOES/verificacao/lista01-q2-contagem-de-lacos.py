import math

def cod1(n,k):
    s=0
    for i in range(1,n+1):
        for j in range(1,n+1): s+=1
    return s

def cod2(n,k):
    s=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            c=j
            while c<=k: s+=1; c+=1
    return s

def cod3(n,k):
    s=0
    for i in range(1,n+1):
        for j in range(1,i+1): s+=1
    return s

def cod4(n,k):
    s=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            c=1
            while c<=k: s+=1; c*=2
    return s

def cod5(n,k):
    s=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            c=1
            while c<=n: s+=1; c*=5
    return s

# forma fechada candidata para cada codigo
f1 = lambda n,k: n*n
f2 = lambda n,k: n*(min(n,k)*(2*k-min(n,k)+1)//2)
f3 = lambda n,k: n*(n+1)//2
f4 = lambda n,k: (math.floor(math.log2(k))+1)*(n*(n+1)//2)
f5 = lambda n,k: n*n*(math.floor(math.log(n,5))+1)

testes=[("codigo 1",cod1,f1,"n^2"),("codigo 2",cod2,f2,"n*k(k+1)/2  (n>=k)"),
        ("codigo 3",cod3,f3,"n(n+1)/2"),("codigo 4",cod4,f4,"(floor(lg k)+1)*n(n+1)/2"),
        ("codigo 5",cod5,f5,"n^2*(floor(log_5 n)+1)")]

for nome,fn,ff,desc in testes:
    print(f"\n=== {nome}  |  forma fechada: {desc} ===")
    ok=True
    for k in [1,2,5,8,20]:
        for n in [1,2,3,4,5,7,10,25,60,125,130]:
            m=fn(n,k); p=ff(n,k)
            if m!=p:
                ok=False; print(f"   DIVERGE  n={n} k={k}: medido={m} formula={p}")
    print("   bate em todos os (n,k) testados" if ok else "   >>> FORMULA ERRADA <<<")

print("\n=== crescimento: medido / candidato assintotico ===")
print(f"{'n':>5} {'c1/n^2':>9} {'c2/n':>9} {'c3/n^2':>9} {'c4/n^2':>9} {'c5/(n^2 lg n)':>15}")
k=8
for n in [10,25,60,125,250,500]:
    print(f"{n:5} {cod1(n,k)/n**2:9.3f} {cod2(n,k)/n:9.3f} {cod3(n,k)/n**2:9.3f} "
          f"{cod4(n,k)/n**2:9.3f} {cod5(n,k)/(n*n*math.log2(n)):15.4f}")
