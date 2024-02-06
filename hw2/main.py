# HW 2
# Mason Francis
# CS 5060

# If you can't install numpy and matplotlib using the requirements.txt file, please install them manually using pip. \
# Also, Tkinter is probably needed to show plots for this code. 

import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # Comment out this line if you aren't using Tkinter. I had to include this to make it work on my machine
import matplotlib.pyplot as plt
import scipy


# Part 1

# My implementation was inspired by material available at https://www.codingninjas.com/studio/library/epsilon-greedy-algorithm

# Dr. Mario's probablilities code
def get_probabilities(drift=0, step=0):

    # set up probability changes for time step 3000
    adj0, adj2, adj7, adj18 = 0, 0, 0, 0
    if step >= 3000:
        adj0, adj2, adj7, adj18 = 7, 3, 1, 2
    
    probs = [
        np.random.normal(0 - drift + adj0,  5),
        np.random.normal(-0.5 - drift, 12),
        np.random.normal(2 - drift + adj2, 3.9),
        np.random.normal(-0.5 - drift, 7),
        np.random.normal(-1.2 - drift, 8),
        np.random.normal(-3 - drift, 7),
        np.random.normal(-10 - drift, 20),
        np.random.normal(-0.5 - drift + adj7, 1),
        np.random.normal(-1 - drift, 2),
        np.random.normal(1 - drift, 6),
        np.random.normal(0.7 - drift, 4),
        np.random.normal(-6 - drift, 11),
        np.random.normal(-7 - drift, 1),
        np.random.normal(-0.5 - drift, 2),
        np.random.normal(-6.5 - drift, 1),
        np.random.normal(-3 - drift, 6),
        np.random.normal(0 - drift, 8),
        np.random.normal(2 - drift, 3.9),
        np.random.normal(-9 - drift + adj18, 12),
        np.random.normal(-1 - drift, 6),
        np.random.normal(-4.5 - drift, 8)              
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
def epsilonGreedy(epsilonValue, plot, movingBandits=False):
    maxRewards = createEmptyList(len(get_probabilities()))
    
    x = range(10000)
    y = []
    rewards = []


    for i in x:
        
        n = np.random.random() # generate random number to compare with epsilon

        if movingBandits:
            drift = -0.001 * i
            probs = get_probabilities(drift=drift, step=i)
        else: # normal run 
            probs = get_probabilities()

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


# Runs the Thompson sampling algorithm, taking into account whether we are working with moving bandits or not
def thompsonSampling(plot, movingBandits=False):
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

        if movingBandits:
            drift = -0.001 * i
            probs = get_probabilities(drift=drift, step=i)
        else: # normal run 
            probs = get_probabilities()

        chosenArmVal = probs[maxSampleIndex]
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


    # Prepare for plotting
    fig, axs = plt.subplots(1, 2)


    # Run Epsilon Greedy algorithms
    epsilonGreedy(0.01, axs[0])
    epsilonGreedy(0.05, axs[0])
    epsilonGreedy(0.1, axs[0])
    epsilonGreedy(0.4, axs[0])

    # plot the reuslts
    axs[0].legend()
    axs[0].set_xlabel("Step")
    axs[0].set_ylabel("Avg. Reward")
    axs[0].set_title('Epsilon Runs')


    # Run Thompson sampling and plot the results
    thompsonSampling(axs[1])
    axs[1].legend()
    axs[1].set_xlabel("Step")
    axs[1].set_ylabel("Avg. Reward")
    axs[1].set_title("Thompson sampling")


    plt.show()


    # Part 2
    print("Executing part 2 of the assignment")

    # Prepare for plotting
    fig, axs = plt.subplots(1, 2)


    # Run Epsilon Greedy algorithms
    epsilonGreedy(0.01, axs[0], movingBandits=True)
    epsilonGreedy(0.05, axs[0], movingBandits=True)
    epsilonGreedy(0.1, axs[0], movingBandits=True)
    epsilonGreedy(0.4, axs[0], movingBandits=True)

    # plot the reuslts
    axs[0].legend()
    axs[0].set_xlabel("Step")
    axs[0].set_ylabel("Avg. Reward")
    axs[0].set_title('Epsilon Runs')


    # Run Thompson sampling and plot the results
    thompsonSampling(axs[1], movingBandits=True)
    axs[1].legend()
    axs[1].set_xlabel("Step")
    axs[1].set_ylabel("Avg. Reward")
    axs[1].set_title("Thompson sampling")

    plt.show()
