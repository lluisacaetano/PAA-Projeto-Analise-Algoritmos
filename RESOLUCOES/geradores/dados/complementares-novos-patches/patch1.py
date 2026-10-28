# -*- coding: utf-8 -*-
"""Lote 1 de correções das questões novas (onda A). Grava a cada troca (7.6); antigo ⊄ novo e antigo some (7.10)."""
import sys
D = "/Users/luisacaetano/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores/dados/complementares-novos"
def troca(arq, antigo, novo):
    p = f"{D}/{arq}.md"; t = open(p, encoding="utf-8").read()
    if antigo in novo: raise SystemExit(f"{arq}: antigo ⊂ novo")
    if antigo not in t and novo in t: print("  já:", arq, antigo[:40]); return
    if t.count(antigo) != 1: raise SystemExit(f"{arq}: {t.count(antigo)} ocorrências de {antigo[:60]!r}")
    t = t.replace(antigo, novo)
    if antigo in t: raise SystemExit("persiste")
    open(p, "w", encoding="utf-8").write(t); print("  ok:", arq, antigo[:40])

# uber-p8 (onda A, coerência): "não pode ser menor que 6" é falso para n0 real em (5,6)
troca("uber-uem-p-8", "n0 = 6; n0 não pode ser menor que 6, porque a definição exige 0 ≤ f(n) e f(n) < 0 para 1 ≤ n ≤ 5)",
      "n0 = 6; nenhum n0 ≤ 5 serve, porque a definição exige 0 ≤ f(n) e f(n) < 0 para 1 ≤ n ≤ 5 — entre os naturais, 6 é o menor n0)")
troca("uber-uem-p-8", "Por que n0 = 6 e não menor:", "Por que nenhum n0 ≤ 5 serve (e 6 é o menor n0 natural):")

# campello-p11 (onda A, matemático): x, y > 1 é suficiente, não necessário, para o O
troca("campello-p-11", "A hipótese x, y > 1 é necessária: com base igual a 1 o logaritmo não está definido, e com base em (0, 1) o logaritmo fica negativo para n ≥ 2. Com x ∈ (0, 1) e y > 1, por exemplo, log_y n NÃO é O(log_x n).",
      "A hipótese x, y > 1 é suficiente, e é a que interessa para custo de algoritmo; ela não é necessária para o O sozinho. Com base 1 o logaritmo não está definido. Com as duas bases em (0, 1), c = log_y x continua positiva e o O vale do mesmo jeito; com x > 1 e y ∈ (0, 1), o O vale trivialmente (log_y n ≤ 0 ≤ log_x n), mas o Θ falha. O O falha só com x ∈ (0, 1) e y > 1: por exemplo, log_2 n NÃO é O(log_(1/2) n).")
troca("campello-p-11", "PASSO 5 — POR QUE x, y > 1 É NECESSÁRIO:", "PASSO 5 — O PAPEL DA HIPÓTESE x, y > 1 (SUFICIENTE; QUANDO ELA FALTA):")
troca("campello-p-11", "Com uma base maior que 1 e a outra em (0, 1), c é negativa, e a definição exige c positiva.",
      "Com uma base maior que 1 e a outra em (0, 1), c é negativa, e então ESTA testemunha não serve, porque a definição exige c positiva. Isso sozinho não decide o O, que pode valer com outra c: depende de qual base está em (0, 1), como mostram (iii) e (iv). Com as duas bases em (0, 1), c > 0 e a igualdade (1) dá o O com n0 = 1, como no caso x, y > 1.")
troca("campello-p-11", "Portanto, sem x, y > 1, ou a conclusão é falsa, ou ela não diz o que a frase \"a base não afeta a complexidade\" pretende dizer.",
      "Portanto, com bases dos dois lados de 1, ou o O é falso (iii) ou o Θ é falso (iv); com as duas bases em (0, 1) as funções são negativas para n ≥ 2 e o Θ na forma do CLRS (que exige 0 ≤ c1·g(n)) também falha. Por isso a frase \"a base não afeta a complexidade\" se lê com bases maiores que 1.")

# Conferências: tirar referência ao "chão determinístico" (artefato interno que o leitor não vê)
C = "conferido numericamente em Python (fora da prova)"
troca("campello-p-11", "Conferência: o chão determinístico confirma, para", f"Conferência ({C}): para")
troca("campello-p-11", "Os valores de c que ele imprime batem", "Os valores de c calculados batem")
troca("campello-p-22", "Conferência: o chão determinístico, usando o mesmo modelo M, contou", f"Conferência ({C}): uma implementação instrumentada no mesmo modelo M contou")
troca("campello-p-22", "não foram testadas no chão; estão provadas", "não entram nessa contagem; estão provadas")
troca("ifmg-slide-23", "Conferência: o CHÃO DETERMINÍSTICO simulou o Algoritmo 6", f"Conferência ({C}): a simulação do Algoritmo 6")
troca("ifmg-slide-26", "Conferência: o CHÃO DETERMINÍSTICO, execução literal do Algoritmo 7 com TORRE-HANOI(4, A, C, B), lista", f"Conferência ({C}): a execução literal do Algoritmo 7 com TORRE-HANOI(4, A, C, B) lista")
troca("ifmg-slide-26", "; ele reporta \"chamadas 15 movimentos 15\", que coincide", ": 15 chamadas e 15 movimentos, o que coincide")
troca("ifmg-slide-26", " As somas impressas no fim do chão (Σ i·i! e Σ i·2ⁱ) não são usadas nesta resolução.", "")
troca("loureiro-p-185", "Conferência: o chão determinístico confirma os valores", f"Conferência ({C}): conferem os valores")
troca("loureiro-p-87", "Conferência: o chão determinístico confirma a fórmula", f"Conferência ({C}): confere a fórmula")
troca("loureiro-p-87", " Os três valores de n coincidem com os do chão, que acusou violação em cada um.", " Nos três valores de n a cota superior é violada.")
troca("rezende-unicamp-p-10", "Conferência: o chão determinístico calculou", f"Conferência ({C}): calculei")
troca("rezende-unicamp-p-9-recorr-ncia-3", "Conferência: o chão determinístico confirma, para", f"Conferência ({C}): para")
troca("rezende-unicamp-p-9-recorr-ncia-3", " As demais linhas do chão referem-se à recorrência (4), que não é objeto deste exercício.", "")
troca("rezende-unicamp-p-9-recorr-ncia-4", "Conferência: o chão determinístico confirma T(2) = 4 e T(3) = 5, os valores que o texto calcula. Ele confirma que", f"Conferência ({C}): T(2) = 4 e T(3) = 5, os valores que o texto calcula; e")
troca("uber-uem-p-12", "Conferência: o CHÃO DETERMINÍSTICO confirma as desigualdades usadas na parte Ω — linha Ω2: (1/4)n²",
      f"Conferência ({C}): no item 2, (1/4)n²")
troca("uber-uem-p-12", "para c = 1/4; linha Ω3: 3n ≤", "para c = 1/4 entre os naturais; no item 3, 3n ≤")
troca("uber-uem-p-12", "sem falhas; linha Ω4: para c = 0,01", "sem falhas; no item 4, para c = 0,01")
troca("uber-uem-p-12", " As linhas O1, O5 confirmam as igualdades 100n² = 100n² e 720 = 720 usadas nos itens 1 e 5. As demais linhas (O2–O4, Θ2, Θ3) tratam de O e Θ, que este enunciado não pede, e não foram usadas.",
      " Os itens 1 e 5 são as igualdades 100n² = 100n² e 720 = 720.")
troca("uber-uem-p-17", "Conferência: o chão determinístico confirma O1 (100n² ≤ 100n² em todo n ≥ 1), O2, Ω2 e Θ2 (n²/4",
      f"Conferência ({C}): item 1, 100n² ≤ 100n² em todo n ≥ 1; item 2, n²/4")
troca("uber-uem-p-17", "o que justifica n₀ = 12), O5 (720 ≤ 720), Ω3 (3n ≤ 3n² + 20 em todo n ≥ 1, a cota inferior do item 3), Θ3 (com c = 300 a cota superior do item 3 falha; o chão aponta n = 100,",
      "o que justifica n₀ = 12 entre os naturais com c₁ = 1/4; item 5, 720 ≤ 720; item 3, 3n ≤ 3n² + 20 em todo n ≥ 1 (cota inferior) e, com c₂ = 300, a cota superior falha já em n = 100,")
troca("uber-uem-p-17", "também falha) e Ω4 (com c = 0,01 a cota inferior do item 4 falha em n = 601, o mesmo n da fórmula). As linhas O3 (\"3n + 20 ≤ 23n²\") e O4 (\"6n³ ≤ cn²\") testam expressões que não são as deste enunciado e não foram usadas na prova.",
      "também falha; item 4, com c₁ = 0,01 a cota inferior falha em n = 601, o mesmo n da fórmula.")
troca("uber-uem-p-8", "Conferência: o chão determinístico confirma as testemunhas", f"Conferência ({C}): as testemunhas")
troca("uber-uem-p-8", "o que justifica n0 = 6 (item 2)", "o que justifica n0 = 6 entre os naturais (item 2)")
troca("uber-uem-p-8", " As linhas Ω e Θ do chão não são pedidas por este enunciado, que só trata da notação O.", "")
troca("walace-ifmg-slide-16-item-2", "Conferência: o CHÃO DETERMINÍSTICO registra Σ i·i!", f"Conferência ({C}): Σ i·i!")
troca("walace-ifmg-slide-16-item-2", " A segunda fórmula listada no chão, Σ i·2^i = (n − 1)2^(n+1) + 2, refere-se a outro item e não é usada aqui.", "")
troca("walace-ifmg-slide-16-item-3", "Conferência: o chão determinístico registra Σ i·2^i", f"Conferência ({C}): Σ i·2^i")
troca("walace-ifmg-slide-16-item-3", " A fórmula para Σ i·i! que aparece no mesmo chão é de outro item e não é usada aqui.", "")
print("fim")
