# *Homo ergodicus*

In biological and cultural evolutionary process, the real impacts of losses are often stronger than those of gains.
If there is even one zero in the sequence of generations, we are extinct.
In this contexts, the big losses are essentially all that matter in the long run.

![simple_gamble](./image/simple_gamble.png)

One consequence is that variance in fitness realy matters.
A lineage (or a community) A with lower mean fitness than lineage (or a community) B can still win if variance in fitness is sufficiently smaller.
An effective way to reduce variance is to cooperate, by sharing wealth.

One why to reduce variance in fitness ooperatation.
t if two agents can share their "wealth," together they reduce the variance and this increases the gain for both. That is, cooperating is not an altruistic act as it was proposed. There is a concrete physical advantage in multiplicative process.







This also had effects on how people behave.
When the asymmetry between real physical effects of gains and losses is large, people quite reasonably 'pay to avoid losses'.
When the asymmetry vanishes people don't unreasonably mind losses, and won't pay to avoid them.
**La simetria o asimentria depende del medioambiente en el cual los agentes toman decisiones**

## Analysing environments

In order to analyze an **environment** in which agents make decisions, we need to **represent** it with some kind of stochastic **function**.
The development of probability theory was motivated this purpose.
The actual starting point is the famous exchange of letters between Fermat and Pascal in 1654.
They wanted to solve how to assess people's hopes and expectations in a fair way.

In economics, a gamble is a random variable, $\delta x$, representing possible changes in wealth, $x$.
For example, a gamble can model the following situation: toss a coin, and for heads you win 50% of your current wealth, for tails you lose 40%.
Having an stocastic function that represent the environment the question is how to find the optimal policy.

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
