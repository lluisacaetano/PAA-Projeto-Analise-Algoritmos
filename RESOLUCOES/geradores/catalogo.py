# -*- coding: utf-8 -*-
"""Catálogo de questões do banco de PAA.
Cada item: (tema, fonte, marcador, enunciado_html, chave_resolucao)
  marcador: 'caiu' = já caiu na prova de 2025; 'prova' = é da prova de 2025
  chave_resolucao: ('L1', indice) → bloco extraído de lista-01-resolucao.html
                   ('WF', 'IFMG', '(1)') → item do workflow dos complementares
                   ('PV', 'PROVA-A', 'a') → item do workflow da prova
"""

TEMAS = [
 ("T1", "Notação assintótica — provar propriedades e limites"),
 ("T2", "Verdadeiro ou falso, e questões conceituais"),
 ("T3", "Complexidade de laços e de algoritmos"),
 ("T4", "Indução matemática"),
 ("T5", "Recorrências e Teorema Mestre"),
 ("T6", "Somatórios"),
 ("T7", "Projeto de algoritmo"),
]

Q = []
def add(tema, fonte, enun, res, marcador=None):
    Q.append(dict(tema=tema, fonte=fonte, enunciado=enun, res=res, marcador=marcador))

# ══════════ T1 — Notação assintótica: provar propriedades ══════════
# Índices ("L1", i) = i-ésimo <div class="item"> de lista-01-resolucao.html. A atualização de
# 09/09/2026 inseriu o item Q1(f) na posição 5 e deslocou os blocos seguintes em +1; o ajuste de
# 13/09/2026 retirou o Q1(f) e os blocos voltaram a −1 (Q2 códigos = 5–9, Q3 = 10–14).
add("T1","Lista 1, Q3(a)","Demonstre que <i>f</i>(n) = 2<sup>117</sup> pertence a O(1).",("L1",10))
add("T1","Lista 1, Q3(b)","Demonstre que <i>f</i>(n) = n² + 2n pertence a O(n²).",("L1",11))
add("T1","Lista 1, Q3(c)","Demonstre que <i>f</i>(n) = n² − 2n + 3 pertence a Θ(n²).",("L1",12))
add("T1","Lista 1, Q3(d)","Demonstre que <i>f</i>(n) = 5n pertence a Ω(n).",("L1",13))
add("T1","Lista 1, Q3(e)","Demonstre que <i>f</i>(n) = n² + 2n − 8 pertence a Ω(n²).",("L1",14))

add("T1","Lista 2, Q2(a)","Explique por que a frase <i>“O tempo de execução do algoritmo A é no mínimo O(n²)”</i> não faz sentido. Justifique formalmente.",("L2",7))
add("T1","Lista 2, Q3(a)","Prove que a sentença é verdadeira ou falsa: <i>f</i>(n) ∈ O(<i>g</i>(n)) <b>se e somente se</b> <i>g</i>(n) ∈ Ω(<i>f</i>(n)). Considere <i>f</i> e <i>g</i> assintoticamente não negativas.",("L2",9),"caiu")
add("T1","Lista 2, Q3(b)","Prove que a sentença é verdadeira ou falsa: se <i>f</i>(n) ∈ O(<i>g</i>(n)) então <i>g</i>(n) ∈ O(<i>f</i>(n)).",("L2",10))
add("T1","Lista 2, Q3(c)","Prove que a sentença é verdadeira ou falsa: se <i>f</i>(n) ∈ O(<i>u</i>(n)) e <i>g</i>(n) ∈ O(<i>v</i>(n)) então <i>f</i>(n) + <i>g</i>(n) ∈ O(<i>u</i>(n) + <i>v</i>(n)).",("L2",11))
add("T1","Lista 2, Q3(d)","Prove que a sentença é verdadeira ou falsa: se <i>f</i>(n) ∈ O(<i>g</i>(n)) e <i>g</i>(n) ∈ O(<i>f</i>(n)) então <i>f</i>(n) ∈ Θ(<i>g</i>(n)).",("L2",12),"caiu")

add("T1","Lista 3, Q2","Considere <i>f</i>(n) = n se n é ímpar, e <i>f</i>(n) = n² se n é par. Apresente um limite assintótico para <i>f</i> tão firme (restrito/justo) quanto possível, usando a notação Big O.",("L3",(5,6,7)))

add("T1","Campello, ex. 1","<i>f</i>(n) = 5n é <i>o</i>(n)? Justifique. <span class='dica'>Lembre: <i>o</i>( ) exige a desigualdade para <b>todo</b> c &gt; 0.</span>",("WF","CAMPELLO","(1)"))
add("T1","Campello, ex. 2","<i>f</i>(n) = 5n² é ω(n²)? Justifique.",("WF","CAMPELLO","(2)"))
add("T1","Campello, ex. 3","Seja <i>f</i>(n) que assume o valor 3n² se n for par, ou 7n se n for ímpar. Mostre que essa função é O(n²) e Ω(n).",("WF","CAMPELLO","(3)"))
add("T1","Campello, ex. 6","Mostre, usando a definição formal do operador Big-O, que qualquer função <i>f</i>(n) = d, onde d é uma constante positiva qualquer, é O(1).",("WF","CAMPELLO","(6)"))
add("T1","Campello, ex. 8","Ordene as funções abaixo de acordo com suas taxas de crescimento assintótico, e justifique:<br><code>4n·log n + 2n, &nbsp; 2¹⁰, &nbsp; 2^(log n), &nbsp; 3n + 100·log n, &nbsp; 4n, &nbsp; 2ⁿ, &nbsp; 3^(3n), &nbsp; n² + 10n, &nbsp; n³, &nbsp; n·log n</code>",("WF","CAMPELLO","(8)"))

# ══════════ T2 — V/F e conceituais ══════════
add("T2","Lista 1, Q1(a)","Responda V ou F e justifique: se eu provar que um algoritmo leva O(n²) no pior caso, é possível que leve O(n) em <b>algumas</b> entradas?",("L1",0))
add("T2","Lista 1, Q1(b)","Responda V ou F e justifique: se eu provar que um algoritmo leva O(n²) no pior caso, é possível que leve O(n) em <b>todas</b> as entradas?",("L1",1))
add("T2","Lista 1, Q1(c)","Responda V ou F e justifique: se eu provar que um algoritmo leva Θ(n²) no pior caso, é possível que leve O(n) em <b>algumas</b> entradas?",("L1",2))
add("T2","Lista 1, Q1(d)","Responda V ou F e justifique: se eu provar que um algoritmo leva Θ(n²) no pior caso, é possível que leve O(n) em <b>todas</b> as entradas?",("L1",3))
add("T2","Lista 1, Q1(e)","Responda V ou F e justifique: se eu provar que um algoritmo leva <b>θ(n²)</b> no pior caso, é possível existir alguma entrada suficientemente grande para a qual o algoritmo realiza pelo menos 100·n operações primitivas? <span class='dica'>Na versão original da lista (antes de 09/09/2026) este item dizia O(n²).</span>",("L1",4))

add("T2","Lista 1, Q4","Suponha que um algoritmo para um certo problema consome O(n²) unidades de tempo, sendo n o tamanho de uma instância. Meu amigo diz ter outro algoritmo para o mesmo problema que consome apenas Ω(n) unidades de tempo. Devo ficar impressionado(a)?",("L1","Q4"))
add("T2","Lista 1, Q5","Meu algoritmo para um certo problema consome O(n²) unidades de tempo. Meu amigo diz ter outro que consome O(n·lg n). Devo ficar impressionado(a)?",("L1","Q5"))

add("T2","Lista 2, Q1(a)","Os algoritmos A e B têm complexidade de pior caso Θ(n³) e Θ(n²), respectivamente. Em alguns conjuntos de dados, o tempo de A é <b>menor</b> que o de B, no mesmo ambiente. Forneça <b>três</b> possíveis explicações para esse fenômeno.",("L2",(0,1,2)))
add("T2","Lista 2, Q1(b)","Um pesquisador tem 2 algoritmos: um O(n²) e outro O(n³). Ele escolheu o O(n³). Cite <b>quatro</b> razões que poderiam ter motivado essa opção.",("L2",(3,4,5,6)))
add("T2","Lista 2, Q1(c)","O algoritmo A exige 10⁸·n instruções e o algoritmo B exige 10·n² instruções. Pode-se afirmar que A é <b>sempre</b> preferível a B?",("L2","H3:<h3>(c) <span class=\"resp\">Não</span></h3>"))
add("T2","Lista 2, Q2(b)","Se um algoritmo A tem tempo de execução Θ(n²) sobre qualquer entrada de tamanho n, ele pode ter tempo de execução Ω(n log n) no pior caso? Justifique formalmente.",("L2",8))

add("T2","Lista 3, Q1","Alice afirma que seu algoritmo Θ(n·lg n) é melhor que o de Bob, que é Θ(n²). Ao medirem no mesmo ambiente, descobriram que para n &lt; 100 o Θ(n²) é mais rápido, e só a partir de n ≥ 100 o Θ(n·lg n) vence. Explique como essa situação pode ocorrer.",("L3",(0,1,2,3,4)),"caiu")

add("T2","Campello, ex. 7","Explique por que, no melhor caso, o tempo de execução da busca binária iterativa é O(1). Pode-se então concluir que esse algoritmo é Θ(1)?",("WF","CAMPELLO","(7)"))

# ══════════ T3 — Complexidade de laços e algoritmos ══════════
for i,(cod,desc) in enumerate([
 (1,"soma = 0;<br>for (i = 1; i &lt;= n; i++)<br>&nbsp;&nbsp;for (j = 1; j &lt;= n; j++)<br>&nbsp;&nbsp;&nbsp;&nbsp;soma = soma + 1;"),
 (2,"soma = 0;<br>for (i = 1; i &lt;= n; i++)<br>&nbsp;&nbsp;for (j = 1; j &lt;= n; j++)<br>&nbsp;&nbsp;&nbsp;&nbsp;for (c = j; c &lt;= k; c++)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;soma = soma + 1;"),
 (3,"soma = 0;<br>for (i = 1; i &lt;= n; i++)<br>&nbsp;&nbsp;for (j = 1; j &lt;= i; j++)<br>&nbsp;&nbsp;&nbsp;&nbsp;soma = soma + 1;"),
 (4,"soma = 0;<br>for (i = 1; i &lt;= n; i++)<br>&nbsp;&nbsp;for (j = i; j &lt;= n; j++) {<br>&nbsp;&nbsp;&nbsp;&nbsp;c := 1;<br>&nbsp;&nbsp;&nbsp;&nbsp;while (c &lt;= k) { soma = soma + 1; c = c * 2; }<br>&nbsp;&nbsp;}"),
 (5,"soma = 0;<br>for (i = 1; i &lt;= n; i++)<br>&nbsp;&nbsp;for (j = 1; j &lt;= n; j++) {<br>&nbsp;&nbsp;&nbsp;&nbsp;c = 1;<br>&nbsp;&nbsp;&nbsp;&nbsp;while (c &lt;= n) { soma = soma + 1; c = c * 5; }<br>&nbsp;&nbsp;}"),
]):
    add("T3",f"Lista 1, Q2 — código {cod}",
        f"Encontre a complexidade assintótica em Big O, com limite tão firme quanto possível, considerando o pior caso. <b>k é constante.</b><div class='cod2'>{desc}</div>",("L1",5+i))  # 13/09/2026: era 6+i antes da retirada do Q1(f)

for i,(cod,desc) in enumerate([
 (1,"soma = 0;  i = 1;<br>while (i &lt;= n) { soma = soma + 1;  i = i * 10; }"),
 (2,"soma = 0;  i = n;<br>while (i &gt; 0) { soma = soma + i;  i = i / 2; }&nbsp;&nbsp;<span class='dica'>divisão inteira</span>"),
 (3,"x = escolha(1, n);&nbsp;<span class='dica'>inteiro em [1..n], em O(1)</span><br>soma = 0;<br>for (i = 1; i &lt;= n; i++) {<br>&nbsp;&nbsp;if (i != x) { soma = soma + i; }<br>&nbsp;&nbsp;else { for (j = 1; j &lt;= i; j++) soma = soma + j*x; }<br>}"),
 (4,"x = escolha(1, n);<br>soma = 0;<br>for (i = 1; i &lt;= n; i++) {<br>&nbsp;&nbsp;if (i == x) { soma = soma + i; }<br>&nbsp;&nbsp;else { for (j = 1; j &lt;= i; j++) soma = soma + j*x; }<br>}"),
 (5,"soma = 0;<br>for (i = 1; i &lt;= n; i++)<br>&nbsp;&nbsp;for (j = 1; j &lt;= i; j = 3*j)<br>&nbsp;&nbsp;&nbsp;&nbsp;for (k = 1; k &lt;= 25; k++)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;soma = soma + 1;"),
]):
    add("T3",f"Lista 2, Q4 — código {cod}",
        f"Encontre a complexidade assintótica em Big O, com limite tão firme quanto possível, considerando o pior caso. <b>k é constante.</b><div class='cod2'>{desc}</div>",("L2",13+i))

add("T3","Campello, ex. 4","Qual é o maior tamanho de entrada n de um problema P tal que P pode ser resolvido em tempo t, se o algoritmo leva <i>f</i>(n) microssegundos? Responda em uma tabela com todas as combinações de t = 1 s, 1 hora, 1 mês, 1 século e <i>f</i>(n) = log n, n, n·log n, n², n³, 2ⁿ.",("WF","CAMPELLO","(4)"))
add("T3","Campello, ex. 5","Qual a complexidade assintótica de pior caso da busca binária iterativa? Justifique formalmente usando a definição do operador Big-O.",("WF","CAMPELLO","(5)"))
add("T3","IFMG, ex. 3","Projete um algoritmo recursivo, em pseudocódigo, que calcule o valor F<sub>n</sub> da sequência de Fibonacci para o n informado.",("WF","IFMG","(3)"))
add("T3","IFMG, ex. 4","Desenhe um diagrama de árvore que ilustre as chamadas recursivas do algoritmo de Fibonacci recursivo para n = 6.",("WF","IFMG","(4)"))

# ══════════ T4 — Indução matemática ══════════
# Lista 3 atualizada em 09/09/2026: entraram a Q3 (moedas) e a Q5 (passo sem base); a antiga Q3
# virou Q4. Índices ("L3", i): Q1 0–4, Q2 5–7, Q3 8–10, Q4 11–15, Q5 16–18.
add("T4","Lista 3, Q3","Têm-se 2ⁿ moedas de ouro, sendo uma delas falsa, com peso menor do que as demais. Dispõe-se de uma balança de dois pratos, sem nenhum peso. Mostre, por indução sobre n, que é possível achar a moeda falsa com n pesagens. <span class='dica'>Enuncie P(n) para <b>qualquer</b> conjunto de 2ⁿ moedas: a hipótese será aplicada a uma metade.</span>",("L3",(8,9,10)))
add("T4","Lista 3, Q4(a)","Prove por indução: n! &gt; 2ⁿ, para todo n ≥ 4. <span class='dica'>Atenção ao valor inicial da base.</span>",("L3",11))
add("T4","Lista 3, Q4(b)","Prove por indução: 2 + 4 + 6 + … + 2n = n² + n, para todo n ≥ 1.",("L3",12))
add("T4","Lista 3, Q4(c)","Prove por indução: 1 + 2 + 3 + … + n = n(n+1)/2, para todo n ≥ 1.",("L3",13))
add("T4","Lista 3, Q5","Seja a sentença aberta em ℕ: P(n): 1 + 2 + ··· + n = n(n+1)/2 + 1. Mostre que: (i) qualquer que seja n ∈ ℕ, se P(n) é verdadeira, então P(n+1) é verdadeira; (ii) P(n) não é verdadeira para nenhum valor de n ∈ ℕ. <span class='dica'>O passo vale e a proposição é sempre falsa: é a base que falta.</span>",("L3",(16,17,18)))
add("T4","IFMG, ex. 1","Prove, para n inteiro positivo, que 0² + 1² + 2² + … + n² = (2n+1)(n+1)(n)/6.",("WF","IFMG","(1)"))
add("T4","IFMG, ex. 2","Prove, para n inteiro positivo, que 1 + 4 + 7 + … + (3n−2) = n(3n−1)/2.",("WF","IFMG","(2)"))
add("T4","USP, ex. 2.1","Mostre por indução que 1/(1·2) + 1/(2·3) + … + 1/(n·(n+1)) = n/(n+1), para todo n ≥ 1.",("WF","USP","2.1"))
add("T4","USP, ex. 2.2","Mostre por indução que 2n³ &gt; 3n² + 3n + 1 para todo n ≥ 3. <span class='dica'>A base em 3 é justa — confira por quê.</span>",("WF","USP","2.2"))
add("T4","USP, ex. 2.3","Mostre por indução que, na sequência de Fibonacci, F<sub>5n</sub> é sempre múltiplo de 5.",("WF","USP","2.3"))
add("T4","USP, ex. 2.4","Mostre que (PIF) ⟹ (PBO): por indução, mostre que todo conjunto não-vazio dos inteiros positivos contém elemento minimal.",("WF","USP","2.4"))

# ══════════ T5 — Recorrências e Teorema Mestre ══════════
add("T5","Lista 3, Q4(d)","Prove por indução que a fórmula fechada da recorrência T(1) = 1; T(n) = T(n−1) + n (n ≥ 2) é T(n) = n(n+1)/2.",("L3",14))
add("T5","Lista 3, Q4(e)","Prove por indução que a fórmula fechada da recorrência T(1) = 1; T(n) = 2·T(n−1) + 1 (n ≥ 2) é T(n) = 2ⁿ − 1.",("L3",15))
add("T5","IFMG, ex. 5","Dê a relação de recorrência para o algoritmo <code>ORDENACAO-POR-SELECAO(V, j)</code>, que devolve V se j = 1 e, caso contrário, percorre V[1..j] achando o índice do maior elemento, troca-o com V[j] e chama a si mesmo com j−1.",("WF","IFMG","(5)"))
add("T5","IFMG, ex. 6","A Torre de Hanói tem o menor número de movimentações dado por T(1) = 1 e T(n) = 2·T(n−1) + 1. Use o método <b>expandir, conjecturar e verificar</b> para encontrar a forma fechada.",("WF","IFMG","(6)"))
add("T5","Loureiro, ex. 5","Resolva pelo Teorema Mestre: T(n) = 4T(n/2) + n.",("WF","LOUREIRO","(5)"))
add("T5","Loureiro, ex. 6","Resolva pelo Teorema Mestre: T(n) = 4T(n/2) + n².",("WF","LOUREIRO","(6)"))
add("T5","Loureiro, ex. 7","Resolva pelo Teorema Mestre: T(n) = 4T(n/2) + n³. <span class='dica'>Verifique a condição de regularidade.</span>",("WF","LOUREIRO","(7)"))
add("T5","Loureiro, ex. 8","O algoritmo A tem T(n) = 7T(n/2) + n². Outro algoritmo A′ tem T′(n) = a·T′(n/4) + n². Qual é o maior valor <b>inteiro</b> de a tal que A′ é assintoticamente mais rápido que A?",("WF","LOUREIRO","(8)"))

# ══════════ T6 — Somatórios ══════════
add("T6","Walace (IFMG), ex. 1","Examine o processo de <b>perturbação</b> da soma dos quadrados: Σ<sub>i=1..n+1</sub> i² = ?",("PV","SOMATORIOS","1"))
add("T6","Walace (IFMG), ex. 2","Resolva usando o <b>operador diferença</b>: Σ<sub>i=1..n</sub> i·2ⁱ = ?",("PV","SOMATORIOS","2"))

# ══════════ Prova de 2025 ══════════
add("T7","Prova 2025, Q1","Você está em um campo minado infinitamente grande, com um detector que só identifica uma mina a <b>no máximo um passo</b> de distância. A mina está diretamente à sua esquerda ou à sua direita, mas você não sabe a que distância m. <b>(3,0)</b> Projete um algoritmo para achar a mina em O(<i>f</i>(m)) passos, com <i>f</i>(m) polinomial. <b>(2,0)</b> Argumente que seu algoritmo tem a complexidade requerida.",("PV","PROVA-A","1"),"prova")
add("T1","Prova 2025, Q2(a)","Prove que é verdadeira ou falsa: se <i>f</i>(n) ∈ O(<i>u</i>(n)) e <i>g</i>(n) ∈ O(<i>v</i>(n)) então <i>f</i>(n) − <i>g</i>(n) ∈ O(<i>u</i>(n) − <i>v</i>(n)).",("PV","PROVA-A","2a"),"prova")
add("T1","Prova 2025, Q2(b)","Prove que é verdadeira ou falsa: se <i>f</i>(n) ∈ O(<i>g</i>(n)) então <i>g</i>(n) ∈ Ω(<i>f</i>(n)).",("PV","PROVA-A","2b"),"prova")
add("T1","Prova 2025, Q2(c)","Prove que é verdadeira ou falsa: se <i>f</i>(n) ∈ O(<i>g</i>(n)) e <i>g</i>(n) ∈ O(<i>f</i>(n)) então <i>f</i>(n) ∈ Θ(<i>g</i>(n)).",("PV","PROVA-A","2c"),"prova")
add("T5","Prova 2025, Q3(a)","V ou F, com justificativa: a solução da recorrência T(n) = 2T(n/7) + n pertence a O(n²).",("PV","PROVA-B","3a"),"prova")
add("T1","Prova 2025, Q3(b)","V ou F, com justificativa: se <i>f</i>(n) = 3n² − n + 4 então <i>f</i>(n) ∈ Θ(n²).",("PV","PROVA-B","3b"),"prova")
add("T2","Prova 2025, Q3(c)","V ou F, com justificativa: sejam <i>f</i> e <i>g</i> assintoticamente positivas e considere que <i>g</i> domina assintoticamente <i>f</i>; então <i>f</i>(n) + <i>g</i>(n) ∈ Ω(<i>f</i>(n)).",("PV","PROVA-B","3c"),"prova")
add("T2","Prova 2025, Q4(a)","Alice e Bob: explique como o algoritmo Θ(n²) pode ser mais rápido que o Θ(n·lg n) para n &lt; 100. <span class='dica'>Mesma questão da Lista 3, Q1.</span>",("PV","PROVA-B","4a"),"prova")
add("T2","Prova 2025, Q4(b)","Sejam <i>f</i> e <i>g</i> assintoticamente positivas, com <i>g</i> dominando <i>f</i>. Pode-se afirmar que <i>f</i>(n) + <i>g</i>(n) ∈ Ω(<i>f</i>(n))? Justifique formalmente.",("PV","PROVA-B","4b"),"prova")
add("T5","Prova 2025, Q5(a)","O algoritmo A divide o problema em <b>um único</b> subproblema de tamanho n/5 e combina em tempo Θ(n). O algoritmo B divide em <b>um único</b> subproblema de tamanho n−1 e combina em tempo constante. Qual o consumo de tempo de cada um? Expresse em Θ e justifique.",("PV","PROVA-B","5a"),"prova")
add("T5","Prova 2025, Q5(b)","Qual dos dois algoritmos da questão anterior é assintoticamente mais eficiente no pior caso? Justifique.",("PV","PROVA-B","5b"),"prova")

# ══════════ Lista 4 (30/08/2026) — semana 5 ══════════
# Blocos extraídos de lista-04-resolucao.html. Os textos que passaram pelos
# verificadores adversariais estão em geradores/dados/lista04/q*-limpo.md; o
# HTML é a diagramação deles, e verificacao/lista04-html-bate-com-verificado.py
# confere que os dois dizem a mesma coisa.

add("T4","Lista 4, Q1(a)","Use indução matemática para provar: <i>S</i>(n) : 1 + 3 + 5 + … + (2·n − 1) = n², ∀n ≥ 1.",("L4",0))
add("T4","Lista 4, Q1(b)","Use indução matemática para provar que a fórmula fechada da recorrência <i>T</i>(n) = 2 se n = 1, <i>T</i>(n) = 2<i>T</i>(n−1) se n ≥ 2, é <i>T</i>(n) = 2<sup>n</sup>. <span class='dica'>Atenção à base: com <i>T</i>(1) = 1 a resposta seria 2<sup>n−1</sup>.</span>",("L4",1))
add("T4","Lista 4, Q1(c)","Use indução matemática para provar que a fórmula fechada da recorrência <i>T</i>(n) = 1 se n = 1, <i>T</i>(n) = <i>T</i>(n−1) + 1 se n ≥ 2, é <i>T</i>(n) = n.",("L4",2))
add("T4","Lista 4, Q1(d)","Use indução matemática para provar que a fórmula fechada da recorrência <i>T</i>(n) = 1 se n = 1, <i>T</i>(n) = <i>T</i>(n−1) + 3 se n ≥ 2, é <i>T</i>(n) = 3·n − 2.",("L4",3))
add("T4","Lista 4, Q1(e)","Use indução matemática para provar que a fórmula fechada da recorrência <i>T</i>(n) = 1 se n = 1, <i>T</i>(n) = <i>T</i>(n−1) + 2 se n ≥ 2, pertence a Θ(n). <span class='dica'>Duas fases: a indução dá a forma fechada; as testemunhas dão o Θ.</span>",("L4",4))

add("T5","Lista 4, Q2(a)","Indique o limite assintótico Θ de <i>T</i>(n) = 2<i>T</i>(n/3) + 1, supondo n potência exata de b e caso base constante. Justifique. <span class='dica'>O “+1” é n<sup>0</sup>, isto é k = 0 — não k = 1.</span>",("L4",(5,6,7,8)))
add("T5","Lista 4, Q2(b)","Indique o limite assintótico Θ de <i>T</i>(n) = 5<i>T</i>(n/4) + n, supondo n potência exata de b. Justifique.",("L4",9))
add("T5","Lista 4, Q2(c)","Indique o limite assintótico Θ de <i>T</i>(n) = 7<i>T</i>(n/7) + n, supondo n potência exata de b. Justifique. <span class='dica'>a = b sugere Θ(n) — e está errado. Confira a razão <i>T</i>(n)/n.</span>",("L4",10))
add("T5","Lista 4, Q2(d)","Indique o limite assintótico Θ de <i>T</i>(n) = 9<i>T</i>(n/3) + n², supondo n potência exata de b. Justifique.",("L4",11))
add("T5","Lista 4, Q2(e)","Indique o limite assintótico Θ de <i>T</i>(n) = 8<i>T</i>(n/2) + n³, supondo n potência exata de b. Justifique.",("L4",(12,13)))

add("T4","Lista 4, Q3","Uma “prova por indução” afirma: <i>dado um conjunto de n pessoas, se pelo menos uma tem nacionalidade chinesa, então todas as demais também são</i>. A base é n = 1; de {T₁,T₂,T₃} e {T₁,T₂,T₄} conclui-se para n = 4, e o texto encerra dizendo que “a generalização da construção para k e k+1 é a prova desejada”. <b>Essa prova está correta? Justifique formalmente.</b>",("L4",(14,15,16,17,18,19)))

# Lista 4 atualizada em 09/09/2026: entraram a Q4 (bloco 20) e a Q5 (blocos 21–26); o apêndice
# do slide passou para os blocos 27–32.
add("T4","Lista 4, Q4","Prove a proposição P(n) = 1² + 2² + 3² + … + n² = n(n+1)(2n+1)/6 usando o método da indução matemática.",("L4",20))
add("T4","Lista 4, Q5","Um estudante “prova” por indução que toda árvore com n vértices tem exatamente n − 1 arestas: base n = 1; no passo, toma uma árvore T com n vértices (n − 1 arestas pela hipótese), acrescenta um novo vértice ligado por uma única aresta a algum vértice de T, obtém uma árvore com n + 1 vértices e n arestas, e conclui que <i>toda</i> árvore com n + 1 vértices tem n arestas. <b>Embora a afirmação seja verdadeira, a prova é logicamente incorreta. Identifique precisamente o erro no passo indutivo e explique por que a construção não basta.</b> <span class='dica'>Compare com a Q3: lá o passo falha num valor; aqui não se provou que a construção cobre a classe inteira.</span>",("L4",(21,22,23,24,25,26)))

add("T7","Slides UNICAMP MC458, Exemplo 3","Dada uma árvore binária com n nós, o algoritmo <code>FatorAltura</code> calcula os fatores de balanceamento usando hipótese de indução fortalecida, e o slide mostra que o caso degenerado custa Θ(n). <b>Há algum ganho em complexidade quando ambos n<sub>e</sub> e n<sub>d</sub> são aproximadamente n/2 ao longo da recursão?</b>",("L4",(27,28,29,30,31,32)))

# ══════════ Lista 5 (14/09/2026) — avaliada, entrega em 24/09/2026 ══════════
# Blocos extraídos de lista-05-resolucao.html, que é GERADO por gerar_lista05.py a partir de
# geradores/dados/lista05/q*-limpo.md (o texto que passou pelos verificadores). Índices dos
# <div class="item">: Q1 = 0–4, Q2 = 5–8, Q3 = 9–15, Q4 = 16–21, Q5 = 22–35 (o último de cada
# questão é o quadro "Resposta"). Conferir com a lista impressa por gerar_lista05.py.
add("T7","Lista 5, Q1","Encontrar o valor máximo de um vetor com n números reais por divisão e conquista (considere n par). <b>(a)</b> Projete um algoritmo com um subproblema de tamanho n − 1. <b>(b)</b> Projete um algoritmo que divide o problema em dois subproblemas de tamanho n/2. <b>(c)</b> Qual abordagem produz um algoritmo assintoticamente mais eficiente no pior caso? Justifique. <span class='dica'>Dividir ao meio não dá lg n aqui: são dois subproblemas, não um como na busca binária.</span>",("L5",(0,1,2,3,4)))
add("T7","Lista 5, Q2","Vetor A[.] de tamanho infinito: as primeiras m posições contêm inteiros em ordem crescente e as demais valem ∞; m é desconhecido. <b>(a)</b> Descreva um algoritmo que recebe um inteiro x e encontra uma posição contendo x, se existir, em tempo o(n). <b>(b)</b> Argumente que ele tem essa complexidade. <span class='dica'>Mesma técnica da Q1 da prova de 2025 (campo minado): dobrar o alcance até passar do alvo.</span>",("L5",(5,6,7,8)))
add("T5","Lista 5, Q3","Três algoritmos, pior caso: A divide em cinco subproblemas de tamanho n/2 e combina em tempo linear; B resolve dois subproblemas de tamanho n − 1 e combina em tempo constante; C divide em nove subproblemas de tamanho n/3 e combina em tempo θ(n²). Qual é assintoticamente mais eficiente? Responda em notação θ e justifique. <span class='dica'>Mesma estrutura da Q5 da prova de 2025.</span>",("L5",(9,10,11,12,13,14,15)))
add("T4","Lista 5, Q4","Prove por indução matemática: 1/2 + 1/4 + 1/8 + ··· + 1/2<sup>n</sup> &lt; 1, ∀n ≥ 1. <span class='dica'>Separando o último termo, a hipótese “&lt; 1” sozinha não fecha o passo.</span>",("L5",(16,17,18,19,20,21)))
add("T5","Lista 5, Q5","Usando o Teorema Mestre (forma de Brassard &amp; Bratley, a da prova), indique o limite Θ de cada recorrência ou explique por que essa versão não se aplica: (a) T(n) = T(n/3) + 1; (b) T(n) = 2T(n/2) + n lg n; (c) T(n) = T(2n/3) + n; (d) T(n) = 5T(n/4) − n; (e) T(n) = T(n − 1) + 3; (f) T(n) = T(n/3) + 0; (g) T(n) = 5T(n/4) − n²; (h) T(n) = T(2n/4) + n; (i) T(n) = 3/2T(n/4) − n²; (j) T(n) = 3T(n/2) + n. <span class='dica'>Só três se aplicam. Em (f), aplicar a fórmula às cegas daria Θ(lg n) — e o certo é Θ(1).</span>",("L5",tuple(range(22,36))))

# ══════════ ENUNCIADOS LITERAIS DOS COMPLEMENTARES (06/10/2026) ══════════
# Os 25 enunciados acima eram paráfrases (e três traziam dicas que não existem no original; o
# Campello ex. 7 dizia Θ(1) onde o slide pergunta Ω(1)). Transcritos da IMAGEM das páginas (7.21)
# para dados/complementares-enunciados-literais.json; aqui substituem a paráfrase. Guarda: cada
# transcrição casa com exatamente uma questão, e nenhuma questão dos complementares fica sem.
import json as _json, os as _os
_LIT = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dados",
                                      "complementares-enunciados-literais.json"), encoding="utf-8"))
for _f, _v in _LIT.items():
    _alvo = [q for q in Q if q["fonte"] == _f]
    assert len(_alvo) == 1, f"transcrição literal {_f!r} casa com {len(_alvo)} questões"
    _alvo[0]["enunciado"] = _v["html"]
# MC458: o algoritmo e os dois slides de complexidade estão no quadro de enunciado do apêndice da
# Lista 4, FORA dos <div class="item"> que o banco extrai (7.13). Fonte única: lê o quadro de lá.
import re as _re
_h = open(_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "fontes-html",
                       "lista-04-resolucao.html"), encoding="utf-8").read()
_i = _h.index('<div class="enunciado">', _h.index("<h2>Apêndice"))
_d, _fim = 0, None
for _m in _re.finditer(r"<div\b|</div>", _h[_i:]):
    _d += 1 if _m.group().startswith("<div") else -1
    if _d == 0: _fim = _i + _m.end(); break
assert _fim and "FatorAltura (A)" in _h[_i:_fim] and "Há algum ganho" in _h[_i:_fim], "quadro do apêndice mudou"
_alvo = [q for q in Q if q["fonte"] == "Slides UNICAMP MC458, Exemplo 3"]
assert len(_alvo) == 1
_alvo[0]["enunciado"] = _h[_i:_fim] + "<p class='orig'>[transcrição literal do algoritmo, dos dois slides de complexidade e do exercício — MC458 (UNICAMP), p. 2–3; o contexto em prosa e a numeração corrida são nossos]</p>"
_sem = [q["fonte"] for q in Q if not q["fonte"].startswith(("Lista ", "Prova")) and q["fonte"] not in _LIT]
assert not _sem, f"complementares sem enunciado literal: {_sem}"

# ══════════ QUESTÕES NOVAS DOS COMPLEMENTARES (06/10/2026) ══════════
# 31 exercícios que a varredura de filtro duplo achou sem resolução, agrupados em 18 questões (os 5 itens
# V/F de cada slide do Uber formam uma questão). Enunciado + contexto do material transcritos da IMAGEM das
# páginas (dados/complementares-novos-enunciados.json); resolução = dados/complementares-novos/<slug>.md,
# o texto que passou pelos verificadores (fonte "NV" em gerar_banco.resolucao).
_NOVOS = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dados",
                                        "complementares-novos-enunciados.json"), encoding="utf-8"))
for _f, _v in _NOVOS.items():
    assert not [q for q in Q if q["fonte"] == _f], f"questão nova {_f!r} duplicada no catálogo"
    _ctx = (f"<div style='border-left:2pt solid #c8ccd2;padding-left:2mm;margin:1.2mm 0;font-size:8.6pt'>"
            f"<b>Contexto do material</b> (transcrição literal, necessária para resolver):{_v['contexto_html']}</div>"
            if _v["contexto_html"] else "")
    add(_v["tema"], _f, _v["html"] + _ctx + f"<p class='orig'>[transcrição literal — {_f}]</p>", ("NV", _v["slug"]))
