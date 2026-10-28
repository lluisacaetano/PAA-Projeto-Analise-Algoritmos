Resposta. A primeira chamada deve ser ORDENACAO-POR-SELECAO(V, n), com V o vetor inteiro e j = n = número de elementos de V; para o vetor dado, ORDENACAO-POR-SELECAO(V, 10). O parâmetro j é o tamanho do prefixo V[1..j] que ainda não está ordenado, e no início nada está ordenado. Executando o algoritmo, há 10 chamadas (j = 10, 9, …, 1). Em cada chamada com j ≥ 2, o maior elemento de V[1..j] vai para a posição j. Os estados sucessivos são: [10, 2, 13, 22, 8, 3, 12, 9, 1, 50] → (j=10, sem mudança) → (j=9) [10, 2, 13, 1, 8, 3, 12, 9, 22, 50] → (j=8) [10, 2, 9, 1, 8, 3, 12, 13, 22, 50] → (j=7, sem mudança) → (j=6) [3, 2, 9, 1, 8, 10, 12, 13, 22, 50] → (j=5) [3, 2, 8, 1, 9, 10, 12, 13, 22, 50] → (j=4) [3, 2, 1, 8, 9, 10, 12, 13, 22, 50] → (j=3) [1, 2, 3, 8, 9, 10, 12, 13, 22, 50] → (j=2, sem mudança) → (j=1, caso base) devolve [1, 2, 3, 8, 9, 10, 12, 13, 22, 50].

INTERPRETAÇÃO.
A primeira pergunta pode ser lida de duas formas: (i) quais argumentos passar na chamada inicial; (ii) o que acontece nessa chamada. Respondo (i), que é o que "como deve ser a primeira chamada" pede, e uso (ii) para justificar. A segunda pergunta pede a execução literal do Algoritmo 6 a partir dessa chamada, mostrando o vetor depois de cada troca (linhas 10–12). Convenções do próprio código: os índices começam em 1; a comparação da linha 6 é estrita (>), então, em caso de empate, fica o primeiro índice (no vetor dado não há valores repetidos). As trocas das linhas 10–12 e a chamada da linha 13 atuam sobre o mesmo V: o vetor é passado por referência e ordenado no lugar. É por isso que o ramo else não precisa de return: quando a recursão termina, quem chamou já vê o V ordenado.

PARTE 1 — O QUE O PARÂMETRO j SIGNIFICA E POR QUE A PRIMEIRA CHAMADA É (V, n).
Na chamada com parâmetro j, o laço das linhas 5–9 percorre só V[1..j]. As linhas 10–12 trocam V[j] com V[indice], e a linha 13 chama de novo com j − 1. Então j é o fim do trecho que ainda falta ordenar. O trecho V[j+1..n] já está pronto e não é mais tocado.

Invariante da recursão. Na chamada com parâmetro j, valem: (a) V é uma permutação do vetor original; (b) V[j+1..n] está em ordem crescente; (c) todo elemento de V[1..j] é ≤ todo elemento de V[j+1..n].

Para que a primeira chamada satisfaça o invariante com qualquer vetor de entrada, o trecho "pronto" V[j+1..n] tem de ser vazio, e isso exige j = n. Com j = n, as condições (b) e (c) valem por vacuidade e (a) vale trivialmente.

Por que nenhum outro valor serve:
    j < n: as posições j+1..n nunca são examinadas (todas as chamadas usam índices ≤ j). Contraexemplo: V = [2, 1] com j = 1 cai direto no caso base e devolve [2, 1], que não está ordenado. (Com o vetor deste slide, a chamada (V, 9) por acaso daria certo, porque V[10] = 50 já é o máximo. Isso é coincidência desta entrada e não justifica j = 9.)
    j > n: a linha 6 acessa V[n+1], fora do vetor.
    j = 0 (ou j < 1): o teste da linha 1 falha, o laço da linha 5 não executa e a linha 10 acessa V[0], fora do vetor. Além disso, j − 1 nunca chega a 1, então a recursão não para.

Para ver que j = n de fato ordena, verifica-se o passo do invariante. Suponha (a), (b), (c) na chamada com j ≥ 2. Invariante do laço: depois da iteração i, V[indice] é o máximo de V[1..i]. Vale com i = 1, porque indice = 1. Se vale para i − 1, a linha 6 troca indice por i exatamente quando V[i] é maior que o máximo de V[1..i−1]. Ao fim do laço, V[indice] = máx V[1..j]. As linhas 10–12 trocam V[j] com esse máximo. Isso preserva (a); deixa V[j] ≥ todo elemento de V[1..j−1]; e, por (c), V[j] ≤ todo elemento de V[j+1..n]. Logo V[j..n] fica crescente e todo elemento de V[1..j−1] é ≤ todo elemento de V[j..n]. Esse é o invariante para a chamada com j − 1. No caso base j = 1, (b) diz que V[2..n] está crescente e (c) diz que V[1] ≤ V[2..n]. Logo V inteiro está ordenado. Partindo de j = n, isso vale para toda entrada com n ≥ 1.

PARTE 2 — EXECUÇÃO LITERAL COM V = [10, 2, 13, 22, 8, 3, 12, 9, 1, 50] E PRIMEIRA CHAMADA (V, 10).
Em cada chamada mostro a varredura da linha 6 (quando indice muda), a troca das linhas 10–12 e o vetor depois da troca. Os elementos já na posição final aparecem depois da barra "|".

CHAMADA j = 10.
    Varredura de V[1..10] = 10, 2, 13, 22, 8, 3, 12, 9, 1, 50: indice = 1 (10); i = 3: 13 > 10, indice = 3; i = 4: 22 > 13, indice = 4; i = 10: 50 > 22, indice = 10. Os outros i não mudam indice.
    Troca V[10] ↔ V[10] (o elemento troca consigo mesmo).
    V = [10, 2, 13, 22, 8, 3, 12, 9, 1 | 50]

CHAMADA j = 9.
    Varredura de V[1..9] = 10, 2, 13, 22, 8, 3, 12, 9, 1: indice = 1 → 3 (13) → 4 (22). Máximo 22 em V[4].
    Troca V[9] = 1 ↔ V[4] = 22.
    V = [10, 2, 13, 1, 8, 3, 12, 9 | 22, 50]

CHAMADA j = 8.
    Varredura de V[1..8] = 10, 2, 13, 1, 8, 3, 12, 9: indice = 1 → 3 (13). Máximo 13 em V[3].
    Troca V[8] = 9 ↔ V[3] = 13.
    V = [10, 2, 9, 1, 8, 3, 12 | 13, 22, 50]

CHAMADA j = 7.
    Varredura de V[1..7] = 10, 2, 9, 1, 8, 3, 12: indice = 1 → 7 (12 > 10). Máximo 12 em V[7].
    Troca V[7] ↔ V[7] (o elemento troca consigo mesmo).
    V = [10, 2, 9, 1, 8, 3 | 12, 13, 22, 50]

CHAMADA j = 6.
    Varredura de V[1..6] = 10, 2, 9, 1, 8, 3: nenhum supera 10, indice = 1.
    Troca V[6] = 3 ↔ V[1] = 10.
    V = [3, 2, 9, 1, 8 | 10, 12, 13, 22, 50]

CHAMADA j = 5.
    Varredura de V[1..5] = 3, 2, 9, 1, 8: indice = 1 → 3 (9). Máximo 9 em V[3].
    Troca V[5] = 8 ↔ V[3] = 9.
    V = [3, 2, 8, 1 | 9, 10, 12, 13, 22, 50]

CHAMADA j = 4.
    Varredura de V[1..4] = 3, 2, 8, 1: indice = 1 → 3 (8). Máximo 8 em V[3].
    Troca V[4] = 1 ↔ V[3] = 8.
    V = [3, 2, 1 | 8, 9, 10, 12, 13, 22, 50]

CHAMADA j = 3.
    Varredura de V[1..3] = 3, 2, 1: nenhum supera 3, indice = 1.
    Troca V[3] = 1 ↔ V[1] = 3.
    V = [1, 2 | 3, 8, 9, 10, 12, 13, 22, 50]

CHAMADA j = 2.
    Varredura de V[1..2] = 1, 2: indice = 1 → 2 (2 > 1). Máximo 2 em V[2].
    Troca V[2] ↔ V[2] (o elemento troca consigo mesmo).
    V = [1 | 2, 3, 8, 9, 10, 12, 13, 22, 50]

CHAMADA j = 1.
    Caso base (linhas 1–2): devolve V = [1, 2, 3, 8, 9, 10, 12, 13, 22, 50], que está ordenado.

Resumo da execução: 10 chamadas. As chamadas com j = 10, 7 e 2 trocam um elemento consigo mesmo, então o vetor não muda nelas. As seis chamadas com j = 9, 8, 6, 5, 4, 3 alteram o vetor. A linha 6 executa j vezes na chamada com parâmetro j ≥ 2 (para i = 1, …, j) e nenhuma vez no caso base. No total, para n = 10, são 2 + 3 + … + 10 = 10·11/2 − 1 = 54 comparações entre elementos. Esse número vale para qualquer vetor de 10 elementos, porque o laço não para antes do fim.

Conferência numérica (Python; não faz parte da prova): a simulação do Algoritmo 6 com a primeira chamada (V, 10) confirma, chamada por chamada, os mesmos índices do máximo (10, 4, 3, 7, 1, 3, 3, 1, 2), as mesmas trocas, os mesmos vetores intermediários e o resultado final [1, 2, 3, 8, 9, 10, 12, 13, 22, 50] ordenado (True). A justificativa de j = n e o invariante não dependem da simulação.
