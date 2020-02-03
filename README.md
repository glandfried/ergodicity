# *Homo ergodicus*

In biological and cultural evolutionary process, the real impacts of losses are often stronger than those of gains.
If there is even one zero in the sequence of generations, we are extinct.
In this contexts, typically multiplicative and noisy, the big losses are essentially all that matter in the long run.

Consider the following situation: toss a coin, and for heads you win 50% of your current wealth, for tails you lose 40%.
**Having a stocastic *function* that *represent* an *environment* the question is how to *find the optimal behavior* **.
The development of probability theory was motivated by this purpose.

The expected utility theory considers it is preferable to participate in this game, given that the expected value is positive.
However, if we look at what actually happens to many individual players, we will see that no one achieves what the current economic theory predicts.

![simple_gamble](./static/simple_gamble.png)

The expected utility theory systematically observed how people acted contrary to what was considered optimal.
Paired with a firm belief in its models, this has led to a narrative of human irrationality in large parts of economics.


A lineage (or a community) A with lower mean fitness than lineage (or a community) B can still win if variance in fitness is sufficiently smaller.
An effective way to reduce variance is to cooperate, by sharing wealth.
That is, cooperating is not an altruistic act as it was proposed. There is a concrete physical advantage in multiplicative process.


This also had effects on how people behave.
When the asymmetry between real physical effects of gains and losses is large, people quite reasonably 'pay to avoid losses'.
When the asymmetry vanishes people don't unreasonably mind losses, and won't pay to avoid them.

## The original treatment

The actual starting point of the **original treatment** is the famous exchange of letters between Fermat and Pascal in 1654.
A few years later, the following rule of thumb had become a well-established behavioral model: **The environment can be summarized in a single number through the expected value of the stochastic function that we use to represent it.**.

$$\text{expected value of $f$} = \sum_s p(s)f(s) $$

This is, multiply each possible earnings by its probability of obtaining it, and add everything.
In the previous example, the expected value of the environment is $0.05 = 0.5 \times 0.5 + (-0.4) \times 0.5$.
**If** we consider that **the expected value is an objective description of what happens to the agents in the environment**, then this would be the "fair" value to be paid to participate in the game**.

However, it was quickly recognized that when people decide whether to take part in an stochacstic game, they don’t consider the expected changes in wealth.
In 1713 Nicolas Bernoulli proposed a hypothetical game whose expectation value was divergent with a non-existent first moment, known as the **St. Petersburg paradox**.
The expected wealth model tells us that we would pay any finite fee, but that went against intuition.

The modern **utility theory** born as a solution to this St. Petersburg paradox.
In 1738 Daniel Bernoulli proposed that people don't consider the expected changes in wealth, $x$, but the expected changes in the utility of wealth, $u(x)$.
When the utility of extra wealth is roughly inversely proportional to how many wealth one already has, this leads to a diferential change in utility $du = 1/x dx$,
![change_in_utility](./static/change_in_utility)
with solution $u(x) = ln x$
![utility](./static/utility)

Thus, the utility function encodes the psychology of a particular individual.
Each person $i$ has an idiosyncratic utility function $u_i(x)$, $u_\text{brave}(x) = x$ and $u_\text{scared}(x) = ln x$, and intuitively computes their own expectation $E(u_i(x))$.




One consequence is that variance in fitness realy matters.





**La simetria o asimentria depende del medioambiente en el cual los agentes toman decisiones**

## Analysing environments

In economics, a gamble is a random variable, $\delta x$, representing possible changes in wealth, $x$.

After Pascal and Fermat onwards a rule of thumb had become as the well-established behavioural model: given the choice between two gambles, we pick the greater expected wealth change.
The belief that the expected value was sufficient to describe any stochastic function was consolidated. 

$$\int_{} $$

But is this model realistic?












This is because we are facing a multiplicative process.



When the asymmetry between real physical effects of gains and losses is large, people quite reasonably 'pay to avoid losses' (e.g. buy insurance).

When it is not large, people don't unreasonably mind losses, and won't pay to avoid them.


*Comparing what happens over time to what happens in expectation is a well-known problem in statistical mechanics, called "the ergodicity problem.*



## The start twit ([see](https://twitter.com/rlmcelreath/status/1218456256358375424?s=20))

*If the ergodicity debate about behavioral econ is new to you, maybe a good place to start* 

*In evolutionary theory everyone is taught the fact that lineage growth is a multiplicative process. If there is even one zero in the sequence of generations, you are extinct. More generally, the big losses are essentially all that matter in the long run.*

*One well-known consequence is that variance in fitness matters. A lineage A with lower mean fitness than lineage B can still win if variance in fitness is sufficiently smaller*

## The core twit ([see](https://twitter.com/ole_b_peters/status/1218171528438853632?s=20))

*The real physical impacts of losses are often stronger than those of gains.*
*This is so, even in the simplest mathematical finance model (geometric Brownian motion).*
*But it's only visible when we compute what happens over time, not in expectation.*

*Comparing what happens over time to what happens in expectation is a well-known problem in statistical mechanics, called "the ergodicity problem.*



## The paper

## The experiment

## The consecuences

## Some code



A system is ergodic if its time average equals its expectation value, that is, if it satisfies Birkhoff’s equation:

$$ \int $$

## meder2019-ergodicityBreaking




La tema de la ergodicidad es central siempre que se vaya a representar el entorno de unos agentes. Parece obvio decir que es necesario elegir una función que represente CORRECTAMENTE el entorno de los agentes. Durante mucho tiempo se representó el entorno a través del "valor esperado", el promedio ponderado de todos los entornos que podría alcanzar el sistema. Sin embargo, al menos en los sistemas evolutivos, biológico, cultural, económico, en los que "tocar el cero" implica la extinción o la marginación irreversible (en general en cualquier proceso multiplicativo), es un error representar el entorno a través del valor esperado porque este es DISTINTO del verdadero entorno de los agentes, aquello que efectivamente pueden conseguir en promedio en su período de vida (incluso en el infinito). Cuando las dos representaciones del entorno dan valor distintos se dice que el sistema es no-ergódico y viceversa.
