Resposta. Para todo inteiro n ≥ 0 (com a soma vazia valendo 0 quando n = 0), Σ_(i=1)^(n) i ∗ 2^i = (n − 1)·2^(n+1) + 2. Obtém-se pelo método da perturbação (slide 15): escreve-se S_(n+1) de duas formas, isolando o último termo e deslocando o índice, e isola-se S_n. A forma fechada é depois confirmada por indução em n.

LEITURA DO ENUNCIADO:
O símbolo "∗" é a multiplicação, como no restante do material, e "2^(i)" é a potência 2 elevada a i. A pergunta "= ?" pede a forma fechada da soma S_n = Σ_(i=1)^(n) i·2^i em função de n. Outra leitura possível seria pedir só a ordem de crescimento (por exemplo Θ(n·2^n)). Fica a da forma fechada exata, porque o exercício está na seção "3.2. Perturbação", cujo método produz uma expressão exata, e a ordem de crescimento sai dela de imediato. O limite inferior é i = 1. O termo i = 0 valeria 0·2^0 = 0, então começar em 0 ou em 1 dá o mesmo valor, e isso é usado abaixo.

NOTAÇÃO E FATO AUXILIAR:
Seja S_n = Σ_(i=1)^(n) i·2^i, para n ≥ 0 (S_0 = 0, soma vazia). Usa-se também a soma geométrica G_n = Σ_(i=0)^(n) 2^i = 2^(n+1) − 1, para n ≥ 0. Ela também sai por perturbação. De um lado, G_(n+1) = G_n + 2^(n+1), separando o último termo. Do outro, G_(n+1) = 2^0 + Σ_(i=1)^(n+1) 2^i = 1 + Σ_(j=0)^(n) 2^(j+1) = 1 + 2·G_n (com i = j + 1). Igualando, G_n + 2^(n+1) = 1 + 2·G_n, logo G_n = 2^(n+1) − 1.

PASSO 1 — PRIMEIRA FORMA DE S_(n+1) (ACRESCENTAR UM TERMO):
Separando o termo i = n + 1:
    S_(n+1) = Σ_(i=1)^(n) i·2^i + (n + 1)·2^(n+1) = S_n + (n + 1)·2^(n+1).

PASSO 2 — SEGUNDA FORMA DE S_(n+1) (REESCREVER A SOMA):
Com a troca de índice i = j + 1 (quando i vai de 1 a n + 1, j vai de 0 a n):
    S_(n+1) = Σ_(j=0)^(n) (j + 1)·2^(j+1)
            = Σ_(j=0)^(n) (2·j·2^j + 2·2^j)
            = 2·Σ_(j=0)^(n) j·2^j + 2·Σ_(j=0)^(n) 2^j.
Na primeira soma, o termo j = 0 vale 0·2^0 = 0, então Σ_(j=0)^(n) j·2^j = Σ_(j=1)^(n) j·2^j = S_n. A segunda soma é G_n = 2^(n+1) − 1. Logo
    S_(n+1) = 2·S_n + 2·(2^(n+1) − 1) = 2·S_n + 2^(n+2) − 2.

PASSO 3 — ISOLAR S_n:
Igualando as duas expressões de S_(n+1):
    S_n + (n + 1)·2^(n+1) = 2·S_n + 2^(n+2) − 2,
    S_n = (n + 1)·2^(n+1) − 2^(n+2) + 2 = (n + 1)·2^(n+1) − 2·2^(n+1) + 2 = (n − 1)·2^(n+1) + 2.
Esta é a mesma estratégia do slide 15, que aplica ao somatório Σ i³ um termo a mais e reescreve a soma. Aqui a soma perturbada já é a própria S_n: a parte que "sobra" do lado direito (2·S_n) traz S_n com coeficiente 2 ≠ 1, então ela não se cancela e pode ser isolada. Não foi preciso perturbar uma soma de grau maior, como acontece com Σ i² no slide.

PASSO 4 — CONFERÊNCIA POR INDUÇÃO EM n:
P(n): Σ_(i=1)^(n) i·2^i = (n − 1)·2^(n+1) + 2, para o inteiro n ≥ 0.
Base, n = 0: o lado esquerdo é a soma vazia, igual a 0. O lado direito é (0 − 1)·2^1 + 2 = −2 + 2 = 0. P(0) vale. (Para quem preferir começar em n = 1: o lado esquerdo é 1·2^1 = 2, e o direito é (1 − 1)·2^2 + 2 = 2. P(1) também vale.)
Passo: seja n ≥ 0 e suponha P(n), isto é, S_n = (n − 1)·2^(n+1) + 2 (hipótese de indução). Então
    S_(n+1) = S_n + (n + 1)·2^(n+1)                    (separando o último termo)
            = (n − 1)·2^(n+1) + 2 + (n + 1)·2^(n+1)    (hipótese de indução)
            = 2n·2^(n+1) + 2
            = n·2^(n+2) + 2
            = ((n + 1) − 1)·2^((n+1)+1) + 2,
que é exatamente P(n + 1). Pelo princípio da indução, P(n) vale para todo inteiro n ≥ 0.

OBSERVAÇÃO SOBRE A ORDEM DE CRESCIMENTO (consequência, não pedida):
Para n ≥ 1, S_n = (n − 1)·2^(n+1) + 2 ≤ n·2^(n+1) = 2·n·2^n, porque (n − 1)·2^(n+1) + 2 ≤ n·2^(n+1) equivale a 2 ≤ 2^(n+1), que vale para n ≥ 0. Também S_n ≥ (n − 1)·2^(n+1) ≥ (n/2)·2^(n+1) = n·2^n quando n − 1 ≥ n/2, isto é, n ≥ 2. Então S_n ∈ Θ(n·2^n) com testemunhas c₁ = 1, c₂ = 2, n₀ = 2. Em n = n₀ = 2: S_2 = 1·2 + 2·4 = 10, c₁·n·2^n = 8 ≤ 10 e c₂·n·2^n = 16 ≥ 10.

Conferência numérica (Python; não faz parte da prova): Σ i·2^i = (n − 1)·2^(n+1) + 2 para n = 0..14, a mesma forma fechada obtida acima. Contas à mão em valores pequenos batem: n = 0 dá 0, n = 1 dá 2, n = 2 dá 2 + 8 = 10 = 1·8 + 2, n = 3 dá 10 + 24 = 34 = 2·16 + 2.
