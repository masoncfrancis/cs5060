import matplotlib.pyplot as plt
import random

def getProcValue():
    return random.random(1, 1000)


def getDaysProcValues():
    dayProcValues = list() # list to store processor values for the day
    
    for i in range(1000): # calculate day's values
        dayProcValues.append(getProcValue())

    return dayProcValues


def main():
    pass


if __name__ == "__main__":
    main()
