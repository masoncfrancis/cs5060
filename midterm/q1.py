import matplotlib.pyplot as plt
import random

# PART 1 METHODS

def getProcValue():
    return random.random(1, 1000)


def getDaysProcValues():
    dayProcValues = list() # list to store processor values for the day
    
    for i in range(1000): # calculate day's values
        dayProcValues.append(getProcValue())

    return dayProcValues

def getOnlyEHPProcs(daysProcValues):
    procValues = dict()
    for i in range(1,51):
        procValues[i] = []
        for j in daysProcValues:
            pass # continue here
    pass


def part1():
    print("Running code for part 1")
    


# PART 2 METHODS

def part2():
    pass

def main():
    part1()


if __name__ == "__main__":
    main()
