import matplotlib.pyplot as plt
import numpy as np
import random
import scipy


# GENERAL METHODS


def getMineralValue(areaNum: int):
    # Giving credit where credit is due:
    # I designed this function myself, but I had GitHub Copilot help me write the code
    # faster than it would take to type it out. So it is my own work, but completed faster
    # using GitHub Copilot.

    if areaNum == 1:
        return np.random.beta(2, 2) + 1
    elif areaNum == 2:
        return np.random.beta(3, 7) * 3
    elif areaNum == 3:
        return np.random.normal(2.4, 1.8)
    elif areaNum == 4:
        return np.random.uniform(-1, 4)
    elif areaNum == 5:
        return np.random.normal(0, 9)
    elif areaNum == 6:
        return np.random.beta(7, 3) + 2
    elif areaNum == 7:
        return np.random.uniform(0, 4)
    elif areaNum == 8:
        return np.random.beta(3, 7) * 2
    elif areaNum == 9:
        return np.random.normal(2, 1.4)
    elif areaNum == 10:
        return np.random.normal(1.3, 7)


# PART 1 METHODS


def part1():
    print("Running code for Q2 part 1")

    # get the plot ready
    fix, axs = plt.subplots(2, 5)

    for i in range(1, 11):  # check for all areas
        areaValues = dict()
        for j in range(24):  # check for 2 years once a month
            areaValues[j] = getMineralValue(i)
        areaValueKeys = list(areaValues.keys())
        areaValueValues = [i for i in areaValues.values()]

        # calculate subplot position in grid - ChatGPT helped me with this in formatting my graph nicely
        row = (i - 1) // 5
        col = (i - 1) % 5

        axs[row, col].plot(areaValueKeys, areaValueValues)
        axs[row, col].set_xlabel("Month")
        axs[row, col].set_ylabel("Value")
        axs[row, col].set_title("Area" + str(i))

    plt.show()

    print("Q2 part 1 code finished")


# PART 3 METHODS


def part3():
    print("Running code for Q2 part 3")

    # get the plot ready
    fix, axs = plt.subplots(2, 5)

    for i in range(1, 11):  # check for all areas
        areaValueKeys, areaValueValues = epsilonGreedy(.01, movingBandits=True)

        # calculate subplot position in grid - ChatGPT helped me with this in formatting my graph nicely
        row = (i - 1) // 5
        col = (i - 1) % 5

        axs[row, col].plot(areaValueKeys, areaValueValues)
        axs[row, col].set_xlabel("Month")
        axs[row, col].set_ylabel("Value")
        axs[row, col].set_title("Area" + str(i))

    plt.show()

    print("Q2 part 3 code finished")


def epsilonGreedy(epsilonValue, movingBandits=False):
    maxRewards = createEmptyList(len(get_probabilities()))

    x = range(5)
    y = []
    rewards = []  # holds the history of rewards, used in calculating average

    for i in x:

        n = np.random.random()  # generate random number to compare with epsilon

        probs = get_probabilities()
        machineIndex = -1

        if n > epsilonValue:  # Exploit
            machineIndex = maxRewards.index(max(maxRewards))
            if maxRewards[machineIndex] <= probs[machineIndex]:  # set the value if reward was higher
                maxRewards[machineIndex] = probs[machineIndex]

        else:  # Explore
            machineIndex = probs.index(random.choice(probs))
            if maxRewards[machineIndex] <= probs[machineIndex]:  # set the value if reward was higher
                maxRewards[machineIndex] = probs[machineIndex]

        # Calculate average rewards
        rewards.append(probs[machineIndex])
        y.append(calculateAverageRewards(rewards))

    return x, y


def get_probabilities():
    probs = [
        np.random.beta(2, 2) + 1,
        np.random.beta(3, 7) * 3,
        np.random.normal(2.4, 1.8),
        np.random.uniform(-1, 4),
        np.random.normal(0, 9),
        np.random.beta(7, 3) + 2,
        np.random.uniform(0, 4),
        np.random.beta(3, 7) * 2,
        np.random.normal(2, 1.4),
        np.random.normal(1.3, 7)
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
    return sumAmount / entryCount


# GENERAL METHODS


def main():
    part1()
    part3()


if __name__ == "__main__":
    main()
