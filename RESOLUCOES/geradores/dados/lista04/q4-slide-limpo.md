# Exercício do slide (UNICAMP MC458, Exemplo 3) — resposta limpa, para verificação adversarial

## ENUNCIADO / CONTEXTO (literal do slide)
Problema: dada uma árvore binária A com n nós, calcular os fatores de balanceamento (f.b.) de
cada nó. O f.b. de um nó é a altura da subárvore esquerda menos a altura da subárvore direita.
Convenção: árvore vazia tem altura −1 e f.b. zero.

Algoritmo obtido pela hipótese de indução fortalecida ("sabemos calcular f.b. E ALTURAS de
árvores com menos que n nós"):

    FatorAltura(A)
    ▷ Entrada: uma árvore binária A com n ≥ 0 nós
    ▷ Saída: a árvore A com os f.b.s nos seus nós, e a altura de A
    1. se n = 0 então h ← −1
    2. senão
    3.     seja r a raiz de A
    4.     he ← FatorAltura(Ae)
    5.     hd ← FatorAltura(Ad)
    6.     ▷ armazena o f.b. da raiz em r.f
    7.     r.f ← he − hd
    8.     h ← max(he, hd) + 1
    9. devolva h

Análise do slide, literal: "Seja T(n) o número de operações executadas pelo algoritmo para
calcular os f.b.s e a altura de uma árvore A de n nós. Então T(n) = Θ(1) se n = 0, e
T(n) = T(ne) + T(nd) + Θ(1) se n > 0, onde ne, nd são os números de nós das subárvores esquerda
e direita." E: "O pior caso da recorrência parece ser quando, ao longo da recursão, um de ne, nd
é sempre igual a zero (e o outro é sempre igual a n − 1). Chega-se então a
T(n) = T(1) + Σ(i=2 até n) Θ(1) = (n + 1)Θ(1) + nΘ(1) ∈ Θ(n)."

EXERCÍCIO: "Há algum ganho em complexidade quando ambos ne e nd são aproximadamente n/2 ao
longo da recursão?"

## SOLUÇÃO FINAL

### 0. Modelo de custo
Duas constantes positivas, fixas e uniformes sobre todas as chamadas (é o que os Θ(1) do slide
escondem; explicitá-las é necessário para somar um número variável delas):
  a > 0 : custo de uma chamada FatorAltura(A) com A vazia (linha 1 e a devolução).
  b > 0 : custo da parte não recursiva de uma chamada com A não vazia (linha 1 e linhas
          3, 7, 8, 9).
Nenhuma depende de n, da forma da árvore, nem da posição do nó na recursão.
Recorrência estrutural exata:
  T(A) = a,                          se A é vazia;
  T(A) = b + T(Ae) + T(Ad),          se A tem raiz r e subárvores Ae, Ad.

### 1. O caso balanceado pelo Teorema Mestre (Brassard & Bratley)
Quando ne ≈ nd ≈ n/2 ao longo de toda a recursão, a recorrência vira T(n) = 2·T(n/2) + Θ(1).
As constantes a e b já estão ocupadas pelos custos da §0, então escrevo daqui em diante os
parâmetros do teorema como α (número de chamadas recursivas), β (fator de redução) e k, na forma
T(n) = α·T(n/β) + c·n^k, com o critério α ≷ β^k.
Para aplicar o teorema nessa forma é preciso um termo motor literalmente c·n^k. Substituindo o
Θ(1) por constantes explícitas: existem d1, d2 > 0 com
d1 ≤ (custo não recursivo de uma chamada) ≤ d2 (basta d1 = min(a,b), d2 = max(a,b), com a e b os
custos da §0); logo 2T(n/2) + d1 ≤ T(n) ≤ 2T(n/2) + d2, e cada lado é uma recorrência na forma
exigida com k = 0, porque c·n^0 = c é constante.
Parâmetros: α = 2 (linhas 4 e 5: esquerda E direita são visitadas); β = 2 (cada subárvore tem
≈ n/2 nós); k = 0 (o trabalho fora da recursão é constante).
Comparação: β^k = 2^0 = 1, e α = 2. Portanto α > β^k.
Conclusão — é o caso α > β^k, que no formulário entregue na prova aparece como o terceiro dos
três (a ordem impressa é a < b^k, a = b^k, a > b^k):
T(n) = Θ(n^(log_β α)) = Θ(n^(log_2 2)) = Θ(n^1) = Θ(n).
Aplicando à cota inferior (c = d1) obtém-se Ω(n) e à superior (c = d2) obtém-se O(n); juntas,
Θ(n).
Ressalva: nessa formulação o resultado é enunciado para n potência exata de β (aqui, potência
de 2) e estendido pela regularidade de n^k; "n/2" ignora pisos e tetos. O argumento da §3 dispensa a ressalva: dá o
custo exato, com pisos e tetos incluídos, para qualquer n e qualquer forma.

Conferência independente pela árvore de recursão: numa árvore perfeita com n = 2^m − 1 nós, o
nível i da recursão tem 2^i chamadas com árvore não vazia, para i = 0,…,m−1, e o nível m tem
2^m chamadas com árvore vazia. Somando as progressões geométricas em forma fechada:
chamadas não vazias 2^0 + 2^1 + … + 2^(m−1) = 2^m − 1 = n; chamadas vazias 2^m = n + 1;
custo total b·n + a·(n+1). Bate com o resultado geral da §3, e é Θ(n).

### 2. O caso degenerado (cadeia), já resolvido pelo slide
Quando um dos filhos é sempre vazio, T(n) = T(n−1) + T(0) + b. Desenrolando, com T(0) = a:
  T(n) = T(n−1) + a + b = T(n−2) + 2(a+b) = … = T(0) + n(a+b) = a + n(a+b) = (n+1)a + n·b.
Isto é Θ(n) — e é literalmente a expressão "(n+1)Θ(1) + nΘ(1)" que o slide escreveu.

### 3. A razão estrutural: a forma da árvore é irrelevante para o custo

3.1 Teorema (custo exato). Para toda árvore binária A com n ≥ 0 nós,
    T(A) = (n+1)·a + n·b, qualquer que seja a forma de A.
Prova, por indução forte em n.
Base (n = 0): A é vazia; por definição T(A) = a. A fórmula dá (0+1)a + 0·b = a. ✓
Passo (n ≥ 1): suponha a fórmula válida para toda árvore com estritamente menos que n nós
(hipótese forte — necessária, porque não se sabe como os n−1 nós se repartem). Seja A com n nós,
raiz r, subárvores Ae com ne nós e Ad com nd nós. Como a raiz não está em nenhuma das duas,
ne + nd = n − 1; e como n ≥ 1 vale ne ≤ n−1 < n e nd ≤ n−1 < n, logo a hipótese se aplica às
duas. Então
  T(A) = b + T(Ae) + T(Ad)
       = b + [(ne+1)a + ne·b] + [(nd+1)a + nd·b]
       = b + (ne + nd + 2)·a + (ne + nd)·b
       = b + (n+1)·a + (n−1)·b        [usando ne + nd = n − 1]
       = (n+1)·a + n·b. ∎

Corolário (contagem de chamadas). Tomando a = b = 1, o número total de invocações de
FatorAltura numa árvore de n nós é exatamente 2n + 1: n chamadas com árvore não vazia (uma por
nó — cada nó é raiz de exatamente uma chamada) e n + 1 chamadas com árvore vazia. As n+1
chamadas vazias são exatamente os n+1 ponteiros nulos de uma árvore binária com n nós — segundo
cruzamento de conferência. Casos pequenos: n = 0 → 1 chamada; n = 1 → 3 chamadas (a raiz e os
dois filhos vazios) = 2·1+1.

3.2 Consequência: T(n) está bem definida. Escrever "T(n)" para um algoritmo cujo custo depende
da forma da entrada normalmente só faz sentido como pior caso sobre todas as formas. Aqui o
custo depende só de n, então T(n) é função genuína de n, e pior caso = melhor caso = caso médio.

3.3 Testemunhas numéricas para Θ(n). Seja T(n) = (a+b)·n + a, com a, b > 0.
Afirmação: T(n) = Θ(n) com c1 = a + b, c2 = 2a + b e n0 = 1.
 Cota inferior: T(n) = (a+b)n + a ≥ (a+b)n, pois a > 0. Vale para todo n ≥ 0.
 Cota superior: para n ≥ 1 tem-se a ≤ a·n, logo T(n) = (a+b)n + a ≤ (a+b)n + a·n = (2a+b)n.
Conferência em n = n0 = 1 exatamente: T(1) = (a+b)·1 + a = 2a + b.
 cota inferior c1·1 = a + b ≤ 2a + b ⟺ 0 ≤ a ✓ (estrito, pois a > 0);
 cota superior c2·1 = 2a + b ≥ 2a + b ✓ (com igualdade — c2 não pode ser menor com este n0).
Instância concreta (custo unitário, a = b = 1): T(n) = 2n + 1, c1 = 2, c2 = 3, n0 = 1.
 Em n = 1: T(1) = 3, e 2 ≤ 3 ≤ 3 ✓. Em n = 5: T(5) = 11, e 10 ≤ 11 ≤ 15 ✓.

3.4 Por que tinha de ser assim. O algoritmo faz, por nó, uma quantidade fixa de trabalho: uma
subtração (he − hd), um max, uma soma. Nenhum nó é visitado duas vezes e nenhum é pulado — é um
percurso em pós-ordem disfarçado de recorrência. Um percurso completo custa proporcional ao
número de nós, e o número de nós é n seja qual for a forma. A forma redistribui as n unidades de
trabalho entre os níveis, mas não muda quantas são.
Contraste que torna isso não trivial: se o passo de combinação custasse Θ(tamanho da subárvore)
em vez de Θ(1) — como no MergeSort —, a forma importaria muito: cadeia daria Θ(n²) e balanceada
daria Θ(n lg n). O que anula o efeito da forma aqui é especificamente o custo de combinação ser
constante.

3.5 Cota inferior do problema. Qualquer algoritmo correto precisa escrever um f.b. em cada um
dos n nós, portanto executa Ω(n) operações (testemunhas: ≥ 1 escrita por nó, logo ≥ 1·n
operações para todo n ≥ 1, isto é c = 1, n0 = 1). Como FatorAltura é O(n), ele é
assintoticamente ótimo. Nenhum balanceamento baixa a classe: o gargalo é o tamanho da saída.

### 4. O que muda e o que não muda com o balanceamento
| Aspecto | Cadeia | Balanceada (ne ≈ nd ≈ n/2) | Muda? |
| Tempo assintótico | Θ(n) | Θ(n) | Não |
| Número exato de chamadas | 2n + 1 | 2n + 1 | Não — idênticos, não só "mesma classe" |
| Custo exato | (n+1)a + n·b | (n+1)a + n·b | Não |
| Profundidade máxima da recursão | n + 1 quadros = Θ(n) | ⌊lg n⌋ + 2 quadros no split perfeito, Θ(lg n) em qualquer split de fração constante | Sim, drasticamente |
| Risco de estouro de pilha | alto para n grande | praticamente nulo | Sim |

Profundidade da pilha. Os quadros simultaneamente ativos formam um caminho da raiz até uma
chamada vazia. Numa cadeia de n nós, o caminho mais longo tem os n nós mais a chamada vazia
final: n + 1 quadros. Numa árvore perfeitamente balanceada de altura h = ⌊lg n⌋ (em arestas),
são h + 1 nós no caminho mais a chamada vazia: ⌊lg n⌋ + 2 quadros. Conferindo em n = 1: cadeia
dá 1+1 = 2; balanceada dá ⌊lg 1⌋ + 2 = 0 + 2 = 2 ✓ (coincidem, como deve ser, pois com um nó só
as duas formas são a mesma árvore).
Para n = 10^6 é a diferença entre 10^6 + 1 quadros na pilha (estouro certo na maioria dos
ambientes) e ⌊lg 10^6⌋ + 2 = 21 quadros. Não é ganho de complexidade de tempo; é ganho de complexidade de
espaço auxiliar, de Θ(n) para Θ(lg n). Dizer "Θ(n) nos dois casos, logo tanto faz" seria uma
resposta errada por omissão.

Por que não é como a busca binária. A busca binária tem T(n) = T(n/2) + Θ(1), ou seja α = 1,
β = 2, k = 0, β^k = 1; aqui α = β^k, que é o segundo caso do Teorema Mestre, dando
Θ(n^k lg n) = Θ(lg n). A queda para logarítmico vem de α = 1: a busca binária descarta uma das
metades. FatorAltura tem α = 2: desce nas duas metades e não descarta nada, porque precisa do
f.b. de todo mundo. Balancear divide bem o trabalho entre os ramos, mas não elimina trabalho — e
é a eliminação, não a divisão equilibrada, que produz ganho assintótico.

### 5. Sobre a contagem escrita no slide
(i) O resultado final do slide está exatamente certo. A expressão "(n+1)Θ(1) + nΘ(1)"
corresponde termo a termo ao provado: n + 1 chamadas com árvore vazia (custo a cada uma) e n
chamadas com árvore não vazia (custo b cada). Não é aproximação: é o custo exato, e vale para
qualquer forma, não só para a cadeia.
(ii) O passo intermediário é abreviado, não errado. O slide escreve
T(n) = T(1) + Σ_{i=2}^{n} Θ(1), e isso de fato liga os extremos: cada Θ(1) da soma é o incremento
de um passo do desenrolar, que já embute o T(0) do filho vazio, de modo que
T(1) + (n−1)·(T(0) + b) = (2a + b) + (n−1)(a + b) = (n+1)a + n·b — exatamente o lado direito que
o slide escreve. (Conferido numericamente para n = 1…25.) Objetar que "a soma tem n−1 parcelas e
o total tem 2n+1" seria contar parcelas, e Θ(1) não se compromete com constante nenhuma.
O que vale registrar é outra coisa: somar um número variável de termos Θ(1) só é legítimo porque
existe uma constante uniforme limitando todos eles — aqui max(a, b) —, e essa uniformidade não
está na notação, está no algoritmo. E o caso base declarado na recorrência é n = 0, não n = 1:
parar em T(1) é atalho legítimo, mas é preciso saber que T(1) = 2a + b, e não a.
(iii) O slide diz "o pior caso da recorrência parece ser quando um de ne, nd é sempre zero". O
teorema da §3 mostra que, no modelo de contagem de operações, não há pior caso de forma: toda
árvore com n nós custa exatamente o mesmo. A cadeia é o pior caso para outra grandeza — a
profundidade da pilha —, não para o tempo. O "parece ser" do slide é prudente, e o exercício é o
convite a descobrir que a suspeita não se confirma no tempo.

## RESPOSTA
Não há ganho algum de complexidade de tempo. Pelo Teorema Mestre (Brassard & Bratley), o caso
balanceado T(n) = 2T(n/2) + Θ(1) tem α = 2, β = 2, k = 0, β^k = 1 e, como α > β^k, resulta
Θ(n^(log_2 2)) = Θ(n) — a mesma classe do caso degenerado. De fato o custo é idêntico, e não
apenas da mesma ordem: toda árvore com n nós gera exatamente 2n+1 chamadas e custo
(n+1)a + n·b, com a e b as constantes de custo da §0 (no modelo unitário a = b = 1, o que dá
justamente 2n+1), seja qual for sua forma. O que o balanceamento melhora, e melhora muito, é a
profundidade máxima da recursão, que cai de Θ(n) para Θ(lg n) — ganho de espaço de pilha (e de
robustez contra estouro), não de tempo.

### Ressalvas declaradas
- A conta de profundidade de pilha supõe o modelo usual de recursão com um quadro por chamada
  ativa e sem otimização de chamada em cauda. A chamada da linha 5 não está em posição de cauda
  (a linha 7 usa he), então nenhuma otimização razoável elimina a pilha aqui.
- Adota-se o modelo de custo uniforme (uma subtração, um max e uma soma custam Θ(1)
  independentemente da magnitude das alturas), que é o modelo RAM do CLRS 3ª ed., §2.2.
