ÚNICA EXCEÇÃO À REGRA ABAIXO: você pode usar Read para ler ESTE arquivo de instruções e o arquivo do problema indicado no seu prompt, e Write UMA vez para gravar a solução final no caminho indicado. Nenhuma outra ferramenta (nada de Bash/Python).

NO COMPUTATION. Do not use Bash, Python, WebSearch, Read, Write, or any tool that runs code or fetches data. Numerical verification is not a proof step. "I computed n=1..10 and the pattern holds" is not a proof.

(If your agent harness requires a StructuredOutput or similar return-mechanism tool call, that is NOT a computation tool — call it to return your answer. The restriction is on tools that DO work, not tools that REPORT work.)

Your internal process (iterate until done):
- Solve: Complete rigorous solution.
- Self-improve: Reread. Fix gaps before a grader sees it.
- Self-verify: Strict grader mode. Every step justified?
- Correct: Fix and re-verify. Up to 5 rounds.
- Stop: Self-verify passes twice clean, OR 5 rounds, OR approach fundamentally wrong.

A correct answer from flawed reasoning is a failure. If incomplete, say so honestly. Never hide gaps.

PROBLEM: o arquivo indicado no fim traz o ENUNCIADO (transcrição literal do material do professor), o CONTEXTO do material de que ele depende e um CHÃO DETERMINÍSTICO (contas feitas em Python antes, para você conferir — não são prova). Disciplina: Projeto e Análise de Algoritmos (graduação, IFMG). Resolva EXATAMENTE o que o enunciado literal pede (interpretation check primeiro: liste as leituras possíveis e diga qual resolve e por quê).

OBRIGAÇÕES DA DISCIPLINA: toda afirmação O/Ω/Θ com testemunhas NUMÉRICAS (c, n0; c1, c2, n0 para Θ), conferidas em n = n0 exatamente, com a ordem ∃c ∃n0 ∀n ≥ n0; para provar que NÃO pertence, negue a definição corretamente (para todo c e n0 existe n ≥ n0 que viola) e exiba o n em função de c e n0. Somatórios em forma fechada. Indução com P(n) escrito, base, hipótese usada exatamente como enunciada. Diga sobre qual conjunto de entradas vale cada afirmação (pior caso, melhor caso, toda entrada). Use as definições do CONTEXTO do material. Cuidado com FRASES GERAIS ("sempre", "em geral", "qualquer", "nunca"): só escreva se forem verdadeiras fora do exemplo; senão, restrinja.

FORMATO DO ARQUIVO DE SAÍDA (texto puro em português, com acentos; Unicode para Θ, Ω, ≤, ², ⌊ ⌋ etc.; SEM markdown — sem #, sem **, sem tabelas com |):
- 1º parágrafo começa EXATAMENTE com "Resposta." e dá a resposta completa em poucas linhas (todos os itens, se houver vários).
- Depois, parágrafos separados por linha em branco; títulos de seção em MAIÚSCULAS terminando com ponto ou dois-pontos (ex.: "PASSO 1 — ...:" ou "ITEM 3."). Pseudocódigo/árvores em blocos com linhas numeradas "N:" ou recuados com 4+ espaços.
- Último parágrafo: "Conferência: ..." dizendo o que o CHÃO DETERMINÍSTICO confirma.
No relatório final (sua resposta), devolva só: Verdict / Rounds / Self-verification notes (curto). A solução vai no arquivo.

ANGLE: <ângulo>
ARQUIVO DO PROBLEMA: <caminho>
GRAVAR A SOLUÇÃO EM: <caminho>
