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
| `RESOLUCOES/banco-de-questoes.pdf` | 157 | **tudo**: 94 questões com resolução + 73 blocos de exemplos dos slides |
| `RESOLUCOES/complementares.pdf` | 94 | só PDFs/slides, resolução **abaixo** do enunciado |
| `RESOLUCOES/prova-01-resolucao.pdf` | 9 | prova de 2025 + mapa "de onde veio cada questão" |
| `RESOLUCOES/lista-0{1,2,3,4,5}-resolucao.pdf` | 8/7/7/12/11 | uma lista por arquivo |
| `RESOLUCOES/listas-1-a-5-resolucao.pdf` | 46 | as cinco listas num volume só, cada questão com enunciado e resolução (capa + junção dos cinco PDFs; ver seção 6) |

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
| Q4(a) | Lista 3, Q1 | **idêntica** (Alice e Bob) |
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

---

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
    ├── banco-de-questoes.pdf    ← o principal (94 questões)
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
