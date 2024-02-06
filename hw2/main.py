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
import scipy


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


# Generates beta distribution. Function provided by Dr. Mario
def beta(a, b):
    beta_dist = scipy.stats.beta(a, b)
    return beta_dist
    

# Takes a list of numbers and calculates the mean of all values
def calculateAverageRewards(rewardsList):
    entryCount = len(rewardsList)
    sumAmount = sum(rewardsList)
    return sumAmount/entryCount

    
# Runs the epsilon greedy algorithm for a given epsilon value    
def epsilonGreedy(epsilonValue, plot):
    maxRewards = createEmptyList(len(get_probabilities()))
    
    x = range(10000)
    y = []
    rewards = []


    for i in x:
        
        n = np.random.random() # generate random number to compare with epsilon

        probs = get_probabilities()
        machineIndex = -1

        if n > epsilonValue: # Exploit
            machineIndex = maxRewards.index(max(maxRewards))
            if maxRewards[machineIndex] <= probs[machineIndex]: # set the value if reward was higher
                maxRewards[machineIndex] = probs[machineIndex]
            
        else: # Explore
            machineIndex = probs.index(random.choice(probs))
            if maxRewards[machineIndex] <= probs[machineIndex]: # set the value if reward was higher
                maxRewards[machineIndex] = probs[machineIndex]
            
        rewards.append(probs[machineIndex])
        y.append(calculateAverageRewards(rewards))
            

    plotLabel = str(epsilonValue) + " Epsilon"
    plot.plot(x, y, label=plotLabel)


def thompsonSampling(plot):
    x = range(10000)
    y = []
    rewards = []

    # prepare initial distributions for each arm
    distributions = []
    for i in range(len(get_probabilities())):
        distributions.append({'a': 1, 'b': 1, 'dist': beta(1, 1)})

    for i in x:
        # take samples
        samples = []
        for dist in distributions:
            samples.append(dist['dist'].rvs(size=1))
        
        maxSampleIndex = samples.index(max(samples))


        chosenArmVal = get_probabilities()[maxSampleIndex]
        rewards.append(chosenArmVal)
        y.append(calculateAverageRewards(rewardsList=rewards))
        
        if chosenArmVal >= 1:
            distributions[maxSampleIndex]['a'] += 1
        else:
            distributions[maxSampleIndex]['b'] += 1
        distributions[maxSampleIndex]['dist'] = beta(distributions[maxSampleIndex]['a'], distributions[maxSampleIndex]['b'])
    
    plot.plot(x, y, label="Thompson")



if __name__ == "__main__":

    # Part 1
    print("Executing part 1 of the assignment")

    fig, axs = plt.subplots(1, 2)

    epsilonGreedy(0.01, axs[0])
    epsilonGreedy(0.05, axs[0])
    epsilonGreedy(0.1, axs[0])
    epsilonGreedy(0.4, axs[0])

    axs[0].legend()
    axs[0].set_xlabel("Step")
    axs[0].set_ylabel("Avg. Reward")
    axs[0].set_title('Epsilon Runs')

    thompsonSampling(axs[1])
    axs[1].legend()
    axs[1].set_xlabel("Step")
    axs[1].set_ylabel("Avg. Reward")
    axs[1].set_title("Thompson sampling")


    plt.show()


    # Part 2
    print("Executing part 2 of the assignment")

