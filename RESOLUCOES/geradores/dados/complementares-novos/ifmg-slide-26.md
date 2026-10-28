Resposta. Com a chamada inicial TORRE-HANOI(4, A, C, B) (origem = A, destino = C, auxiliar = B, como na figura do slide), a árvore de chamadas é binária completa com 4 níveis: 1 chamada com n = 4, 2 com n = 3, 4 com n = 2 e 8 com n = 1, num total de 15 nós, dos quais 7 internos (n ≥ 2) e 8 folhas (n = 1). Cada nó executa exatamente um movimento (linha 2 ou linha 5), logo são 15 movimentos; o disco 1 move-se 8 vezes, o disco 2 quatro, o disco 3 duas e o disco 4 uma. A ordem dos movimentos é a do percurso em ordem simétrica da árvore (subárvore esquerda, movimento do nó, subárvore direita). O número de chamadas (e o de movimentos) satisfaz C(1) = 1, C(n) = 2C(n − 1) + 1, cuja solução é C(n) = 2ⁿ − 1, e C(4) = 15.

INTERPRETAÇÃO DO ENUNCIADO.

O enunciado pede "uma árvore com as chamadas recursivas do algoritmo acima" para n = 4. Leituras possíveis: (i) a árvore de chamadas do Algoritmo 7, com os parâmetros de cada chamada; (ii) uma árvore de recursão de custos (cada nó rotulado pelo custo). Resolvo a leitura (i), que é a pedida literalmente ("árvore com as chamadas recursivas"), e acrescento em cada nó o movimento que ele executa, de onde sai também a leitura (ii) (custo 1 movimento por nó). O enunciado não fixa os pilares da chamada inicial; adoto os da figura do slide, em que os discos começam em A e terminam em C, passando por B: TORRE-HANOI(4, A, C, B). Qualquer outra escolha de pilares produz a mesma forma de árvore, apenas com os rótulos dos pilares permutados.

Observação sobre a figura: ela rotula os quatro quadros "H(4,A,B)", "m(A,C)", "H(4,B,C)". Pelo Algoritmo 7, as duas chamadas que a chamada com n = 4 faz têm parâmetro n − 1 = 3 (linhas 4 e 6); então o primeiro e o último quadro correspondem, no algoritmo, às chamadas TORRE-HANOI(3, A, B, C) e TORRE-HANOI(3, B, C, A), e "m(A,C)" é a linha 5, que move o disco 4 de A para C. A árvore abaixo segue o algoritmo.

ÁRVORE DE CHAMADAS (n = 4).

Notação: H(n, origem, destino, auxiliar) é a chamada TORRE-HANOI(n, origem, destino, auxiliar). Ao lado de cada nó está o movimento que ele executa e, entre colchetes, a posição desse movimento na sequência de execução (1 a 15). Filhos aparecem recuados abaixo do pai, na ordem em que são chamados (linha 4 e depois linha 6).

    H(4, A, C, B)  move disco 4: A → C  [8]
        H(3, A, B, C)  move disco 3: A → B  [4]
            H(2, A, C, B)  move disco 2: A → C  [2]
                H(1, A, B, C)  move disco 1: A → B  [1]   (folha)
                H(1, B, C, A)  move disco 1: B → C  [3]   (folha)
            H(2, C, B, A)  move disco 2: C → B  [6]
                H(1, C, A, B)  move disco 1: C → A  [5]   (folha)
                H(1, A, B, C)  move disco 1: A → B  [7]   (folha)
        H(3, B, C, A)  move disco 3: B → C  [12]
            H(2, B, A, C)  move disco 2: B → A  [10]
                H(1, B, C, A)  move disco 1: B → C  [9]   (folha)
                H(1, C, A, B)  move disco 1: C → A  [11]  (folha)
            H(2, A, C, B)  move disco 2: A → C  [14]
                H(1, A, B, C)  move disco 1: A → B  [13]  (folha)
                H(1, B, C, A)  move disco 1: B → C  [15]  (folha)

Como os filhos de cada nó foram obtidos: um nó H(n, o, d, x) com n ≥ 2 tem o teste da linha 1 falso e executa, nesta ordem, a linha 4, que chama H(n − 1, o, x, d) (filho esquerdo: origem e destino do pai, mas com destino e auxiliar trocados), a linha 5, que move o disco n de o para d, e a linha 6, que chama H(n − 1, x, d, o) (filho direito). Um nó H(1, o, d, x) tem o teste da linha 1 verdadeiro, move o disco 1 de o para d (linha 2) e não faz chamada: é folha. Por exemplo, a raiz H(4, A, C, B) tem filhos H(3, A, B, C) e H(3, B, C, A), e o nó H(3, B, C, A) tem filhos H(2, B, A, C) e H(2, A, C, B).

Atenção à ordem: a árvore está desenhada por pais e filhos, mas o movimento de um nó só acontece depois que toda a sua subárvore esquerda terminou (linha 5 vem depois da linha 4). Por isso a numeração [1] a [15] é a ordem simétrica da árvore, e não a ordem de cima para baixo do desenho.

SEQUÊNCIA DE MOVIMENTOS, NA ORDEM DE EXECUÇÃO.

     1: disco 1 A → B
     2: disco 2 A → C
     3: disco 1 B → C
     4: disco 3 A → B
     5: disco 1 C → A
     6: disco 2 C → B
     7: disco 1 A → B
     8: disco 4 A → C
     9: disco 1 B → C
    10: disco 2 B → A
    11: disco 1 C → A
    12: disco 3 B → C
    13: disco 1 A → B
    14: disco 2 A → C
    15: disco 1 B → C

Acompanhando os pilares (topo à direita), partindo de A = [4 3 2 1], B = [ ], C = [ ]: após o movimento 7 tem-se A = [4], B = [3 2 1], C = [ ] (os três discos menores foram para o auxiliar, que é exatamente o efeito de H(3, A, B, C)); o movimento 8 leva o disco 4 para C; após o movimento 15, A = [ ], B = [ ], C = [4 3 2 1]. Conferi passo a passo que nenhum dos 15 movimentos coloca um disco sobre um disco menor. (A correção do algoritmo para n geral não é pedida no exercício e não é provada aqui; a afirmação vale para esta execução com n = 4.)

CONTAGEM NA ÁRVORE DE n = 4.

Por níveis: nível 0 tem 1 nó (n = 4), nível 1 tem 2 nós (n = 3), nível 2 tem 4 nós (n = 2), nível 3 tem 8 nós (n = 1). Total de nós: 1 + 2 + 4 + 8 = 15 = 2⁴ − 1. Nós internos (n ≥ 2): 1 + 2 + 4 = 7 = 2³ − 1. Folhas (n = 1): 8 = 2³. Movimentos: um por nó, 15. Por disco: o disco k é movido exatamente pelos nós com parâmetro n = k (linha 2 se k = 1, linha 5 se k ≥ 2), e há 2^(4−k) desses nós; logo disco 4: 1, disco 3: 2, disco 2: 4, disco 1: 8, e 1 + 2 + 4 + 8 = 15, o que bate com a lista acima.

RELAÇÃO COM T(n) = 2T(n − 1) + 1.

Seja C(n) o número total de chamadas (nós da árvore, contando a própria chamada) e M(n) o número de movimentos executados por uma chamada TORRE-HANOI(n, o, d, x), para n ≥ 1 inteiro (o algoritmo não trata n = 0). Pela estrutura do algoritmo, C e M não dependem dos pilares o, d, x: dependem só de n. A leitura das linhas dá:

    C(1) = 1,  C(n) = 1 + 2C(n − 1) para n ≥ 2   (a própria chamada + as duas das linhas 4 e 6);
    M(1) = 1,  M(n) = 2M(n − 1) + 1 para n ≥ 2   (os movimentos das duas subchamadas + o da linha 5).

São a mesma recorrência T(n) = 2T(n − 1) + 1 com T(1) = 1. Na árvore, o "+1" é o próprio nó e o "2T(n − 1)" são as duas subárvores, cada uma de altura uma unidade menor.

Afirmação: para todo inteiro n ≥ 1, C(n) = M(n) = 2ⁿ − 1, e o número de folhas é F(n) = 2ⁿ⁻¹.

Prova por indução em n. P(n): "para quaisquer pilares distintos o, d, x, a chamada TORRE-HANOI(n, o, d, x) gera exatamente 2ⁿ − 1 chamadas no total (contando ela própria), executa exatamente 2ⁿ − 1 movimentos e a sua árvore tem exatamente 2ⁿ⁻¹ folhas". (P(n) é enunciada para quaisquer pilares porque as subchamadas usam pilares em outra ordem.)

Base, n = 1: o teste da linha 1 é verdadeiro; a chamada executa um movimento (linha 2) e nenhuma subchamada. Chamadas: 1 = 2¹ − 1. Movimentos: 1 = 2¹ − 1. Folhas: a própria chamada, 1 = 2⁰. P(1) vale.

Passo: seja n ≥ 2 e suponha P(n − 1) (hipótese de indução, para quaisquer pilares). A chamada TORRE-HANOI(n, o, d, x) tem o teste da linha 1 falso (n ≠ 1) e executa as linhas 4, 5 e 6: as subchamadas TORRE-HANOI(n − 1, o, x, d) e TORRE-HANOI(n − 1, x, d, o), com n − 1 ≥ 1, e um movimento. Pela hipótese aplicada a cada uma (com os pilares (o, x, d) e (x, d, o), respectivamente), cada subchamada gera 2ⁿ⁻¹ − 1 chamadas, executa 2ⁿ⁻¹ − 1 movimentos e tem 2ⁿ⁻² folhas. Logo:
chamadas = 1 + 2(2ⁿ⁻¹ − 1) = 2ⁿ − 1;
movimentos = 2(2ⁿ⁻¹ − 1) + 1 = 2ⁿ − 1;
folhas = 2 · 2ⁿ⁻² = 2ⁿ⁻¹ (a chamada em si não é folha, pois faz subchamadas).
Isso é P(n). Por indução, P(n) vale para todo n ≥ 1.

Para n = 4: C(4) = M(4) = 2⁴ − 1 = 15 e F(4) = 2³ = 8, como contado na árvore. Desenrolando a recorrência: T(4) = 2T(3) + 1 = 2(2T(2) + 1) + 1 = 4T(2) + 3 = 4(2T(1) + 1) + 3 = 8T(1) + 7 = 15; os coeficientes 1, 2, 4, 8 são os números de nós por nível, e 7 = 1 + 2 + 4 é o número de nós internos.

ORDEM DE CRESCIMENTO.

Tomando como custo o número de movimentos (ou de chamadas; cada chamada faz, fora das subchamadas, um teste e um movimento, isto é, trabalho limitado por uma constante), T(n) = 2ⁿ − 1 ∈ Θ(2ⁿ). Testemunhas: c₁ = 1/2, c₂ = 1, n₀ = 1, isto é, para todo n ≥ 1, (1/2)·2ⁿ ≤ 2ⁿ − 1 ≤ 1·2ⁿ.
Lado direito: 2ⁿ − 1 ≤ 2ⁿ, pois −1 ≤ 0.
Lado esquerdo: 2ⁿ − 1 ≥ 2ⁿ⁻¹ equivale a 2ⁿ⁻¹ ≥ 1, verdadeiro para n ≥ 1.
Em n = n₀ = 1 exatamente: (1/2)·2 = 1 ≤ 2¹ − 1 = 1 ≤ 2. Vale (com igualdade à esquerda).
Esse valor vale para toda entrada de tamanho n, não só no pior caso: o algoritmo não toma decisão que dependa de outra coisa além de n, então melhor caso, pior caso e qualquer caso coincidem.

Conferência numérica (Python; não faz parte da prova): a execução literal do Algoritmo 7 com TORRE-HANOI(4, A, C, B) lista exatamente as 15 chamadas da árvore acima com os mesmos parâmetros e a mesma relação pai–filho (indentação), e os 15 movimentos na mesma ordem da sequência numerada 1 a 15: 15 chamadas e 15 movimentos, o que coincide com C(4) = M(4) = 2⁴ − 1 = 15.
