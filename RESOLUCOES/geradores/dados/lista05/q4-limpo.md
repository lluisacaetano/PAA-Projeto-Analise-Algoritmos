# Lista 5 — Questão 4 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"(1.0 ponto) Prove a assertiva abaixo usando o método da indução matemática.
a) 1/2 + 1/4 + 1/8 + ··· + 1/2^n < 1 , ∀n ≥ 1"

## SOLUÇÃO FINAL

### Notação
Para cada inteiro n ≥ 1, S(n) = ∑_{i=1}^{n} 1/2^i. A escrita 1/2 + 1/4 + 1/8 + … + 1/2^n do
enunciado é a notação usual para essa soma: só entram os termos com i ≤ n. Para n ≤ 2 a forma
com reticências é apenas ilustrativa — vale a definição por ∑: S(1) = 1/2 (um único termo) e
S(2) = 1/2 + 1/4 = 3/4.

### Por que a indução ingênua (separando o último termo) não fecha
Tentando provar Q(n): S(n) < 1 separando o **último** termo, o passo seria
S(n+1) = S(n) + 1/2^(n+1) < 1 + 1/2^(n+1) — e isso não é < 1. Usando só a informação
"S(n) < 1", o passo exigiria a implicação, para todo real s, "se s < 1 então
s + 1/2^(n+1) < 1", que é falsa (contraexemplo da implicação, não da assertiva: s = 31/32 e
n = 3 dão 31/32 + 1/16 = 33/32 ≥ 1). A hipótese "S(n) < 1" perde a informação de **quanto**
falta para 1. Há duas saídas: fortalecer a hipótese (Prova 1) ou separar o **primeiro** termo
em vez do último (Prova 2). As duas são provas completas; basta uma.

### Prova 1 — fortalecendo a hipótese
Proposição. Para todo inteiro n ≥ 1, P(n): S(n) = 1 − 1/2^n.

Base (n = 1). Lado esquerdo: S(1) = 1/2. Lado direito: 1 − 1/2¹ = 1/2. Iguais: P(1) vale.

Hipótese de indução. Seja n ≥ 1 um inteiro fixado e suponha P(n): S(n) = 1 − 1/2^n.

Passo. Separando o último termo da soma até n + 1:
  S(n+1) = S(n) + 1/2^(n+1)
         = 1 − 1/2^n + 1/2^(n+1)          ← h.i. aplicada a S(n)
         = 1 − 2/2^(n+1) + 1/2^(n+1)
         = 1 − 1/2^(n+1),
que é P(n+1). Como P(1) vale e P(n) ⇒ P(n+1) para todo n ≥ 1, pelo princípio da indução P(n)
vale para todo n ≥ 1.

Conclusão. Como 2^n > 0, tem-se 1/2^n > 0 e S(n) = 1 − 1/2^n < 1 para todo n ≥ 1. ∎

### Prova 2 — a própria assertiva como hipótese de indução, Q(n), separando o primeiro termo
Proposição. Para todo inteiro n ≥ 1, Q(n): S(n) < 1.

Base (n = 1). S(1) = 1/2 < 1.

Hipótese de indução. Seja n ≥ 1 um inteiro fixado e suponha Q(n): S(n) < 1.

Passo. Separando o primeiro termo e pondo 1/2 em evidência no restante:
  S(n+1) = 1/2 + ∑_{i=2}^{n+1} 1/2^i = 1/2 + ∑_{j=1}^{n} 1/2^(j+1) = 1/2 + (1/2)·∑_{j=1}^{n} 1/2^j
         = 1/2 + S(n)/2
         < 1/2 + 1/2 = 1                  ← h.i.: S(n) < 1, logo S(n)/2 < 1/2 (divide-se por 2 > 0)
isto é, Q(n+1). Como Q(1) vale e Q(n) ⇒ Q(n+1) para todo n ≥ 1, pelo princípio da indução Q(n)
vale para todo n ≥ 1. ∎
(A troca de índice é j = i − 1, que leva i = 2, …, n+1 em j = 1, …, n; com n = 1 as duas somas
têm um único termo, 1/4.)

### Conferência
S(1) = 1/2, S(2) = 3/4, S(3) = 7/8 = 1 − 1/8. A identidade S(n) = 1 − 1/2^n, a desigualdade
S(n) < 1 e a relação S(n+1) = 1/2 + S(n)/2 foram conferidas em aritmética racional exata para
n = 1, …, 399.

## RESPOSTA
Por indução em n, prova-se a forma mais forte P(n): 1/2 + 1/4 + … + 1/2^n = 1 − 1/2^n (base:
1/2 = 1/2; passo: 1 − 1/2^n + 1/2^(n+1) = 1 − 1/2^(n+1)); daí a soma é < 1, pois 1/2^n > 0.
A indução direta em "< 1" separando o último termo não fecha; ela fecha separando o primeiro:
S(n+1) = 1/2 + S(n)/2 < 1/2 + 1/2 = 1.
