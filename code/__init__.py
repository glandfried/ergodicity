"""
   :copyright: (c) 2020 by Gustavo Landfried
   :license: BSD, see LICENSE for more details.
"""
import math
import numpy as np
from numpy.random import normal as rnorm
from matplotlib import pyplot as plt 


def dW(pos=0,step=1):
    return rnorm(pos,step,1)[0]

def wiener(iterations,step_length):
    """
    Norbert Wiener process:
        A real valued continuous time stochastic process 
        of the one-dimensional Brownian motion.
    """
    res = [0]
    for i in range(iterations):
        pos = res[-1]
        res.append(dW(pos,step_length))
    return res

def show_walks(n,iteratons=100,step_length=1):
    """
    Examples
    ---------
    show_walks(10)
    show_walks(10,1000,0.01) # See changes on scale
    """
    
    for i in range(n):
        plt.plot(wiener(iteratons,step_length))
        
def simple_gamble(x):
    r = np.random.random()
    if r <= 0.5:
        res = 1.5*x
    else:
        res = 0.6*x
    return res

def walk_simple_gamble(iteratons):
    res = [1]
    for i in range(iteratons):
        res.append(simple_gamble(res[-1]))
    return res

def show_simple_gamble_walks(n,iterations=100):
    """
    show_simple_gamble_walks(10,1000)
    """
    delta_expected = 1.5*0.5+0.6*0.5 - 1 # <\Delta x>
    time_average = np.log(1.5)*0.5+np.log(0.6)*0.5 # <\Delta ln x>
    for i in range(n):
        plt.plot(np.log10(walk_simple_gamble(iterations)))
    plt.plot([0,iterations],np.log10([1,(1+delta_expected)**iterations ]) )
    plt.plot([0,iterations],np.log10([1,(1+time_average)**iterations ]) )
    
def mult(n,rate,dt):
    wealth = [1]
    time = [0]
    for i in range(n):
        wealth.append(wealth[-1]*rate)
        time.append(time[-1]+dt)
    return time, wealth

def show_mult(n=120,rate=1.01,dt=1/12):
    """
    show_mult(1,1.20,dt=1)
    show_mult(12,1.01,dt=1/12)
    """
    x, y = mult(n,rate,dt)
    plt.plot(x,y)
    
def gr_mult(rate,dt):
    """
    Constant growth rate in a multiplicative process
    
    Examples
    --------
    gr_mult(1.125,1)
    gr_mult(1.01,1/12)
    """
    return np.log(rate)/dt

"""
To perturb the process in a consistent way, we remind ourselves
that what's constant about the process in the absence of noise is the
growth rate
"""

def perturbed_payment(rate=1.01,dt=1/12,sigma=0.1):
    """
    perturbed_payment(1.125,1,1)
    """
    gamma = np.log(rate)/dt
    dv = gamma*dt + sigma*dW(0,dt)
    return dv

def walk_perturbed_payment(n,rate,dt,sigma=100):
    """
    walk_perturbed_payment(1000,1.01,1/12,100)
    """
    wealth = [1]
    for i in range(n):
        dv = perturbed_payment(rate,dt,sigma)
        wealth.append(wealth[-1]+wealth[-1]*dv)
    return wealth
        
def show_walk_perturbed_payment(n=10,iterations=1000,rate=1.005,dt=1/12,sigma=100):
    """
    show_walk_perturbed_payment(n=10,sigma=2)
    show_walk_perturbed_payment(n=1,sigma=0)
    """
    for i in range(n):
        plt.plot(np.log10(walk_perturbed_payment(iterations,rate,dt,sigma)) )
        




