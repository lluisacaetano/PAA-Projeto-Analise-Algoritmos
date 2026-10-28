# Lista 4 — Questão 1 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Use o método da indução matemática para provar as assertivas abaixo."
(a) S(n) : 1 + 3 + 5 + ... + (2*n - 1) = n², ∀n ≥ 1
(b) T(n) = 2 se n = 1 ; T(n) = 2T(n-1) se n ≥ 2. A fórmula fechada para essa recorrência é T(n) = 2^n
(c) T(n) = 1 se n = 1 ; T(n) = T(n-1) + 1 se n ≥ 2. A fórmula fechada para essa recorrência é T(n) = n
(d) T(n) = 1 se n = 1 ; T(n) = T(n-1) + 3 se n ≥ 2. A fórmula fechada para essa recorrência é T(n) = 3*n - 2
(e) T(n) = 1 se n = 1 ; T(n) = T(n-1) + 2 se n ≥ 2. A fórmula fechada para essa recorrência ∈ Θ(n)

## SOLUÇÃO FINAL

### Preliminar — o princípio usado
Seja P(n) proposição definida para todo inteiro n ≥ 1. Se (base) P(1) é verdadeira e
(passo) para todo inteiro n ≥ 1, P(n) implica P(n+1), então P(n) vale para todo inteiro n ≥ 1.

Observação de domínio, válida para (b)–(e): cada recorrência está definida sobre os inteiros
n ≥ 1, não sobre n ≥ 0. A primeira cláusula fixa o valor em n = 1; a segunda cláusula,
T(n) = ... T(n−1) ..., está enunciada sob a condição "se n ≥ 2" e só pode ser aplicada quando
o argumento é ≥ 2. Em cada passo indutivo calcula-se T(n+1) com n ≥ 1; como n ≥ 1 implica
n+1 ≥ 2, a segunda cláusula é aplicável — e é aí que a restrição de domínio é consumida.

### (a)
P(n): soma_{k=1}^{n} (2k − 1) = n².
Para n = 1 a soma tem um único termo (a reticência não representa termo algum).

Base (n = 1): lado esquerdo = 2·1 − 1 = 1; lado direito = 1² = 1. Como 1 = 1, P(1) vale.

Hipótese (h.i.): seja n ≥ 1 fixado e suponha soma_{k=1}^{n} (2k − 1) = n².

Passo: separa-se o somatório até n+1 no somatório até n mais o termo k = n+1 — separação
válida para todo n ≥ 0, inclusive quando a soma restante é vazia:
  soma_{k=1}^{n+1} (2k−1) = [soma_{k=1}^{n} (2k−1)] + (2(n+1) − 1)
                          = n² + (2(n+1) − 1)          ← (h.i.) aplicada ao colchete
                          = n² + 2n + 1 = (n+1)².
Logo P(n+1) vale. Pelo princípio da indução, P(n) vale para todo n ≥ 1. ∎

### (b)
P(n): T(n) = 2^n.
Base (n = 1): T(1) = 2 pela primeira cláusula; 2^1 = 2. Como 2 = 2, P(1) vale.
Hipótese: seja n ≥ 1 fixado e suponha T(n) = 2^n.
Passo: como n ≥ 1, então n+1 ≥ 2, e por isso a segunda cláusula é aplicável ao argumento n+1:
  T(n+1) = 2·T((n+1)−1) = 2·T(n) = 2·2^n   ← (h.i.)
         = 2^{n+1}.
Logo P(n+1) vale. Pelo princípio da indução, T(n) = 2^n para todo n ≥ 1. ∎

Nota: com base T(1) = 1 a mesma recorrência resolveria para 2^{n−1}. É a base que fixa a constante.

### (c)
P(n): T(n) = n.
Base (n = 1): T(1) = 1 pela primeira cláusula; e n = 1. Como 1 = 1, P(1) vale.
Hipótese: seja n ≥ 1 fixado e suponha T(n) = n.
Passo: como n ≥ 1, então n+1 ≥ 2, e a segunda cláusula é aplicável ao argumento n+1:
  T(n+1) = T((n+1)−1) + 1 = T(n) + 1 = n + 1   ← (h.i.)
Logo P(n+1) vale. Pelo princípio da indução, T(n) = n para todo n ≥ 1. ∎

### (d)
P(n): T(n) = 3n − 2.
Base (n = 1): T(1) = 1 pela primeira cláusula; 3·1 − 2 = 1. Como 1 = 1, P(1) vale.
(É aqui que uma fórmula quase certa, como 3n − 3 ou 3n − 1, seria refutada.)
Hipótese: seja n ≥ 1 fixado e suponha T(n) = 3n − 2.
Passo: como n ≥ 1, então n+1 ≥ 2, e a segunda cláusula é aplicável ao argumento n+1:
  T(n+1) = T((n+1)−1) + 3 = T(n) + 3 = (3n − 2) + 3   ← (h.i.)
         = 3n + 1 = 3n + 3 − 2 = 3(n+1) − 2.
A constante da hipótese (o −2) reaparece intacta na conclusão. Logo P(n+1) vale.
Pelo princípio da indução, T(n) = 3n − 2 para todo n ≥ 1. ∎

### (e)
Duas fases.

Fase 1 — forma fechada por indução: T(n) = 2n − 1.
De onde vem o palpite: desenrolando a recorrência, T(n) = T(n−1) + 2 = T(n−2) + 2·2 = … =
T(1) + 2(n−1) = 1 + 2n − 2 = 2n − 1. O desenrolar é heurística, não demonstração — quem
demonstra é a indução abaixo, que parte da definição recursiva e chega à fórmula.
P(n): T(n) = 2n − 1.
Base (n = 1): T(1) = 1 pela primeira cláusula; 2·1 − 1 = 1. Como 1 = 1, P(1) vale.
Hipótese: seja n ≥ 1 fixado e suponha T(n) = 2n − 1.
Passo: como n ≥ 1, então n+1 ≥ 2, e a segunda cláusula é aplicável ao argumento n+1:
  T(n+1) = T((n+1)−1) + 2 = T(n) + 2 = (2n − 1) + 2   ← (h.i.)
         = 2n + 1 = 2n + 2 − 1 = 2(n+1) − 1.
Logo P(n+1) vale. Pelo princípio da indução, T(n) = 2n − 1 para todo n ≥ 1. ∎

Fase 2 — de T(n) = 2n − 1 para T(n) ∈ Θ(n).
Definição (CLRS 3ª ed., §3.1): Θ(g(n)) é o conjunto das funções f para as quais existem
constantes positivas c1, c2 e n0 tais que, para todo n ≥ n0, 0 ≤ c1·g(n) ≤ f(n) ≤ c2·g(n).
Ordem dos quantificadores: ∃c1 ∃c2 ∃n0 ∀n ≥ n0. As constantes são escolhidas primeiro e não
podem depender de n.

Testemunhas: c1 = 1, c2 = 2, n0 = 1. Todas positivas (1 > 0, 2 > 0, 1 > 0) e nenhuma contém n.
Aqui f(n) = T(n) = 2n − 1 e g(n) = n.

Verificação em n = n0 = 1 exatamente:
  c1·g(1) = 1·1 = 1 ;  T(1) = 2·1 − 1 = 1 (e T(1) = 1 pela recorrência — concordam) ;
  c2·g(1) = 2·1 = 2.
Logo 0 ≤ 1 ≤ 1 ≤ 2. Vale em n = n0, com igualdade na cota inferior — permitido, pois a
definição usa ≤ e não <.

Verificação para todo n ≥ 1 (algébrica, não amostral). Seja n inteiro com n ≥ n0 = 1.
 (1) c1·g(n) = n ≥ 1 > 0, logo 0 ≤ c1·g(n).
 (2) c1·g(n) ≤ T(n): n ≤ 2n − 1 equivale, subtraindo n dos dois lados, a 0 ≤ n − 1,
     isto é 1 ≤ n — verdadeira por hipótese.
 (3) T(n) ≤ c2·g(n): 2n − 1 ≤ 2n equivale, subtraindo 2n dos dois lados, a −1 ≤ 0,
     verdadeira incondicionalmente.
Reunindo: para todo n ≥ 1, 0 ≤ 1·n ≤ 2n − 1 = T(n) ≤ 2·n. Portanto T(n) = 2n − 1 ∈ Θ(n). ∎

Observação: Θ(n) é teto e piso simultaneamente; não diz que T(n) = n. De fato T(n) ≠ n para
n ≥ 2, e ainda assim T ∈ Θ(n) — é para isso que servem c1 e c2.

## RESPOSTA (resumo)
(a) soma_{k=1}^{n}(2k−1) = n², ∀n ≥ 1.
(b) T(n) = 2^n, ∀n ≥ 1.
(c) T(n) = n, ∀n ≥ 1.
(d) T(n) = 3n − 2, ∀n ≥ 1.
(e) forma fechada T(n) = 2n − 1; T(n) ∈ Θ(n) com c1 = 1, c2 = 2, n0 = 1.
