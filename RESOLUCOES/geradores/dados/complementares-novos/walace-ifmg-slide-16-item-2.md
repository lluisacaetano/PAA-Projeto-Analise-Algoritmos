Resposta. Σ_(i=1)^(n) i·i! = (n + 1)! − 1, para todo inteiro n ≥ 0 (em n = 0 a soma é vazia e vale 0 = 1! − 1). Obtém-se pelo método da perturbação aplicado à soma auxiliar T(n) = Σ_(i=1)^(n) i! ("perturbe i!"): escrevendo T(n + 1) de duas formas, T(n) aparece dos dois lados e se cancela, sobrando S(n) = (n + 1)! − 1. A forma fechada é conferida por indução em n.

INTERPRETAÇÃO.

O símbolo "∗" do enunciado é a multiplicação e "i!" é o fatorial de i; a soma pedida é S(n) = Σ_(i=1)^(n) i·i! = 1·1! + 2·2! + … + n·n!, e "= ?" pede uma forma fechada em função de n. A dica "perturbe i!" pode ser lida de duas maneiras: (a) perturbar a própria soma S(n), acrescentando o termo (n + 1)·(n + 1)!; (b) perturbar a soma auxiliar dos fatoriais, T(n) = Σ_(i=1)^(n) i!, do mesmo modo que o slide 15 perturba a soma dos cubos para achar a soma dos quadrados. A leitura (b) é a que segue o modelo do slide 15 (perturba-se uma soma "vizinha", cuja expansão faz aparecer a soma procurada) e é a que funciona diretamente, porque (i + 1)! = (i + 1)·i! = i·i! + i! faz surgir exatamente o termo i·i!. É a que resolvo. (A leitura (a) também pode ser levada a termo, mas a expansão de (i + 1)·(i + 1)! não reproduz S(n) com coeficiente que se cancele de forma útil; não é o caminho da dica.)

PASSO 1 — A SOMA AUXILIAR E O TERMO A MAIS:

Seja T(n) = Σ_(i=1)^(n) i!, para n ≥ 0 (T(0) = 0, soma vazia). Acrescentando mais um termo:

    1: T(n + 1) = Σ_(i=1)^(n+1) i! = Σ_(i=1)^(n) i! + (n + 1)! = T(n) + (n + 1)!.

PASSO 2 — A MESMA SOMA REESCRITA DE OUTRA FORMA:

Trocando o índice i por i + 1 (o novo índice vai de 0 a n) e separando o termo i = 0:

    2: T(n + 1) = Σ_(i=0)^(n) (i + 1)! = 1! + Σ_(i=1)^(n) (i + 1)! = 1 + Σ_(i=1)^(n) (i + 1)!.

Pela definição de fatorial, (i + 1)! = (i + 1)·i! = i·i! + i! para todo i ≥ 0. Logo, pela linearidade da soma finita,

    3: T(n + 1) = 1 + Σ_(i=1)^(n) (i·i! + i!) = 1 + Σ_(i=1)^(n) i·i! + Σ_(i=1)^(n) i! = 1 + S(n) + T(n).

Para n = 0 as linhas 2 e 3 continuam válidas: Σ_(i=0)^(0) (i + 1)! = 1! = 1, e as somas de i = 1 a 0 são vazias, valendo 0; fica T(1) = 1 = 1 + 0 + 0.

PASSO 3 — IGUALAR AS DUAS FORMAS:

As linhas 1 e 3 são duas expressões do mesmo número T(n + 1):

    4: T(n) + (n + 1)! = 1 + S(n) + T(n).

T(n) é um número finito (soma de n parcelas finitas), então pode ser subtraído dos dois lados:

    5: S(n) = (n + 1)! − 1.

Como no exemplo do slide 15 (onde Σ i³ aparece dos dois lados e se cancela), a soma perturbada T(n) se cancela por inteiro: não é preciso conhecer T(n), que serve só de veículo para chegar a S(n). A diferença está no que sobra: no slide 15 sobram as somas auxiliares Σ i e Σ 1, cujas formas fechadas é preciso conhecer, e a incógnita Σ i² aparece com coeficiente 3; aqui não sobra nenhuma soma além de S(n), que aparece com coeficiente 1.

PASSO 4 — CONFERÊNCIA DA FORMA FECHADA POR INDUÇÃO:

Seja P(n): Σ_(i=1)^(n) i·i! = (n + 1)! − 1. Provo P(n) para todo inteiro n ≥ 0.

Base, n = 0: o lado esquerdo é a soma vazia, igual a 0; o lado direito é 1! − 1 = 1 − 1 = 0. P(0) vale. (Se se preferir começar em n = 1, como o enunciado sugere: lado esquerdo 1·1! = 1, lado direito 2! − 1 = 1; P(1) vale.)

Passo: seja n ≥ 0 e suponha P(n), isto é, Σ_(i=1)^(n) i·i! = (n + 1)! − 1 (hipótese de indução). Então

    6: Σ_(i=1)^(n+1) i·i! = Σ_(i=1)^(n) i·i! + (n + 1)·(n + 1)!
    7:                    = (n + 1)! − 1 + (n + 1)·(n + 1)!          (hipótese de indução)
    8:                    = (n + 1)!·(1 + (n + 1)) − 1
    9:                    = (n + 2)·(n + 1)! − 1
    10:                   = (n + 2)! − 1,

que é exatamente P(n + 1). Pelo princípio da indução, P(n) vale para todo n ≥ 0.

OBSERVAÇÃO — POR QUE FUNCIONA (TELESCOPAGEM).

A identidade da linha 3, i·i! = (i + 1)! − i!, mostra que cada parcela é uma diferença de fatoriais consecutivos; somando de i = 1 a n, os termos intermediários se cancelam: S(n) = (2! − 1!) + (3! − 2!) + … + ((n + 1)! − n!) = (n + 1)! − 1! = (n + 1)! − 1. É o mesmo resultado, obtido sem a soma auxiliar; a perturbação faz esse cancelamento de forma implícita.

Exemplos: n = 1: 1 = 2! − 1; n = 2: 1 + 4 = 5 = 3! − 1; n = 3: 1 + 4 + 18 = 23 = 4! − 1; n = 4: 23 + 96 = 119 = 5! − 1.

Conferência numérica (Python; não faz parte da prova): Σ i·i! = (n + 1)! − 1 para n = 0..14, o que coincide com a forma fechada obtida pela perturbação e provada por indução (inclusive em n = 0, soma vazia). A conferência numérica não substitui a prova; a prova é a do PASSO 4.
