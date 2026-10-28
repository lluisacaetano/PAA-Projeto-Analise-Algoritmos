# Lista 5 — registro das correções

Fonte de verdade: `q{1..5}-limpo.md` nesta pasta. As versões julgadas na rodada 1 estão em
`historico/q*-limpo-r1.md`. Cada linha abaixo diz o que mudou, em que faixa (7.11 do CLAUDE.md)
e quantos verificadores independentes acharam. Nenhuma correção tocou enunciado nem mudou
resposta final.

## Rodada 1 (14/09/2026) — 20 verificadores, 4 por questão

| Questão | Votos | Resultado |
|---|---|---|
| Q1 | 4 HOLE | refutada |
| Q2 | 4 HOLE | refutada |
| Q3 | 4 HOLE | refutada (achados leves) |
| Q4 | 2 HOLDS, 2 HOLE | refutada (achados leves) |
| Q5 | 2 HOLDS, 2 HOLE | refutada (achado leve) |

### Q1
| # | Faixa | Achado | Quem | Correção |
|---|---|---|---|---|
| 1 | lógico | "o custo de uma entrada de tamanho n não depende dos valores" é falso no modelo de custo por linha: a linha 4 (MaxA) / 6 (MaxB) só executa no ramo "senão" | 4 de 4 | custo não recursivo entre c′ e c″; pior caso = vetor estritamente crescente = d + c″(n−1) e dn + c″(n−1); melhor caso também Θ(n) |
| 2 | lógico/coerência | "Chamadas recursivas: n" — são n − 1 recursivas; n é o total com a inicial; (b) contava o total | 4 de 4 | "Chamadas (contando a inicial): n" e "2n − 1" |
| 3 | apresentação→corrigido | `d` era variável do pseudocódigo e constante de custo | 4 de 4 | variáveis renomeadas para `esq`/`dir` |
| 4 | apresentação | Θ(lg n) da pilha sem testemunhas; Ω(n) sem hipótese do modelo; "trabalho total dobra"; "as mesmas n − 1 comparações" | 2 | testemunhas c₁=1, c₂=2, n₀=2; modelo declarado; frases reescritas |

### Q2
| # | Faixa | Achado | Quem | Correção |
|---|---|---|---|---|
| 1 | lógico | linhas 7–8 liam A[meio] duas vezes; a cota 2⌊lg m⌋+3 só valia com uma leitura (literal: 3⌊lg m⌋+4) | 4 de 4 | linha 6 guarda `v ← A[meio]`; linhas 7–8 comparam v |
| 2 | coerência | RESPOSTA dizia Θ(lg m); o corpo só provava O | 4 de 4 | cota inferior x = A[m]+1 ⇒ ⌊lg m⌋+2 acessos; Θ(lg m) com c₁=1, c₂=5, m₀=2 |
| 3 | lógico | "hi ≤ 2m" falso em m = 0 | 3 de 4 | "hi ≤ 2m quando J ≥ 1; hi = 1 quando J = 0" |
| 4 | coerência | RESPOSTA: "no máximo J leituras" falso quando J = 0 | 2 de 4 | "(1 posição / 1 leitura se J = 0)" |
| 5 | lógico (menor) | f(0) indefinido na cadeia K·f(m) ≤ K·f(n) | 3 de 4 | f(0) := 2 definido; f não decrescente em m ≥ 0 |
| 6 | apresentação→corrigido | Lema 1 falava da "última execução" antes de provar finitude | 1 | prova reordenada |

### Q3
| # | Faixa | Achado | Quem | Correção |
|---|---|---|---|---|
| 1 | coerência | transcrição da hierarquia omitia "onde c é uma constante arbitrária inteira ≥ 2" | 2 de 4 | cláusula restaurada + nota de que a hierarquia não cobre estas comparações |
| 2 | coerência | RESPOSTA de B escrevia a igualdade exata 2^(n−1)(t+c) − c para custo só Θ(1) | 2 de 4 | "com custo constante c … e pelo lema da §4 qualquer Θ(1) fica entre duas dessas" |
| 3 | lógico (lacuna) | H5 não conferida para C; para A só com t = c = 1 | 1 (+3 como apresentação) | argumento geral T(b·n) = aT(n) + f(bn) > T(n); formas fechadas e testemunhas para t, c quaisquer |
| 4 | apresentação→corrigido | "≈ Θ(n^2,32)"; L'Hôpital em n inteiro; "para qualquer constante"; g não decrescente na Observação | 2–4 | reescritos |

### Q4
| # | Faixa | Achado | Quem | Correção |
|---|---|---|---|---|
| 1 | lógico (lacuna formal) | Prova 2 terminava em Q(n+1) sem invocar o princípio da indução, e o texto dizia "as duas são completas" | 1 (+1 como apresentação) | frase de conclusão acrescentada |
| 2 | coerência | título "a assertiva exata como P(n)" colidia com P(n) da Prova 1 | 1 (+1 como apresentação) | "a própria assertiva como hipótese de indução, Q(n)" |
| 3 | apresentação→corrigido | "não dá para fazer a indução ingênua" sugeria impossibilidade; implicação "falsa em geral" | 2 | título e frase restritos a "separando o último termo" e "para todo real s" |

### Q5
| # | Faixa | Achado | Quem | Correção |
|---|---|---|---|---|
| 1 | coerência/lógico | "em (d), (f), (g) e (i) às cegas daria resposta errada" — em (d) só vale com T(1) ≤ 4 | 2 de 4 (+2 como apresentação) | seção 0 e quadro qualificados |
| 2 | lógico (lacuna) | limiar "T(1) > 4" em (d) assume recorrência desde n = 4; com T(n) = c para n ≤ n0 vira c > 4·4^(m0) | 1 | acrescentado, com exemplo n0 = 4, c = 10 |
| 3 | apresentação→corrigido | (i) sem o resultado às cegas nem a outra leitura; (b) k ∈ {0,1}; (e) b = n/(n−1) vale 2 em n = 2; "corta O(1) níveis" sem conta | 1–3 | acrescentados, com as formas fechadas para base em n ≤ n0 |

Todas as contas novas estão no bloco "RODADA 2" de `verificacao/lista05-chao-deterministico.py`.

## Rodada 2 — 20 verificadores novos, cegos às rodadas anteriores

| Questão | Votos | Resultado |
|---|---|---|
| Q1 | 4 HOLE | refutada — **defeito criado pela correção da rodada 1** (CLAUDE.md 7.2) |
| Q2 | 4 HOLDS | **confirmada** |
| Q3 | 3 HOLDS, 1 HOLE | corrigida mesmo assim (achado lógico, 7.11) |
| Q4 | 4 HOLDS | **confirmada** |
| Q5 | 3 HOLDS, 1 HOLE | corrigida (os 4 notaram o mesmo ponto) |

- **Q1 (lógico, 4 de 4).** A frase nova "no nível i da árvore de MaxB há 2^i chamadas, cada uma
  com custo de combinação constante" é falsa para n = 6 (níveis 1, 2, 4, 4) e para as folhas.
  Restringida a n potência de 2, com as folhas separadas. **Coerência (2 de 4):** d e c″ eram
  os mesmos símbolos para MaxA e MaxB, que têm constantes diferentes — viraram d_a, c″_a, d_b, c″_b.
- **Q3 (lógico, 1 de 4).** O texto igualava "assintoticamente não decrescente" (a partir de algum
  N) a "não decrescente em todo natural". Corrigida a definição; a Observação passou a exigir
  b^j ≥ máx(n₀, N, b).
- **Q5 (lógico, 1 de 4; 3 como apresentação).** No caso base T(n) = c para n ≤ n0, faltava c > 0
  (em (j) o coeficiente líder exige c > −2^(m0+1)). Acrescentado; em (d), o limiar passou a
  ter os três sinais (positivo, zero, negativo) e "caso base grande" virou "T(1) > 4".

## Rodada 3 — 12 verificadores (Q1, Q3, Q5)

| Questão | Votos | Resultado |
|---|---|---|
| Q1 | 3 HOLDS, 1 HOLE | corrigida (coerência) |
| Q3 | 4 HOLDS | **confirmada** |
| Q5 | 3 HOLDS, 1 HOLE | corrigida (coerência) |

- **Q1 (coerência).** A letra c, sem índice, aparecia nas recorrências dos dois algoritmos e na
  RESPOSTA; e d_b, declarado > 0, era posto igual a 0 para contar chamadas. Viraram c_a, c_b e
  uma recorrência genérica R(1) = u, R(s) = R(⌈s/2⌉) + R(⌊s/2⌋) + v só para a contagem.
- **Q5 (coerência, 7.4).** No item (d), a letra c valia −1 (coeficiente de f) e, cinco linhas
  depois, 10 (constante do caso base). A constante do caso base virou C, com nota explicando
  que o enunciado a chama de c. Acrescentado também, em (g) e (i), que com T(n) = C para n ≤ n0
  o coeficiente de n² não depende do caso base (conferido no chão determinístico).

## Rodada 4 — 8 verificadores (Q1, Q5)

| Questão | Votos | Resultado |
|---|---|---|
| Q1 | 4 HOLDS | **confirmada** |
| Q5 | 3 HOLDS, 1 HOLE | corrigida (coerência, 7.1) |

- **Q5 (coerência, 7.1).** O quadro-resumo dizia, na linha (e), "de fato 3n − 2 ∈ Θ(n)" sem a
  condição "com T(1) = 1" que o corpo impõe (com T(n) = C para n ≤ n0 a forma exata muda: C = 5,
  n0 = 3 dá 3n − 4). Virou "de fato Θ(n); 3n − 2 com T(1) = 1". No mesmo patch, por sugestão de
  três verificadores (apresentação), "(e n₀) mudam" virou "(e o n₀ das testemunhas) mudam", para
  não confundir com o n0 do caso base.

## Rodada 5 — 4 verificadores (Q5)

| Questão | Votos | Resultado |
|---|---|---|
| Q5 | 4 HOLDS | **confirmada** |

## Resumo

| Questão | Confirmada na rodada | Verificadores que a leram |
|---|---|---|
| Q1 | 4 | 16 |
| Q2 | 2 | 8 |
| Q3 | 3 | 12 |
| Q4 | 2 | 8 |
| Q5 | 5 | 20 |

64 verificadores ao todo. Nenhuma correção mudou resposta final nem tocou enunciado. Os achados
de apresentação das rodadas finais (por exemplo, em (f) da Q5, "com k ≥ 1 a fórmula às cegas
daria Θ(nᵏ)"; o n0 do caso base × o n₀ das testemunhas) ficam registrados e não mexidos (7.11).
