Resposta. T(n) ∈ O(n lg n). Juntando os termos iguais, a recorrência é T(n) = 336·T(⌊n/672⌋ + 135) + 336·T(⌊n/672⌋ + 189) + 456n + 1. Com o caso base declarado abaixo (T(n) = 1 para 1 ≤ n ≤ 189, recorrência para n ≥ 190), vale T(n) ≤ c·n·lg n para todo n ≥ n0, com c = 2·10¹⁰ e n0 = 2. O deslocamento (+135, +189) não muda a classe: para n ≥ 127008 o argumento ⌊n/672⌋ + 189 é no máximo n/336, e o que ele custa a mais é uma parcela da ordem de c·lg n, que é o(n) e cabe na folga c·n·lg 336 que a divisão produz. (Observação, não provada aqui: com a = 672 = b¹ e f(n) = 456n + 1, o mesmo raciocínio do Teorema Master indica que o limite é justo, Θ(n lg n); o enunciado só pede o limite superior.)

INTERPRETAÇÃO DO ENUNCIADO.
Leituras possíveis de "encontre um limite superior": (i) qualquer função g com T ∈ O(g); (ii) o limite superior assintótico natural, aquele que a técnica do texto (p. 9–10, constantes somadas ao argumento) produz. A leitura (i) é trivialmente satisfeita por funções enormes e não é o que o exercício treina; resolvo a (ii), com prova por substituição e testemunhas numéricas. O argumento é inteiro: n percorre os naturais n ≥ 1, e ⌊·⌋ é o piso. Afirmações sobre T valem para todo n do domínio (a recorrência é determinística; não há pior ou melhor caso aqui).

SIMPLIFICAÇÃO.
Os dois primeiros termos são iguais, assim como os dois últimos, logo
    T(n) = 336·T(⌊n/672⌋ + 135) + 336·T(⌊n/672⌋ + 189) + 456n + 1.
O total de chamadas é a = 336 + 336 = 672, e os argumentos são ≈ n/672.

CASO BASE (O TEXTO NÃO DÁ; DECLARO).
Para 1 ≤ n ≤ 189 temos ⌊n/672⌋ = 0, logo o segundo argumento vale 189 ≥ n: a recorrência não reduz o argumento (em n = 189 ela chamaria T(189) para definir T(189)). Por isso declaro o caso base em toda a faixa 1 ≤ n ≤ 189 — é uma escolha de conveniência (não a única possível), que garante que, para n ≥ 190, a recorrência só chame argumentos menores que n. Declaro:
    T(n) = 1 para 1 ≤ n ≤ 189;  a recorrência vale para n ≥ 190.
Ela está bem definida para n ≥ 190: os argumentos m₁ = ⌊n/672⌋ + 135 e m₂ = ⌊n/672⌋ + 189 satisfazem 135 ≤ m₁ < m₂ ≤ n/672 + 189 < n, porque n/672 + 189 < n ⇔ 189 < 671n/672 ⇔ n > 189,28…, o que vale para n ≥ 190 (em n = 190 exatamente: m₂ = 0 + 189 = 189 < 190). Nunca se chega a argumento 0. Outro caso base positivo muda apenas a constante c, não a classe (ver a observação no fim do PASSO 3).

PALPITE.
a = 672 chamadas sobre argumentos ≈ n/b com b = 672 e custo não recursivo linear: a = b¹, o caso "a = bᵏ" do Teorema Master, que dá n lg n. Palpite: T(n) ≤ c·n·lg n.

AFIRMAÇÃO A PROVAR.
P(n): T(n) ≤ c·n·lg n, com c = 2·10¹⁰. Provo P(n) para todo n ≥ n0 = 2, por indução forte em n. (n0 = 2 porque lg 1 = 0 e T(1) = 1 > 0; a afirmação é falsa em n = 1 e não é necessária lá: os argumentos recursivos são sempre ≥ 135.)
A ordem dos quantificadores é a da definição: existem c = 2·10¹⁰ e n0 = 2, fixos, tais que para todo n ≥ 2 vale 0 ≤ T(n) ≤ c·n·lg n. (T(n) ≥ 0 é imediato: a base é positiva e a recorrência soma termos não negativos.)

PASSO 1 — BASE DA INDUÇÃO: 2 ≤ n ≤ 524287.
Cotas explícitas para T nessa faixa, todas por cálculo direto da recorrência:
(a) 2 ≤ n ≤ 189: T(n) = 1.
(b) n = 190: ⌊190/672⌋ = 0, argumentos 135 e 189 (base), então T(190) = 336·1 + 336·1 + 456·190 + 1 = 672 + 86640 + 1 = 87313.
(c) 190 ≤ n ≤ 969: ⌊n/672⌋ ≤ 1, logo os argumentos são ≤ 1 + 189 = 190, e por (a) e (b) cada T(argumento) ≤ 87313. Assim T(n) ≤ 672·87313 + 456·969 + 1 = 58674336 + 441864 + 1 = 59116201.
(d) 190 ≤ n ≤ 524287: ⌊n/672⌋ ≤ ⌊524287/672⌋ = 780 (pois 780·672 = 524160 ≤ 524287 < 524832 = 781·672), logo os argumentos são ≤ 780 + 189 = 969, e por (a)–(c) cada T(argumento) ≤ 59116201. Assim
    T(n) ≤ 672·59116201 + 456·524287 + 1 = 39726087072 + 239074872 + 1 = 39965161945 < 4·10¹⁰.
(Contas: 59116201·672 = 59116201·700 − 59116201·28 = 41381340700 − 1655253628; 456·524287 = 456·2¹⁹ − 456 = 239075328 − 456.)
Logo T(n) < 4·10¹⁰ para todo 2 ≤ n ≤ 524287. Como n·lg n ≥ 2·lg 2 = 2 nessa faixa (n lg n é crescente para n ≥ 1), c·n·lg n ≥ 2·10¹⁰·2 = 4·10¹⁰ > T(n). P(n) vale para 2 ≤ n ≤ 524287; em n = n0 = 2 exatamente: T(2) = 1 ≤ 2·10¹⁰·2·1 = 4·10¹⁰.

PASSO 2 — PASSO INDUTIVO: n ≥ 524288 = 2¹⁹.
Hipótese de indução (forte): P(k) vale para todo k com 2 ≤ k ≤ n − 1.
Os argumentos m₁, m₂ satisfazem 2 ≤ 135 ≤ m₁ ≤ m₂ < n (visto no CASO BASE), então a hipótese se aplica a ambos:
    T(n) ≤ 336·c·m₁·lg m₁ + 336·c·m₂·lg m₂ + 456n + 1.
Seja m = n/672 + 189 (real). Tem-se m₁ ≤ m₂ ≤ m (o piso só diminui), e x·lg x é crescente para x ≥ 1, logo
    T(n) ≤ 672·c·m·lg m + 456n + 1 = c·(n + 127008)·lg m + 456n + 1,
pois 672·m = n + 672·189 = n + 127008.
Tratamento do deslocamento: como n ≥ 524288 ≥ 127008 = 672·189, vale 189 ≤ n/672, logo m ≤ n/672 + n/672 = n/336 e lg m ≤ lg n − lg 336 < lg n − 8 (porque 336 > 256 = 2⁸). O fator lg n − 8 é positivo (lg n ≥ 19), e n + 127008 > 0, então
    T(n) ≤ c·(n + 127008)·(lg n − 8) + 456n + 1
         = c·n·lg n − [ 8cn − 127008·c·(lg n − 8) − 456n − 1 ].
Basta mostrar que o colchete é ≥ 0. Separo 8cn = 4cn + 4cn:
(i) 4cn − 456n − 1 ≥ 0: como c ≥ 115, 4cn ≥ 460n = 456n + 4n ≥ 456n + 1 para n ≥ 1.
(ii) 4cn − 127008·c·(lg n − 8) ≥ 0 ⇔ n ≥ 31752·(lg n − 8) (dividindo por 4c > 0; 127008/4 = 31752). Seja h(n) = n − 31752·(lg n − 8). Em n = 2¹⁹ exatamente: h = 524288 − 31752·11 = 524288 − 349272 = 175016 > 0. E h é crescente para n ≥ 2¹⁹: h(n+1) − h(n) = 1 − 31752·lg(1 + 1/n), e lg(1 + 1/n) ≤ (1/n)/ln 2 < 2/n, logo h(n+1) − h(n) > 1 − 63504/n ≥ 1 − 63504/524288 > 0. Portanto h(n) > 0 para todo n ≥ 2¹⁹.
Somando (i) e (ii), o colchete é ≥ 0 e T(n) ≤ c·n·lg n, isto é, P(n). Pelo princípio da indução forte (base no PASSO 1 cobrindo 2..524287, passo para n ≥ 524288), P(n) vale para todo n ≥ 2.

PASSO 3 — CONCLUSÃO E TESTEMUNHAS.
Com c = 2·10¹⁰ e n0 = 2: para todo n ≥ 2, 0 ≤ T(n) ≤ c·n·lg n. Logo T(n) ∈ O(n lg n). Em n = n0 = 2: T(2) = 1 ≤ 4·10¹⁰ = c·2·lg 2. A constante é enorme porque absorve os valores de T na faixa onde o passo indutivo ainda não funciona (n < 2¹⁹); o passo em si só exige c ≥ 115. Isso não afeta a classe.
Observação sobre o caso base: se, em vez de T(n) = 1, a base for T(n) = dₙ ≥ 0 com dₙ ≤ M para 1 ≤ n ≤ 189 (M ≥ 1), as cotas (b)–(d) do PASSO 1 crescem no máximo por um fator M (cada uma é ≤ M vezes a anterior, pois 456n + 1 ≤ M·(456n + 1)), e c = 2·10¹⁰·M serve; o PASSO 2 não usa a base. A classe O(n lg n) não depende da base.

POR QUE O DESLOCAMENTO NÃO MUDA A CLASSE.
É a intuição da p. 9 do texto ("se fizermos n suficientemente grande, ⌊n/2⌋ + 37 se torna muito próximo de ⌊n/2⌋"), aqui tornada quantitativa:
1: O piso só diminui o argumento, e x lg x é crescente, então ele só ajuda numa cota superior.
2: A constante +189 (a maior das duas) é absorvida assim que n/672 ≥ 189: o argumento fica ≤ n/336, que ainda é uma fração fixa de n; em vez de ganhar lg 672 por nível, ganha-se lg 336 > 8, o que ainda produz a folga c·n·(lg 336) > 8cn.
3: O preço do deslocamento é a parcela c·127008·lg m ≤ c·127008·(lg n − 8), que é o(n); ela cabe em metade da folga (4cn) para n ≥ 2¹⁹.
4: Só sobra a faixa finita n < 2¹⁹, onde T é limitado por uma constante — e um número finito de valores é sempre absorvido aumentando c.
Nada disso depende de 135 e 189 serem esses números: qualquer deslocamento constante só muda o limiar (127008, 2¹⁹) e a constante c.

Conferência numérica (Python; não faz parte da prova): com outro caso base, T(n) = 1 para n ≤ 1000, a recorrência dá T(n)/(n lg n) entre 27,5 e 48,3 nas potências de 10 de 10⁴ a 10⁹ (numa amostra densa do mesmo intervalo, entre cerca de 23,9 e 52,2) — razão limitada, compatível com T ∈ O(n lg n), e bem abaixo da testemunha c = 2·10¹⁰, que é folgada de propósito. A oscilação da razão (sem tendência de crescimento) também é compatível com o palpite Θ(n lg n) do Teorema Master. Confere ainda o domínio: o argumento ⌊n/672⌋ + 189 só fica menor que n para n > ~190, que é exatamente o limite n ≥ 190 usado acima. Os números do PASSO 1 e do PASSO 2 estão escritos por extenso para conferência.
