## Situação em 14/09/2026

| # | O que | Situação |
|---|---|---|
| 12 | **Listas 1, 3 e 4 revisadas pelo professor** (09/09/2026) | **feito** — 5 questões novas resolvidas e verificadas; antiga L3 Q3 renumerada para Q4 |
| 13 | Banco consolidado com as questões novas | **feito** — 90 questões, 142 páginas |
| 15 | Frase de abertura da **Lista 1, Q1** (parágrafo "Os seis itens giram em torno…" em `fontes-html/lista-01-resolucao.html`) | **feito** — v5 confirmada (4 HOLDS × 1 HOLE, este na v4, corrigido) em 14/09/2026 |

**Item 15, para retomar.** O texto antigo (de agosto) dizia que "(a) e (b) diferem", e isso é
falso (os dois são V). A frase foi reescrita quatro vezes; cada versão foi a verificadores
novos (prompt com os seis itens, sem ler arquivos):
- v1: refutada — atribuía (a) e (b) à mesma causa ("O não impõe piso");
- v2: refutada — "uma entrada fora do máximo pode custar menos" não implica custar O(n);
- v3: 3 HOLDS, 1 HOLE — "só é possível sem piso" é falso como regra geral (um piso Θ(n) é
  compatível com todas as entradas O(n));
- v4: "é incompatível com um piso de ordem n²" — 3 HOLDS, 1 HOLE: "custo O(n) em algumas
  entradas é **sempre** possível" é falso como regra universal (laço duplo de custo n² em
  toda entrada: nenhuma entrada é O(n));
- **v5 (no PDF atual)**: v4 sem o "sempre" — "é possível — existe algoritmo em que isso
  ocorre —". Mudança só enfraquece a afirmação. Pela regra de voto (3–1 = indefinido),
  um 5º verificador foi disparado em 14/09/2026 e voltou **HOLDS** — frase confirmada (4–1).
  Lição: cinco versões para um parágrafo introdutório; cada rodada achou uma generalização
  falsa diferente ("mesma causa", "menos ⇒ O(n)", "sem piso", "sempre"). Parágrafo de
  abertura é afirmação matemática como qualquer outra — vai para verificação.
  As respostas V/F e o corpo dos itens nunca estiveram em dúvida — só o parágrafo de abertura.

Detalhe das questões novas: L1 Q1(e) (θ no lugar de O) e Q1(f) (retirado pelo professor em 13/09/2026); L3 Q3 (moedas) e
Q5 (passo sem base); L4 Q4 (soma dos quadrados) e Q5 (prova defeituosa sobre
árvores). Verificação: 4 verificadores por questão; 3 questões voltaram com defeito em
nota lateral, foram corrigidas e reverificadas com 4 de 4. Registro em
`verificacao/README.md`, seção "Atualização de 09/09/2026".

---

## Situação em 31/08/2026

| # | O que | Situação |
|---|---|---|
| 1–6 | tudo o que estava fechado em 27/08 | **feito** (quadro abaixo) |
| 7 | **Lista 4** (Q1 a–e, Q2 a–e, Q3) | **feito** — `lista-04-resolucao.pdf`, 10 páginas |
| 8 | **Exercício do slide da UNICAMP** (ganho com nₑ ≈ n_d ≈ n/2) | **feito** — apêndice da Lista 4 |
| 9 | Banco consolidado com a Lista 4 | **feito** — 85 questões, 137 páginas |
| 10 | Livro do OBMEP (~100 sub-itens) | **pendente** — adiado por volume |
| 11 | Exercícios do Rosen e do Gersting (~75) | **bloqueado** — enunciados não disponíveis |

### Varredura da semana 5 (31/08/2026)

Filtro duplo (imperativo + rótulo, sem exigir número) aplicado aos dois PDFs novos:

| Material | Exercícios | Exemplos resolvidos |
|---|---|---|
| `using-induction-to-design-algorithms-manber-cacm-1988.pdf` | **0** | 8 algoritmos, todos com solução no próprio texto |
| `inducao-no-projeto-de-algoritmos-unicamp-mc458.pdf` | **1** (“Exercício:” no Exemplo 3) | 3 (Exemplos 3, 4 e 5) |

O único exercício em aberto foi resolvido e está no apêndice da
`lista-04-resolucao.pdf`. O artigo do Manber é metodologia, não lista — não há
nada a resolver nele.

---

## Situação em 27/08/2026

| # | O que | Situação |
|---|---|---|
| 1 | Listas 1, 2 e 3 | **feito** — `lista-0*-resolucao.pdf` |
| 2 | Exercícios dos materiais complementares (24) | **feito** |
| 3 | Somatórios do Prof. Walace (2) | **feito** |
| 4 | Prova de 2025 (11 questões) | **feito** |
| 5 | Exemplos resolvidos dos slides (**73 blocos**) | **feito** — reproduzidos como imagem |
| 6 | **Banco de questões consolidado** | **feito** — `banco-de-questoes.pdf`, 124 páginas |
| 7 | Livro do OBMEP (~100 sub-itens) | **pendente** — adiado por volume |
| 8 | Exercícios do Rosen e do Gersting (~75) | **bloqueado** — enunciados não disponíveis |

Tudo que tinha enunciado disponível nesta máquina, fora o OBMEP, está resolvido e
verificado. O que resta são os itens 7 e 8, detalhados abaixo.

### Correção de escopo — 27/08/2026

Uma auditoria posterior encontrou **46 páginas com exemplos** que os scans iniciais
tinham perdido, em 8 dos PDFs. A causa: os dois primeiros filtros procuravam
`Exercício N` e `Exemplo N`, e os que aparecem como `Exemplo:` ou `Exemplo de…`
escaparam de ambos. O maior buraco era o slide de 204 páginas da semana 1, do qual
só 4 exercícios tinham sido extraídos.

Todas foram renderizadas e incorporadas à Parte III do banco, que passou de 38 para
73 blocos. Algumas dessas páginas são slides de teoria e não exemplos resolvidos —
entraram porque o filtro amplo as capturou, e servem como referência.

**Lição para a próxima varredura:** filtrar por imperativo (`Prove que`, `Mostre que`,
`Calcule`) E por rótulo (`Exemplo`, `Exercício`, `Problema`), sem exigir número.

---

## Exercícios não cobertos — varredura de filtro duplo de 06/10/2026 — **RESOLVIDOS em 07/10/2026**

Os 31 exercícios abaixo (18 questões) estão resolvidos, com enunciado literal, no `complementares.pdf` (43 questões)
e no `banco-de-questoes.pdf` (112). Fonte de verdade: `geradores/dados/complementares-novos/*.md`; enunciados em
`geradores/dados/complementares-novos-enunciados.json`; placar de verificação (4 de 4 sobre o texto final em todas)
em `geradores/dados/complementares-novos-placar-2026-10-07.md`.

A tabela "Materiais que NÃO têm exercícios" abaixo está **desatualizada**: a varredura antiga usou só o filtro
por imperativo. A de 06/10/2026 (rótulo + imperativo, página a página, olhando a imagem) achou **31 exercícios
claros sem resolução** e mais 21 duvidosos/triviais/fora do PDF. Inventário completo, com página e motivo, em
`geradores/dados/varredura-exercicios-2026-10-06.json` (202 entradas). Os 31 claros:

| Material | Qtd | Itens |
|---|---|---|
| `crescimento-de-funcoes-uber-uem.pdf` | 15 | p. 8, 12, 17: V/F pela definição de O, Ω e Θ (5 cada), rotulados "Exemplos" mas **sem resposta** |
| `relacoes-de-recorrencia-rezende-unicamp.pdf` | 7 | p. 9 (2 "para o leitor"), p. 10, p. 17, p. 18, p. 19, p. 21 (suplementar) |
| `matematica-discreta-...-diego-mello-ifmg.pdf` | 3 | p. 23 (primeira chamada; ordenação passo a passo), p. 26 (árvore TORRE-HANOI, n = 4) |
| `slides-analise-de-complexidade-loureiro-ufmg.pdf` | 2 | p. 87 (6n³ ≠ Θ(n²)), p. 185 (retas no plano) |
| `analise-de-algoritmos-parte-2-campello.pdf` | 2 | p. 11 (base do log), p. 22 (Prefix1/Prefix2) |
| `somatorios-walace-rodrigues-ifmg.pdf` | 2 | p. 16 itens 2 (Σ i·i! por perturbação) e 3 (Σ i·2ⁱ por perturbação) |

## Inventário completo: onde há exercício e onde não há

Varredura feita em todos os PDFs da pasta, com filtro de imperativo
("Prove que", "Mostre que", "Calcule", "Determine", "Resolva").

### Materiais que NÃO têm exercícios (só exemplos resolvidos)

Cada "Prove que" nesses PDFs é seguido de `prova:` ou `Solução:` no próprio slide.
**Não há nada a resolver neles.**

| Material | Semana | Exemplos resolvidos |
|---|---|---|
| `inducao-matematica-loureiro-ufmg.pdf` | 4 | 12 |
| `notacao-assintotica-sheila-almeida-utfpr.pdf` | compl. | 12 |
| `inducao-matematica-cavalcanti-ufpe.pdf` | compl. | 8 |
| `o-poderoso-principio-da-inducao-matematica-uesb.pdf` | compl. | 13 |
| `relacoes-de-recorrencia-rezende-unicamp.pdf` | 4 | 3 |
| `crescimento-de-funcoes-uber-uem.pdf` | compl. | só teoria |
| `resumo-complexidade-prof-mario-oliveira.pdf` | 2 e 3 | só teoria |

### Materiais COM exercícios

| Material | Qtd | Situação |
|---|---|---|
| `matematica-discreta-...-diego-mello-ifmg.pdf` (semana 4) | 6 | em andamento |
| `analise-de-algoritmos-parte-2-campello.pdf` | 8 | em andamento |
| `slides-analise-de-complexidade-loureiro-ufmg.pdf` (semana 1) | 4 | em andamento |
| `principio-de-inducao-finita-usp.pdf` | 4 | em andamento |
| `somatorios-walace-rodrigues-ifmg.pdf` | **2** | **a fazer** — perturbação e operador diferença |
| `inducao-matematica-obmep.pdf` | ~100 | adiado (item 4) |

---

## Detalhe — Livros do Rosen e do Gersting — enunciados não disponíveis

O material do **Prof. Diego Mello (IFMG Formiga)**, em
`semana-04-inducao-e-recorrencias/matematica-discreta-recorrencia-e-inducao-diego-mello-ifmg.pdf`
(slide 37, "Atividades Recomendadas"), indica ~75 exercícios de dois livros que
**não estão nesta máquina**. Só as referências foram dadas, não os enunciados.

### ROSEN, K. H. — *Matemática Discreta e suas Aplicações*

| Página | Exercícios |
|---|---|
| 279 | 1, 2, 3, 4, 5–8, 9, 10, 15, 16, 18, 19, 28, 31–34, 47, 58 |
| 291 | 1, 2, 3, 4 |
| 308 | 1–4, 7, 9, 13, 23, 24, 26, 27, 38 |
| 321 | 1, 2, 7, 8, 9 |

Leitura correspondente: seções 4.1, 4.2 (p. 283–290), 4.3 (p. 294–303),
4.4 (p. 311–314).

### GERSTING, J. L. — *Fundamentos Matemáticos para a Ciência da Computação*

| Página | Exercícios |
|---|---|
| 84 | 1, 2, 3, 4, 5, 6, 7, 8, 27, 29, 41, 42, 43, 55, 57, 59, 66, 68, 71 |
| 111 | 1–10, 11, 12, 32, 34, 39, 40, 41, 56, 57, 62, 67, 69, 73, 75, 79, 80 |

Leitura correspondente: seções 2.2, 2.4 (p. 88–106).

**Para destravar:** conseguir os PDFs dos dois livros (biblioteca do IFMG, ou
pedir ao professor). Com os enunciados em mãos, é só rodar o mesmo fluxo das
listas.

## Detalhe — Livro do OBMEP — Indução Matemática

`material-complementar/inducao-matematica/inducao-matematica-obmep.pdf` — 95
páginas, **~50 enunciados numerados com ~100 sub-itens**, distribuídos em 12
seções de "Problemas":

- Capítulo 1: 18 enunciados (indução básica, somatórios, desigualdades)
- Capítulo 2: 8 enunciados
- Capítulo 3: 24 enunciados

Os enunciados **estão disponíveis** — é só volume. É um livro de olimpíada, então
o nível passa do que PAA cobra, mas o capítulo 1 casa bem com a matéria.

**Decisão em 27/08/2026:** ficou de fora por ora; fazer primeiro os 24 exercícios
das outras fontes.

## Já resolvido

Ver `exercicios-*.pdf` nesta pasta e as três listas em `lista-0*-resolucao.pdf`.
