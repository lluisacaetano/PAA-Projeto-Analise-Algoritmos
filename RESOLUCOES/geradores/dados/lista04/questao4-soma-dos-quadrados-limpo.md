# Lista 4 (versão de 09/09/2026) — Questão 4 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Questão 4. Prove a proposição P(n) = 1² + 2² + 3² + ... + n² = n ∗ (n + 1) ∗ (2n + 1)/6
usando o método da indução matemática."

## SOLUÇÃO FINAL

### Suposições declaradas
1. O enunciado escreve "P(n) = ...", mas P(n) é uma proposição, não um número. Lê-se
   P(n): 1² + 2² + ... + n² = n(n+1)(2n+1)/6.
2. O enunciado não fixa o domínio de n. Supõe-se n inteiro, n ≥ 1, que é o menor valor
   em que a soma escrita "1² + 2² + ... + n²" tem ao menos o termo 1². (A identidade também
   vale em n = 0, lendo o lado esquerdo como soma vazia, igual a 0: 0·1·1/6 = 0. Isso não
   é necessário para o que se pede.)
3. Em notação de somatório, P(n): ∑_{k=1}^{n} k² = n(n+1)(2n+1)/6.

### Princípio usado
Se P(1) é verdadeira e, para todo inteiro n ≥ 1, P(n) implica P(n+1), então P(n) é
verdadeira para todo inteiro n ≥ 1.

### Base (n = 1)
Lado esquerdo: 1² = 1. Lado direito: 1·(1+1)·(2·1+1)/6 = 1·2·3/6 = 6/6 = 1.
Como 1 = 1, P(1) é verdadeira.

### Hipótese de indução
Seja n ≥ 1 um inteiro fixado, e suponha P(n):  ∑_{k=1}^{n} k² = n(n+1)(2n+1)/6.

### Passo
Quer-se P(n+1):  ∑_{k=1}^{n+1} k² = (n+1)((n+1)+1)(2(n+1)+1)/6 = (n+1)(n+2)(2n+3)/6.

Separa-se o último termo da soma:
  ∑_{k=1}^{n+1} k² = [∑_{k=1}^{n} k²] + (n+1)²
                   = n(n+1)(2n+1)/6 + (n+1)²          ← hipótese de indução aplicada ao colchete
                   = [n(n+1)(2n+1) + 6(n+1)²]/6
                   = (n+1)·[n(2n+1) + 6(n+1)]/6        ← fator comum (n+1)
                   = (n+1)·(2n² + n + 6n + 6)/6
                   = (n+1)(2n² + 7n + 6)/6.
Fatorando o trinômio: (n+2)(2n+3) = 2n² + 3n + 4n + 6 = 2n² + 7n + 6. Logo
  ∑_{k=1}^{n+1} k² = (n+1)(n+2)(2n+3)/6,
que é exatamente o lado direito de P(n+1). Portanto P(n) implica P(n+1), para todo n ≥ 1.

### Conclusão
Pelo princípio da indução matemática, P(n) é verdadeira para todo inteiro n ≥ 1. ∎

### Conferência de fencepost
- n = 1: 1 = 1 (base).  n = 2: 1 + 4 = 5 e 2·3·5/6 = 5.  n = 3: 1 + 4 + 9 = 14 e 3·4·7/6 = 14.
- O passo com n = 1 (o menor valor em que é aplicado): 1·2·3/6 + 2² = 1 + 4 = 5 = 2·3·5/6. ✓

## RESPOSTA
P(n): 1² + 2² + ... + n² = n(n+1)(2n+1)/6 vale para todo inteiro n ≥ 1, pela indução acima
(base em n = 1; passo n → n+1 usando a hipótese uma vez, no colchete; fatoração
2n² + 7n + 6 = (n+2)(2n+3)).
