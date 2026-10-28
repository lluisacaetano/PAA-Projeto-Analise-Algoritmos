import sys,os
S=os.path.dirname(os.path.abspath(__file__)); p=f"{S}/QUADRO.md"
L=open(p).read().splitlines()
for a in sys.argv[1:]:
    slug,v=a.split("=",1)
    for i,l in enumerate(L):
        if l.startswith(f"- {slug}:"): L[i]=l.rstrip()+f" {v}"; break
    else: L.append(f"- {slug}: {v}")
open(p,"w").write("\n".join(L)+"\n"); print("\n".join(L))
