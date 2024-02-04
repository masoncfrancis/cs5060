# HW 2
# Mason Francis
# CS 5060

# If you can't install scipy, numpy, and matplotlib using the requirements.txt file, please install them manually
# using pip. Also, Tkinter is required to show plots for this code. 

import scipy
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # comment out this line if you aren't using Tkinter. I had to include this to make it work on my machine
import matplotlib.pyplot as plt

def beta(a, b):
    beta_dist = scipy.stats.beta(a, b)
    return beta_dist

x = np.linspace(0,1,100)

print(np.random.normal(0.5,0.5))
a_current = 1
b_current = 1

for i in range(5):
    draw = np.random.normal(0.5,0.5)
    if draw > 0.5:
        b_current += 1
    else:
        a_current += 1
    plt.plot(beta(a_current, b_current).pdf(x))
    plt.show()
