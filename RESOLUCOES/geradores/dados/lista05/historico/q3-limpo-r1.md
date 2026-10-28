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
A lista também fornece a hierarquia 1 ≺ log n ≺ √n ≺ n ≺ n·log n ≺ n^c ≺ c^n ≺ n! ≺ n^n.

## SOLUÇÃO FINAL

### 0. As três recorrências
Casos base: T(1) = t > 0 (qualquer constante positiva). O custo de combinar é positivo:
  A: T_A(n) = 5·T_A(n/2) + f_A(n),  f_A(n) ∈ Θ(n)   ("tempo linear")
  B: T_B(n) = 2·T_B(n − 1) + f_B(n), f_B(n) ∈ Θ(1)  ("tempo constante")
  C: T_C(n) = 9·T_C(n/3) + f_C(n),  f_C(n) ∈ Θ(n²)
Primeiro resolve-se cada uma com f exatamente da forma c·n^k (a que o teorema exige); depois,
na §4, mostra-se que trocar "= c·n^k" por "∈ Θ(n^k)" não muda a classe.

### 1. Algoritmo A — Teorema Mestre, terceira linha
T_A(n) = 5T_A(n/2) + c·n: a = 5, b = 2, k = 1, c > 0. b^k = 2¹ = 2 e a = 5 > 2: **terceira
linha** do formulário (a > b^k). Logo
  **T_A(n) ∈ Θ(n^(log₂ 5))**, com log₂ 5 ≈ 2,3219.
Conferência por forma fechada (T(1) = 1, c = 1, n = 2^m): T_A(n) = (5/3)·n^(log₂ 5) − (2/3)·n.
Checagem: T_A(2) = 5·1 + 2 = 7 e (5/3)·5 − (2/3)·2 = 25/3 − 4/3 = 7 ✓.
Testemunhas: c₁ = 1, c₂ = 5/3, n₀ = 1. A cota superior é imediata; a inferior,
(5/3)n^(log₂ 5) − (2/3)n ≥ n^(log₂ 5), equivale a (2/3)n^(log₂ 5) ≥ (2/3)n, isto é,
n^(log₂ 5 − 1) ≥ 1, verdadeira para n ≥ 1. Em n = n₀ = 1: 1 ≤ 1 ≤ 5/3 ✓.
Hipóteses do teorema: T_A é positiva e crescente sobre as potências de 2 (pela forma fechada).

### 2. Algoritmo B — fora do Teorema Mestre
A chamada é T(n − 1), não T(n/b): subtrair 1 não é dividir por uma constante b (n − 1 = n/b
exigiria b = n/(n − 1), que depende de n). O teorema não se aplica; resolve-se por expansão.
Com T_B(1) = t e f_B(n) = c > 0:
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
Conferência por forma fechada (T(1) = 1, c = 1, n = 3^m): T_C(n) = n²·(log₃ n + 1) — cada um
dos m níveis da árvore custa 9^i·(3^(m−i))² = 9^m = n², mais as n² folhas.
Checagem: T_C(3) = 9 + 9 = 18 = 9·(1 + 1) ✓.
Testemunhas: c₁ = 1/lg 3, c₂ = 2/lg 3, n₀ = 3. Como log₃ n = lg n / lg 3 e, para n ≥ 3,
1 ≤ lg n / lg 3: (1/lg 3)·n² lg n ≤ n²(log₃ n + 1) ≤ (2/lg 3)·n² lg n. Em n = n₀ = 3:
n² lg n = 9 lg 3, logo c₁·9 lg 3 = 9 ≤ 18 ≤ 18 = c₂·9 lg 3 ✓ (igualdade na cota superior).
n₀ = 1 não serve: lg 1 = 0 e T_C(1) = 1 > 0.

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
Θ (§1–§3 valem para qualquer c > 0). Logo T_A ∈ Θ(n^(log₂ 5)), T_B ∈ Θ(2^n), T_C ∈ Θ(n² lg n).

### 5. Comparação
**C é assintoticamente mais eficiente que A.** n² lg n / n^(log₂ 5) = lg n / n^ε com
ε = log₂ 5 − 2 = log₂(5/4) ≈ 0,3219 > 0. Por L'Hôpital,
lim lg n / n^ε = lim (1/(n ln 2)) / (ε·n^(ε−1)) = lim 1/(ε·ln 2·n^ε) = 0.
Então n² lg n ∈ o(n^(log₂ 5)): para qualquer constante, a partir de algum n, c₂^C·n² lg n fica
abaixo de c₁^A·n^(log₂ 5), e portanto T_C(n) < T_A(n).
**A é assintoticamente mais eficiente que B.** n^(log₂ 5) ≤ n³ para n ≥ 1, e n³/2^n → 0 (três
aplicações de L'Hôpital: n³/2^n → 3n²/(2^n ln 2) → 6n/(2^n ln² 2) → 6/(2^n ln³ 2) → 0). Logo
n^(log₂ 5) ∈ o(2^n).
Ordem: **C ≺ A ≺ B**, isto é, Θ(n² lg n) ≺ Θ(n^(log₂ 5)) ≺ Θ(2^n).

Observação — comparar A (definido nas potências de 2) com C (potências de 3) no mesmo n. O
teorema é enunciado para n potência exata de b; é a hipótese "T assintoticamente não
decrescente" que permite estender a conclusão a todo n. Esboço: se T é não decrescente e
c₁g(b^j) ≤ T(b^j) ≤ c₂g(b^j), então para b^j ≤ n < b^(j+1) vale
T(n) ≤ T(b^(j+1)) ≤ c₂g(b^(j+1)) ≤ c₂g(b·n) e T(n) ≥ T(b^j) ≥ c₁g(b^j) ≥ c₁g(n/b); para
g(n) = n^e·lg^p n (é o caso de n^(log₂ 5) e de n² lg n) tem-se g(b·n) ≤ b^e·2^p·g(n) e
g(n/b) ≥ g(n)/(b^e·2^p) para n ≥ b², de modo que a classe Θ(g) vale para todo n grande. Com isso,
T_A e T_C são comparáveis no mesmo n.

A vantagem de C é assintótica e demora a aparecer: a razão das funções de referência,
lg n / n^0,3219, ainda vale ≈ 1,07 em n = 2^10 e cai para ≈ 0,23 em n = 2^20.

## RESPOSTA
A: T(n) = 5T(n/2) + Θ(n) ⇒ a = 5 > b^k = 2 (terceira linha) ⇒ Θ(n^(log₂ 5)) ≈ Θ(n^2,32).
B: T(n) = 2T(n − 1) + Θ(1) ⇒ fora do teorema; por expansão T(n) = 2^(n−1)(t + c) − c ⇒ Θ(2^n).
C: T(n) = 9T(n/3) + Θ(n²) ⇒ a = 9 = b^k = 9 (segunda linha) ⇒ Θ(n² lg n).
O mais eficiente no pior caso é **C, com Θ(n² lg n)**; a ordem é C ≺ A ≺ B, porque
n² lg n ∈ o(n^(log₂ 5)) (log₂ 5 > 2 e lg n ∈ o(n^ε) para ε > 0) e n^(log₂ 5) ∈ o(2^n).
