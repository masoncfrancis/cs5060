# HW 2
# Mason Francis
# CS 5060

# If you can't install scipy, numpy, and matplotlib using the requirements.txt file, please install them manually
# using pip. Also, Tkinter is required to show plots for this code. 

import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # comment out this line if you aren't using Tkinter. I had to include this to make it work on my machine
import matplotlib.pyplot as plt


# Part 1

# My implementation was inspired by material available at https://www.codingninjas.com/studio/library/epsilon-greedy-algorithm

# Dr. Mario's probablilities code
def get_probabilities(drift=0):
    
    probs = [
        np.random.normal(0, 5),
        np.random.normal(-0.5,12),
        np.random.normal(2,3.9),
        np.random.normal(-0.5,7),
        np.random.normal(-1.2,8),
        np.random.normal(-3,7),
        np.random.normal(-10,20),
        np.random.normal(-0.5,1),
        np.random.normal(-1,2),
        np.random.normal(1,6),
        np.random.normal(0.7,4),
        np.random.normal(-6,11),
        np.random.normal(-7,1),
        np.random.normal(-0.5,2),
        np.random.normal(-6.5,1),
        np.random.normal(-3,6),
        np.random.normal(0,8),
        np.random.normal(2,3.9),
        np.random.normal(-9,12),
        np.random.normal(-1,6),
        np.random.normal(-4.5,8)              
    ]
    
    return probs


def createEmptyList(length):
    list = []
    for i in length:
        list.append(0)
    return list
    