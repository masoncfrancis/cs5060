# HW 2
# Mason Francis
# CS 5060

# If you can't install numpy and matplotlib using the requirements.txt file, please install them manually using pip. \
# Also, Tkinter is required to show plots for this code. 

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


# Creates a List of 0s of the defined length
def createEmptyList(length):
    list = []
    for i in range(length):
        list.append(0)
    return list
    
# Creates a List of empty Lists
def createListOfLists(length):
    list = []
    for i in range(length):
        list.append([])
    return list
    

    
def epsilonGreedy(epsilonValue):
    maxRewards = createEmptyList(len(get_probabilities()))
    
    x = range(1, 10000 + 1) # values for the x axis of the plot
    y = [] # values for each step of which machine index was drawn each time
    # Note to self: y should be average reward

    for i in x:
        n = np.random.random() # generate random number to compare with epsilon

        probs = get_probabilities()

        if n > epsilonValue: # Exploit
            machineIndex = maxRewards.index(max(maxRewards))
            y.append(machineIndex)
            if maxRewards[machineIndex] <= probs[machineIndex]: # set the value if reward was higher
                maxRewards[machineIndex] = probs[machineIndex]
        else: # Explore
            machineIndex = probs.index(random.choice(probs))
            y.append(machineIndex)
            if maxRewards[machineIndex] <= probs[machineIndex]: # set the value if reward was higher
                maxRewards[machineIndex] = probs[machineIndex]
    
   
            

    plotLabel = str(epsilonValue)
    plt.plot(x, y, label=plotLabel)
    plt.show()


if __name__ == "__main__":

    epsilonGreedy(0.01)
    epsilonGreedy(0.05)
    epsilonGreedy(0.1)
    epsilonGreedy(0.4)
    