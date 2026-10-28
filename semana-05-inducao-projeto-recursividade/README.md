# Semana 5 — Indução como paradigma de projeto de algoritmos

## Conteúdo
- **Indução como paradigma de projeto** de algoritmos (não só como técnica de prova
  de corretude): reduzir a instância de tamanho *n* a uma instância menor e
  estender a solução
- **Fortalecimento da hipótese de indução** — o movimento central da técnica:
  quando a h.i. simples não fecha, pedir *mais* da h.i. torna o problema mais fácil
- **Problema da celebridade**
- **Conceito de recursividade** e suas aplicações no projeto de algoritmos

## Leitura (CLRS, 3ª edição)
- Capítulo 4 (recorrências, para a análise dos algoritmos recursivos obtidos)
- Apêndice A (somatórios, para as somas que aparecem nas análises)

> A indução como *paradigma de projeto* não tem um capítulo próprio no CLRS — é
> exatamente por isso que o professor indicou o artigo do Manber e os slides da
> UNICAMP.

## Material desta aula
- `using-induction-to-design-algorithms-manber-cacm-1988.pdf` — MANBER, Udi.
  *Using Induction to Design Algorithms*. Communications of the ACM, v. 31, n. 11,
  nov. 1988, p. 1300–1313. **O artigo fundador da abordagem.**
- `inducao-no-projeto-de-algoritmos-unicamp-mc458.pdf` — slides de MC458
  (Projeto e Análise de Algoritmos I), UNICAMP: C. C. de Souza, C. N. da Silva,
  O. Lee, P. J. de Rezende. 1º semestre de 2012.

## O que tem em cada um

### Slides da UNICAMP (MC458) — 3 exemplos resolvidos + 1 exercício

| | Exemplo | Ideia | Complexidade |
|---|---|---|---|
| **Exemplo 3** | Fatores de balanceamento em árvore binária | h.i. simples falha (o f.b. da raiz depende das **alturas**, não dos f.b.s das subárvores) → **fortalecer** a h.i. para calcular f.b. **e** altura | Θ(n) |
| **Exemplo 4** | **Problema da celebridade** | 1ª tentativa (remover a pessoa *n*) dá quadrática; 2ª tentativa: **uma comparação elimina alguém** — remove-se quem já se sabe não ser celebridade | Θ(n) |
| **Exemplo 5** | Subsequência consecutiva máxima (SCM) | h.i. simples não fecha o caso `j < n-1` → **fortalecer**: calcular a SCM **e o sufixo máximo** | Θ(n) |

**Exercício deixado no slide** (Exemplo 3, complexidade): *"Há algum ganho em
complexidade quando ambos nₑ e n_d são aproximadamente n/2 ao longo da recursão?"*
→ resolvido em `../RESOLUCOES/lista-04-resolucao.pdf`.

Os três exemplos repetem o **mesmo movimento**: a hipótese de indução ingênua não
fecha, e fortalecê-la resolve. O último slide diz, literalmente:
*"Reforçar a hipótese de indução: preciso lembrar disso…"*

### Manber (CACM 1988) — 8 algoritmos, sem exercícios numerados

Artigo de metodologia, não de exercícios. A tese: **cada técnica de prova por
indução tem uma técnica de projeto de algoritmo análoga.** As seções são as
técnicas; os algoritmos são as ilustrações.

| Seção (técnica de prova) | Algoritmo(s) usados como exemplo |
|---|---|
| **Three Examples** (indução direta) | Evaluating Polynomials (chega na **regra de Horner**); Finding One-to-One Mappings; Checking Intervals for Containment |
| **Choosing the Induction Sequence Wisely** | Topological Sorting; **The Celebrity Problem** |
| **Strengthening the Induction Hypothesis** | Computing Balance Factors in Binary Trees; **Closest Pair** (par de pontos mais próximo no plano) |
| **Strong Induction** | The Knapsack Problem |
| **Maximal Counterexample** | Perfect Matching in Very Dense Graphs |
| **Other Proof Techniques** | Reductions; Double Induction; Reversed Induction; Choosing the Base of the Induction Wisely |

Duas seções desse artigo são exatamente os dois movimentos dos slides da UNICAMP:

- **Choosing the induction sequence wisely** é a chave da celebridade. A indução
  ingênua remove a pessoa *n*; a boa remove **uma pessoa que já se sabe não ser
  celebridade**. Mesma h.i., ordem diferente — e a complexidade cai de quadrática
  para linear. Manber chama o problema de *"a popular exercise in algorithm design"*.
- **Strengthening the induction hypothesis** é a chave dos Exemplos 3 e 5
  (fatores de balanceamento e SCM).

O exemplo dos fatores de balanceamento aparece nos dois materiais, com a mesma
h.i. fortalecida — é o ponto de contato mais direto entre o artigo e os slides.

## Lista de exercícios
- `../listas-de-exercicios/lista-04-2026-2.pdf` (30/08/2026, revisada em 09/09/2026) — estudo, sem entrega
- Resolução: `../RESOLUCOES/lista-04-resolucao.pdf`

A Lista 4 cobre: **indução** (Q1: 5 provas, incluindo 4 recorrências lineares; Q4: soma
dos quadrados), **Teorema Mestre** (Q2: 5 recorrências de divisão e conquista) e
**crítica de provas por indução defeituosas** (Q3: o passo falha em k = 1 e a proposição
é falsa; Q5: o passo "constrói" árvores de n+1 vértices em vez de partir de uma
arbitrária, e a proposição é verdadeira — dois defeitos diferentes).

## Links
- Recursão (Feofiloff, IME-USP):
  https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/recursion.html
- Recorrências (Feofiloff, IME-USP):
  https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/recurrence.html

## Ver também
- `../material-complementar/inducao-matematica/`
- `../semana-04-inducao-e-recorrencias/` — indução como técnica de **prova** e
  resolução de recorrências; a semana 5 usa a mesma ferramenta para **projetar**

## Referência
CORMEN, T. et al. *Algoritmos: Teoria e Prática*. 3ª ed. Campus, 2012.
MANBER, U. *Using Induction to Design Algorithms*. CACM 31(11), 1988.
