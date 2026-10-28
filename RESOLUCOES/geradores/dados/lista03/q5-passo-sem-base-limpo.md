# Lista 3 (versão de 09/09/2026) — Questão 5 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Questão 5. Seja a sentença aberta em N:
P(n): 1 + 2 + ··· + n = n(n + 1)/2 + 1,
mostre que:
(i) Qualquer que seja n ∈ N, se P(n) é verdadeira, então P(n + 1) é verdadeira.
(ii) P(n) não é verdadeira para nenhum valor de n ∈ N."

## SOLUÇÃO FINAL

### Convenção
Seja S(n) = 1 + 2 + ··· + n = ∑_{k=1}^{n} k. O enunciado não diz se 0 ∈ N; a solução cobre
as duas convenções. Para n = 0, S(0) é a soma vazia, igual a 0.
Assim, P(n) é a afirmação  S(n) = n(n+1)/2 + 1.

### (i) Para todo n ∈ N, P(n) → P(n+1)
Seja n ∈ N arbitrário e suponha P(n), isto é,  S(n) = n(n+1)/2 + 1.
Como S(n+1) = S(n) + (n+1) (separação do último termo; vale também para n = 0, pois
S(1) = 0 + 1),
  S(n+1) = S(n) + (n+1)
         = n(n+1)/2 + 1 + (n+1)            ← hipótese P(n)
         = [n(n+1) + 2(n+1)]/2 + 1
         = (n+1)(n+2)/2 + 1.
Como (n+1)((n+1)+1)/2 = (n+1)(n+2)/2, isto é exatamente P(n+1).
Como n foi arbitrário, a implicação P(n) → P(n+1) vale para todo n ∈ N. ∎
(Observação: a prova de (i) é direta e usa apenas a hipótese P(n) e a definição de S; não
usa (ii) nem a fórmula verdadeira de S(n).)

### (ii) P(n) é falsa para todo n ∈ N
**Lema.** Para todo n ∈ N, S(n) = n(n+1)/2.
Prova por indução. Base: S(1) = 1 = 1·2/2; e, se 0 ∈ N, S(0) = 0 = 0·1/2.
Hipótese: para um n ∈ N fixado, S(n) = n(n+1)/2.
Passo: S(n+1) = S(n) + (n+1) = n(n+1)/2 + (n+1) = (n+1)(n+2)/2 ← hipótese aplicada.
Logo o Lema vale para todo n ∈ N. ∎
(É a mesma identidade da Questão 4(c) desta lista, aqui estendida a n = 0.)

**Conclusão de (ii).** Para qualquer n ∈ N, pelo Lema, o lado esquerdo de P(n) vale
S(n) = n(n+1)/2, e o lado direito vale n(n+1)/2 + 1 = S(n) + 1. Como S(n) ≠ S(n) + 1,
P(n) é falsa. Como n foi arbitrário, P(n) não é verdadeira para nenhum n ∈ N. ∎

### Por que (ii) não se prova só olhando a base
Verificar que P(1) é falsa (1 ≠ 2) mostra que a base falha, mas NÃO mostra que P(n) é falsa
para todo n: uma propriedade pode falhar nos primeiros valores e valer depois (por exemplo,
n! > 2ⁿ é falsa em n = 1, 2, 3 e verdadeira para todo n ≥ 4 — Questão 4(a) desta lista).
Por isso (ii) precisa de um argumento que valha para TODO n, e não só da base. Aqui esse
argumento é o Lema, que mostra que os dois lados diferem por exatamente 1 em todo n. Não é o
único caminho: a conta de (i) é reversível — como S(n+1) = S(n) + (n+1) e
(n+1)(n+2)/2 + 1 = [n(n+1)/2 + 1] + (n+1), vale S(n+1) = (n+1)(n+2)/2 + 1 se e somente se
S(n) = n(n+1)/2 + 1 —, logo P(n+1) → P(n), isto é, ¬P(n) → ¬P(n+1); uma indução sobre ¬P,
com base ¬P(1) (ou ¬P(0)), também prova (ii). Nos dois caminhos há base E passo: a falha
da base, sozinha, não basta.

### O que a questão ensina
(i) e (ii) juntos mostram que o passo indutivo sozinho não prova nada: aqui P(n) → P(n+1)
vale para todo n e, mesmo assim, P(n) é falsa para todo n. O que falta é um ponto de
partida: P(1) (ou P(0)) é falsa e, por (ii), nenhum P(m) é verdadeiro, de modo que a cadeia
de implicações nunca é disparada, qualquer que seja o valor inicial escolhido. A questão
mostra que a base é indispensável: um passo válido, sozinho, não prova nada.

## RESPOSTA
(i) Supondo S(n) = n(n+1)/2 + 1, soma-se n+1 aos dois lados e obtém-se
S(n+1) = (n+1)(n+2)/2 + 1, que é P(n+1); vale para todo n ∈ N.
(ii) Pelo Lema S(n) = n(n+1)/2 (provado por indução), o lado direito de P(n) excede o
esquerdo em exatamente 1 para todo n ∈ N, logo P(n) é sempre falsa.
Moral: o passo vale, a base não — e sem base a indução não conclui nada.
