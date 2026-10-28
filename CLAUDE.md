# Projeto e Análise de Algoritmos (PAA) — instruções do projeto

IFMG, Campus Formiga · Bacharelado em Ciência da Computação · 2026/2
Professor: Mário Luiz Rodrigues Oliveira · Aluna: Luisa Caetano

---

## 1. Ative as skills SEMPRE

Ao trabalhar com qualquer conteúdo desta pasta — resolver ou conferir exercício,
demonstrar limite assintótico, analisar complexidade de laço, resolver
recorrência, provar por indução, fechar somatório, responder item V/F —
**invoque obrigatoriamente**, antes de escrever qualquer resposta:

1. **`paa-analise-de-algoritmos`** (skill pessoal, em `~/.claude/skills/`)
   As obrigações formais da disciplina e a conferência numérica.
2. **`math-olympiad`** (plugin oficial da Anthropic, já instalado)
   O fluxo de verificação adversarial em contexto limpo.

**Isto vale mesmo que a questão pareça trivial.** O gatilho automático do
`math-olympiad` foi desenhado para NÃO disparar em análise de complexidade —
está explícito em `evals/trigger_eval.json` do plugin:
*"Help me verify the time complexity of this sorting algorithm"* →
`should_trigger: false`. Por isso a invocação aqui é manual e obrigatória.

Não vale resolver primeiro e verificar depois "se der tempo". **A verificação vem
antes de apresentar a resposta.**

### Por que

Autoverificação não pega o erro. arXiv:2503.21934 (*"Proof or Bluff"*): 85,7% de
acerto autoverificado vira menos de 5% sob correção humana. O verificador que viu
o raciocínio concorda com ele. Por isso: contexto limpo, verificador cego ao
raciocínio, missão de derrubar a prova.

---

## 2. Estado do projeto (14/09/2026)

### Pronto e verificado

| Documento | Páginas | Conteúdo |
|---|---|---|
| `RESOLUCOES/banco-de-questoes.pdf` | 213 | **tudo**: 112 questões com resolução + 73 blocos de exemplos dos slides |
| `RESOLUCOES/complementares.pdf` | 127 | só PDFs/slides (43 questões, enunciados literais), resolução **abaixo** do enunciado |
| `RESOLUCOES/prova-01-resolucao.pdf` | 12 | prova de 2025 + mapa "de onde veio cada questão" |
| `RESOLUCOES/lista-0{1,2,3,4,5}-resolucao.pdf` | 8/7/7/13/11 | uma lista por arquivo |
| `RESOLUCOES/listas-1-a-5-resolucao.pdf` | 47 | as cinco listas num volume só, cada questão com enunciado e resolução (capa + junção dos cinco PDFs; ver seção 6) |

As 90 questões vêm de: Lista 1 (18), Lista 2 (14), Lista 3 (9), Lista 4 (14),
complementares (24), Prova 2025 (11).

### Enunciados literais nas listas 1–5 — feito em 06/10/2026

Auditoria das resoluções contra os PDFs do professor: **toda questão e todo item têm resolução**, mas
os enunciados das listas 1–4 estavam **parafraseados** (Θ no lugar de θ, "·" no lugar de "∗", frases
reescritas), os **códigos** das L1 Q2 e L2 Q4 estavam resumidos (sem chaves, sem numeração de linhas,
comentários reescritos), a L2 Q4 tinha perdido "Respostas sem justificativas não serão consideradas" e a
L3 Q4(d)(e) tinha perdido "para essa recorrência". E um erro de conteúdo: **L1 Q3(a) é f(n) = 2¹¹⁷**, e a
resolução dizia 2117 (expoente perdido no pdftotext). Corrigido para c = 2¹¹⁷; reverificação 4 de 4.
Agora cada lista traz cabeçalho e instruções, enunciados literais, códigos linha a linha num quadro
"Enunciado — código N" (dentro do `item`, então o banco herda) e o anexo "Informações que podem ser
úteis". Script de edição: `geradores/dados/historico-enunciados-2026-10-06/` guarda as versões
anteriores. Conferência: `verificacao/enunciados-literais-2026-10-06.py` (toda linha do PDF do
professor tem de aparecer no PDF da resolução). Volume único: 46 páginas.
**Pendente:** a Parte I do banco (`catalogo.py`) ainda usa enunciados resumidos, de propósito curtos.

**Prova de 2025, mesma auditoria (06/10/2026).** Enunciados, cabeçalho, código de honra, instruções e
anexo agora literais (`gerar_prova.py`). Nenhuma resposta mudou; corrigido nas justificativas (lotes 7 e
8 de `correcoes.py`): "domina assintoticamente" lido como o(g) — no Loureiro é |f| ≤ C|g|, um O —
nas 3(c)/4(b); cruzamento da 4(a) (raiz de n/lg n = 15 é 99,56; 99,82 é com +20); testemunhas de B na
5(a) (d = T_B(1) − c pode ser negativo: c₁ = min(c, T_B(1)), c₂ = max); ponte Θ(n) → c·nᵏ do formulário
com testemunhas numéricas (n₀ = 5, n potência de 5); constantes incomparáveis na 5(b). Quatro rodadas
de 4 verificadores, todas HOLDS; os achados de cada rodada foram **em frases que eu acabara de
escrever** (7.15 de novo: "entre c·n e 5/4 disso" falhava em n = 1). A tarja da 4(a) não diz mais
"idêntica palavra por palavra": a lista tem "ambos os algoritmos", a prova "os dois algoritmos".

**Listas 1–5 pela skill `paa-analise-de-algoritmos` (06/10/2026).** As 24 questões e o apêndice da L4
foram para verificadores em contexto limpo, com Bash, e cada um recebeu a questão inteira (enunciado
literal mais resolução), extraída por `HTMLParser` com uma invariante de integridade. **Nenhuma resposta
mudou.** Onze blocos voltaram com furo de justificativa, e todos foram corrigidos e reverificados até 4 de 4:
- L1 Q2 código 2: k ≥ 1 não estava declarado.
- L1 Q3(e): "bastaria n₀ = 2" com c = 1/2 é falso; o certo é 3.
- L1 Q4: premissa oculta.
- L1 Q5: "precisa ser justo" era condição suficiente vendida como necessária (7.5). Depois, a ressalva
  "não ser O(n lg n)" também não basta: o contraexemplo oscilante pede n lg n = o(W).
- L2 Q1(b)(iv).
- L2 Q3(c): u, v ≥ 0 saem de 0 ≤ f ≤ c₁u.
- L2 Q4: faltavam testemunhas numéricas nos códigos 4 e 5.
- L3 Q2: o título dizia "menor teto".
- L4 apêndice: o enquadramento 2T(n/2) + d₁ ≤ T(n) era falso. Foi trocado pela forma exata
  U(m) = T(m − 1), e a frase sobre o ganho da busca binária ficou como condição **suficiente**, com fração q < 1.

Dos furos das rodadas 2 em diante, **todos estavam em frases que eu tinha acabado de escrever** (7.15 pela
terceira vez). O conferidor de enunciados passou a sair com código 1 quando falha. Antes, ele imprimia
"2 linhas sem correspondência" e saía com 0. As duas linhas eram o Σ aⁱ do anexo das L1/L2, um falso
positivo da 7.21 conferido na imagem.

### Complementares auditados — 06/10/2026

O `complementares.pdf` era de 27/08 e estava defasado; o gerador só excluía "Lista 1/2/3" (as Listas 4 e 5
vazariam — a guarda `len == 24` abortou). Agora: 25 questões (entrou o exercício do slide MC458) e
**enunciados literais**, transcritos da imagem das páginas para `geradores/dados/complementares-enunciados-literais.json`
(o `catalogo.py` substitui as paráfrases por eles; conferência: `verificacao/complementares-enunciados-literais.py`).
Três paráfrases traziam dicas que não existem no original, e **uma trocava a pergunta: Campello ex. 7 pergunta
"é Ω(1)?", a paráfrase dizia Θ(1), e a resolução provava "não é Θ(1)"** — resposta a outra pergunta. Refeita
(3 solvers concordaram; substituição integral em `correcoes.py`, `SUBSTITUICOES`): SIM, é Ω(1) para toda
entrada, mas não "por ser O(1)" — vem de o melhor caso ser também ≥ constante e ser o mínimo sobre as entradas.

As 25 foram a 4 de 4 sobre o texto final (placar em `dados/complementares-placar-auditoria-2026-10-06.md`). Furos
corrigidos (lotes 9–9e de `correcoes.py`): Loureiro ex. 5 (níveis lg n + 1; "folhas dominam ⇒ Caso 1" é só
necessária), Loureiro ex. 8 (Θ com expoente arredondado é falso), remissões "item (5)" que apontavam para outra
questão, Campello ex. 4 (conta impressa; "n representável" confundia valor e tamanho; log_b k), ex. 5
(n_k ≥ n/2^k − 1 era **falso**; trocado pela entrada x > A[n]; símbolos c₂, n₀, b colidindo), IFMG ex. 5
(custo "unitário" falso; recorrência exata só como par de cotas), USP 2.4 ("não há prova direta" era falso),
Walace ex. 1 (perturbação: o cancelamento não é "o coração do método"). **Nenhuma resposta mudou, exceto a do
Campello ex. 7.** O apêndice da Lista 4 ganhou o algoritmo **literal** do slide (o slide numera duas linhas "3."),
com a numeração corrida 1–9 declarada como nossa — por isso a Lista 4 tem 13 páginas e o volume 47 (Lista 5 na p. 37).

### Os 31 exercícios não cobertos — resolvidos em 06–07/10/2026

A varredura de filtro duplo achou 31 exercícios claros sem resolução (15 V/F do Uber rotulados "Exemplos", 7 do
Rezende, Loureiro p. 87 e 185, Campello p. 11 e 22, Diego Mello p. 23 e 26, Walace p. 16 itens 2–3). Viraram **18
questões novas**, com enunciado literal transcrito da imagem (`geradores/dados/complementares-novos-enunciados.json`,
conferido por `verificacao/complementares-enunciados-literais.py`, agora com as 43) e resolução em
`geradores/dados/complementares-novos/<slug>.md` — **a fonte de verdade**; o `catalogo.py` (fonte `"NV"`) e o
`gerar_banco.py` leem dali. Complementares: 25 → **43**; banco: 94 → **112**.

As 18 foram a **4 de 4 sobre o texto final**, em 8 ondas (A–H), com toda correção zerando a contagem da questão.
Placar em `geradores/dados/complementares-novos-placar-2026-10-07.md`; patches, prompts e ajudantes em
`geradores/dados/complementares-novos-patches/`. **Nenhuma resposta central mudou, exceto a Rezende p. 18**, que
foi reescrita duas vezes: a frase do texto (construção O(n log n) + remoções Σ lg(n−i+1) = lg n!) é só a parcela
do heap; o algoritmo completo é O(n² + k n log n) com matriz (Θ(n²) no pior caso para k constante ≥ 1, O(n log n)
com k = 0, O(1) com k ≥ n) e O(m + (k+1) n log n) com listas — seguindo o algoritmo **literal** (parada |V| < k + 1)
e a premissa do texto de que os graus ficam armazenados na construção. Fato do material: na Rezende p. 19, o
parêntese "(2^65536 é o menor N com log* N > 4)" está errado — é 65537; a resolução aponta, o enunciado fica.
Ver a lição 7.23.

### Lista 1 ajustada pelo professor — 13/09/2026 (feito em 14/09)

E-mail: "fiz um ajuste na lista de exercícios 1". A única mudança é a **retirada do Q1(f)**;
o resto é idêntico (diff de texto e das imagens das páginas). Versão de 09/09 em
`listas-de-exercicios/versoes-anteriores/lista-01-2026-2-versao-09-09.pdf`; resolução e catálogo
antigos em `RESOLUCOES/geradores/dados/lista01/historico/`. A resolução segue a lista atual
(cinco itens); o (e) ganhou uma nota curta sobre a variante retirada, e a resolução completa do
(f) continua em `dados/lista01/q1ef-limpo.md`. Banco: 95 → **94** questões. Conferência:
`verificacao/lista01-ajuste-2026-09-13.py` (inclui a invariante de índice da 7.20).
Verificação do texto novo: 3 de 4 na primeira rodada — o quarto achou, no item (b) (texto de
agosto), "n comparações" com c = 1 sem dizer "de chave"; corrigido, a reverificação deu 4 de 4.

Agora a distribuição é: Lista 1 (17), Lista 2 (14), Lista 3 (9), Lista 4 (14), Lista 5 (5),
complementares (24), Prova 2025 (11).

### Lista 5 — feito em 14/09/2026 (AVALIADA, 5 pontos, entrega em 24/09/2026)

`listas-de-exercicios/lista-05-2026-2.pdf` → `RESOLUCOES/lista-05-resolucao.pdf` (10 p.) e 5
questões novas no banco (agora 95). Textos verificados em `geradores/dados/lista05/q*-limpo.md`;
o HTML é **gerado** deles (`gerar_lista05.py`, ver seção 6). Registro das 5 rodadas em
`dados/lista05/correcoes-lista05.md`; versões refutadas em `dados/lista05/historico/`.

| Q | Resposta | Confirmada |
|---|---|---|
| 1 | máximo por D&C: **nenhuma** abordagem é melhor — ambas Θ(n) no pior caso, n − 1 comparações; só a pilha difere (Θ(n) × Θ(lg n)) | 4/4, rodada 4 |
| 2 | vetor sem fim: galope (1, 2, 4, …) + busca binária, ≤ 2⌊lg m⌋ + 3 acessos, Θ(lg m) ⊂ o(n) | 4/4, rodada 2 |
| 3 | **C, Θ(n² lg n)**; A Θ(n^log₂5), B Θ(2ⁿ) | 4/4, rodada 3 |
| 4 | 1/2 + … + 1/2ⁿ < 1: indução na forma forte (= 1 − 1/2ⁿ) ou separando o primeiro termo | 4/4, rodada 2 |
| 5 | só (a) Θ(lg n), (h) Θ(n), (j) Θ(n^log₂3) aplicam; os outros 7 violam hipótese | 4/4, rodada 5 |

64 verificadores. O que caiu está nas lições 7.15–7.19.

### Listas 1, 3 e 4 revisadas pelo professor — feito em 14/09/2026

E-mail de 09/09: "fiz atualizações nas listas de exercícios 1, 3 e 4". As versões
originais estão em `listas-de-exercicios/versoes-anteriores/`. Cinco questões novas,
resolvidas e verificadas (4 de 4 verificadores na versão final de cada uma):

| Lista | Novo | Resposta |
|---|---|---|
| 1 | Q1(e) agora diz **θ(n²)** (era O) | **V**: o piso c₁n² força entrada > 100n para n ≥ máx(n₀, ⌊100/c₁⌋+1) |
| 1 | Q1(f): O(n²) + "há **obrigatoriamente**" | **F**: custo constante é O(n²) e nunca chega a 100n — **retirado pelo professor em 13/09** |
| 3 | Q3: 2ⁿ moedas, n pesagens | bissecção; P(n) enunciada para **qualquer** conjunto (a h.i. vai numa metade) |
| 3 | Q5: P(n): 1+…+n = n(n+1)/2 + 1 | o passo vale, P(n) é sempre falsa — é a base que falta |
| 4 | Q4: soma dos quadrados | indução direta; 2n² + 7n + 6 = (n+2)(2n+3) |
| 4 | Q5: prova defeituosa de "árvore tem n−1 arestas" | *build-up*: o passo constrói árvores de n+1 em vez de partir de uma arbitrária |

**A antiga Q3 da Lista 3 agora é a Q4** — rótulos no banco, no mapa da prova e nos
scripts foram renumerados. Mesmo padrão da seção 3 (item (e) × (f)): **o professor
troca O por θ e "é possível" por "obrigatoriamente", e a resposta se inverte.**

### Semana 5 — feito em 31/08/2026

`semana-05-inducao-projeto-recursividade/` com os dois materiais do professor:
o artigo do **Manber** (CACM 1988, o texto fundador de "indução como paradigma de
projeto") e os **slides de MC458 da UNICAMP** (fatores de balanceamento,
**problema da celebridade**, subsequência consecutiva máxima).

A **Lista 4** está resolvida e verificada: Q1 (5 induções), Q2 (5 recorrências
pelo Teorema Mestre) e Q3 (crítica de uma prova por indução defeituosa — é o
"todos os cavalos têm a mesma cor" disfarçado). Mais o **exercício deixado em
aberto no slide** ("há ganho quando nₑ ≈ n_d ≈ n/2?"), que a varredura de filtro
duplo da seção 4 encontrou. Resposta: não há ganho de tempo — o custo é
*idêntico*, 2n+1 chamadas em qualquer formato de árvore; o que muda é a
profundidade da pilha, de Θ(n) para Θ(lg n).

### Pendente — ver `RESOLUCOES/PENDENTE.md`

- **Livro do OBMEP** (~100 sub-itens de indução). Adiado por volume em 27/08/2026.
  Descoberta relevante: a prova de 2025 **não tem uma única questão de indução**,
  então esse material é o de menor prioridade para a Prova 1.
- **Rosen e Gersting** (~75 exercícios citados pelo material do IFMG).
  Bloqueado: só as referências de página estão disponíveis, não os enunciados.
  Para destravar, é preciso conseguir os PDFs dos dois livros.

---

## 3. O que descobrimos sobre a prova

**O professor reaproveita as listas na prova.** Comparação feita entre a prova de
2025 e todo o material:

| Prova 2025 | Origem | Relação |
|---|---|---|
| Q2(c) | Lista 2, Q3(d) | **idêntica, palavra por palavra** |
| Q4(a) | Lista 3, Q1 | **idêntica a menos de uma expressão** (Alice e Bob): "executaram *ambos os* algoritmos" na lista, "*os dois* algoritmos" na prova |
| Q2(b) | Lista 2, Q3(a) | metade — a lista pede "se e somente se" |
| Q2(a) | Lista 2, Q3(c) | **operador + trocado por −, resposta se inverte** |
| Q3(b) | Lista 1, Q3(c) | mesma técnica, polinômio trocado |
| Q3(a) | Loureiro, ex. 5–8 | mesma técnica (Teorema Mestre) |
| Q5(a)(b) | Lista 3, Q4(d)(e) (era Q3 antes de 09/09/2026) | mesma técnica (recorrência) |
| Q1 (campo minado) | nenhuma | **totalmente nova** — única de projeto de algoritmo |

### O que a Lista 4 acrescenta a esse mapa

A Q2 da Lista 4 é **Teorema Mestre puro**, cinco itens, na forma de Brassard &
Bratley — a mesma técnica da Q3(a) da prova de 2025. A Q1 são cinco induções
sobre recorrências lineares, e a Q1(b) tem a mesma armadilha de constante que o
professor usou na Q2(a) da prova: base `T(1) = 2` dá `2ⁿ`, base `T(1) = 1` daria
`2ⁿ⁻¹`. Decorar a fórmula sem olhar a base perde o item.

### O que a Lista 5 acrescenta a esse mapa (14/09/2026)

A Lista 5 é **avaliada** (5 pontos, entrega em 24/09/2026) e conversa com a prova de 2025:

| Lista 5 | Prova 2025 | Relação |
|---|---|---|
| Q2 (vetor sem fim, m desconhecido, tempo o(n)) | Q1 (campo minado) | **mesma técnica**: dobrar o alcance (1, 2, 4, …) até passar do alvo, e pagar só O(lg alvo) ou O(alvo). A única questão "totalmente nova" de 2025 agora tem par numa lista. |
| Q3 (escolher entre A, B, C) | Q5(a)(b) | mesma estrutura: um algoritmo com n/b, outro com n − 1 |
| Q5 (dez recorrências) | Q3(a) | Teorema Mestre de Brassard & Bratley — mas **7 dos 10 itens não se aplicam** |

A novidade da Q5 é cobrar as **hipóteses** do formulário, não só a fórmula: c > 0 (itens com
−n, −n² e + 0), a e b naturais (3/2), f = c·nᵏ (n lg n) e a forma T(n/b) (T(n − 1)). Em (f),
(g), (i) — e em (d) com T(1) = 1 — aplicar a fórmula às cegas dá resposta **errada**, não só
injustificada. Na prova: conferir as hipóteses **antes** de comparar a com bᵏ.

### Duas coisas práticas

1. **A Q2(a) é a armadilha.** A Lista 2 Q3(c) diz `f + g ∈ O(u + v)` (verdadeira);
   a prova troca para `f − g ∈ O(u − v)` (falsa). Decorar o gabarito da lista faz
   perder os pontos. O que transfere é entender *por que* a soma funciona e a
   subtração não (O é fechado para soma; para subtrair seria preciso uma cota
   **inferior** de g).
2. **A prova fornece o Teorema Mestre na forma de Brassard & Bratley**
   (compara `a` com `b^k`), não a do CLRS (compara `f(n)` com `n^log_b a`).
   Treinar na forma da prova evita perder tempo traduzindo.

---

## 4. Como continuar nas próximas semanas

### Quando chegar material novo (semana 5 em diante)

1. Colocar o PDF na pasta da semana correspondente e atualizar o `README.md` dela.
2. **Varrer o PDF procurando exercício com filtro duplo** — este é o passo que
   falhou três vezes nesta sessão:
   - por **imperativo**: `Prove que`, `Mostre que`, `Calcule`, `Determine`, `Resolva`
   - por **rótulo**: `Exemplo`, `Exercício`, `Problema` — **sem exigir número**
   Os que aparecem como `Exemplo:` ou `Exemplo de…` escapam de filtros que
   procuram `Exemplo N`. Foi assim que 46 páginas ficaram de fora.
3. Distinguir **exercício** (para resolver) de **exemplo resolvido** (a solução já
   está no slide). Os exemplos entram na Parte III do banco como imagem da página
   original — reprodução fiel, sem risco de erro de transcrição.
4. Rodar o fluxo (seção 5) e regerar os documentos (seção 6).

### Quando resolver uma lista ou prova nova

Ver seção 5. O fluxo está estabelecido e funcionou em 5 rodadas.

---

## 5. O fluxo de resolução

```
enunciado
   │
   ├─1─ chão determinístico   → Python conta iterações / testa desigualdades.
   │                            SEMPRE antes dos agentes. Não precisa de biblioteca.
   ├─2─ solver(es)            → resolve, com o chão determinístico no prompt
   ├─3─ limpeza               → extrai só a prova final; o raciocínio é DESCARTADO
   ├─4─ verificadores         → contexto limpo, cegos ao raciocínio e uns aos outros
   ├─5─ voto assimétrico      → 4 HOLDS confirma / 2 HOLE_FOUND refuta
   ├─6─ correções             → aplicar os achados
   └─7─ REVERIFICAR           → mandar a versão corrigida de volta aos verificadores
```

**O passo 7 não é opcional.** Nesta sessão eu pulei ele: corrigi 8 blocos
refutados e escrevi o documento final sem reverificar. A reverificação posterior
encontrou 76 problemas nas minhas correções, incluindo um de gravidade alta que
**eu mesma introduzi** ao corrigir.

### Dê Bash aos verificadores

Nas primeiras rodadas os verificadores eram *thinking only* e vários erros
aritméticos passaram. Ao instruir *"use python3 para conferir as contas — não
confie em aritmética de cabeça"*, a qualidade dos achados mudou de patamar: 89
chamadas de ferramenta numa rodada, e achados do tipo "a conta impressa
`62.746 × 15,94 = 1.000.171` refuta a própria célula da tabela".

### Ataques que mais rendem nesta disciplina

| Padrão | O que checar |
|---|---|
| **#17 fencepost** | substituir `n = n₀` **exatamente** e fazer a conta dos dois lados. O mais produtivo de todos. |
| **#58 quantificadores** | `c` ou `n₀` dependem de n? Colisão de símbolos? Constante uniforme sobre todas as entradas? |
| **#60 interpretação** | "algumas" vs "todas"? melhor caso vs pior caso? ponto de cruzamento vs `n₀` da definição? |
| **#23 escopo** | vale em n=1? `lg 1 = 0`? laço que não executa? hipótese usada sem declarar? |
| **#40 passo limpo demais** | "claramente", "obviamente", "analogamente"? Num "se e somente se", as duas direções? |
| **#18 circularidade** | usou a tese para provar a tese? A "conferência" só substituiu na fórmula que queria conferir? |
| **coerência** | a linha "Resposta" bate com o corpo? As unidades são as mesmas (comparações vs operações primitivas, nós vs arestas)? |

---

## 6. Regerar os documentos

Os geradores estão em `RESOLUCOES/geradores/` e funcionam a partir dali:

```bash
cd ~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores
python3 gerar_banco.py            # banco-de-questoes.html
python3 gerar_complementares.py   # complementares.html
python3 gerar_prova.py            # prova-01-resolucao.html
```

Depois, HTML → PDF com Chrome headless:

```bash
R=~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --allow-file-access-from-files \
  --print-to-pdf="$R/banco-de-questoes.pdf" \
  "file://$R/fontes-html/banco-de-questoes.html"
```

| Arquivo | Papel |
|---|---|
| `catalogo.py` | as 73 questões: tema, fonte, enunciado, ponteiro para a resolução |
| `correcoes.py` | **31 patches** aplicados às saídas dos workflows, com o motivo de cada um |
| `gerar_*.py` | montam o HTML |
| `dados/*.output` | saídas cruas dos workflows (os geradores leem daqui) |
| `dados/lista04/q{1,2,3,4}-limpo.md` | os textos da Lista 4 que passaram pelos verificadores — **é a fonte de verdade**, o HTML é a diagramação deles |
| `dados/lista04/correcoes-lista04.py` | os **53 patches** da Lista 4, com motivo, gravidade e quem achou; idempotente, e marca os patches que rodadas posteriores sobrescreveram |
| `inventario.json` | mapa das 125 imagens de página dos slides |

As resoluções das listas 1–4 são HTML editado à mão em
`RESOLUCOES/fontes-html/` — o gerador do banco extrai os blocos de lá, casando
`<div class="item">` por contagem de aninhamento (ver 7.7). Para regerar a
Lista 4 isolada:

```bash
R=~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --allow-file-access-from-files \
  --print-to-pdf="$R/lista-04-resolucao.pdf" \
  "file://$R/fontes-html/lista-04-resolucao.html"
python3 $R/verificacao/lista04-html-bate-com-verificado.py   # o PDF diz o mesmo que os .md verificados?
```

A **Lista 5** é diferente: o HTML não é editado à mão, é **gerado** dos `.md` verificados
(`dados/lista05/q*-limpo.md`), e o gerador confere linha a linha que nada caiu nem duplicou:

```bash
cd ~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES/geradores
python3 gerar_lista05.py          # fontes-html/lista-05-resolucao.html; aborta se faltar linha do .md
# depois o Chrome headless como acima, com lista-05-resolucao.{html,pdf}
cd ../.. && for f in RESOLUCOES/verificacao/lista05-*.py; do echo "== $f"; python3 "$f" | tail -2; done
```

Para mexer na Lista 5, **edite o `.md`** (e registre em `dados/lista05/correcoes-lista05.md`),
nunca o HTML. O estado da verificação que sai no rodapé fica em `dados/lista05/estado-verificacao.txt`.

### Volume único das listas 1 a 5

`listas-1-a-5-resolucao.pdf` é a capa (`fontes-html/listas-1-a-5-capa.html`, com o sumário) mais os
cinco PDFs de lista, juntados sem alteração. **Não se atualiza sozinho**: depois de regerar qualquer
lista, remonte — e se o número de páginas de alguma lista mudar, corrija as páginas do sumário na capa.

```bash
R=~/DEV/PAA-Projeto-Analise-Algoritmos/RESOLUCOES
"$CHROME" --headless --disable-gpu --no-pdf-header-footer --allow-file-access-from-files \
  --print-to-pdf=/tmp/capa.pdf "file://$R/fontes-html/listas-1-a-5-capa.html"
pdfunite /tmp/capa.pdf $R/lista-0{1,2,3,4,5}-resolucao.pdf $R/listas-1-a-5-resolucao.pdf
```

**Nunca edite os PDFs.** Edite o HTML (ou `correcoes.py`, para o texto vindo de
workflow) e regere.

---

## 7. Armadilhas conhecidas — leia antes de editar

Três padrões se repetiram nos meus próprios erros nesta sessão. Todos foram
pegos pelos verificadores, nenhum pela minha intuição.

### 7.1 Corrigir o corpo e esquecer a linha "Resposta"

**Aconteceu três vezes.** Corrigi o corpo do IFMG item (4) para "altura 5 arestas"
e deixei o campo `resposta` dizendo "altura 6" — dois verificadores independentes
classificaram como **gravidade alta**, o único desse nível em 76 achados.
Depois se repetiu com o algoritmo do campo minado e com a citação do Teorema 3.1.

**Sempre confira corpo E campo `resposta` a cada patch.**

### 7.2 O patch que introduz problema novo

A nota do `log n` no Campello ficou com a frase duplicada e sem acentos. O
"descarta no máximo metade" da busca binária continuou **falso** mesmo depois do
meu primeiro remendo (com n=4 um ramo deixa 1 de 4: descarta 75%).

**Todo lote de correção deve voltar para verificação.**

Em 31/08/2026 isso se pagou duas vezes, nas duas com o patch criando defeito novo:
(i) ao reescrever o vocabulário lógico da Questão 3, a frase inserida “Duas regras
trabalham juntas” criou um antecedente para “nenhuma das duas se aplica”, que ficou
**falsa** — a descarga de hipótese *se aplica* com `n = 3` fixo, e produz exatamente
a implicação que a oração seguinte diz que o texto estabelece; (ii) ao explicar que
o Lema da Questão 2 vale para `c = 1`, escrevi que “as testemunhas apenas se
reescalam por `c`”, o que é **falso para 0 < c < 1** (o termo do caso base não leva
o `c`). Os dois foram achados pela reverificação, nenhum pela releitura.

### 7.2b A seção 6 do fluxo não é opcional para o gerador

Regerar o `banco-de-questoes.pdf` depois de mexer no `catalogo.py` ou no
`gerar_banco.py` precisa da mesma disciplina: `verificacao/lista04-no-banco.py`
confere que as questões novas entraram **e** que as antigas continuam lá. A
armadilha específica: o banco renderiza a fonte em versalete, e o `pdftotext`
quebra isso em `"L ista 4, Q1( a )"` — a primeira conferência deu 12 falsos
negativos por causa disso. Normalize removendo todo espaço antes de comparar
rótulos.

### 7.3 A extração para verificação corrompendo o texto

Ao preparar o texto para mandar aos verificadores, apliquei remoção de tags HTML
(`<[^>]+>`) em **texto plano**. Isso comeu tudo entre `<` e `>`: o bloco do
Campello perdeu **49% do conteúdo** (`0 <= f(n) <= c*n²` virou `0 = n0`), e os
sobrescritos foram achatados (`Θ(n⁵)` virou `Θ(n5)`).

Consequência: os verificadores julgaram texto quebrado e o bloco voltou
"REFUTADO" por um problema que não existia. Ao reenviar o texto íntegro, o mesmo
bloco voltou **CONFIRMADO**.

**Antes de enviar qualquer texto para verificação:**
- não aplicar limpeza de HTML em texto plano;
- converter `<sup>x</sup>` em `^x` antes de remover tags;
- comparar o tamanho do texto extraído com o original — perda de um caractere
  sequer aborta o envio;
- pedir ao verificador que confirme a **integridade** antes de julgar o mérito
  (campo `integridade_ok` no schema).

### 7.4 O patch que conserta metade das ocorrências

Aconteceu duas vezes em 31/08/2026, e nas duas o problema era o mesmo símbolo
usado com dois sentidos. No apêndice da Lista 4, `a` e `b` eram as constantes de
custo **e** os parâmetros do Teorema Mestre; renomeei os do teorema para `α`, `β`
— e deixei duas ocorrências para trás, uma delas *depois* da declaração de
renomeação, onde “n potência exata de `b`” passou a significar “potência da
constante de custo”, que é sem sentido. Na Questão 2, renomeei `n₀` para
`n_base` e esqueci a primeira frase do mesmo parágrafo.

**Depois de renomear qualquer símbolo, faça um `grep` do nome antigo no arquivo
inteiro e olhe cada ocorrência.** Não confie em ter lembrado de todas.

### 7.5 Condição suficiente vendida como necessária

O erro mais fino desta sessão. Na Questão 3 eu escrevi que o passo indutivo
“equivale a exigir `T₁ ∈ A ∩ B`”. Falso: basta `A ∩ B ≠ ∅`, porque aplicar a
hipótese ao primeiro subconjunto **cria novas testemunhas** — todo elemento dele
passa a ser sabidamente chinês. Nesta construção as duas condições coincidem, e
por isso o veredito e o limiar `k ≥ 2` não mudaram; mas a questão pede
justificativa *formal*, e o critério estava errado.

Pior: eu tinha rejeitado explicitamente a formulação correta, chamando-a de “a
versão genérica”. **Quando o texto se gaba de ser mais preciso que a alternativa,
é ali que vale enumerar.** Dois verificadores independentes acharam, com o mesmo
contraexemplo (`k = 3`, `A = {T₁,T₂,T₃}`, `B = {T₂,T₃,T₄}`).

O mesmo padrão apareceu, mais leve, na Questão 1: “o somatório tem pelo menos
dois termos, **logo** pode ser separado” — a separação vale já com a soma vazia.

### 7.6 O script de edição que descarta o próprio trabalho

Escrevi um ajudante que aplicava uma lista de substituições e **gravava o arquivo
só no fim do laço**. Uma delas não casou, a exceção subiu, e as três anteriores —
já aplicadas em memória — foram perdidas em silêncio. Só percebi porque a
conferência do PDF acusou uma frase antiga que eu “tinha corrigido”.

**Grave a cada substituição, não no fim.** E o teste de idempotência
(`se o texto novo já está lá, pule`) precisa exigir um trecho longo: um `novo`
curto pode ser substring do arquivo e fingir que o patch já foi aplicado.

### 7.7 O extrator que trunca em silêncio

O `gerar_banco.py` extraía os blocos das resoluções com um regex cujo *lookahead*
listava o que pode vir **depois** do bloco. Funcionava para as listas 1–3 por
acidente do que elas contêm; na Lista 4, que usa `<p class="nota">` genérico entre
seções, truncava **9 dos 26 blocos** sem erro nenhum. Trocado por um extrator que
casa `<div>` contando aninhamento, com uma guarda que aborta se um bloco sair
desbalanceado — e conferido que reproduz os 15 + 18 + 13 blocos das listas 1–3
exatamente como antes.

**Todo extrator precisa de uma invariante que ele mesmo cheque.** “Extraiu 26
blocos” não é verificação; “os 26 têm as tags balanceadas” é.

### 7.8 Acusar o material do professor sem fazer a conta

O erro mais constrangedor desta sessão. Escrevi que o passo intermediário do
slide da UNICAMP — `T(n) = T(1) + Σ Θ(1)` — "não liga os extremos", e listei
uma divergência de contagem de parcelas. **Falso.** Fazendo a conta:

```
T(1) + (n−1)·(T(0) + b) = (2a + b) + (n−1)(a + b) = (n+1)a + n·b
```

que é exatamente o lado direito que o slide escreve. Conferido em n = 1…25.
Minha objeção contava *parcelas*, e `Θ(1)` não se compromete com constante
nenhuma — cada `Θ(1)` da soma é o incremento de um passo, que já embute o `T(0)`
do filho vazio. Pior: três linhas adiante o meu próprio texto dizia que "cada
Θ(1) pode esconder constante diferente", o que torna a contagem de parcelas
ilegítima pelo meu próprio critério.

A regra da seção 8 já dizia para não alterar enunciado. **Estende-se: antes de
apontar erro no material do professor, faça a conta e mostre o número.** Se a
conta fechar, o defeito é da minha leitura.

### 7.9 O rótulo do caso tem de bater com o formulário da prova

A prova imprime o Teorema Mestre nesta ordem:

| | Comparação | Solução |
|---|---|---|
| 1º | `a < bᵏ` | `Θ(nᵏ)` |
| 2º | `a = bᵏ` | `Θ(nᵏ lg n)` |
| 3º | `a > bᵏ` | `Θ(n^{log_b a})` |

Nossos textos da Lista 4 chamavam `a > bᵏ` de "primeiro caso" — e o
`prova-01-resolucao.html`, escrito antes, já usava a ordem do professor. Nenhuma
conta muda, mas com a folha na mesa o rótulo aponta para a linha errada, e isso
é ponto perdido de graça. **Ao citar "primeiro/segundo/terceiro caso", use a
ordem impressa no formulário, não a que for conveniente.**

O mesmo enunciado exige uma hipótese que os nossos textos omitiam: **T
assintoticamente não decrescente**.

### 7.10 O patch cujo `antigo` é prefixo do `novo` duplica em silêncio

O pior bug desta sessão, e o mais fácil de não ver. Um patch da Questão 3 tinha:

```python
antigo = "...se rompe logo após a base."
novo   = "...se rompe logo após a base. Soma-se a isso um defeito ..."
```

Depois de aplicado, `antigo` **continua no arquivo** — ele é prefixo do `novo`.
Então a próxima execução do script casa de novo e anexa outra cópia. Rodei o
aplicador oito vezes ao longo das rodadas: o parágrafo apareceu **oito vezes
seguidas** na seção RESPOSTA, e o script reportou "0 falhas" todas as vezes.

Quem pegou foi um verificador adversarial, não eu, e não a conferência
automática — porque a conferência procurava *presença* de frases, nunca
*quantidade*.

**Duas guardas, as duas agora no `correcoes-lista04.py`:**

```python
if p["antigo"] in p["novo"]:
    raise SystemExit("`antigo` é substring de `novo` — vai duplicar a cada execução")
texto = texto.replace(p["antigo"], p["novo"])
if p["antigo"] in texto:
    raise SystemExit("`antigo` ainda aparece depois da substituição")
```

E o teste que prova que funciona: **rodar o aplicador três vezes seguidas e
contar** — se o número mudar, está quebrado.

### 7.11 Quando parar de remendar

Seis rodadas de correção nesta lista; **três delas introduziram defeito novo**.
Em algum ponto o remendo passa a custar mais do que rende. O critério que ficou:

- achado **matemático ou lógico** (afirmação falsa, com contraexemplo) → corrige
  e reverifica, sempre;
- achado de **coerência** (o documento se contradiz, ou o corpo diverge da
  resposta) → corrige e reverifica;
- achado de **apresentação** (redação, ênfase, redundância, escolha de palavra,
  nada falso) → **registra e não mexe**.

Por isso os prompts de verificação da última rodada pedem que cada achado venha
**classificado nessas três faixas**. Sem isso, a decisão de parar vira gosto.

### 7.12 O chão determinístico pode estar errado

Duas vezes o meu próprio Python induziu o erro:

- Contei execuções de `soma = soma + 1` e chamei de complexidade. O código 2 da
  Lista 1 é **Θ(n²)**, não Θ(n) — o laço do meio paga n testes de condição por
  iteração de `i`, execute o corpo ou não. **Conte todas as operações primitivas**,
  não só o corpo mais interno.
- Escrevi "praticamente ilimitado" para o maior n com `f(n) = log n`, e o solver
  copiou. Está errado: o máximo existe e vale `2^t`.

### 7.13 O banco só enxerga o que está dentro de `<div class="item">`

Em 14/09/2026, os parágrafos de abertura das questões novas — inclusive a
**definição de S(n)** da Lista 3 Q5 — ficaram fora dos blocos `item` no HTML da
lista. No PDF da lista estava tudo certo; no banco, eles **sumiam sem erro**, e a
questão aparecia usando um símbolo nunca definido. Quem pegou foi a conferência do
banco, procurando uma frase da resposta. **Todo texto de uma questão vai dentro de
algum `<div class="item">`**, e inserir item novo desloca os índices de
`catalogo.py` — confira com o dump de blocos antes de regerar.

### 7.14 Resíduo curto casa texto legítimo

Na mesma rodada, o conferidor acusou o resíduo refutado "3n + 2" — que casou a
contagem **correta** do código 1 da Lista 1 Q2 — e "direção errada", que casou o
rodapé que **cita** a frase removida. É o espelho da 7.6 (o `novo` curto que finge
que o patch já foi aplicado). **Resíduo é a frase refutada em uso, longa o bastante
para não casar citação nem texto de outra questão.**

### 7.15 A correção que cria o defeito — de novo (Lista 5, 14/09/2026)

A rodada 1 derrubou a Q1 por "o custo não depende dos valores". Na correção, escrevi uma frase
de intuição nova — "no nível i da árvore há 2ⁱ chamadas, cada uma com uma combinação" — e a
rodada 2 derrubou **por 4 de 4**: com n = 6 os níveis têm 1, 2, 4, 4 chamadas, e as folhas não
combinam. É a 7.2 outra vez: das quatro rodadas da Q1, duas refutaram texto que eu tinha acabado
de escrever. **Frase de intuição também é afirmação: teste num n que não é potência de 2.**

### 7.16 A letra do formulário já tem dono

O enunciado da Q5 usa `c` para o coeficiente de f **e** para a constante do caso base ("T(n) = c
para n ≤ n0"). Herdei as duas no mesmo item: no (d) a letra valia −1 e, cinco linhas depois, 10.
Na Q1, `a` e `b` rotulavam MaxA e MaxB e também eram os parâmetros do Teorema Mestre no mesmo
parágrafo. **Antes de batizar uma constante, confira se o formulário da prova já usa a letra.**
Se usa, renomeie a sua (C, c_a, c_b) e diga que renomeou.

### 7.17 O extrator do banco exige `class="item"` literal

O gerador da Lista 5 marcava o quadro final como `<div class="item resposta">`. O extrator do
banco procura a string exata `<div class="item">` — as cinco respostas sumiriam do banco sem
erro nenhum, o mesmo padrão da 7.13. Pego ao reler o extrator antes de ligar a lista ao banco.
**Estilo vai numa `<div>` interna; o `item` fica literal.**

### 7.18 A guarda `antigo ⊂ novo` barra inserções — e está certa

A guarda da 7.10 abortou um lote de patches no meio: eram **inserções** (texto novo junto de uma
âncora), e nelas o `antigo` está sempre dentro do `novo` — rodar de novo duplicaria. Os patches
anteriores do lote já estavam gravados, sem nada pela metade (7.6 funcionando). Para inserção,
a idempotência é outra: **procure uma marca longa do texto inserido; se já está lá, pule.**

### 7.19 Três falsos positivos do meu próprio conferidor

(i) O formulário do Teorema Mestre está, de propósito, nos enunciados da Q1 **e** da Q3 — o teste
de duplicação comparava o HTML inteiro com um `.md` só. (ii) Tirar `<strong>` trocando por espaço
deixou "falso ." contra "falso.". (iii) A normalização em minúsculas fez o resíduo refutado
"T(n) = c para n ≤ n0" casar a frase **corrigida** "T(n) = C para n ≤ n0" (a 7.14 de novo). Os
três eram do conferidor, não do texto — e nos três o certo foi ler a linha acusada antes de
mexer em qualquer coisa.

### 7.20 Índice calculado escapa do ajuste por regex (Lista 1, 13/09/2026)

Ao retirar o Q1(f), desloquei em −1 os índices `("L1", n)` do catálogo com um regex sobre
literais. Os cinco códigos da Q2 não são literais: vêm de um laço com `("L1", 6+i)`. O regex não
os viu, e cada código sairia no banco **com a resolução do código seguinte** — o código 5 com a
Q3(a) —, sem erro nenhum. Pego ao ler o laço antes de regerar. O teste que fica
(`lista01-ajuste-2026-09-13.py`): **para toda entrada do catálogo, o `<h3>` do bloco apontado tem
de corresponder ao rótulo.** Contar blocos não pega deslocamento; casar rótulo com cabeçalho pega.

### 7.21 O pdftotext come expoente — e o enunciado vira outro (06/10/2026)

`f(n) = 2^117` saiu do pdftotext como `2117`, e a resolução inteira foi escrita para 2117. A
classe não mudou por sorte (constante é constante); com `n^2` viraria `n2`. **Transcreva enunciado
olhando a página renderizada (`pdftoppm`), não o texto extraído**, e confira com
`verificacao/enunciados-literais-2026-10-06.py`, que tolera expoente deslocado mas lista quais.
Conferidor que imprime "N falhas" e sai com exit 0 é invisível num laço `for f in verificacao/*.py`:
**todo script de conferência sai com código ≠ 0 quando acha falha.**

### 7.22 A frase de comentário é onde o erro mora (06/10/2026, complementares)

Na auditoria dos complementares, **9 dos 12 furos foram em frases laterais**, não nas contas: "o cancelamento é
o coração do método", "só é exponencial se o expoente for proporcional a n", "não há como construir o mínimo por
indução", "qualquer n representável cabe em 1 s", "fator k^(1/grau)" como regra geral. E uma delas era **minha,
da correção anterior** (a soma geométrica com S_n começando em i = 1). O que fez a onda B achá-las foi uma linha
no prompt dos verificadores: *"procure frases de intuição ('em geral', 'sempre', 'nenhum', 'qualquer') e teste cada
uma fora do exemplo"*. **Mantenha essa linha em todo prompt de verificação.**

E o erro mais grave da auditoria não estava em resolução nenhuma: **a paráfrase do enunciado trocou Ω por Θ**, e a
resolução respondeu com rigor à pergunta errada. Enunciado se transcreve da imagem, sempre (7.21).

---

### 7.23 A correção cria o defeito — quarta vez, e o material também tem dono (07/10/2026)

Nas 18 questões novas, **a maioria dos furos das ondas B em diante estava em frases que eu (ou um revisor) tinha
acabado de escrever**: a estrela K_{1,n−1} "custa Θ(n²)" (só no pior caso sobre a ordem das listas), "k da ordem de
n ⇒ Θ(n³)" (falso com k = n − 1), "x, y > 1 é necessário" (é suficiente), a faixa 27,5–48,3 que só valia nas
potências de 10. A 7.15 continua valendo: **frase nova é afirmação nova, e vai para verificação.**

Duas classes novas:
- **Afirmação sobre o material sem conferir o PDF.** "A análise da matriz está no trecho omitido" (está depois do
  exercício), "No texto, Kₙ com k = n…" (o texto não menciona Kₙ), e — a grave — a resolução da p. 18 cobrava n²
  para calcular os graus que **o próprio texto supõe armazenados**, e analisava um algoritmo sem a parada
  |V| < k + 1 do texto. Os verificadores só pegaram depois que o prompt passou a dar o caminho do PDF. **Ao
  verificar resolução que fala do material, dê o PDF ao verificador e mande conferir cada atribuição.**
- **A 7.3 dentro do conferidor.** O `complementares-enunciados-literais.py` tirava `<[^>]+>` também do texto do
  PDF, e "grau < k, … >" da Rezende p. 18 comia a página inteira (1/13 palavras). Tags só se tiram de HTML.

E uma prática que poupou rodadas: a sentença lateral classificada como **apresentação** (7.11) não é mexida —
mexer zera a contagem da questão inteira.

## 8. Regras de resposta

- **Justifique tudo.** As listas dizem explicitamente que resposta sem
  justificativa não é considerada.
- **Exiba as testemunhas.** Nada de O/Ω/Θ sem `c`, `n₀` (e `c₁`, `c₂` para Θ)
  numéricos. **Confira a desigualdade em `n = n₀` exatamente.**
- **Confira numericamente** antes de afirmar. Python puro, sem dependência.
- **Abstenha em vez de blefar.** "Sem solução confiável, travei em X" é melhor que
  um passo inventado que parece certo.
- **CLRS 3ª edição.** Toda citação de capítulo nesta disciplina é da 3ª edição.
- **Não altere os enunciados.** Eles são do professor. Todas as 34 correções desta
  sessão foram no texto de resolução — verifiquei automaticamente que nenhuma
  tocou enunciado.

---

## 9. Ferramentas em uso

| O quê | Onde | Para quê |
|---|---|---|
| skill `paa-analise-de-algoritmos` | `~/.claude/skills/paa-analise-de-algoritmos/SKILL.md` | obrigações formais + conferência numérica |
| plugin `math-olympiad` | `~/.claude/plugins/cache/claude-plugins-official/math-olympiad/` | verificação adversarial; `references/verifier_patterns.md` tem os ataques |
| `pdftotext`, `pdftoppm` | homebrew (poppler) | extrair texto e renderizar páginas dos PDFs |
| Chrome headless | `/Applications/Google Chrome.app` | HTML → PDF |
| `pdflatex` | `/Library/TeX/texbin` | instalado, mas não usado (o fluxo é HTML) |

Python puro para toda conferência numérica — **sem numpy nem sympy**, de
propósito: contar iteração de laço e testar desigualdade não precisa de
biblioteca, e uma dependência a menos é uma coisa a menos para quebrar.

---

## 10. Estrutura da pasta

```
PAA-Projeto-Analise-Algoritmos/
├── CLAUDE.md                    este arquivo
├── README.md                    índice da disciplina, mapa semana → CLRS
├── semana-01..05/               material por semana + README com os tópicos
├── material-complementar/       assintótica, indução, somatórios, videoaulas
├── listas-de-exercicios/        os enunciados das listas 1–5 (a 5 é avaliada)
├── provas/                      prova de 2025
├── anotacoes/                   suas anotações
└── RESOLUCOES/
    ├── banco-de-questoes.pdf    ← o principal (112 questões)
    ├── complementares.pdf
    ├── prova-01-resolucao.pdf
    ├── lista-0{1,2,3,4,5}-resolucao.pdf   (a 5 é gerada de geradores/dados/lista05/)
    ├── listas-1-a-5-resolucao.pdf   as cinco listas num volume (enunciado + resolução)
    ├── PENDENTE.md              OBMEP, Rosen, Gersting + inventário do que não tem exercício
    ├── fontes-html/             os HTML que geram os PDFs
    ├── geradores/               scripts + dados dos workflows
    ├── verificacao/             19 scripts de conferência numérica
    └── banco-img/               125 páginas de slides renderizadas
```

Ver `README.md` para o mapa semana → capítulo do CLRS.
