# Verificação numérica

Scripts que confirmam as respostas por medição, não por argumento.
Python puro, sem dependência. Rode com `python3 <arquivo>`.

## Lista 1

| Arquivo | O que faz |
|---|---|
| `lista01-q2-operacoes-primitivas.py` | **O que vale para a Q2.** Conta *todas* as operações primitivas dos 5 códigos, conforme o guia RAM. Confirma as fórmulas exatas e as classes. |
| `lista01-q2-contagem-de-lacos.py` | Conta só as execuções de `soma = soma + 1`. **Ver aviso abaixo.** |
| `lista01-q3-testemunhas.py` | Testa os pares (c, n₀) da Q3 contra a definição do CLRS, em 300 000 valores de n. |

## Lista 2

| Arquivo | O que faz |
|---|---|
| `lista02-q4-operacoes-primitivas.py` | Conta todas as operações primitivas dos 5 códigos da Q4. Faz varredura exaustiva de `x` para descobrir qual valor realiza o pior caso nos códigos 3 e 4 — e eles são **opostos** (x = n no código 3, x = 1 no código 4). |
| `lista02-q1-cruzamentos.py` | Confere os pontos de cruzamento da Q1, com foco nas **bordas**: empate exato em n = 2500 e em n = 10⁷. |


## Lista 3

| Arquivo | O que faz |
|---|---|
| `lista03-inducao-e-recorrencias.py` | Confere as fórmulas fechadas das recorrências (d) e (e) por recursão direta; as somas de (b) e (c); a fronteira de (a) (`n! > 2ⁿ` é **falso** em n = 1, 2, 3 e verdadeiro a partir de 4); a ausência de cota inferior de ordem n² na Q2; e a calibração das constantes da Q1 varrendo **toda** a faixa n = 1…200. |

## Aviso — o caso degenerado lg 1 = 0

Ao calibrar constantes envolvendo `n·lg n`, lembre que **lg 1 = 0**, então o termo
zera em n = 1. Uma calibração com `T(n) = 15·n·lg n` dá `T(1) = 0` — tempo de
execução zero, fisicamente impossível — e inverte o resultado exatamente no
primeiro ponto. Some um termo constante (`+ 20`) ou declare o domínio n ≥ 2.

Esse erro passou na Lista 3 porque a calibração foi testada em n = 10, 50, 98, 99,
100, 200 e 1000 — **nunca em n = 1**. É literalmente a regra "sempre inclua
n = 1, 2, 3" sendo desobedecida por quem a escreveu.

## Aviso — a armadilha da contagem de laços

`lista01-q2-contagem-de-lacos.py` mede **quantas vezes o corpo mais interno
executa**, e isso **não é** a complexidade do código.

No código 2 da Lista 1, por exemplo, `soma = soma + 1` executa Θ(n) vezes — mas o
algoritmo é Θ(n²). O laço do meio paga n testes de condição por iteração de `i`,
**rode o corpo ou não**, e esses n² testes dominam. É a regra 4 do guia do
enunciado: custo do laço = (corpo + condição) × número de iterações.

Contar só o corpo dá a resposta errada exatamente nos casos em que a questão quer
te pegar. O script fica aqui porque a comparação entre os dois é instrutiva, não
porque a medição dele responde à questão.

## Cuidado com ponto flutuante em logaritmo

`math.log(243, 3)` devolve 4.999999999999999, e `math.floor` derruba para 4 em vez
de 5. Ao conferir laços com passo multiplicativo (`j = 3*j`), use aritmética
inteira:

```python
def floor_log3(i):
    t = 0; p = 1
    while p * 3 <= i: p *= 3; t += 1
    return t
```

Isso derrubou uma conferência da Lista 2 antes de ser percebido — o erro estava no
conferidor, não na resposta.

## Como ler o resultado

Bater em todos os pontos não é demonstração — mas divergir em qualquer ponto é
refutação imediata. O script serve para matar resposta errada antes de ela virar
resposta escrita.

Sempre inclua n = 1, 2, 3 e o ponto de fronteira exato: erro de borda
(`<=` vs `<`, empate no cruzamento, laço que não executa) só aparece ali.

---

## Lista 4 (31/08/2026)

| Script | O que confere |
|---|---|
| `lista04-chao-deterministico.py` | O **chão determinístico**, rodado antes de qualquer redação: as cinco formas fechadas da Q1 por recursão direta (incluindo n = 1, 2, 3); as cinco recorrências da Q2 em aritmética inteira exata, com a razão T(n)/g(n) para mostrar que fica limitada; e, para a Q3, enumeração exaustiva das 2ⁿ atribuições de nacionalidade mais a localização do k em que a construção quebra. |
| `lista04-formas-fechadas-e-testemunhas.py` | O Lema da expansão, (F1), (F2), a identidade A − B = 1 e os dois Corolários, varridos em dezenas de triplas (a, b, k) — inclusive o caso `a < b^k`, que **nenhum item do enunciado exerce**. Testemunhas conferidas em n = n₀ *exatamente*, com refutação explícita de n₀ = 1 nos casos de igualdade (lg 1 = 0). No fim, o **adendo da rodada 3**: as testemunhas para c ≠ 1, e a contraprova numérica de que a versão anterior (“reescalar por c”) é falsa para 0 < c < 1. Também implementa `FatorAltura` e mede as 2n+1 chamadas em cadeia, árvore balanceada e árvores aleatórias. |
| `lista04-html-bate-com-verificado.py` | O PDF é montado a partir de HTML escrito à mão, mas quem passou pelos verificadores adversariais foram os `.md` em `geradores/dados/lista04/`. Este script confere que os dois **dizem a mesma coisa**: 26 afirmações decisivas têm de aparecer nos dois, e 12 resíduos das versões refutadas não podem aparecer em nenhum. |
| `lista04-no-banco.py` | Que as 12 questões da Lista 4 entraram no `banco-de-questoes.pdf` **e** que as 73 anteriores continuam lá. Cuidado embutido: o banco usa versalete, e o `pdftotext` quebra isso em `"L ista 4, Q1( a )"` — a normalização remove todo espaço antes de comparar rótulos. |

Os quatro rodam da raiz do projeto e saem com código ≠ 0 se algo falhar:

```bash
cd ~/DEV/PAA-Projeto-Analise-Algoritmos
for f in RESOLUCOES/verificacao/lista04-*.py; do echo "== $f"; python3 "$f" | tail -3; done
```

---

## Atualização de 09/09/2026 (listas 1, 3 e 4 revisadas pelo professor)

| Script | O que confere |
|---|---|
| `atualizacao-2026-09-chao-deterministico.py` | Rodado **antes** de qualquer redação. L1 Q1(e): piso do θ do insertion sort, primeiro n com n(n−1)/2 ≥ 100n (= 201) e o fencepost N = 400 × 401. L1 Q1(f): contraexemplo de custo constante. L3 Q3: bissecção simulada para n = 0…12 em **toda** posição da moeda falsa, a estratégia 3×3 de 8 moedas e a de n − 1 pesagens para n = 3…11. L3 Q5: passo e falsidade em n = 0…10⁵. L4 Q4: identidade e cada linha do passo. L4 Q5: enumeração de todas as árvores rotuladas com até 6 vértices (Cayley), os Lemas 1 e 2, e o contraexemplo de C(4). |
| `atualizacao-2026-09-html-bate-com-verificado.py` | Os três PDFs dizem o mesmo que os `.md` verificados (`geradores/dados/lista0{1,3,4}/`): afirmações decisivas nos dois, resíduos das versões refutadas em nenhum, trechos que não podem duplicar, e a renumeração da L3 (inclusive no mapa da prova de 2025). |
| `atualizacao-2026-09-no-banco.py` | As questões novas entraram no banco, os rótulos "Lista 3, Q3(a)…(e)" sumiram, o texto verificado chegou junto, e a contagem é 90. |

**O que a verificação pegou.** L1 (e)(f): 3 de 4 verificadores derrubaram uma nota que dizia
"busca linear, no máximo 3n + 2 operações" — na contagem usual são 3n + 3. L3 Q5: 3 de 4
derrubaram "(ii) **exige** a fórmula do Lema" — falso, há o caminho por indução sobre ¬P
(o passo é reversível); é o erro da seção 7.5 do CLAUDE.md, de novo. L3 Q3 e L4 Q5
passaram, mas com observações que foram incorporadas e reverificadas. Todas as versões
finais: 4 de 4.

**Dois falsos positivos do conferidor, registrados para não repetir.** O resíduo "3n + 2"
casou a contagem **legítima** do código 1 da L1 Q2; e "direção errada" casou o rodapé que
**cita** a frase removida. Resíduo tem de ser a frase refutada *em uso*, longa o bastante
para não casar citação nem texto antigo.

**Conferentes de diagramação (PDF × `.md` × enunciado do professor), um por lista e um
para o banco.** Nenhuma divergência matemática nas questões novas, mas acharam **dois
defeitos antigos**, anteriores a esta rodada:
- L1 Q1, parágrafo introdutório de agosto: "trocar 'algumas' por 'todas' muda a resposta —
  é por isso que (a) e (b) diferem". **Falso**: (a) e (b) são ambos V. Reescrito ("só muda
  quando há piso") e mandado a 4 verificadores novos.
- L4 Q3, contramodelo: o HTML dizia "com uma pessoa chinesa e não-chinesas em pelo menos uma
  não-chinesa" — um patch de 31/08 casado pela metade (ver `correcoes-lista04.py`, linhas
  357/571). Restaurado o texto do `q3-limpo.md` e acrescentado a `lista04-html-bate-com-verificado.py`
  como decisiva e como resíduo.
- Na L4 Q5 do banco, a dica que eu escrevi ("cobre só uma parte da classe") contradizia a
  própria resolução — para árvores a construção cobre a classe toda; o defeito é não ter
  *provado* isso. Corrigida no `catalogo.py`.
O conferente do banco também checou, uma a uma, que as 33 questões das Listas 1, 3, 4 e do
slide aparecem com a resolução certa depois do deslocamento de índices: todas certas.

**Um bug de diagramação que só `atualizacao-2026-09-no-banco.py` pegou.** O extrator do banco pega só
os `<div class="item">`. Os parágrafos de abertura das questões novas — inclusive a
**definição de S(n)** na L3 Q5 — tinham ficado fora dos blocos e sumiam do banco sem erro
nenhum. Movidos para dentro do primeiro bloco de cada questão, sem deslocar índices.

---

## Lista 5 (14/09/2026) — avaliada, entrega em 24/09/2026

| Script | O que confere |
|---|---|
| `lista05-chao-deterministico.py` | O **chão determinístico**, rodado antes de qualquer redação e estendido a cada rodada de correção. Q1: implementa MaxA e MaxB, confere máximo, n − 1 comparações, n e 2n − 1 chamadas, pilha n e 1 + ⌈lg n⌉, custo idêntico em todas as permutações e — no modelo de custo por linha — que o vetor estritamente crescente é o pior caso nos dois. Q2: busca galopante em vetor sem fim para m = 0…699, com e sem repetição, versão infinita e de comprimento finito; cota 2⌊lg m⌋ + 3 (atingida em m = 2ᵗ − 1), cota inferior ⌊lg m⌋ + 2 e as testemunhas do o(n) para vários c. Q3: as três recorrências em aritmética exata, com t e c genéricos. Q4: a soma em `Fraction` e os dois passos indutivos. Q5: os dez itens, formas fechadas com T(1) = t e com T(n) = C para n ≤ n0, os limiares de (d) e os valores negativos de (d), (g), (i). |
| `lista05-html-bate-com-verificado.py` | O PDF diz o mesmo que os `.md` verificados: afirmações decisivas nos dois, resíduos das versões refutadas (tirados de `geradores/dados/lista05/historico/`) em nenhum, e trechos que não podem duplicar. Confere também que **cada resíduo casa em alguma versão refutada** — senão o teste seria vazio. |
| `lista05-no-banco.py` | As 5 questões entraram no banco (rótulo na Parte I e na Parte II), o **quadro Resposta** de cada uma chegou (é o bloco que sumiria primeiro, ver CLAUDE.md 7.17), as anteriores continuam lá e a capa diz 95. |

Diferente das listas 1–4: o HTML da Lista 5 é **gerado** dos `.md` por
`geradores/gerar_lista05.py`, que aborta se qualquer linha do texto verificado faltar ou
duplicar no HTML. Os dois conferidores acima são a checagem independente, feita no PDF.

**O que a verificação pegou.** 60+ verificadores em até 5 rodadas; o registro completo, com o
achado, a faixa (lógico, coerência, apresentação) e quantos verificadores acharam, está em
`geradores/dados/lista05/correcoes-lista05.md`. Nenhuma resposta final mudou; o que caiu foram
justificativas e contagens — entre elas, a leitura dupla de `A[meio]` na Q2 (a cota impressa
só valia para o algoritmo que o texto não escreveu) e uma frase que **a própria correção da
rodada 1 introduziu** na Q1 (CLAUDE.md 7.15).

**Três falsos positivos dos conferidores, registrados para não repetir** (CLAUDE.md 7.19): o
formulário repetido de propósito em duas questões, o espaço deixado ao remover `<strong>`, e a
normalização em minúsculas fazendo o resíduo "c" casar o texto corrigido "C".

---

## Ajuste de 13/09/2026 — Lista 1 (Q1(f) retirado pelo professor)

| Script | O que confere |
|---|---|
| `lista01-ajuste-2026-09-13.py` | A lista na pasta é o PDF do professor, com Q1 de itens (a)–(e); a resolução não tem mais o bloco do (f) nem frase que o trate como vigente (resíduos das versões anteriores); e a **invariante de índice**: para toda entrada `("L1", i)` do catálogo, o `<h3>` do i-ésimo bloco de `lista-01-resolucao.html` corresponde ao rótulo — Q1(x) → "(x)", "código k" → "Código k", Q3(x) → "(x) f(n)". No banco, cada código da Q2 aparece seguido da sua própria resolução. |

Os códigos da Q2 usavam índice **calculado** (`6+i`), que o deslocamento por regex de literais não
pegou (CLAUDE.md 7.20). `atualizacao-2026-09-*.py` e `lista05-no-banco.py` foram ajustados à nova
contagem (94) e à ausência do Q1(f).
