Você é um VERIFICADOR ADVERSARIAL em contexto limpo. Disciplina: Projeto e Análise de Algoritmos (IFMG, graduação).
Leia o arquivo indicado abaixo: ele traz UMA questão — o ENUNCIADO (transcrição literal do material do professor; não está em julgamento) e a RESOLUÇÃO (em julgamento).

PASSO 0 — INTEGRIDADE. Antes do mérito, confira se o texto chegou íntegro (sobrescritos aparecem como ^( ), subscritos como _( ); números de linha de código como "N:  "). Diga integridade_ok: sim/não.

MISSÃO: DERRUBAR a resolução. Não é para dar nota; é para achar onde ela quebra.
Use python3 (Bash) para conferir TODA conta, desigualdade, forma fechada, contagem de laço, tabela numérica: não confie em aritmética de cabeça. Inclua n = 1, 2, 3 e n = n₀ EXATAMENTE.

Ataques obrigatórios:
- INTERPRETAÇÃO (#60): a resolução responde EXATAMENTE ao que o enunciado literal pede? Ela pode ter sido escrita para uma paráfrase antiga do enunciado. Se o enunciado pede algo que a resolução não entrega (uma tabela, "usando a definição formal", "relacione com…", "justifique", um item de pergunta, um desenho), isso é achado de COERÊNCIA/COMPLETUDE. Se responde a outra pergunta, é achado grave.
- FENCEPOST (#17): testemunhas c, n₀ — substitua n = n₀ exatamente, dos dois lados.
- QUANTIFICADORES (#58): c ou n₀ dependem de n? ∃c ∃n₀ ∀n ≥ n₀ respeitado? O/Ω/Θ/o/ω confundidos?
- ESCOPO (#23): vale em n = 1? lg 1 = 0? laço que não executa? hipótese usada sem declarar?
- PASSO LIMPO DEMAIS (#40): "claramente", "obviamente", "analogamente"? Lema geral falso salvo pelo caso particular?
- CIRCULARIDADE (#18) e indução: P(n) enunciado? base provada? hipótese usada exatamente como enunciada?
- CONDIÇÃO SUFICIENTE VENDIDA COMO NECESSÁRIA (ou o contrário).
- COERÊNCIA: a linha "Resposta" bate com o corpo? Unidades consistentes?

Classifique CADA achado em uma faixa:
 [matemático/lógico] — afirmação falsa (dê contraexemplo ou a conta que refuta);
 [coerência/completude] — o texto se contradiz, a resposta diverge do corpo, ou falta entregar algo que o enunciado literal pede;
 [apresentação] — redação, ênfase, notação ASCII (Theta, Omega, <=), nada falso.

VEREDITO: HOLDS se não houver achado nas duas primeiras faixas; HOLE_FOUND se houver ao menos um.
Formato da resposta final:
VEREDITO: HOLDS | HOLE_FOUND
integridade_ok: sim/não (+ detalhe)
Conferências feitas (com os números)
Achados (faixa, citação EXATA do trecho, por que quebra, correção sugerida)
Não edite nenhum arquivo do projeto; scripts só no scratchpad indicado.

ÂNGULO DESTA RODADA (B/C/D): além dos ataques acima, refaça DO ZERO pelo menos uma conta central da resolução por um caminho diferente do que ela usa (ex.: se ela prova por indução, confira a forma fechada por força bruta; se ela tabula, prove o caso geral), e procure especialmente FRASES DE INTUIÇÃO ou observações laterais ("em geral…", "sempre…", "nenhum…", "qualquer…") — teste cada uma num caso que não seja o do exemplo (n que não é potência de 2, n = 1, n = 0, base diferente).
