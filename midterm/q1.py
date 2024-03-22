import matplotlib.pyplot as plt
import random
import time


def getProcValue():
    return random.uniform(1, 1000)


def getDaysProcValues():
    dayProcValues = list()  # list to store processor values for the day
    for i in range(1000):  # calculate day's values
        dayProcValues.append(getProcValue())

    dayProcValues.sort()
    return dayProcValues


# PART 1 METHODS


def getTopPercentOfValues(percentAsDecimal: list[float]):
    filteredList = []
    percentAsDecimal.sort()
    numOfViableProcs = .58 * 1000
    numOfEhpProcs = int(.002 * numOfViableProcs)
    return percentAsDecimal[-numOfEhpProcs:]


def getEHPProcs(dayProcValues):
    return getTopPercentOfValues(dayProcValues)


def part1():
    print("Running code for part 1")
    # getting values for ehp processors
    procValues = dict()
    timeTaken = dict()
    for i in range(1, 51):  # for 50 days
        startTime = time.time()
        dayProcValues = getDaysProcValues()
        ehpProcs = getEHPProcs(dayProcValues)
        procValues[i] = ehpProcs
        endTime = time.time()
        totalTime = endTime - startTime
        timeTaken[i] = totalTime

    procValueKeys = list(procValues.keys())
    procValueCount = [len(i) for i in procValues.values()]

    timeValueKeys = list(timeTaken.keys())
    timeValueCount = [i for i in timeTaken.values()]

    fix, axs = plt.subplots(1, 2)

    axs[0].plot(procValueKeys, procValueCount)
    axs[0].set_xlabel("Day")
    axs[0].set_ylabel("Number of processors produced")
    axs[0].set_title("EHP processor production")

    axs[1].plot(timeValueKeys, timeValueCount)
    axs[1].set_xlabel("Day #")
    axs[1].set_ylabel("Time Taken (s)")
    axs[1].set_title("Processing Performance")

    plt.show()


# PART 2 METHODS


def part2():
    print("Running code for part 2")
    procValues = dict()
    timeTaken = dict()
    for i in range(1, 51):  # for 50 days
        dayProcValues = getDaysProcValues()
        startTime = time.time()
        for j in procValues.values():
            if j >= (.58 * 1000) - (1000 * .002):
                procValues[i] = j
                break
        endTime = time.time()
        totalTime = endTime - startTime
        timeTaken[i] = totalTime

    timeValueKeys = list(timeTaken.keys())
    timeValueCount = [i for i in timeTaken.values()]

    plt.plot(timeValueKeys, timeValueCount)
    plt.title("Processing Performance")
    plt.xlabel("Day #")
    plt.ylabel("Time Taken (s)")
    plt.show()


# PART 3

def part3():
    print("Running code for part 3")
    procValues = dict()
    timeTaken = dict()
    for i in range(1, 51):  # for 50 days
        dayProcValues = getDaysProcValues()
        startTime = time.time()
        for j in procValues.values():
            if j >= (.58 * 1000) - (1000 * .002):
                procValues[i] = j
                break
        endTime = time.time()
        totalTime = endTime - startTime
        timeTaken[i] = totalTime

    timeValueKeys = list(timeTaken.keys())
    timeValueCount = [i for i in timeTaken.values()]

    plt.plot(timeValueKeys, timeValueCount)
    plt.title("Processing Performance")
    plt.xlabel("Day #")
    plt.ylabel("Time Taken (s)")
    plt.show()


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
