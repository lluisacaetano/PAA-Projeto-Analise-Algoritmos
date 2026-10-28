# Projeto e Análise de Algoritmos (PAA)

Bacharelado em Ciência da Computação — IFMG, Campus Formiga
Professor: Mário Luiz Rodrigues Oliveira
Semestre 2026/2

---

## Estrutura da pasta

```
PAA-Projeto-Analise-Algoritmos/
├── semana-01-analise-de-algoritmos/          apresentação da disciplina + análise de algoritmos
├── semana-02-notacao-assintotica/            O, Ω, Θ, propriedades, somatórios
├── semana-03-notacao-assintotica-somatorios/ continuação da semana 2
├── semana-04-inducao-e-recorrencias/         indução, substituição, árvore de recursão
├── semana-05-inducao-projeto-recursividade/  indução como paradigma de projeto, celebridade
├── listas-de-exercicios/                     listas 1 a 4 (estudo; 1, 3, 4 revisadas em 09/09) e lista 5 (AVALIADA)
├── provas/                                   prova exemplo
├── material-complementar/
│   ├── analise-assintotica/
│   ├── somatorios/
│   ├── inducao-matematica/
│   └── videoaulas/                           playlist UFABC (Carla Negri Lintzmayer)
└── anotacoes/                                minhas anotações
```

Cada pasta `semana-XX/` tem um `README.md` com os tópicos daquela semana, os
capítulos do CLRS correspondentes e os links.

---

## Bibliografia base

CORMEN, T. et al. **Algoritmos: Teoria e Prática**. 3ª edição. Editora Campus, 2012. (CLRS)

> Atenção: todas as indicações de capítulos referem-se à **3ª edição**.

### Mapa CLRS por semana

| Semana | Tema | CLRS (3ª ed.) |
|--------|------|---------------|
| 1 | Algoritmo, problema, instância, corretude, modelo RAM | Cap. 1; Cap. 2, seções 2.1 e 2.2 |
| 2 | Notação assintótica (O, Ω, Θ), propriedades, somatórios | Cap. 3 |
| 3 | Notação assintótica (continuação), algoritmos iterativos | Cap. 3 |
| 4 | Indução, relações de recorrência, substituição, árvore de recursão | Cap. 4, seções 4.3 e 4.4 |
| 5 | Indução como **paradigma de projeto**, problema da celebridade, recursividade | Cap. 4 (para a análise); ver Manber, CACM 1988 |

---

## Links úteis

- Análise de Algoritmos — Paulo Feofiloff (IME-USP)
  - Instância de um problema: https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/instance.html
  - Notação O: https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/Oh.html
  - Recorrências: https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/recurrence.html
  - Recursão: https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/recursion.html
- MANBER, U. *Using Induction to Design Algorithms*. CACM 31(11), nov. 1988, p. 1300–1313.
  (PDF em `semana-05-inducao-projeto-recursividade/`)
- Videoaulas — Profa. Carla Negri Lintzmayer (UFABC), 74 aulas:
  https://www.youtube.com/playlist?list=PLncEdvQ20-mgGanwuFczm-4IwIdIcIiha
  (assistir só as aulas correspondentes ao conteúdo do IFMG Formiga)

---

## Como resolver os exercícios (setup de precisão)

O `CLAUDE.md` desta pasta obriga a ativar, antes de qualquer resposta:

- **`paa-analise-de-algoritmos`** (skill pessoal, em `~/.claude/skills/`) — obrigações
  formais da disciplina (exibir c e n₀, ordem dos quantificadores, constante que não
  escapa na substituição) + conferência numérica em Python.
- **`math-olympiad`** (plugin oficial da Anthropic) — verificação adversarial em
  contexto limpo: o verificador vê só o enunciado e a prova final, nunca o raciocínio.

Motivo: autoverificação não pega o erro (arXiv:2503.21934 — 85,7% autoverificado
vira <5% sob correção humana). O gatilho automático do `math-olympiad` foi desenhado
para NÃO disparar em análise de complexidade, por isso a invocação é manual e está
escrita no `CLAUDE.md`.

---

## Pendências

Exercícios que ficaram para depois estão listados em
`RESOLUCOES/PENDENTE.md`: ~75 exercícios dos livros do
**Rosen** e do **Gersting** citados pelo material do IFMG (enunciados não
disponíveis nesta máquina) e os ~100 sub-itens do livro de indução do **OBMEP**.

---

## Avaliação

- **Listas de exercícios 1 a 4** — estudo e revisão, **não precisam ser entregues**.
- **Lista de exercícios 5** — **avaliada (5 pontos), entrega em 24/09/2026**. Divisão e
  conquista, busca num vetor sem fim, Teorema Mestre. Resolução em
  `RESOLUCOES/lista-05-resolucao.pdf`.
- **Prova I** — ver `provas/prova-01-2025-exemplo.pdf` como referência do formato.
