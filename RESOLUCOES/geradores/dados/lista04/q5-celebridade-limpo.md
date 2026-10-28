# Problema da celebridade (slides UNICAMP MC458, Exemplo 4) — resposta limpa, para verificação adversarial

## ENUNCIADO (transcrição literal do slide)
"Num conjunto S de n pessoas, uma celebridade é alguém que é conhecido por todas as pessoas de S
mas que não conhece ninguém. Note que pode existir no máximo uma celebridade em S.
Para um conjunto de n pessoas, associamos uma matriz n × n M tal que M[i, j] = 1 se a pessoa i
conhece a pessoa j e M[i, j] = 0 caso contrário. Problema: dado um conjunto de n pessoas e a
matriz associada M, encontrar (se existir) uma celebridade no conjunto. Isto é, determinar um k
tal que todos os elementos da coluna k (exceto M[k, k]) são 1s e todos os elementos da linha k
(exceto M[k, k]) são 0s.
Existe uma solução simples mas laboriosa: para cada pessoa i, verifique todos os outros elementos
da linha i e da coluna i. O custo dessa solução é 2n(n − 1).
[1ª tentativa] Hipótese de Indução: sabemos encontrar uma celebridade (se existir) em um conjunto
de n − 1 pessoas. Tome S = {1,…,n}, n > 2, e S' = S \ {n}. Há dois casos: (1) existe uma
celebridade em S', digamos k; então k é celebridade em S se, e somente se, M[n,k] = 1 e
M[k,n] = 0. (2) Se k não for celebridade em S ou não existir celebridade em S', então a pessoa n
é celebridade em S se M[n,j] = 0 e M[j,n] = 1, ∀j < n; caso contrário não há celebridade em S.
Essa primeira tentativa, infelizmente, também conduz a um algoritmo quadrático. Por quê?
[2ª tentativa] Dadas duas pessoas i e j, é possível determinar se uma delas não é uma celebridade
com apenas uma comparação: se M[i,j] = 1, então i não é celebridade; caso contrário j não é
celebridade."

Algoritmo do slide:

    Celebridade(S, M)
    ▷ Entrada: conjunto de pessoas S = {1,2,…,n}; M, a matriz que define quem conhece quem em S.
    ▷ Saída: um inteiro k ≤ n que é celebridade em S, ou k = 0
    1. se |S| = 1 então k ← elemento em S
    2. senão
    3.     sejam i, j quaisquer duas pessoas em S
    4.     se M[i,j] = 1 então s ← i senão s ← j
    5.     S' ← S \ {s}
    6.     k ← Celebridade(S', M)
    7.     se k > 0 então
    8.         se (M[s,k] ≠ 1) ou (M[k,s] ≠ 0) então k ← 0
    9. devolva k

## SOLUÇÃO FINAL

### 0. Convenções de contagem (fixadas antes de qualquer conta)
1. Unidade de custo: um ACESSO A M = leitura de uma posição M[x,y]. É a operação dominante nos
   três algoritmos e é a unidade em que o slide dá 2n(n−1).
2. A diagonal M[k,k] é irrelevante pela definição e nunca é lida.
3. Testes leem as duas entradas. Na linha 8, a condição (M[s,k] ≠ 1) ou (M[k,s] ≠ 0) conta como
   2 acessos, sem curto-circuito. Não é escolha arbitrária: a medição exaustiva dá custo mínimo
   n+1, e só essa convenção o reproduz. Com curto-circuito o melhor caso cairia para n; o pior
   caso 3(n−1) não mudaria.
4. k é celebridade de S quando, para toda x ∈ S com x ≠ k, vale M[x,k] = 1 e M[k,x] = 0. A
   propriedade é RELATIVA ao conjunto: alguém pode ser celebridade de S' e não de S ⊃ S'.
5. Para |S| = 1, digamos S = {x}: a condição é vazia, logo x é celebridade de S. É o que a
   linha 1 devolve.

### (a) Existe no máximo uma celebridade
Resposta: se k1 e k2 são celebridades de S, então k1 = k2.

Demonstração. Suponha por absurdo que k1 e k2 sejam celebridades de S com k1 ≠ k2.
 - k1 é celebridade e k2 ∈ S, k2 ≠ k1: a parte "não conhece ninguém" dá M[k1,k2] = 0.
 - k2 é celebridade e k1 ∈ S, k1 ≠ k2: a parte "é conhecida por todos" dá M[k1,k2] = 1.
A mesma posição vale 0 e 1. Absurdo. Logo k1 = k2. ∎

Escopo: a prova usa uma metade da definição de cada celebridade; nenhuma hipótese sobre a
diagonal é necessária, pois k1 ≠ k2. Para n = 1 o enunciado é trivial. EXISTÊNCIA não está
afirmada: pode haver zero celebridades (com M ≡ 0 e n ≥ 2, ninguém é conhecido por ninguém).

### (b) O custo 2n(n−1) da solução ingênua
Resposta: exatamente 2n(n−1) = 2n² − 2n acessos; é Θ(n²) com c1 = 1, c2 = 2, n0 = 2.

Contagem. Para decidir se i é celebridade é preciso verificar a linha i toda 0 (as n−1 posições
M[i,j], j ≠ i) e a coluna i toda 1 (as n−1 posições M[j,i], j ≠ i): 2(n−1) acessos por pessoa.
Repetindo para as n pessoas, sem interromper e sem reaproveitar leituras: n · 2(n−1) = 2n(n−1).

Conferência cruzada: a matriz tem n² − n posições fora da diagonal, e cada uma é lida exatamente
duas vezes — uma na linha de quem conhece, outra na coluna de quem é conhecido. Total
2(n² − n) = 2n(n−1). Os dois modos de contar coincidem.

Testemunhas de Θ(n²), com f(n) = 2n² − 2n e g(n) = n²: c1 = 1, c2 = 2, n0 = 2.
 - inferior: 2n² − 2n ≥ n² ⟺ n² ≥ 2n ⟺ n ≥ 2 ✓;
 - superior: 2n² − 2n ≤ 2n² ⟺ −2n ≤ 0, verdadeiro para todo n ≥ 1;
 - EM n = n0 = 2 EXATAMENTE: f(2) = 4; c1·g(2) = 4 ≤ 4 ✓; c2·g(2) = 8 ≥ 4 ✓.
O n0 = 2 é necessário: em n = 1 o custo é 0 e a cota inferior 1·1² = 1 falharia.

Variante com aborto antecipado: se a varredura parar no primeiro elemento violado, o custo cai
mas a ordem não. Na família M[i,j] = 1 ⟺ j > i (varrendo linha antes de coluna, j crescente) o
custo é (n−1)(n+4)/2 — medido para n = 2..12 —, ainda Θ(n²).

### (c) Por que a primeira tentativa é quadrática (o "Por quê?" do slide)
Resposta: porque a hipótese é aplicada a S' = S∖{n}, onde a pessoa removida é ARBITRÁRIA — nada
se sabe sobre ela. Quando a recursão não entrega candidato utilizável, é preciso testar a pessoa
n do zero, o que custa até 2(n−1) acessos. Trabalho Θ(n) em cada um dos n níveis dá Θ(n²). No
pior caso o custo é exatamente n² + n − 2 = (n+2)(n−1), que é Θ(n²) com c1 = 1, c2 = 2, n0 = 2.

A causa estrutural. A indução está formalmente correta: a redução é legítima e os dois casos
cobrem tudo. O defeito não é lógico, é econômico.
 - Caso 1 (existe celebridade k em S'): o passo é barato, 2 acessos. A hipótese entregou
   informação sobre todos os elementos de S'; falta só confrontar k com a pessoa nova.
 - Caso 2 (S' sem celebridade, ou k não sobrevive): a hipótese não diz NADA sobre a pessoa n,
   porque n foi escolhida sem critério, antes de olhar para a matriz. Certificá-la ou descartá-la
   exige ler a linha n e a coluna n inteiras: 2(n−1) acessos.
Ou seja: a recursão diminui o tamanho do problema sem diminuir o trabalho por nível, porque o
elemento removido é escolhido sem informação. O erro de projeto é escolher QUEM remover antes de
olhar para os dados.

A recorrência do pior caso. Com |S| = m ≥ 2, o custo do nível é: 2 (caso 1 bem-sucedido);
2 + até 2(m−1) (caso 1 falha e cai no caso 2); ou até 2(m−1) (caso 2 direto). O máximo é
2 + 2(m−1) = 2m. Logo W(n) ≤ W(n−1) + 2n, com W(1) = 0.

A cota é ATINGIDA pela família M[i,j] = 1 ⟺ j > i (cada um conhece exatamente os de índice
maior). Nela, em S = {1,…,n}: a celebridade de S' = {1,…,n−1} é n−1, então o caso 1 dispara e
gasta 2 acessos; o teste falha, pois M[n,n−1] = 0 ≠ 1; cai-se no caso 2, e a pessoa n passa em
TODOS os 2(n−1) testes (M[n,j] = 0 e M[j,n] = 1 para j < n), sem aborto. Total do nível:
2 + 2(n−1) = 2n. E S' tem a mesma estrutura. Portanto vale a igualdade:
  W(1) = 0,  W(n) = W(n−1) + 2n para n ≥ 2.

Solução por indução. P(n): W(n) = n² + n − 2.
 Base n = 1: 1² + 1 − 2 = 0 = W(1). ✓
 Passo n ≥ 2: por h.i., W(n−1) = (n−1)² + (n−1) − 2. Então
   W(n) = W(n−1) + 2n = (n² − 2n + 1) + (n − 1) − 2 + 2n = n² + n − 2. ✓
Logo W(n) = n² + n − 2 = (n+2)(n−1) para todo n ≥ 1. Equivalentemente, somando os custos de
nível: 2·2 + 2·3 + … + 2n = 2·[n(n+1)/2 − 1] = n² + n − 2.

Testemunhas de Θ(n²) para f(n) = n² + n − 2: c1 = 1, c2 = 2, n0 = 2.
 - n² + n − 2 ≥ n² ⟺ n ≥ 2 ✓;  - n² + n − 2 ≤ 2n² ⟺ n − 2 ≤ n², verdadeiro para n ≥ 1;
 - EM n = n0 = 2 EXATAMENTE: f(2) = 4; c1·4 = 4 ≤ 4 ✓; c2·4 = 8 ≥ 4 ✓.

A ARMADILHA. É tentador dizer que o pior caso é "quando ninguém é celebridade, por exemplo todo
mundo conhece todo mundo". É o CONTRÁRIO: com M ≡ 1 fora da diagonal, a recursão devolve k = 0
em todo nível e o laço do caso 2 aborta no PRIMEIRO j (M[n,1] = 1 ≠ 0), gastando 1 acesso por
nível — total n−1, LINEAR. Esse é o melhor caso. O pior caso é uma matriz que tem celebridade em
cada subconjunto inicial e ainda assim força a varredura completa: a ordem total acima. Moral:
pior caso é sobre a entrada que MAXIMIZA o custo, não sobre a resposta que parece mais difícil.

### (d) O fato-chave: um acesso elimina alguém
Lema da Eliminação. Sejam i, j ∈ S com i ≠ j. Então:
 (1) se M[i,j] = 1, então i não é celebridade de S;
 (2) se M[i,j] = 0, então j não é celebridade de S.

Prova de (1). Suponha M[i,j] = 1 e, por absurdo, que i seja celebridade de S. Pela definição,
para toda x ∈ S com x ≠ i vale M[i,x] = 0. Tomando x = j (legítimo: j ∈ S, j ≠ i), obtém-se
M[i,j] = 0, contradizendo M[i,j] = 1. ∎
Prova de (2). Suponha M[i,j] = 0 e, por absurdo, que j seja celebridade de S. Pela definição,
para toda x ∈ S com x ≠ j vale M[x,j] = 1. Tomando x = i (legítimo: i ∈ S, i ≠ j), obtém-se
M[i,j] = 1, contradizendo M[i,j] = 0. ∎

Corolário. Como M[i,j] ∈ {0,1}, exatamente uma das hipóteses ocorre. Portanto UM ÚNICO acesso
identifica um s ∈ {i,j} que não é celebridade de S. É exatamente a linha 4.

Escopo: exige-se i ≠ j (o lema é falso sem isso — M[i,i] não diz nada); a linha 3 só roda no ramo
"senão" da linha 1, logo com |S| ≥ 2, e há duas pessoas distintas.

Contraste com a ingênua: lá cada acesso serve para CONFIRMAR uma pessoa e é jogado fora quando
ela é descartada; aqui cada acesso ELIMINA uma pessoa definitivamente. n−1 eliminações bastam
para restar um único candidato.

### (e) Corretude do algoritmo, por indução
Lema da Hereditariedade. Se c é celebridade de S e S' ⊆ S com c ∈ S', então c é celebridade de
S'. Prova: a condição "para toda x ∈ S', x ≠ c: M[x,c] = 1 e M[c,x] = 0" é a restrição a S' ⊆ S
de uma condição já verificada para todo x ∈ S. ∎
A recíproca é FALSA — celebridade de S' pode falhar em S — e é por isso que a linha 8 existe.

P(n): para todo S com |S| = n ≥ 1 e toda M, Celebridade(S,M) devolve a celebridade de S se ela
existe, e 0 caso contrário.

Base n = 1. S = {x}; a linha 1 devolve k = x. Pela convenção 5, x é celebridade de S, e é única
pelo item (a). Nenhum acesso a M. ✓

Passo n ≥ 2. Suponha P(n−1). A linha 3 escolhe i ≠ j (possível, pois n ≥ 2); a linha 4 faz 1
acesso e, pelo Lema da Eliminação, o s escolhido não é celebridade de S; a linha 5 forma S' com
|S'| = n−1; a linha 6 chama recursivamente. Por P(n−1) (h.i.), k é a celebridade de S' se existir,
e k = 0 caso contrário.

(1) Se o algoritmo devolve k ≠ 0, então k é celebridade de S. Para devolver k ≠ 0 é preciso
k > 0 após a linha 6 e o teste da linha 8 não disparar, isto é, M[s,k] = 1 e M[k,s] = 0. Por
P(n−1), k é celebridade de S': para toda x ∈ S' com x ≠ k, M[x,k] = 1 e M[k,x] = 0. Como
S = S' ∪ {s} e s ∉ S', juntando: para toda x ∈ S com x ≠ k, M[x,k] = 1 e M[k,x] = 0. É a
definição de celebridade de S. ✓

(2) Se S tem celebridade c, o algoritmo devolve c. Pelo Lema da Eliminação, s não é celebridade
de S; como c é, tem-se c ≠ s, logo c ∈ S'. Pelo Lema da Hereditariedade, c é celebridade de S'.
Por P(n−1) e pela unicidade do item (a) aplicada a S', a linha 6 devolve EXATAMENTE k = c — não
"alguma" celebridade, pois a de S' é única. Na linha 8, como c é celebridade de S e s ∈ S com
s ≠ c, valem M[s,c] = 1 e M[c,s] = 0; a condição é falsa e k não é zerado. A linha 9 devolve c. ✓

(3) Se S não tem celebridade, devolve 0. Contrapositiva de (1). ✓

(1)+(2)+(3) estabelecem P(n). Por indução, P(n) vale para todo n ≥ 1. ∎

POR QUE A VERIFICAÇÃO DA LINHA 8 BASTA (o ponto fino). À primeira vista ela é fraca demais:
confronta o candidato com UMA única pessoa, s, enquanto a definição exige n−1 confrontos em cada
direção. Duas leituras.

Leitura indutiva: quando a linha 8 roda, a h.i. JÁ certificou k contra todo o resto de S'. Falta
exatamente uma pessoa: s. Um confronto local basta porque n−2 confrontos já foram pagos pela
recursão.

Leitura operacional — o desenrolar. Partindo de S_n = S com |S_n| = n, cada nível remove uma
pessoa: S_n → S_{n−1} → … → S_1 = {b}, removendo s_n, s_{n−1}, …, s_2. São n−1 remoções, todas
distintas, e sobra um único elemento b. Logo {s_2,…,s_n} = S ∖ {b}: exatamente todas as pessoas
de S diferentes de b. Na volta, b é testado na linha 8 nível a nível, na ordem inversa. Se b
sobrevive a todos, o algoritmo terá verificado M[s,b] = 1 e M[b,s] = 0 para toda s ∈ S∖{b} — isto
é, toda a coluna b fora da diagonal vale 1 e toda a linha b fora da diagonal vale 0. É, letra por
letra, a definição de celebridade. Os n−1 testes locais SE SOMAM à verificação global; não há
verificação faltando nem acesso desperdiçado.

E se algum teste falhar no nível ℓ? Então k ← 0 e, pela guarda da linha 7, nenhum nível acima
gasta acesso com verificação. Isso é correto porque: pelo Lema da Eliminação, s_ℓ não é
celebridade de S_ℓ; pela h.i. e pela unicidade, o único outro candidato possível em S_ℓ era k; k
falhou; logo S_ℓ não tem celebridade. E pela contrapositiva do Lema da Hereditariedade, se S_ℓ
não tem celebridade, nenhum S_m ⊃ S_ℓ da pilha pode ter — pois uma celebridade de S_m
sobreviveria em S_ℓ, já que os removidos entre eles foram todos descartados pelo Lema da
Eliminação. Propagar 0 sem mais testes é legítimo.

Terceira leitura, a mais curta: as n−1 remoções eliminam n−1 pessoas de S como possíveis
celebridades de S. Sobra b como única candidata. Resta certificá-la — e é o que os n−1 testes da
linha 8 fazem.

### (f) Complexidade, contando acessos a M
Resposta: o custo DEPENDE da matriz. Vale 3(n−1) no pior caso (e exatamente 3(n−1) sempre que
existe celebridade), n+1 no melhor caso (n ≥ 2), e é Θ(n) em toda entrada — com c1 = 1, c2 = 3,
n0 = 2.

Custo por nível, com |S| = m ≥ 2: linha 4 sempre 1 acesso; linha 8 dois acessos se k > 0 após a
linha 6, e ZERO se k = 0, porque a linha 7 pula a verificação; as demais linhas não acessam M.
Logo o nível custa 3 (candidato vivo) ou 1 (já descartado). A base |S| = 1 custa 0.

Pior caso: W(1) = 0, W(n) = W(n−1) + 3 para n ≥ 2.
Solução por indução. P(n): W(n) = 3(n−1). Base n = 1: 3·0 = 0 = W(1) ✓. Passo n ≥ 2: por h.i.,
W(n−1) = 3(n−2); então W(n) = 3(n−2) + 3 = 3n − 3 = 3(n−1) ✓.
A cota é atingida sempre que S tem celebridade: pelo argumento (2) de (e), o candidato nunca é
zerado, então todo nível com |S| ≥ 2 gasta os 3 acessos, e há n−1 desses níveis. Decomposição:
 (n−1) eliminações (linha 4) + 2(n−1) verificações (linha 8) = 3(n−1).

Melhor caso: a linha 4 roda em todos os n−1 níveis com |S| ≥ 2, logo ao menos n−1 acessos
sempre; e no nível mais fundo (|S| = 2) a chamada recursiva é a base, que SEMPRE devolve k > 0,
então a linha 8 roda ali obrigatoriamente — mais 2 acessos. Portanto o custo é ≥ (n−1) + 2 = n+1
para todo n ≥ 2, e o valor é atingido com M ≡ 0: no nível |S| = 2 o teste falha, k ← 0, e os
n−2 níveis acima gastam só o acesso da linha 4. Total 3 + (n−2) = n+1.

Θ(n) em toda entrada. Para toda M e todo n ≥ 2, n + 1 ≤ T_M(n) ≤ 3(n−1). Com c1 = 1, c2 = 3,
n0 = 2 e g(n) = n:
 - inferior: T_M(n) ≥ n + 1 > n = c1·g(n) para todo n ≥ 2;
 - superior: T_M(n) ≤ 3n − 3 ≤ 3n = c2·g(n) para todo n ≥ 1;
 - EM n = n0 = 2 EXATAMENTE: T_M(2) = 3 (único valor possível); c1·2 = 2 ≤ 3 ✓; c2·2 = 6 ≥ 3 ✓.
Logo 0 ≤ 1·n ≤ T_M(n) ≤ 3·n para todo n ≥ 2 e toda entrada: Θ(n) no melhor caso, no pior e em
qualquer intermediário. A recorrência do slide, T(n) = Θ(1) para n = 1 e T(n) = T(n−1) + Θ(1)
para n > 1, é a versão assintótica disso — os Θ(1) escondem a diferença entre 1 e 3, que é onde
mora a variação entre n+1 e 3n−3.

SEJA HONESTA: dizer "o algoritmo custa 3(n−1)" sem qualificar é errado. O correto é: 3(n−1) é o
PIOR caso, e é o custo exato quando existe celebridade; quando não existe, pode cair até n+1.

Isso é assintoticamente ótimo. Afirmação: todo algoritmo determinista correto faz pelo menos n
acessos a M no pior caso (n ≥ 2).
Prova. Seja A correto e considere M0 ≡ 0 fora da diagonal. Nela ninguém é celebridade, pois
nenhuma coluna é toda 1 (n ≥ 2); então A devolve 0 depois de ler um conjunto R de posições.
Suponha por absurdo que exista p tal que A não leu nenhuma posição da coluna p (nenhum M0[x,p]
com x ≠ p). Construa M1 igual a M0 exceto M1[x,p] = 1 para todo x ≠ p. Em M1 a pessoa p é
celebridade: a coluna p é toda 1 e a linha p continua toda 0. Mas as duas execuções coincidem:
por indução no número de leituras, cada leitura de A em M1 é a mesma de M0 e devolve o mesmo
valor, porque todas as posições lidas estão fora da coluna p, onde M0 e M1 são idênticas. Logo A
devolve 0 também em M1 — errado. Assim cada uma das n colunas contém ao menos uma posição lida;
como uma posição pertence a exatamente uma coluna, são ao menos n posições distintas. ∎
Portanto o algoritmo do slide é ótimo até constante: gasta no máximo 3(n−1) < 3n, contra o mínimo
teórico de n.

### (g) Comparação
| Critério | Ingênua | 1ª tentativa | Algoritmo do slide |
| Ideia | testa cada pessoa isoladamente | remove uma pessoa ARBITRÁRIA | remove uma pessoa SABIDAMENTE não-celebridade |
| Melhor caso | 2n(n−1) (não adaptativa) | n−1, com M ≡ 1 | n+1 |
| Pior caso | 2n(n−1) = 2n² − 2n | n² + n − 2 = (n+2)(n−1) | 3(n−1) = 3n − 3 |
| Classe (pior caso) | Θ(n²) | Θ(n²) | Θ(n) |
| Testemunhas | c1=1, c2=2, n0=2 | c1=1, c2=2, n0=2 | c1=1, c2=3, n0=2 |
| Ótima? | não | não | sim, a menos de constante |

Números (acessos a M, pior caso):
| n | ingênua 2n(n−1) | 1ª tentativa n²+n−2 | slide 3(n−1) | ingênua/slide | 1ª/slide |
| 10 | 180 | 108 | 27 | 6,67 | 4 |
| 100 | 19.800 | 10.098 | 297 | 66,67 | 34 |
| 1.000 | 1.998.000 | 1.000.998 | 2.997 | 666,67 | 334 |
| 10.000 | 199.980.000 | 100.009.998 | 29.997 | 6.666,67 | 3.334 |

As razões têm forma fechada, o que confere a tabela:
 2n(n−1) / 3(n−1) = 2n/3   e   (n²+n−2) / 3(n−1) = (n+2)(n−1) / 3(n−1) = (n+2)/3.
Em n = 10.000: 2n/3 = 6.666,67 e (n+2)/3 = 3.334 — batem.

Três conclusões:
1. A 1ª tentativa não resolve nada assintoticamente. Ganha um fator constante sobre a ingênua —
   a razão (n²+n−2)/(2n²−2n) tende a 1/2 — mas continua Θ(n²). Uma indução formalmente correta
   pode produzir algoritmo tão ruim quanto a força bruta.
2. O que separa a 1ª da 2ª tentativa é decisão de PROJETO, não de prova. As duas usam a mesma
   redução (n → n−1) e a mesma estrutura de verificação na volta. A diferença inteira está em
   QUEM se remove: alguém arbitrário (e provar/refutar essa pessoa custa Θ(n)) ou alguém que um
   único acesso já provou não ser celebridade (e a volta custa Θ(1)).
3. O ganho é qualitativo: para n = 10.000, de 200 milhões de acessos para 30 mil — quatro ordens
   de grandeza. E não há muito mais a ganhar: qualquer algoritmo correto precisa de ao menos n
   acessos, então o do slide está dentro de um fator 3 do ótimo.

## RESPOSTA
| Solução | Pior caso | Melhor caso | Classe (pior caso) | Testemunhas |
| Ingênua | 2n(n−1) = 2n² − 2n | idem (não adaptativa) | Θ(n²) | c1=1, c2=2, n0=2 |
| 1ª tentativa | n² + n − 2 = (n+2)(n−1); W(n)=W(n−1)+2n, W(1)=0 | n−1 (M ≡ 1) | Θ(n²) | c1=1, c2=2, n0=2 |
| Slide | 3(n−1) = 3n − 3; W(n)=W(n−1)+3, W(1)=0; exato sempre que existe celebridade, = (n−1) eliminações + 2(n−1) verificações | n+1 (n ≥ 2) | Θ(n) em TODA entrada | c1=1, c2=3, n0=2 |
Cota inferior: qualquer algoritmo correto faz ≥ n acessos no pior caso, logo o do slide é ótimo a
menos de constante (fator ≤ 3).
