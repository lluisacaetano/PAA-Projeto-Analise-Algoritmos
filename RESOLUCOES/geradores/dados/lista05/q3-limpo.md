# Lista 5 — Questão 3 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Suponha que, para um problema com entradas de tamanho n, você tenha que escolher um dentre três
algoritmos A, B e C. Considere que trata-se do pior caso de cada algoritmo.
1. O algoritmo A resolve problemas dividindo-os em cinco subproblemas de tamanho n/2,
recursivamente resolve cada subproblema e então combina as soluções em tempo linear.
2. O algoritmo B resolve problemas de tamanho n, recursivamente resolvendo dois subproblema
[sic] de tamanho n − 1 e então combina as soluções em tempo constante.
3. O algoritmo C resolve problemas dividindo-os em nove subproblemas de tamanho n/3,
recursivamente resolve cada subproblema e então combina as soluções em tempo θ(n²).
Indique qual dos algoritmos é assintoticamente mais eficiente no pior caso. Expresse sua
resposta em termos da notação θ. Justifique sua resposta. Resposta sem justificativa não será
considerada."

Formulário fornecido pela lista (Teorema Mestre, forma de Brassard & Bratley): sejam as
constantes naturais a ≥ 1, b ≥ 2 e k ≥ 0; f(n) = c·n^k com c > 0 real; T(n) = aT(n/b) + f(n);
n potência exata de b; T leva naturais em reais positivos e é assintoticamente não decrescente.
Então T(n) ∈ θ(n^k) se a < b^k; θ(n^k·lg n) se a = b^k; θ(n^(log_b a)) se a > b^k.
A lista também fornece a hierarquia 1 ≺ log n ≺ √n ≺ n ≺ n·log n ≺ n^c ≺ c^n ≺ n! ≺ n^n,
"onde c é uma constante arbitrária inteira ≥ 2". Ela não cobre diretamente as comparações desta
questão (log₂ 5 não é inteiro, e em n^c ≺ c^n a base é o mesmo c do expoente); por isso a §5
as prova diretamente.

## SOLUÇÃO FINAL

### 0. As três recorrências
Casos base: T(1) = t > 0 (qualquer constante positiva). O custo de combinar é positivo:
  A: T_A(n) = 5·T_A(n/2) + f_A(n),  f_A(n) ∈ Θ(n)   ("tempo linear")
  B: T_B(n) = 2·T_B(n − 1) + f_B(n), f_B(n) ∈ Θ(1)  ("tempo constante")
  C: T_C(n) = 9·T_C(n/3) + f_C(n),  f_C(n) ∈ Θ(n²)
Primeiro resolve-se cada uma com f exatamente da forma c·n^k, c > 0 (a que o teorema exige);
depois, na §4, mostra-se que trocar "= c·n^k" por "∈ Θ(n^k)" não muda a classe.

Hipótese de monotonia (a última do formulário, "T assintoticamente não decrescente"), para quaisquer t, c > 0. Nas potências de b, onde a
recorrência define T: T(b·n) = a·T(n) + f(b·n) > T(n), pois a ≥ 1, T(n) > 0 e f(b·n) > 0; e
T(1) = t > 0, então por indução T é positiva e crescente sobre as potências de b. Para B, do
mesmo modo, T_B(n) = 2T_B(n − 1) + c > T_B(n − 1) > 0. Que o custo não diminua com n a partir de
algum N (isto é, T(n) ≤ T(n + 1) para todo n ≥ N) é o que "T assintoticamente não decrescente"
significa; o formulário o assume, é natural para tempo de pior caso, e é usado na Observação
da §5.

### 1. Algoritmo A — Teorema Mestre, terceira linha
T_A(n) = 5T_A(n/2) + c·n: a = 5, b = 2, k = 1, c > 0. b^k = 2¹ = 2 e a = 5 > 2: **terceira
linha** do formulário (a > b^k). Logo
  **T_A(n) ∈ Θ(n^(log₂ 5))**, com log₂ 5 ≈ 2,3219.
Forma fechada (n = 2^m, T(1) = t): T_A(n) = (t + 2c/3)·n^(log₂ 5) − (2c/3)·n.
Checagem com t = c = 1: T_A(n) = (5/3)·n^(log₂ 5) − (2/3)·n; T_A(2) = 5·1 + 2 = 7 e
(5/3)·5 − (2/3)·2 = 25/3 − 4/3 = 7 ✓.
Testemunhas (t, c quaisquer): c₁ = t, c₂ = t + 2c/3, n₀ = 1. A cota superior é imediata; a
inferior, (t + 2c/3)n^(log₂ 5) − (2c/3)n ≥ t·n^(log₂ 5), equivale a (2c/3)(n^(log₂ 5) − n) ≥ 0,
verdadeira para n ≥ 1 porque log₂ 5 > 1. Com t = c = 1: c₁ = 1, c₂ = 5/3, e em n = n₀ = 1:
1 ≤ 1 ≤ 5/3 ✓.

### 2. Algoritmo B — fora do Teorema Mestre
A chamada é T(n − 1), não T(n/b): subtrair 1 não é dividir por uma constante b (n − 1 = n/b
exigiria b = n/(n − 1), que varia com n). O teorema não se aplica; resolve-se por expansão.
Com T_B(1) = t e custo de combinação constante f_B(n) = c > 0:
  T_B(n) = 2^(n−1)·t + c·(2^(n−1) − 1) = 2^(n−1)·(t + c) − c   para n ≥ 1.
Prova por indução: n = 1 dá t + c − c = t ✓; se vale para n − 1 (n ≥ 2),
2·[2^(n−2)(t + c) − c] + c = 2^(n−1)(t + c) − c ✓.
Testemunhas: (t/2)·2^n = 2^(n−1)·t ≤ T_B(n) ≤ 2^(n−1)(t + c) = ((t + c)/2)·2^n para n ≥ 1, isto é
c₁ = t/2, c₂ = (t + c)/2, n₀ = 1. Com t = c = 1: T_B(n) = 2^n − 1, c₁ = 1/2, c₂ = 1, e em n = 1:
1 ≤ 1 ≤ 2 ✓. Logo **T_B(n) ∈ Θ(2^n)**.
(Intuição: a árvore de recursão é binária completa de altura n − 1, com 2^n − 1 nós.)

### 3. Algoritmo C — Teorema Mestre, segunda linha
T_C(n) = 9T_C(n/3) + c·n²: a = 9, b = 3, k = 2, c > 0. b^k = 3² = 9 = a: **segunda linha**
(a = b^k). Logo
  **T_C(n) ∈ Θ(n²·lg n)**.
Forma fechada (n = 3^m, T(1) = t): T_C(n) = n²·(t + c·log₃ n) — cada um dos m níveis da árvore
custa c·9^i·(3^(m−i))² = c·9^m = c·n², mais as n² folhas de custo t.
Checagem com t = c = 1: T_C(n) = n²(log₃ n + 1); T_C(3) = 9 + 9 = 18 = 9·(1 + 1) ✓.
Testemunhas (t, c quaisquer): c₁ = c/lg 3, c₂ = (t + c)/lg 3, n₀ = 3. Como log₃ n = lg n / lg 3
e, para n ≥ 3, 1 ≤ lg n / lg 3: (c/lg 3)·n² lg n ≤ n²(t + c log₃ n) ≤ ((t + c)/lg 3)·n² lg n.
Com t = c = 1: c₁ = 1/lg 3, c₂ = 2/lg 3; em n = n₀ = 3, n² lg n = 9 lg 3, logo
c₁·9 lg 3 = 9 ≤ 18 ≤ 18 = c₂·9 lg 3 ✓ (igualdade na cota superior).
n₀ = 1 não serve: lg 1 = 0 e T_C(1) = t > 0.

### 4. De "= c·n^k" para "∈ Θ(n^k)"
O enunciado diz "tempo linear", "tempo constante" e "θ(n²)", não exatamente c·n^k. Isso não
muda nenhuma classe, pelo seguinte lema de comparação.
Lema. Sejam T e T′ definidas pela mesma recorrência (mesmo a, mesma forma de chamada), com o
mesmo valor no caso base e com f(n) ≤ f′(n) para todo n. Então T(n) ≤ T′(n) para todo n.
Prova: indução sobre n (nas potências de b, ou em n ≥ 1 para B), usando a > 0:
T(n) = a·T(·) + f(n) ≤ a·T′(·) + f′(n) = T′(n). ∎
Como f(n) ∈ Θ(n^k) e f(n) > 0 para todo n (combinar custa alguma coisa), existem c′, c″ > 0 com
c′·n^k ≤ f(n) ≤ c″·n^k para **todo** n ≥ 1: para n ≥ n₀ isso é a definição de Θ, e para os
finitos n < n₀ basta diminuir c′ e aumentar c″ (f(n)/n^k é positivo em cada um deles). Pelo
Lema, T fica entre as soluções com f = c′·n^k e com f = c″·n^k, e as duas estão na mesma classe
Θ (§1–§3, cujas formas fechadas e testemunhas valem para quaisquer t, c > 0). Logo
T_A ∈ Θ(n^(log₂ 5)), T_B ∈ Θ(2^n), T_C ∈ Θ(n² lg n).

### 5. Comparação
**C é assintoticamente mais eficiente que A.** n² lg n / n^(log₂ 5) = lg n / n^ε com
ε = log₂ 5 − 2 = log₂(5/4) ≈ 0,3219 > 0. Aplicando L'Hôpital às funções de variável real x > 0
(o limite da sequência é o mesmo),
lim lg x / x^ε = lim (1/(x ln 2)) / (ε·x^(ε−1)) = lim 1/(ε·ln 2·x^ε) = 0.
Então n² lg n ∈ o(n^(log₂ 5)): para quaisquer constantes positivas c₂^C e c₁^A, a partir de
algum n vale c₂^C·n² lg n < c₁^A·n^(log₂ 5), e portanto — com as duas cotas valendo no mesmo n,
pela Observação abaixo — T_C(n) < T_A(n).
**A é assintoticamente mais eficiente que B.** n^(log₂ 5) ≤ n³ para n ≥ 1, e n³/2^n → 0 (três
aplicações de L'Hôpital, de novo em variável real: x³/2^x → 3x²/(2^x ln 2) → 6x/(2^x ln² 2) →
6/(2^x ln³ 2) → 0, cada seta significando "tem o mesmo limite que"). Logo n^(log₂ 5) ∈ o(2^n).
Ordem: **C ≺ A ≺ B**, isto é, Θ(n² lg n) ≺ Θ(n^(log₂ 5)) ≺ Θ(2^n).

Observação — comparar A (definido nas potências de 2) com C (potências de 3) no mesmo n. O
teorema é enunciado para n potência exata de b; é a hipótese "T assintoticamente não
decrescente" que permite estender a conclusão a todo n. Esboço: se T é não decrescente para n ≥ N e
c₁g(b^j) ≤ T(b^j) ≤ c₂g(b^j) para b^j ≥ n₀, então para b^j ≤ n < b^(j+1) (com
b^j ≥ máx(n₀, N, b)) vale
T(n) ≤ T(b^(j+1)) ≤ c₂g(b^(j+1)) ≤ c₂g(b·n) e T(n) ≥ T(b^j) ≥ c₁g(b^j) ≥ c₁g(n/b), usando que g é
não decrescente para n ≥ 1; para g(n) = n^e·lg^p n (e > 0, p ≥ 0 — é o caso de n^(log₂ 5) e de
n² lg n) tem-se g(b·n) ≤ b^e·2^p·g(n) e g(n/b) ≥ g(n)/(b^e·2^p) para n ≥ b², de modo que a
classe Θ(g) vale para todo n grande. Com isso, T_A e T_C são comparáveis no mesmo n.

A vantagem de C é assintótica: para as funções de referência (sem as constantes ocultas, que
não se conhecem), a razão lg n / n^0,3219 ainda vale ≈ 1,07 em n = 2^10 e cai para ≈ 0,23 em
n = 2^20.

## RESPOSTA
A: T(n) = 5T(n/2) + Θ(n) ⇒ a = 5 > b^k = 2 (terceira linha) ⇒ Θ(n^(log₂ 5)), com
   log₂ 5 ≈ 2,32.
B: T(n) = 2T(n − 1) + Θ(1) ⇒ fora do teorema (n − 1 não é n/b); com T(1) = t e custo de
   combinação constante c, a expansão dá T(n) = 2^(n−1)(t + c) − c, e pelo lema da §4 qualquer
   custo em Θ(1) fica entre duas dessas ⇒ Θ(2^n).
C: T(n) = 9T(n/3) + Θ(n²) ⇒ a = 9 = b^k = 9 (segunda linha) ⇒ Θ(n² lg n).
O mais eficiente no pior caso é **C, com Θ(n² lg n)**; a ordem é C ≺ A ≺ B, porque
n² lg n ∈ o(n^(log₂ 5)) (log₂ 5 > 2 e lg n ∈ o(n^ε) para ε > 0) e n^(log₂ 5) ∈ o(2^n).
