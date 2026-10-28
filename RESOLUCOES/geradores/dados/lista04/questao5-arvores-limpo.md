# Lista 4 (versão de 09/09/2026) — Questão 5 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Questão 5. Considere a proposição P(n): Toda árvore com n vértices possui exatamente
n-1 arestas.
Um estudante apresentou a seguinte prova por indução.
Caso base. Para n = 1, uma árvore possui um único vértice e nenhuma aresta. Portanto,
0 = 1 − 1,
e a afirmação é verdadeira para n = 1.
Hipótese de indução. Suponha que toda árvore com n vértices possua exatamente n−1 arestas.
Passo indutivo. Considere uma árvore T com n vértices. Pela hipótese de indução, T possui
n − 1 arestas. Acrescente a T um novo vértice v e ligue-o, por meio de uma única aresta, a
algum vértice de T. O novo vértice v é uma folha, e o grafo resultante continua sendo uma
árvore.
Assim, a nova árvore possui n + 1 vértices e
(n − 1) + 1 = n
arestas. Como
n = (n + 1) − 1,
conclui-se que toda árvore com n + 1 vértices possui n arestas. Logo, pelo princípio da
indução matemática, toda árvore com n vértices possui exatamente n − 1 arestas.
Pergunta: Embora a afirmação seja verdadeira, a prova acima é logicamente incorreta.
Identifique precisamente o erro no passo indutivo e explique por que a construção
apresentada não é suficiente para demonstrar que toda árvore com n + 1 vértices possui
n arestas."

## SOLUÇÃO FINAL

### Convenções
Grafo simples, finito. Árvore = grafo conexo e acíclico. Folha = vértice de grau 1.
n é inteiro, n ≥ 1.

### 1. O que o passo indutivo precisa provar
Fixado n ≥ 1 e suposta a hipótese de indução, o passo precisa estabelecer P(n+1), que é
uma afirmação universal:
  P(n+1):  para TODA árvore T' com n + 1 vértices, |E(T')| = n.
Para provar uma afirmação universal, parte-se de um objeto ARBITRÁRIO da classe — uma
árvore T' qualquer com n + 1 vértices — e mostra-se que ele tem a propriedade.

### 2. O que o passo do estudante efetivamente prova
O texto parte de uma árvore T com n vértices, escolhe um vértice u de T, e forma
T + v (novo vértice v e aresta uv). Mostra que T + v tem (n − 1) + 1 = n arestas. O que
fica provado é:
  para toda árvore T com n vértices e todo vértice u de T, a árvore T + v tem n arestas.
Isto é, a propriedade vale para as árvores de n + 1 vértices QUE SÃO OBTIDAS por esta
construção. A frase final — "conclui-se que toda árvore com n + 1 vértices possui n
arestas" — troca "toda árvore construída assim" por "toda árvore". Essa troca só seria
legítima se estivesse provado que TODA árvore com n + 1 vértices pode ser obtida
pendurando uma folha em alguma árvore de n vértices. Esse fato não é enunciado nem
provado em lugar nenhum do texto.

### 3. O erro, com precisão
O passo começa numa árvore de n vértices e CONSTRÓI uma de n + 1 (n → n + 1). Construir
não é, por si só, inválido; mas, assim, o passo cobre apenas a imagem da construção, e
conclui sobre a classe inteira sem mostrar que a imagem é a classe inteira. O caminho que
evita essa lacuna é o inverso: começar numa árvore ARBITRÁRIA de n + 1 vértices e
REDUZI-LA a uma de n vértices, onde a hipótese se aplica (n + 1 → n).
É um erro de quantificador: prova-se "∀T ∀u: T + v tem n arestas" e conclui-se
"∀T' com n + 1 vértices: T' tem n arestas", sem o elo "∀T' ∃T ∃u: T' = T + v" (igualdade a
menos do nome dos vértices).
(Esse padrão é conhecido em inglês como *build-up error*, "erro de construção".)

### 4. Por que a construção não basta: a mesma forma de argumento prova uma falsidade
Se o argumento do estudante fosse válido pela sua forma, a mesma forma provaria qualquer
coisa com a mesma estrutura. Considere a afirmação FALSA
  C(n): todo grafo com n vértices, todos de grau ≥ 1, é conexo   (n ≥ 2).
"Prova" com a mesma forma:
- Base (n = 2): o único grafo simples com 2 vértices, ambos de grau ≥ 1, é a aresta única,
  que é conexo. C(2) vale.
- Hipótese: todo grafo com n vértices, todos de grau ≥ 1, é conexo.
- "Passo": tome um grafo G com n vértices, todos de grau ≥ 1; pela hipótese, G é conexo.
  Acrescente um novo vértice v ligado por uma aresta a algum vértice de G. O novo grafo tem
  n + 1 vértices, todos de grau ≥ 1, e é conexo (v está ligado a G, que é conexo). "Logo"
  todo grafo com n + 1 vértices, todos de grau ≥ 1, é conexo.
Mas C(4) é falsa: o grafo com vértices {1, 2, 3, 4} e arestas {1,2} e {3,4} tem todos os
graus iguais a 1 e não é conexo. A construção nunca produz esse grafo: ela parte de um
grafo de 3 vértices com todos os graus ≥ 1, e remover qualquer vértice de {1,2},{3,4}
deixa um vértice de grau 0 — logo ele não é imagem da construção. O passo "construtivo"
só enxergou os grafos que ele mesmo gera.
Portanto a forma de argumento usada pelo estudante é inválida; que a proposição P(n) sobre
árvores seja verdadeira é um fato que a prova do estudante não estabelece.

### 5. O conserto: partir de uma árvore arbitrária com n + 1 vértices

**Lema 1.** Toda árvore com m ≥ 2 vértices tem uma folha.
Prova. Seja T' árvore com m ≥ 2 vértices. Como T' é conexa e tem pelo menos dois vértices,
tem pelo menos uma aresta; logo existem caminhos com pelo menos uma aresta. Seja
P = x₀x₁…x_k um caminho de comprimento máximo em T' (existe, pois T' é finita e todo
caminho tem no máximo m vértices); k ≥ 1. Todo vizinho de x₀ está em P: se x₀ tivesse um
vizinho y fora de P, yx₀x₁…x_k seria caminho mais longo. Se x₀ fosse vizinho de x_i com
i ≥ 2, então x₀x₁…x_i x₀ seria um ciclo, impossível em árvore. Logo o único vizinho de x₀
é x₁, e grau(x₀) = 1. ∎

**Lema 2.** Se v é folha de uma árvore T' com m ≥ 2 vértices, então T' − v (remove-se v e
a única aresta incidente a v) é uma árvore com m − 1 vértices.
Prova. Acíclico: todo ciclo de T' − v seria ciclo de T'. Conexo: sejam x, y vértices de
T' − v. Em T' existe um caminho de x a y. Um vértice interno de um caminho tem grau ≥ 2
dentro dele; como grau(v) = 1 e v ∉ {x, y}, v não está nesse caminho, que portanto está
inteiro em T' − v. ∎

**Passo correto.** Seja n ≥ 1 e suponha a hipótese de indução (toda árvore com n vértices
tem n − 1 arestas). Seja T' uma árvore ARBITRÁRIA com n + 1 vértices. Como n + 1 ≥ 2,
pelo Lema 1 T' tem uma folha v. Pelo Lema 2, T = T' − v é árvore com n vértices; pela
hipótese de indução, |E(T)| = n − 1. Como v tem grau 1, T' tem exatamente uma aresta a mais
que T: |E(T')| = (n − 1) + 1 = n. Como T' era arbitrária, P(n+1) vale. Com a base do
estudante (que está correta), a indução fica completa. ∎

### 6. Observações
- Para árvores, a imagem da construção É a classe inteira: pelos Lemas 1 e 2, toda árvore
  T' com n + 1 ≥ 2 vértices é (T' − v) + v. Por isso a conclusão é verdadeira. Mas esse fato
  é exatamente o conteúdo dos Lemas 1 e 2 — o trabalho que o estudante deixou de fazer.
- A afirmação do estudante de que "o grafo resultante continua sendo uma árvore" é
  verdadeira (conexo porque v se liga a T conexa; acíclico porque um ciclo passando por v
  exigiria grau(v) ≥ 2, e um ciclo que não passa por v estaria inteiro em T, que é
  acíclica), mas foi dada sem justificativa. É uma lacuna menor; não é ela que
  invalida a prova.
- A base e a hipótese de indução do estudante estão corretas; o erro está só no passo.

## RESPOSTA
O erro está no passo indutivo: ele parte de uma árvore T com n vértices e constrói, pendurando
uma folha, UMA árvore com n + 1 vértices; prova assim a propriedade apenas para as árvores de
n + 1 vértices obtidas por essa construção, e conclui para TODAS, sem provar que toda árvore
com n + 1 vértices pode ser obtida assim. P(n+1) é universal e exige partir de uma árvore
ARBITRÁRIA T' com n + 1 vértices; o caminho natural é reduzi-la a n vértices. A construção
não basta porque a mesma forma de argumento "prova" a afirmação falsa "todo grafo com
n ≥ 2 vértices, todos de grau ≥ 1, é conexo" (contraexemplo: duas arestas disjuntas,
4 vértices). O conserto: toda árvore com
n + 1 ≥ 2 vértices tem uma folha v (caminho máximo), T' − v é árvore com n vértices, e a
hipótese dá |E(T')| = (n − 1) + 1 = n.
