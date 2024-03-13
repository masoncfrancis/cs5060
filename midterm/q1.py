import matplotlib.pyplot as plt
import random


# PART 1 METHODS


def getProcValue():
    return random.uniform(1, 1000)


def getDaysProcValues():
    dayProcValues = list()  # list to store processor values for the day
    for i in range(1000):  # calculate day's values
        dayProcValues.append(getProcValue())

    dayProcValues.sort()
    return dayProcValues


def getTopPercentOfValues(percentAsDecimal: list[float]):
    filteredList = []
    percentAsDecimal.sort()
    numOfViableProcs = .58 * 1000
    numOfEhpProcs = int(.002 * numOfViableProcs)
    return percentAsDecimal[-numOfEhpProcs - 1:]


def getEHPProcs(dayProcValues):
    return getTopPercentOfValues(dayProcValues)


def part1():
    print("Running code for part 1")
    # getting values for ehp processors
    procValues = dict()
    for i in range(1, 51):  # for 50 days
        dayProcValues = getDaysProcValues()
        ehpProcs = getEHPProcs(dayProcValues)
        procValues[i] = ehpProcs
    print(procValues)


def main():
    part1()


if __name__ == "__main__":
    main()
