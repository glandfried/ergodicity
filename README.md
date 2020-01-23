# *Homo ergodicus*

In biological and cultural evolutionary process, the real impacts of losses are often stronger than those of gains.
If there is even one zero in the sequence of generations, you are extinct.
More generally, the big losses are essentially all that matter in the long run.
This is so, even in the simplest stocastical financial model like the geometric Brownian motion.
One well-known consequence is that variance in fitness matters.
A lineage A with lower mean fitness than lineage B can still win if variance in fitness is sufficiently smaller.
This also had effects on how people behave.
When the asymmetry between real physical effects of gains and losses is large, people quite reasonably 'pay to avoid losses'.
When the asymmetry vanishes people don't unreasonably mind losses, and won't pay to avoid them.

## Where does this asymmetry come from?

The development of probability theory was motivated by gambling problems.
The actual starting point is the famous exchange of letters between Fermat and Pascal in 1654.
They were not looking for gambling advice, they were solving a moral problem: namely how to assess people's hopes and expectations in a fair way.

In economics, a gamble is a random variable, $\delta x$, representing possible changes in wealth, $x$.
For example, a gamble can model the following situation: toss a coin, and for heads you win 50% of your current wealth, for tails you lose 40%.
Formally, any **environment** in which agents make decisions can be **modelled** with some kind of stocastic **functions**.

Having an stocastic function that represent the environment the question is how to find the optimal policy.
From Pascal and Fermat a rule of thumb had become as the well-established behavioural model: given the choice between two gambles, we pick the greater
expected wealth change.

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
