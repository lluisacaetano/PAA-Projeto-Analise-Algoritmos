# Lista 3 (versão de 09/09/2026) — Questão 3 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Questão 3. Têm-se 2ⁿ moedas de ouro, sendo uma delas falsa, com peso menor do que as
demais. Dispõe-se de uma balança de dois pratos, sem nenhum peso. Vamos mostrar, por
indução sobre n, que é possível achar a moeda falsa com n pesagens."

## SOLUÇÃO FINAL

### Suposições declaradas
1. Todas as moedas verdadeiras têm o mesmo peso p; a falsa tem peso q < p. ("As demais" são
   as verdadeiras; o enunciado diz que a falsa pesa menos que elas.)
2. Uma pesagem consiste em pôr um conjunto de moedas em cada prato e observar um de três
   resultados: prato esquerdo mais pesado, prato direito mais pesado, ou equilíbrio.
3. "Com n pesagens" é lido como "com no máximo n pesagens"; o procedimento abaixo usa
   exatamente n.
4. n é inteiro, n ≥ 1. (Se 0 ∈ ℕ, o caso n = 0 também vale e é tratado à parte.)

### A proposição (formulada para QUALQUER conjunto de moedas)
P(n): para todo conjunto M de 2ⁿ moedas no qual exatamente uma é falsa, de peso q, e as
demais têm todas o mesmo peso p > q, é possível identificar a moeda falsa de M usando
n pesagens.

A quantificação "para todo conjunto M" é essencial: no passo, a hipótese de indução será
aplicada a um SUBCONJUNTO das moedas originais, não ao conjunto original.

### Base (n = 1)
M tem 2¹ = 2 moedas. Põe-se uma em cada prato (1 pesagem). Um prato tem peso q e o outro,
p; como q < p, a balança não equilibra, e a moeda do prato mais leve é a falsa. P(1) vale,
com 1 pesagem.
(Caso n = 0, se 0 ∈ ℕ: M tem 2⁰ = 1 moeda, que é a falsa; 0 pesagens. P(0) vale.)

### Hipótese de indução
Seja n ≥ 1 fixado e suponha P(n): em qualquer conjunto de 2ⁿ moedas com exatamente uma
falsa, mais leve, e as demais de mesmo peso, acha-se a falsa com n pesagens.

### Passo
Seja M um conjunto qualquer de 2ⁿ⁺¹ moedas com exatamente uma falsa (peso q) e as demais de
peso p > q. Como 2ⁿ⁺¹ = 2·2ⁿ, divide-se M em dois conjuntos disjuntos M₁ e M₂ com 2ⁿ moedas
cada. Põe-se M₁ num prato e M₂ no outro (1 pesagem).

A falsa está em exatamente um dos dois grupos; chame-o de Mᵢ e o outro de Mⱼ. Então
  peso(Mᵢ) = (2ⁿ − 1)·p + q     e     peso(Mⱼ) = 2ⁿ·p,
e peso(Mⱼ) − peso(Mᵢ) = p − q > 0. Logo a balança não equilibra e o prato mais leve é o
de Mᵢ: a pesagem revela qual grupo contém a falsa.

Mᵢ é um conjunto de 2ⁿ moedas com exatamente uma falsa, de peso q, e as demais de peso p > q
— exatamente a situação de P(n). Pela hipótese de indução, aplicada ao conjunto Mᵢ, a falsa
de Mᵢ (que é a falsa de M) é identificada com n pesagens.

Total: 1 + n = n + 1 pesagens. Logo P(n+1) vale.

### Conclusão
Pelo princípio da indução matemática (base P(1), passo P(n) → P(n+1) para todo n ≥ 1),
P(n) vale para todo n ≥ 1: com 2ⁿ moedas, acha-se a falsa com n pesagens. ∎
(Se 0 ∈ ℕ, a base P(0) com o mesmo passo, aplicado também em n = 0 — divide 2 moedas em
grupos de 1, pesa, e P(0) identifica a falsa no grupo mais leve —, dá o resultado para
todo n ≥ 0.)

### Conferência de fencepost
- Passo com n = 1 (o menor em que é aplicado, na leitura n ≥ 1): 4 moedas → dois grupos de 2 → 1 pesagem →
  grupo mais leve de 2 moedas → base: 1 pesagem. Total 2 = n + 1. ✓
- O procedimento é a bissecção recursiva; o número de pesagens satisfaz
  W(1) = 1, W(n+1) = W(n) + 1, logo W(n) = n = lg(2ⁿ), o logaritmo do número de moedas.

### Observações
- Neste procedimento o resultado "equilíbrio" nunca ocorre: os dois pratos têm o mesmo
  número de moedas e só um contém a falsa.
- n pesagens bastam, mas não são o mínimo para n ≥ 3. Cada pesagem tem 3 resultados
  possíveis, e há 2ⁿ possibilidades para a posição da falsa; logo qualquer estratégia precisa
  de pelo menos ⌈log₃ 2ⁿ⌉ pesagens, e dividir em três grupos aproveita o resultado
  "equilíbrio". Exemplo: 8 moedas (n = 3) em 2 pesagens — pesa-se 3 contra 3; se equilibrar,
  a falsa está entre as 2 restantes, e pesa-se uma contra a outra; se não, está entre as 3 do
  prato mais leve, e pesa-se uma contra outra dessas três: o prato mais leve indica a falsa e,
  no equilíbrio, a falsa é a terceira. Para todo n ≥ 3 isso dá uma estratégia com menos de
  n pesagens: faz-se a bissecção por n − 3 pesagens, até restar um grupo de 2³ = 8 moedas que
  contém a falsa, e resolve-se esse grupo em 2 pesagens como acima; total
  (n − 3) + 2 = n − 1 < n. O enunciado pede apenas que n pesagens sejam suficientes, que é o
  que a indução mostra.

## RESPOSTA
P(n): "em qualquer conjunto de 2ⁿ moedas com exatamente uma falsa, mais leve, e as demais de
mesmo peso, acha-se a falsa com n pesagens". Base n = 1: uma moeda em cada prato, a mais leve é a falsa. Passo: divide-se
2ⁿ⁺¹ moedas em dois grupos de 2ⁿ, pesa-se um contra o outro; o grupo mais leve contém a falsa
(diferença de peso p − q > 0) e é um conjunto de 2ⁿ moedas nas condições de P(n); a hipótese
de indução acha a falsa nele com n pesagens; total n + 1. Logo n pesagens bastam para 2ⁿ moedas.
