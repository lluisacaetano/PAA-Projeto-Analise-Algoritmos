# Lista 4 — Questão 3 (resposta limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Considere a seguinte prova por indução matemática:
1. Proposição. Dado um conjunto de n pessoas, se pelo menos uma pessoa tem a nacionalidade
   chinesa, então todas os demais pessoas também são chinesas. [sic — concordância como no original]
2. Caso base (n = 1): Em um conjunto com uma pessoa, se ela é chinesa, então todas as pessoas
   do conjunto são chinesas. Portanto, a afirmação é verdadeira.
3. Hipótese de indução:
   - Suponha que a proposição é verdadeira para n = 3;
   - Sejam T1, T2, T3 e T4 quatro pessoas das quais pelo menos uma tem nacionalidade chinesa
     (suponha que é T1);
   - Supondo que o conjunto {T1, T2, T3} é a hipótese de que é verdadeiro para n = 3, então
     T2 e T3 são pessoas com nacionalidade chinesa;
   - Analogamente para {T1, T2, T4}, tem-se que T2 e T4 são pessoas com nacionalidade chinesa.
   Portanto, as quatro pessoas têm nacionalidade chinesa! A generalização da construção para k
   e k + 1 é a prova desejada.
Pergunta: Essa prova está correta? Justifique formalmente sua resposta."

## SOLUÇÃO FINAL

### 0. Notação
Para cada inteiro n ≥ 1, seja
  P(n): "Em todo conjunto C de n pessoas, se existe pelo menos uma pessoa chinesa em C, então
         todas as pessoas de C são chinesas."
P(n) é uma afirmação universal sobre todos os conjuntos de tamanho n, e cada instância é uma
implicação (antecedente: "há pelo menos um chinês"; consequente: "todos são chineses").

### 1. Veredito
Não, a prova não está correta. Mais do que incompleta: a proposição que ela pretende demonstrar
é falsa. Como o Princípio da Indução Finita é uma regra de inferência correta — de premissas
verdadeiras nunca extrai conclusão falsa —, uma "demonstração" de uma proposição falsa via
indução tem obrigatoriamente ao menos uma premissa não estabelecida.

### 2. Refutação da proposição por contraexemplo
Tome n = 2 e C = {T1, T2}, com T1 de nacionalidade chinesa e T2 de nacionalidade brasileira.
Antecedente ("existe pelo menos uma pessoa chinesa em C"): verdadeiro (T1).
Consequente ("todas as pessoas de C são chinesas"): falso (T2 não é).
Uma implicação com antecedente verdadeiro e consequente falso é falsa. Logo P(2) é falsa.
Portanto P(1) é verdadeira e P(2) é falsa. O mesmo contraexemplo — C = {T1 chinês, T2, …, Tn
não-chineses} — refuta P(n) para qualquer n ≥ 2 para o qual existam n pessoas; e é P(2) que o
resto desta resposta usa.
Como a conclusão pretendida — "P(n) para todo n" — é falsa, o veredito está encerrado. O que
resta é responder onde.

### 3. Localização exata do defeito lógico

3.1 Reconstrução do passo. O texto não escreve o passo genérico (diz "a generalização … é a
prova desejada"), mas a construção exibida em 3 → 4 tem uma generalização natural — e a §3.4
mostra que a conclusão não depende de qual escolha de elementos removidos se adote.
Generalizando:
  Seja k ≥ 1 e suponha P(k). Seja S = {T1, …, T_{k+1}} com pelo menos uma pessoa chinesa; sem
  perda de generalidade, T1 é chinesa. Defina A = S∖{T_{k+1}} = {T1,…,T_k} e
  B = S∖{T_k} = {T1,…,T_{k−1},T_{k+1}}. Então |A| = |B| = k e A ∪ B = S. Aplicando P(k) a A
  conclui-se que todos de A são chineses; aplicando P(k) a B, que todos de B são chineses;
  como A ∪ B = S, todos de S são chineses. Logo P(k+1).
(No texto, k = 3: A = {T1,T2,T3} e B = {T1,T2,T4}.)

3.2 A condição exata de aplicabilidade da hipótese. P(k) é uma implicação. Aplicá-la a um
conjunto X com |X| = k só produz "todos de X são chineses" se o antecedente estiver verificado
para X, isto é, se soubermos que X contém pelo menos uma pessoa chinesa. Ter |X| = k não basta.
A sutileza é que a lista de pessoas sabidamente chinesas CRESCE ao longo do argumento. No início
a única testemunha é T1; mas ao aplicar P(k) a A, que contém T1, todo elemento de A passa a ser
sabidamente chinês — e então qualquer elemento de A ∩ B serve de testemunha para a segunda
aplicação. Com a rotulação da §3.1 — A é o primeiro subconjunto a receber a hipótese —, o passo encadeado
exige T1 ∈ A e A ∩ B ≠ ∅. Mas T1 ∈ A ∪ B = S sempre vale, de modo que chamar de A aquele que
contém T1 é escolha de rótulo, não exigência: a condição substantiva, a única que pode falhar, é
  A ∩ B ≠ ∅.
(Exigir T1 ∈ A ∩ B também funcionaria, mas é forte demais: para k = 3 o par A = {T1,T2,T3},
B = {T2,T3,T4} fecha o passo sem que T1 esteja em B.)
Na construção do texto as duas condições coincidem, e a conta é imediata:
  A ∩ B = S∖{T_k, T_{k+1}} = {T1, …, T_{k−1}},  com |A ∩ B| = k − 1.
Logo A ∩ B ≠ ∅ se e somente se k − 1 ≥ 1, ou seja k ≥ 2. A cardinalidade nem depende da
rotulação: |A| = |B| = k e |A ∪ B| = k + 1 forçam |A ∩ B| = 2k − (k+1) = k − 1.

3.3 O caso k = 1. Para k = 1 temos S = {T1, T2} com T1 chinês, e a construção dá A = {T1},
B = {T2}.
 - Aplicar P(1) a A é legítimo, mas conclui apenas "T1 é chinês" — nada de novo.
 - Aplicar P(1) a B é ilegítimo: não se sabe que T2 é chinês; esse é exatamente o fato que se
   quer provar. O antecedente de P(1) para B não está verificado, e de P(1) nada se deduz sobre
   B. Insistir seria usar a tese para provar a tese.
 - Consequentemente S = A ∪ B não fica coberto: sobre T2 não se obteve nada.
Conclusão: a implicação P(1) → P(2) não é demonstrada pela construção. É o único elo faltante —
e, pela §2, é também um elo falso (P(1) verdadeira, P(2) falsa). Não há remendo possível.

3.4 O defeito não depende da escolha dos elementos removidos. Qualquer versão dessa construção
obtém os dois subconjuntos de tamanho k removendo de S dois elementos distintos (removendo o
mesmo elemento duas vezes teríamos A = B e A ∪ B ≠ S, e o argumento não cobriria S). Removendo
dois elementos distintos de um conjunto de k+1 = 2 elementos, os subconjuntos resultantes são
forçosamente os singletons {T1} e {T2}, que são disjuntos — e sem interseção não há como
transportar testemunha de um subconjunto para o outro, qualquer que seja a rotulação. Para
k = 1 a falha é estrutural, não um azar de rotulação.

### 4. Defeitos adicionais de redação
(a) A "hipótese de indução" foi enunciada para um valor fixo. O texto escreve "suponha que a
proposição é verdadeira para n = 3". Isso não é hipótese de indução legítima: a hipótese é
"seja k ≥ n0 arbitrário e suponha P(k)". Duas regras trabalham juntas: descarregar a hipótese
P(k) é o que produz a implicação P(k) → P(k+1), e a arbitrariedade de k é o que autoriza a
generalização universal, ∀k (P(k) → P(k+1)). Fixando n = 3, a primeira ainda se aplica — assumir P(3), derivar P(4) e
descarregar produz legitimamente a implicação P(3) → P(4) — mas a segunda não: sem k arbitrário
não há generalização universal. É por isso que o texto fica preso a essa única implicação
concreta.
(b) P(3) nunca foi estabelecida (e é falsa). O caso base provado é P(1); nada liga P(1) a P(3).
Sutileza: supor P(3) dentro de uma prova condicional não é, em si, falácia — obtém-se
legitimamente a implicação P(3) → P(4). A falácia está em concluir o consequente de uma prova condicional sem ter estabelecido o
antecedente — modus ponens sem a premissa menor: a frase "Portanto, as quatro pessoas têm
nacionalidade chinesa!" é apresentada como fato categórico quando só vale sob a hipótese não
demonstrada P(3).
(c) O rótulo está trocado. O que o texto chama de "hipótese de indução" é, na verdade, o passo
indutivo — e apenas na instância concreta 3 → 4. Enunciar a hipótese dentro do passo é prática
comum e não seria defeito; o defeito é o rótulo esconder que ali está sendo feita a parte que
precisaria de k arbitrário, e que a quantificação universal sobre k nunca aparece.
(d) "A generalização da construção para k e k+1 é a prova desejada" é um buraco, não um passo.
É o padrão "analogamente / claramente": a frase ocupa exatamente o lugar onde a demonstração
deveria estar — e é precisamente onde a prova falha. Se o autor tivesse escrito o passo genérico
com os quantificadores explícitos, seria obrigado a justificar que A ∩ B ≠ ∅ — na construção
do texto, que T1 ∈ B — e o caso k = 1
apareceria imediatamente.
(e) A base foi provada exatamente no ponto em que ela não se propaga. A base é n = 1; o passo só
funciona de k = 2 em diante. Base e passo não se encaixam.

### 5. Diagnóstico estrutural
A indução é uma cadeia de implicações ancorada na base:
  P(1) → P(2) → P(3) → P(4) → …
O texto do professor não escreve o passo genérico — ele exibe só a instância 3 → 4 e delega o
resto a um "analogamente". Completando-o como na reconstrução da §3.1, com a aplicabilidade da
hipótese verificada como na §3.2, o que fica de pé é:
  Base: P(1) — verdadeira, e provada pelo próprio texto. ✔
  Passo: P(k) → P(k+1) para todo k ≥ 2 — demonstrável, mas pela reconstrução, não pelo texto. ✔
  Elo P(1) → P(2) — não demonstrado (e falso). ✘
O primeiro dominó cai e os dominós do segundo em diante estão bem posicionados uns em relação
aos outros, mas ninguém empurra o segundo. A única instância P(n) inferível dessas
premissas é P(1).

Por que "base válida + passo válido para quase todo k" não basta — argumento de contramodelo.
Tome um mundo com pelo menos uma pessoa chinesa e pelo menos uma não-chinesa — T1 chinês,
T2 brasileiro, e quantas mais se queira. Confira nele as premissas oferecidas, uma a uma:
 - P(1) é verdadeira, logo a base vale (de fato P(1) é verdadeira em todo mundo);
 - P(k) → P(k+1) vale para todo k ≥ 2, logo o passo vale — a derivação da §3.1 é correta
   sempre que k ≥ 2, qualquer que seja o mundo;
 - e, no entanto, ∀n P(n) é falsa, pois P(2) falha pelo contraexemplo da §2.
Como existe um modelo que satisfaz todas as premissas oferecidas e refuta a conclusão, essas
premissas não implicam a conclusão — nenhuma reescrita da prova poderia salvá-la. E,
coerentemente, a única implicação da cadeia que é falsa nesse modelo é exatamente P(1) → P(2),
a que o texto não demonstrou.
Lição geral: uma única lacuna em k = m corta a cadeia, e nada a respeito de n > m fica
demonstrado — a menos que se prove independentemente uma nova base acima de m. Aqui não há base
a resgatar: qualquer nova base teria de recuperar P(2) para cobrir n = 2, e P(2) é falsa pelo
contraexemplo da §2.

### 6. O nome do padrão
É o disfarce brasileiro de um clássico. A falácia foi levantada por George Pólya em Induction
and Analogy in Mathematics (1954), na forma "quaisquer n moças têm olhos da mesma cor"; a
formulação que ficou famosa — "todos os cavalos têm a mesma cor" — é creditada a Joel E. Cohen
(1961). A anatomia é idêntica à desta questão: base em n = 1 e passo por dois subconjuntos de
tamanho n−1, que só têm elemento em comum quando n − 1 ≥ 2. Sempre que um passo indutivo aplica
a hipótese a dois subconjuntos e conclui pela união, teste imediatamente o menor k.

### 7. O que o Princípio da Indução Finita realmente exige
Seja P(n) propriedade sobre os inteiros e n0 ∈ Z. Se
 1. (Base) P(n0) é verdadeira; e
 2. (Passo) para TODO inteiro k ≥ n0 vale P(k) → P(k+1);
então P(n) é verdadeira para todo inteiro n ≥ n0.
A quantificação em (2) é universal e sem exceções: o passo tem de valer para todo k a partir de
n0, começando no próprio n0. Uma demonstração do passo que use, ainda que tacitamente, uma
hipótese extra — aqui "k ≥ 2", disfarçada na suposição não declarada de que A ∩ B ≠ ∅ (na
construção do texto, de que T1 ∈ B) — estabelece
apenas (2) restrito a esse domínio.
Regra de higiene: em toda prova por indução, substitua k = n0 literalmente no passo e refaça a
conta, em vez de confiar no k genérico. Neste exercício, k = 1 destrói a prova em duas linhas.

## RESPOSTA
A prova está errada. A própria proposição é falsa (contraexemplo: {T1 chinês, T2 brasileiro}
refuta P(2)), e o defeito está em que a hipótese de indução só pode ser aplicada a um
subconjunto que contenha alguém já sabidamente chinês. Como aplicá-la ao primeiro subconjunto
certifica todos os seus elementos, a condição para encadear as duas aplicações é A ∩ B ≠ ∅ — e
na construção do texto (dois subconjuntos de tamanho k obtidos removendo dois elementos
distintos) tem-se |A ∩ B| = k − 1, de modo que a condição A ∩ B ≠ ∅ só é satisfeita para
k ≥ 2. Assim o elo P(1) → P(2)
nunca é estabelecido e a cadeia indutiva se rompe logo após a base. Soma-se a isso um defeito
do texto tal como escrito: ele supõe P(3), que nunca foi derivada da base P(1), e apresenta a
conclusão como fato categórico — de modo que, além da base P(1), o máximo que estabelece é a
implicação P(3) → P(4). É a versão brasileira da
falácia que Pólya levantou em 1954 e que ficou conhecida como "todos os cavalos têm a mesma
cor".
