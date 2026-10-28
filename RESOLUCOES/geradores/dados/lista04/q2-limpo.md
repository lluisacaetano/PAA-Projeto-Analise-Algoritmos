# Lista 4 — Questão 2 (prova limpa, para verificação adversarial)

## ENUNCIADO (literal)
"Indique o limite assintótico usando a notação Θ, para cada uma das equações de recorrência
abaixo. Considere o caso base T(1) = 1 ou T(n) = c, para alguma constante c e ∀n ≤ n0, para
alguma constante n0. Suponha, também, que n uma potência exata de b. Escolha o valor adequado
para a constante b conforme a equação de recorrência a ser resolvida. Justifique todas as suas
respostas. Respostas sem justificativas não serão consideradas."
[Nota de transcrição, fora do enunciado: onde se lê "que n uma potência exata de b", o original
do professor não traz o "é". Transcrito como está, sem correção.]
(a) T(n) = 2T(n/3) + 1
(b) T(n) = 5T(n/4) + n
(c) T(n) = 7T(n/7) + n
(d) T(n) = 9T(n/3) + n²
(e) T(n) = 8T(n/2) + n³

## SOLUÇÃO FINAL

### 0.1 Teorema Mestre, forma de Brassard & Bratley
Para T(n) = a·T(n/b) + c·n^k, com a ≥ 1 natural, b ≥ 2 natural, k ≥ 0, c > 0 real, n potência
exata de b, e T assintoticamente não decrescente — listando os casos na MESMA ORDEM em que o
formulário da prova os imprime, para que "primeiro/segundo/terceiro caso" aponte para a linha
certa com a folha na mesa:
  1º  a < b^k  →  T(n) ∈ Θ(n^k)
  2º  a = b^k  →  T(n) ∈ Θ(n^k · lg n)
  3º  a > b^k  →  T(n) ∈ Θ(n^(log_b a))
O valor de b é lido no argumento da chamada recursiva: se a chamada é T(n/3), então b = 3.
"Escolher o valor adequado de b" significa usar essa base ao supor n = b^m.
Dentro de Θ a base do logaritmo é irrelevante, pois log_x n = lg n / lg x e 1/lg x é constante
positiva. Escreve-se lg = log_2.

### 0.2 Lema da expansão (onde "n é potência exata de b" é usado)
O lema abaixo é enunciado com c = 1, que é o caso dos cinco itens desta questão. Para c > 0
qualquer, o termo motor fica multiplicado por c, mas o termo do caso base a^m não — de modo que
T_c(n) = a^m + c·(T_1(n) − a^m), e não c·T_1(n). As testemunhas mudam por constantes, não por um
simples fator c: no caso a = b^k ficam c1 = c/lg b, c2 = (1+c)/lg b, n0 = b; no caso a > b^k
ficam c1 = 1, c2 = 1 + c·B, n0 = 1 (a identidade A − B = 1 se preserva). Em ambos, as classes Θ
não mudam — que é o que importa aqui.
Lema. Seja T(1) = 1 e T(n) = a·T(n/b) + n^k para n > 1. Se n = b^m com m ≥ 0 inteiro, então
  T(b^m) = a^m + soma_{i=0}^{m−1} a^i · b^{k(m−i)}.

Prova por indução em m.
Base m = 0: o lado direito vale a^0 = 1 (a soma é vazia) e T(b^0) = T(1) = 1. Confere.
Passo: suponha a fórmula para m. Então
  T(b^{m+1}) = a·T(b^m) + (b^{m+1})^k
             = a·a^m + soma_{i=0}^{m−1} a^{i+1} b^{k(m−i)} + b^{k(m+1)}.
Trocando o índice para j = i+1, a soma vira soma_{j=1}^{m} a^j b^{k(m+1−j)}; e o termo isolado
b^{k(m+1)} é exatamente a parcela j = 0 dessa mesma soma. Logo
  T(b^{m+1}) = a^{m+1} + soma_{j=0}^{m} a^j b^{k(m+1−j)},
que é a fórmula para m+1. ∎

Onde a hipótese é usada: em cada um dos m desdobramentos o argumento b^m / b^i = b^{m−i} é
inteiro, e a recursão atinge o caso base T(1) após exatamente m = log_b n níveis. Sem essa
hipótese apareceriam pisos/tetos e a igualdade acima seria apenas aproximada.

### 0.3 Somando a série geométrica
Escrevendo b^{k(m−i)} = b^{km}·(b^{−k})^i, tem-se
  soma_{i=0}^{m−1} a^i b^{k(m−i)} = b^{km} · soma_{i=0}^{m−1} (a/b^k)^i,
com b^{km} = (b^m)^k = n^k e a^m = b^{m·log_b a} = (b^m)^{log_b a} = n^{log_b a}.

Caso a = b^k. A razão é 1, a soma tem m parcelas iguais a 1, e
  (F1)  T(n) = (m+1)·n^k = n^k·(log_b n + 1).

Caso a ≠ b^k. A soma geométrica de razão a/b^k ≠ 1 vale ((a/b^k)^m − 1)/((a/b^k) − 1).
Multiplicando numerador e denominador por b^k e usando b^{km}(a/b^k)^m = a^m:
  (F2)  T(n) = (a/(a − b^k))·n^{log_b a} − (b^k/(a − b^k))·n^k.

Corolário 1 (testemunhas no caso a > b^k, o terceiro). Escreva A = a/(a−b^k) e B = b^k/(a−b^k), ambos
positivos, com A − B = 1. Como a > b^k implica log_b a > k, o expoente k − log_b a é negativo,
logo n^{k−log_b a} ≤ 1 para todo n ≥ 1. Então T(n) = n^{log_b a}·(A − B·n^{k−log_b a}), e daí
  1·n^{log_b a} = (A−B)·n^{log_b a} ≤ T(n) ≤ A·n^{log_b a}  para todo n = b^m ≥ 1,
isto é c1 = 1, c2 = A, n0 = 1. Isso é Θ(n^{log_b a}).
Checagem de consistência: em n = 1 a fórmula dá T(1) = A − B = 1, que é o caso base dado.

Corolário 2 (testemunhas no caso a = b^k, o segundo). De (F1), T(n) = n^k·(lg n / lg b + 1). Para n ≥ b
vale lg n ≥ lg b, isto é 1 ≤ lg n / lg b; portanto
  (1/lg b)·n^k lg n ≤ T(n) ≤ (2/lg b)·n^k lg n  para todo n = b^m ≥ b,
isto é c1 = 1/lg b, c2 = 2/lg b, n0 = b. Isso é Θ(n^k lg n).
A restrição n ≥ b não é cosmética: em n = 1 ter-se-ia lg 1 = 0 e a cota superior seria
T(1) = 1 ≤ c2·0 = 0, falsa. Por isso n0 = b, e não n0 = 1.

### (a) T(n) = 2T(n/3) + 1
Identificação: chamada T(n/3) ⇒ b = 3; duas chamadas ⇒ a = 2; termo não recursivo 1 = 1·n^0
⇒ k = 0, c = 1.
Comparação: b^k = 3^0 = 1. Como 2 > 1, tem-se a > b^k: terceiro caso.
Conclusão: T(n) ∈ Θ(n^(log_3 2)), com log_3 2 = ln 2/ln 3 ≈ 0,630930 (a forma exata log_3 2 é
a resposta; o decimal é orientação).
Confirmação por expansão (n = 3^m, T(1) = 1): a/b^k = 2, e (F2) dá A = 2/(2−1) = 2,
B = 1/(2−1) = 1, ou seja T(3^m) = 2^{m+1} − 1, isto é T(n) = 2·n^(log_3 2) − 1.
Conferindo: T(3) = 2·T(1) + 1 = 3 = 2² − 1; T(9) = 2·3 + 1 = 7 = 2³ − 1.
Testemunhas (Corolário 1, A = 2): c1 = 1, c2 = 2, n0 = 1, pois
n^(log_3 2) ≤ 2n^(log_3 2) − 1 ≤ 2n^(log_3 2) para n ≥ 1 — a cota inferior equivale a
n^(log_3 2) ≥ 1, verdadeira exatamente para n ≥ 1. Em n = n0 = 1: 1 ≤ 1 ≤ 2.
Confirmação pela forma do CLRS: n^(log_b a) = n^(log_3 2) e f(n) = 1 = O(n^(log_3 2 − ε)) para
ε = 0,5 > 0. Caso 1 do CLRS ⇒ Θ(n^(log_3 2)). Mesma resposta.

### (b) T(n) = 5T(n/4) + n
Identificação: b = 4, a = 5, f(n) = n = 1·n^1 ⇒ k = 1, c = 1.
Comparação: b^k = 4^1 = 4. Como 5 > 4, tem-se a > b^k: terceiro caso.
Conclusão: T(n) ∈ Θ(n^(log_4 5)), com log_4 5 = ln 5/ln 4 ≈ 1,160964.
Confirmação por expansão (n = 4^m): a − b^k = 1, logo A = 5, B = 4 em (F2):
T(4^m) = 5·5^m − 4·4^m, isto é T(n) = 5·n^(log_4 5) − 4n.
Conferindo: T(4) = 5·1 + 4 = 9 e 5·5 − 4·4 = 9; T(16) = 5·9 + 16 = 61 e 125 − 64 = 61.
Testemunhas (Corolário 1, A = 5): c1 = 1, c2 = 5, n0 = 1. A cota inferior 5n^α − 4n ≥ n^α
(α = log_4 5) equivale a 4n^α ≥ 4n, isto é n^{α−1} ≥ 1 com α − 1 ≈ 0,161 > 0 — verdadeira para
todo n ≥ 1. Em n = n0 = 1: T(1) = 5 − 4 = 1, e 1 ≤ 1 ≤ 5. Em n = 4: n^α = 5, e 5 ≤ 9 ≤ 25.
Observação: o quociente T(n)/n^(log_4 5) = 5 − 4·n^{1−log_4 5} é crescente e limitado por 5 —
convergência lenta porque 1 − log_4 5 ≈ −0,161 é pequeno em módulo. Não falta fator logarítmico.
Confirmação pela forma do CLRS: f(n) = n = O(n^(log_4 5 − ε)) com ε = 0,1 (pois 1 ≤ 1,061).
Caso 1 ⇒ Θ(n^(log_4 5)). Mesma resposta.

### (c) T(n) = 7T(n/7) + n
Identificação: b = 7, a = 7, f(n) = n = 1·n^1 ⇒ k = 1, c = 1.
Comparação: b^k = 7^1 = 7 = a. Segundo caso (a = b^k).
Conclusão: T(n) ∈ Θ(n^k·lg n) = Θ(n lg n).
Confirmação por expansão (n = 7^m): como a = b^k, cada nível custa o mesmo — no nível i há 7^i
subproblemas de tamanho 7^{m−i}, custo total 7^i·7^{m−i} = 7^m = n por nível, para i = 0,…,m−1;
as 7^m = n folhas custam T(1) = 1 cada. Por (F1):
T(7^m) = (m+1)·7^m, isto é T(n) = n·(log_7 n + 1) = (1/lg 7)·n lg n + n.
Conferindo: T(7) = 7·1 + 7 = 14 = 2·7; T(49) = 7·14 + 49 = 147 = 3·49.
Testemunhas (Corolário 2, b = 7, lg 7 ≈ 2,807355): c1 = 1/lg 7 ≈ 0,356207,
c2 = 2/lg 7 ≈ 0,712414, n0 = 7. Em n = n0 = 7 exatamente: n lg n = 7·lg 7 ≈ 19,6515;
c1·19,6515 ≈ 7,0 e c2·19,6515 ≈ 14,0. Como T(7) = 14, vale 7 ≤ 14 ≤ 14 — a cota superior é
atingida com igualdade em n0, o que é permitido pela definição (≤), mas mostra que c2 não pode
ser reduzido mantendo n0 = 7.
Por que NÃO é Θ(n): pela forma fechada, T(n)/n = log_7 n + 1, que diverge — vale 2, 3, 4, 5 em
n = 7, 49, 343, 2401. Não existe c com T(n) ≤ c·n para todo n grande, logo T ∉ O(n) e a
fortiori T ∉ Θ(n). O fator lg n vem do número de níveis, não do custo por nível.
Confirmação pela forma do CLRS: n^(log_7 7) = n e f(n) = n = Θ(n^(log_b a)). Caso 2 ⇒ Θ(n lg n).

### (d) T(n) = 9T(n/3) + n²
Identificação: b = 3, a = 9, f(n) = n² = 1·n^2 ⇒ k = 2, c = 1.
Comparação: b^k = 3² = 9 = a. Segundo caso (a = b^k).
Conclusão: T(n) ∈ Θ(n^k·lg n) = Θ(n² lg n).
Confirmação por expansão (n = 3^m): no nível i há 9^i subproblemas de tamanho 3^{m−i}, custo
9^i·(3^{m−i})² = 9^i·9^{m−i} = 9^m = n² — custo idêntico em todos os níveis. Por (F1) com
k = 2, b = 3, e usando 9^m = (3^m)² = n²:
T(3^m) = (m+1)·9^m, isto é T(n) = n²·(log_3 n + 1) = (1/lg 3)·n² lg n + n².
Conferindo: T(3) = 9·1 + 9 = 18 = 2·9; T(9) = 9·18 + 81 = 243 = 3·81.
Testemunhas (Corolário 2, b = 3, lg 3 ≈ 1,584963): c1 = 1/lg 3 ≈ 0,630930,
c2 = 2/lg 3 ≈ 1,261860, n0 = 3. Em n = n0 = 3 exatamente: n² lg n = 9·lg 3 ≈ 14,2647;
c1·14,2647 ≈ 9,0 e c2·14,2647 ≈ 18,0; com T(3) = 18, vale 9 ≤ 18 ≤ 18.
Confirmação pela forma do CLRS: n^(log_3 9) = n² e f(n) = n² = Θ(n²). Caso 2 ⇒ Θ(n² lg n).

### (e) T(n) = 8T(n/2) + n³
Identificação: b = 2, a = 8, f(n) = n³ = 1·n^3 ⇒ k = 3, c = 1.
Comparação: b^k = 2³ = 8 = a. Segundo caso (a = b^k).
Conclusão: T(n) ∈ Θ(n^k·lg n) = Θ(n³ lg n).
Confirmação por expansão (n = 2^m): no nível i há 8^i subproblemas de tamanho 2^{m−i}, custo
8^i·(2^{m−i})³ = 8^i·8^{m−i} = 8^m = n³ por nível. Por (F1) com k = 3, b = 2 (log_2 n = lg n):
T(2^m) = (m+1)·8^m, isto é T(n) = n³·(lg n + 1) = n³ lg n + n³.
Conferindo: T(2) = 8·1 + 8 = 16 = 2·8; T(4) = 8·16 + 64 = 192 = 3·64.
Testemunhas (Corolário 2, b = 2, lg 2 = 1): c1 = 1, c2 = 2, n0 = 2. Em n = n0 = 2 exatamente:
n³ lg n = 8·1 = 8; c1·8 = 8 e c2·8 = 16; com T(2) = 16, vale 8 ≤ 16 ≤ 16.
Confirmação pela forma do CLRS: n^(log_2 8) = n³ e f(n) = n³ = Θ(n³). Caso 2 ⇒ Θ(n³ lg n).

### Observação sobre o caso base
O enunciado admite T(1) = 1 ou T(n) = c para todo n ≤ n_base. Isso não altera nenhuma das
classes Θ.
Refazendo o Lema com T(1) = c, o único termo afetado é a^m·T(1) = c·a^m:
(a) T(n) = (c+1)·n^(log_3 2) − 1 — ainda Θ(n^(log_3 2));
(b) T(n) = (c+4)·n^(log_4 5) − 4n — ainda Θ(n^(log_4 5));
(c) T(n) = n·(log_7 n + c) — ainda Θ(n lg n);
(d) T(n) = n²·(log_3 n + c) — ainda Θ(n² lg n);
(e) T(n) = n³·(lg n + c) — ainda Θ(n³ lg n).
Aqui c é a constante do caso base, não o coeficiente do termo motor da §0.2 — e os dois papéis
dão testemunhas diferentes. Com T(1) = c a razão T(n)/(n^k lg n) vale 1/lg b + c/lg n, cujo
ínfimo é 1/lg b e não depende de c; no regime do termo motor a razão é 1/lg n + c/lg b, com
ínfimo c/lg b. Portanto, no caso a = b^k com T(1) = c, as testemunhas são c1 = 1/lg b,
c2 = (1+c)/lg b, n0 = b. E no caso a > b^k com T(1) = c vale
T_c(n) = T_1(n) + (c−1)·a^m = (A + c − 1)·n^(log_b a) − B·n^k; como A − B = 1, a diferença
(A + c − 1) − B é exatamente c, e as testemunhas ficam c1 = c, c2 = c + B, n0 = 1. Em todos os
casos, portanto, c > 0 muda c1 e c2 apenas por constantes — nunca a classe. Nos casos de
igualdade o fator lg n sobrevive
porque vem do número de níveis (log_b n), que independe do caso base. Interromper a recursão em
n ≤ n_base (o limiar do enunciado, que não deve ser confundido com o n0 das testemunhas de Θ)
em vez de n = 1 corta apenas log_b n_base = O(1) níveis do topo do intervalo de somação — que
são os níveis mais profundos da árvore de recursão.

### Quadro-resumo
| item | recorrência | a | b | k | b^k | comparação | caso | forma fechada (n = b^m, T(1)=1) | resposta |
| (a) | 2T(n/3)+1  | 2 | 3 | 0 | 1 | 2 > 1 | 3º | 2n^(log_3 2) − 1 | Θ(n^(log_3 2)) ≈ Θ(n^0,6309) |
| (b) | 5T(n/4)+n  | 5 | 4 | 1 | 4 | 5 > 4 | 3º | 5n^(log_4 5) − 4n | Θ(n^(log_4 5)) ≈ Θ(n^1,1610) |
| (c) | 7T(n/7)+n  | 7 | 7 | 1 | 7 | 7 = 7 | 2º | n(log_7 n + 1) | Θ(n lg n) |
| (d) | 9T(n/3)+n² | 9 | 3 | 2 | 9 | 9 = 9 | 2º | n²(log_3 n + 1) | Θ(n² lg n) |
| (e) | 8T(n/2)+n³ | 8 | 2 | 3 | 8 | 8 = 8 | 2º | n³(lg n + 1) | Θ(n³ lg n) |

## RESPOSTA
(a) Θ(n^(log_3 2)), log_3 2 ≈ 0,630930. Forma fechada: 2n^(log_3 2) − 1.
(b) Θ(n^(log_4 5)), log_4 5 ≈ 1,160964. Forma fechada: 5n^(log_4 5) − 4n.
(c) Θ(n lg n). Forma fechada: n(log_7 n + 1).
(d) Θ(n² lg n). Forma fechada: n²(log_3 n + 1).
(e) Θ(n³ lg n). Forma fechada: n³(lg n + 1).

### Ressalva de escopo declarada
As formas fechadas exatas valem apenas sobre n = b^m. Para n arbitrário, com pisos, a conclusão
Θ continua válida, mas a igualdade exata não. As testemunhas c1, c2, n0 exibidas certificam o Θ
nessa subsequência, que é o que o enunciado pede ao mandar supor potência exata de b.
