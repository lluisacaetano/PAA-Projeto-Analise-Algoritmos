# Lista 5 — Questão 5 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"(0.5 ponto) Usando o teorema mestre, indique o limite assintótico usando a notação Θ, para cada
uma das equações de recorrência abaixo. Considere o caso base T(1) = 1 ou T(n) = c, para alguma
constante c e ∀n ≤ n0, para alguma constante n0. Suponha, também, que n uma [sic] potência exata
de b. Escolha o valor adequado para b conforme a equação de recorrência a ser resolvida.
Justifique todas as suas respostas. Respostas sem justificativas não serão consideradas. Pode
acontecer de não ser aplicável a versão do teorema mestre discutida em sala de aula e também
apresentada nessa lista de exercícios (veja em Informações que pode [sic] ser úteis). Nesse(s)
caso(s) apresente o motivo pelo qual essa versão do teorema mestre não se aplica.
(a) T(n) = T(n/3) + 1
(b) T(n) = 2T(n/2) + n ∗ lgn
(c) T(n) = T(2n/3) + n
(d) T(n) = 5T(n/4) − n
(e) T(n) = T(n − 1) + 3
(f) T(n) = T(n/3) + 0
(g) T(n) = 5T(n/4) − n²
(h) T(n) = T(2n/4) + n
(i) T(n) = 3/2T(n/4) − n²
(j) T(n) = 3T(n/2) + n"

Teorema mestre (literal, das "Informações que podem ser úteis"): "Sejam as constantes naturais
a ≥ 1, b ≥ 2 e k ≥ 0. Considere a função f(n) da forma c ∗ n^k, na qual c > 0 e ∈ R, seja a
equação de recorrência dada por T(n) = aT(n/b) + f(n) e suponha n uma potência exata de b.
Considere ainda que T é uma função que leva números naturais em números reais positivos e que T
é assintoticamente não decrescente, Nessas condições, [BRASSARD and BRATLEY, 1996] indicam que a
solução dessa recorrência é limitada assintoticamente por T(n) = θ(n^k) se a < b^k;
θ(n^k ∗ lg n) se a = b^k; θ(n^(log_b a)) se a > b^k."

## SOLUÇÃO FINAL

### 0. O que o teorema exige — a lista de conferência
Para aplicar esta versão é preciso ter, **todas ao mesmo tempo**:
  (H1) a forma T(n) = a·T(n/b) + f(n) — uma única chamada "dividida por b", repetida a vezes;
  (H2) a natural, a ≥ 1;
  (H3) b natural, b ≥ 2;
  (H4) f(n) = c·n^k exatamente, com c > 0 real e k ≥ 0 natural;
  (H5) T com valores reais positivos e assintoticamente não decrescente (conferida abaixo nas
       potências de b, que é onde a recorrência define T).
Os casos, **na ordem em que o formulário os imprime**:
  1ª linha: a < b^k → Θ(n^k);  2ª linha: a = b^k → Θ(n^k lg n);  3ª linha: a > b^k → Θ(n^(log_b a)).
Nos itens aplicáveis confere-se o resultado com a forma fechada exata (T(1) = 1, n = b^m) e
exibem-se testemunhas c₁, c₂, n₀ verificadas em n = n₀. Nos itens não aplicáveis dá-se o motivo
e, à parte, o que a recorrência realmente faz — o que mostra que a hipótese violada não é
detalhe: em (f), (g) e (i), aplicar a fórmula às cegas daria resposta **errada** qualquer que
seja o caso base; em (d), daria resposta errada com o caso base T(1) = 1 do enunciado (e com
qualquer T(1) ≤ 4).

### (a) T(n) = T(n/3) + 1 — APLICA
a = 1, b = 3, f(n) = 1 = 1·n⁰ ⇒ c = 1 > 0, k = 0. (H1)–(H4) valem.
b^k = 3⁰ = 1 = a: **2ª linha** ⇒ T(n) ∈ Θ(n⁰·lg n) = **Θ(lg n)**.
Forma fechada (n = 3^m, T(1) = 1): T(3^m) = m + 1, isto é, T(n) = log₃ n + 1. Positiva e
crescente nas potências de 3: (H5) ✓.
Testemunhas: c₁ = 1/lg 3, c₂ = 2/lg 3, n₀ = 3. Com log₃ n = lg n / lg 3 e 1 ≤ lg n / lg 3 para
n ≥ 3: (1/lg 3)·lg n ≤ log₃ n + 1 ≤ (2/lg 3)·lg n. Em n = n₀ = 3: 1 ≤ T(3) = 2 ≤ 2 ✓.
n₀ = 1 não serve: lg 1 = 0 e T(1) = 1 > c₂·0.

### (b) T(n) = 2T(n/2) + n·lg n — NÃO APLICA
a = 2, b = 2 servem, mas **f(n) = n lg n não é da forma c·n^k** (viola H4). Não existem c, k
com n lg n = c·n^k para todo n potência de 2: n = 2 daria 2 = c·2^k e n = 4 daria 8 = c·4^k,
donde 2^k = 4, k = 2 e c = 1/2; mas em n = 8, c·8^k = 32 ≠ 24 = 8·lg 8. Nem mesmo "f ∈ Θ(n^k)"
salvaria: para k ∈ {0, 1}, n lg n / n^k ≥ lg n → ∞; para k ≥ 2, n lg n / n^k ≤ lg n / n → 0.
Então f não está em Θ(n^k) para k natural nenhum.
À parte (fora do teorema): por expansão, T(2^m) = 2^m·(1 + m(m + 1)/2), isto é,
T(n) = n·(1 + lg n·(lg n + 1)/2) ∈ Θ(n lg² n) (c₁ = 1/2, c₂ = 2, n₀ = 2; em n = 2: 1 ≤ 4 ≤ 4).

### (c) T(n) = T(2n/3) + n — NÃO APLICA
2n/3 = n/(3/2): o "b" seria **3/2, que não é natural nem ≥ 2** (viola H3). Também não há "n
potência exata de b" inteira: (3/2)^m = 3^m/2^m, com numerador ímpar e denominador par, não é
inteiro para m ≥ 1.
À parte: com piso, T(n) = T(⌊2n/3⌋) + n e T(1) = 1, vale n ≤ T(n) ≤ 3n (soma geométrica de
razão 2/3), logo Θ(n) — conferido para n = 1…200 000.

### (d) T(n) = 5T(n/4) − n — NÃO APLICA
a = 5, b = 4, mas f(n) = −n = (−1)·n¹: **c = −1 < 0** (viola H4). Com o caso base T(1) = 1,
(H5) também falha: T(4) = 5 − 4 = 1 e T(16) = 5 − 16 = −11 < 0 — T deixa de ser positiva.
À parte: com a recorrência aplicada desde n = 4, T(4^m) = (T(1) − 4)·n^(log₄ 5) + 4n. A resposta
dependeria do caso base: Θ(n^(log₄ 5)) se T(1) > 4; exatamente 4n se T(1) = 4; negativa a partir
de algum n se T(1) < 4. Com a outra opção do enunciado, T(n) = c para n ≤ n0, o limiar muda:
sendo 4^(m0) a maior potência de 4 que é ≤ n0, T(4^m) = ((c − 4·4^(m0))/5^(m0))·n^(log₄ 5) + 4n
para m ≥ m0, e o sinal do coeficiente líder depende de c > 4·4^(m0) (por exemplo, n0 = 4 e c = 10
dão T(4⁶) < 0). Aplicar o teorema às cegas (a = 5 > 4 = b^k, 3ª linha) daria Θ(n^(log₄ 5)) —
errado com T(1) = 1, quando T é negativa; só coincidiria com o comportamento real quando o caso
base é grande.

### (e) T(n) = T(n − 1) + 3 — NÃO APLICA
A chamada é T(n − 1), não T(n/b) (viola H1): n − 1 = n/b exigiria b = n/(n − 1), que varia com n
(vale 2 só em n = 2 e fica entre 1 e 2 para n ≥ 3) — não é uma constante. É uma recorrência
subtrativa.
À parte: por expansão, T(n) = T(1) + 3(n − 1) = 3n − 2 (com T(1) = 1) ∈ Θ(n); c₁ = 1, c₂ = 3,
n₀ = 1 (n ≤ 3n − 2 ⟺ n ≥ 1; em n = 1: 1 ≤ 1 ≤ 3).

### (f) T(n) = T(n/3) + 0 — NÃO APLICA
a = 1, b = 3, mas f(n) = 0 **não é da forma c·n^k com c > 0** (viola H4): 0 = c·n^k obriga
c = 0. A exigência não é formalidade: aplicando a fórmula com "c = 0, k = 0" (a = 1 = b⁰, 2ª
linha) sairia Θ(lg n), que é **falso**.
À parte: T(3^m) = T(1) para todo m — T é constante, Θ(1) (c₁ = c₂ = 1, n₀ = 1, com T(1) = 1).

### (g) T(n) = 5T(n/4) − n² — NÃO APLICA
a = 5, b = 4, mas f(n) = −n²: **c = −1 < 0** (viola H4). E T não é positiva (viola H5): com
T(1) = 1, T(4) = 5 − 16 = −11.
À parte: T(4^m) = (T(1) + 16/11)·n^(log₄ 5) − (16/11)·n². Como log₄ 5 ≈ 1,161 < 2, o termo
−(16/11)n² domina e T fica negativa a partir de algum n **qualquer que seja o caso base** (com
T(1) = 1 já em n = 4; com T(1) = 10⁶, em n = 4¹²). Às cegas (a = 5 < 16 = b^k, 1ª linha) sairia
Θ(n²) — absurdo para uma função que tende a −∞.

### (h) T(n) = T(2n/4) + n — APLICA
Simplificando o argumento: 2n/4 = n/2, logo **b = 2** (natural ≥ 2). a = 1, f(n) = n = 1·n¹ ⇒
c = 1 > 0, k = 1. (H1)–(H4) valem.
b^k = 2¹ = 2 > 1 = a, isto é, a < b^k: **1ª linha** ⇒ T(n) ∈ **Θ(n)**.
Forma fechada (n = 2^m, T(1) = 1): T(n) = 2n − 1 (T(2) = 1 + 2 = 3 ✓). Positiva e crescente:
(H5) ✓.
Testemunhas: c₁ = 1, c₂ = 2, n₀ = 1: n ≤ 2n − 1 ⟺ n ≥ 1, e 2n − 1 ≤ 2n. Em n = 1: 1 ≤ 1 ≤ 2 ✓.
A armadilha do item: ler "2n/4" e escolher b = 4 (ou a = 2). O valor adequado de b sai do
argumento já simplificado.

### (i) T(n) = (3/2)·T(n/4) − n² — NÃO APLICA
Lendo "3/2T(n/4)" como (3/2)·T(n/4): **a = 3/2 não é natural** (viola H2) e **c = −1 < 0**
(viola H4) — dois motivos independentes. (Na outra leitura, 3/(2·T(n/4)), nem a forma
a·T(n/b) + f(n) existe — H1; e em qualquer leitura f(n) = −n² tem c < 0. O veredito não depende
da leitura.) E T não é positiva (H5): com T(1) = 1, T(4) = 3/2 − 16 = −29/2.
À parte: T(4^m) = (T(1) + 32/29)·(3/2)^m − (32/29)·n², negativa a partir de algum n para
qualquer caso base, pois (3/2)^m = n^(log₄(3/2)) e log₄(3/2) ≈ 0,29 < 2. Às cegas
(a = 3/2 < 16 = b^k, 1ª linha) sairia Θ(n²) — absurdo para uma função que tende a −∞.

### (j) T(n) = 3T(n/2) + n — APLICA
a = 3, b = 2, f(n) = n = 1·n¹ ⇒ c = 1 > 0, k = 1. (H1)–(H4) valem.
b^k = 2 < 3 = a: **3ª linha** ⇒ T(n) ∈ **Θ(n^(log₂ 3))**, com log₂ 3 ≈ 1,585.
Forma fechada (n = 2^m, T(1) = 1): T(n) = 3·n^(log₂ 3) − 2n, isto é, T(2^m) = 3^(m+1) − 2^(m+1)
(T(2) = 3 + 2 = 5 = 9 − 4 ✓). Positiva e crescente: T(2^(m+1)) − T(2^m) = 2·3^(m+1) − 2^(m+1) > 0.
Testemunhas: c₁ = 1, c₂ = 3, n₀ = 1: a cota inferior 3n^(log₂ 3) − 2n ≥ n^(log₂ 3) equivale a
n^(log₂ 3 − 1) ≥ 1, verdadeira para n ≥ 1. Em n = 1: 1 ≤ 1 ≤ 3 ✓.

### O caso base não muda as classes dos itens aplicáveis
Com T(1) = t > 0 em vez de 1: (a) T(n) = log₃ n + t; (h) T(n) = 2n − 2 + t; (j)
T(n) = (t + 2)·n^(log₂ 3) − 2n. Com T(n) = c para n ≤ n0 (a outra opção do enunciado), sendo
b^(m0) a maior potência de b que é ≤ n0: (a) T(3^m) = c + (m − m0); (h) T(2^m) = 2n + c − 2^(m0+1);
(j) T(2^m) = ((c + 2·2^(m0))/3^(m0))·n^(log₂ 3) − 2n, para m ≥ m0. Em todos os casos o termo
dominante tem coeficiente positivo e as classes Θ(lg n), Θ(n) e Θ(n^(log₂ 3)) se mantêm; só as
constantes c₁, c₂ (e n₀) mudam.

### Quadro-resumo
| item | a | b | f(n) | hipótese violada | resposta |
| (a) | 1 | 3 | 1 = n⁰ | — | a = b^k = 1, 2ª linha: Θ(lg n) |
| (b) | 2 | 2 | n lg n | H4: não é c·n^k | não aplica (de fato Θ(n lg² n)) |
| (c) | 1 | 3/2 | n | H3: b = 3/2 | não aplica (de fato Θ(n)) |
| (d) | 5 | 4 | −n | H4: c < 0; H5 com T(1) = 1 | não aplica (T fica negativa com T(1) = 1) |
| (e) | — | — | 3 | H1: T(n − 1) | não aplica (de fato 3n − 2 ∈ Θ(n)) |
| (f) | 1 | 3 | 0 | H4: c = 0 | não aplica (de fato Θ(1), não Θ(lg n)) |
| (g) | 5 | 4 | −n² | H4: c < 0; H5 | não aplica (T → −∞ para todo caso base) |
| (h) | 1 | 2 | n | — | a = 1 < b^k = 2, 1ª linha: Θ(n) |
| (i) | 3/2 | 4 | −n² | H2: a = 3/2; H4: c < 0; H5 | não aplica (T → −∞ para todo caso base) |
| (j) | 3 | 2 | n | — | a = 3 > b^k = 2, 3ª linha: Θ(n^(log₂ 3)) |

## RESPOSTA
(a) Θ(lg n) — a = 1, b = 3, k = 0, a = b^k.
(b) Não se aplica: f(n) = n lg n não é da forma c·n^k.
(c) Não se aplica: b = 3/2 não é natural ≥ 2.
(d) Não se aplica: c = −1 < 0 (e, com T(1) = 1, T fica negativa: T(16) = −11).
(e) Não se aplica: T(n − 1) não é da forma T(n/b) (recorrência subtrativa).
(f) Não se aplica: f(n) = 0 exige c = 0, e o teorema pede c > 0 (a fórmula daria Θ(lg n); o
    certo é Θ(1)).
(g) Não se aplica: c = −1 < 0 (e T fica negativa: T(4) = −11 com T(1) = 1).
(h) Θ(n) — 2n/4 = n/2, logo a = 1, b = 2, k = 1, a < b^k.
(i) Não se aplica: a = 3/2 não é natural, e c = −1 < 0.
(j) Θ(n^(log₂ 3)) — a = 3, b = 2, k = 1, a > b^k.
