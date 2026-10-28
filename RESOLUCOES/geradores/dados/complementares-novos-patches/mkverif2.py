"""Monta verif/<slug>.txt a partir da FONTE DE VERDADE (dados/complementares-novos/<slug>.md), sem copiar nada."""
import sys, os
S=os.path.dirname(os.path.abspath(__file__)); D=os.path.expanduser("~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores/dados/complementares-novos")
for slug in sys.argv[1:]:
    sol=open(f"{D}/{slug}.md",encoding="utf-8").read().strip()
    assert sol.startswith("Resposta."), slug
    prob=open(f"{S}/prob/{slug}.txt",encoding="utf-8").read().split("=== CHÃO DETERMINÍSTICO")[0].strip()
    open(f"{S}/verif/{slug}.txt","w",encoding="utf-8").write(prob+"\n\n=== RESOLUÇÃO (em julgamento) ===\n\n"+sol+"\n")
    print(slug, len(sol))
