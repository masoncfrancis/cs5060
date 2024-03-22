import pandas as pd
import matplotlib.pyplot as plt


# GENERAL METHODS

def trimColNames(colName: str):
    return colName.strip()


# PART 1 METHODS

def readCsv(fileName: str):
    frame = pd.read_csv(fileName, header=0)
    frame.columns = [trimColNames(colName) for colName in
                     frame]  # GitHub Copilot helped me figure out how to trim whitespace from column names
    frameReordered = frame.iloc[::-1]  # figured out how to do this reordering action using Phind.com
    return frameReordered


def getCloseDict(frame):
    processedDict = dict()
    for index, row in frame.iterrows():  # ChatGPT helped me learn how to iterate through a pandas data frame
        if str(row['Close'])[0] == "$":
            closeVal = float(row['Close'][1:])
        else:
            closeVal = float(row['Close'])

        processedDict[row['Date']] = closeVal

    return processedDict


def getCloseDiffDict(closeDict: dict):
    previousClosePrice = 0.0
    closeDiffDict = dict()
    for date, closePrice in closeDict.items():
        if previousClosePrice == 0.0:
            closeDiffDict[date] = 0.0
        else:
            closeDiffDict[date] = closePrice - previousClosePrice
        previousClosePrice = closePrice

    return closeDiffDict


def getHighLowDiffDict(frame):
    processedDict = dict()
    for index, row in frame.iterrows():  # ChatGPT helped me learn how to iterate through a pandas data frame
        if str(row['High'])[0] == "$" and str(row['Low'])[0] == "$":
            highVal = float(row['High'][1:])
            lowVal = float(row['Low'][1:])
        else:
            highVal = float(row['High'])
            lowVal = float(row['Low'])

        processedDict[row['Date']] = (highVal - lowVal)

    return processedDict


def part1():
    print("Running code for Q3 part 1")

    # get plotting stuff initialized
    fix, axs = plt.subplots(2, 3)

    # read in AAPL
    appleFrame = readCsv('data/AAPL.csv')
    appleCloseDict = getCloseDict(appleFrame)
    appleCloseDiffDict = getCloseDiffDict(appleCloseDict)
    appleHighLowDiffDict = getHighLowDiffDict(appleFrame)

    # note: for plotting, GitHub copilot helped me format the labels on the x axis

    # plot AAPL Close values
    axs[0, 0].plot(appleCloseDict.keys(), appleCloseDict.values())
    axs[0, 0].set_xlabel("Date")
    axs[0, 0].set_ylabel("Value ($)")
    axs[0, 0].set_title("AAPL Closing Values")
    axs[0, 0].set_xticks(
        [list(appleCloseDict.keys())[0], list(appleCloseDict.keys())[-1]])  # Set x axis to only first and last date

    # plot AAPL Close difference values
    axs[0, 1].plot(appleCloseDiffDict.keys(), appleCloseDiffDict.values())
    axs[0, 1].set_xlabel("Date")
    axs[0, 1].set_ylabel("Change in Value ($)")
    axs[0, 1].set_title("AAPL Closing Difference Values")
    axs[0, 1].set_xticks(
        [list(appleCloseDiffDict.keys())[0],
         list(appleCloseDiffDict.keys())[-1]])  # Set x axis to only first and last date

    # plot AAPL High/Low difference values. To calculate, high-low=value was used
    axs[0, 2].plot(appleHighLowDiffDict.keys(), appleHighLowDiffDict.values())
    axs[0, 2].set_xlabel("Date")
    axs[0, 2].set_ylabel("Value ($)")
    axs[0, 2].set_title("AAPL High/Low Difference")
    axs[0, 2].set_xticks([list(appleHighLowDiffDict.keys())[0],
                          list(appleHighLowDiffDict.keys())[-1]])  # Set x axis to only first and last date

    # read in TSLA
    teslaFrame = readCsv('data/TSLA.csv')
    teslaCloseDict = getCloseDict(teslaFrame)
    teslaCloseDiffDict = getCloseDiffDict(teslaCloseDict)
    teslaHighLowDiffDict = getHighLowDiffDict(teslaFrame)

    # plot TSLA Close values
    axs[1, 0].plot(teslaCloseDict.keys(), teslaCloseDict.values())
    axs[1, 0].set_xlabel("Date")
    axs[1, 0].set_ylabel("Value ($)")
    axs[1, 0].set_title("TSLA Closing Values")
    axs[1, 0].set_xticks(
        [list(teslaCloseDict.keys())[0], list(teslaCloseDict.keys())[-1]])  # Set x axis to only first and last date

    # plot AAPL Close difference values
    axs[1, 1].plot(teslaCloseDiffDict.keys(), teslaCloseDiffDict.values())
    axs[1, 1].set_xlabel("Date")
    axs[1, 1].set_ylabel("Change in Value ($)")
    axs[1, 1].set_title("TSLA Closing Difference Values")
    axs[1, 1].set_xticks(
        [list(teslaCloseDiffDict.keys())[0],
         list(teslaCloseDiffDict.keys())[-1]])  # Set x axis to only first and last date

    # plot TSLA High/Low difference values. To calculate, high-low=value was used
    axs[1, 2].plot(teslaHighLowDiffDict.keys(), teslaHighLowDiffDict.values())
    axs[1, 2].set_xlabel("Date")
    axs[1, 2].set_ylabel("Value ($)")
    axs[1, 2].set_title("TSLA High/Low Difference")
    axs[1, 2].set_xticks([list(teslaHighLowDiffDict.keys())[0],
                          list(teslaHighLowDiffDict.keys())[-1]])  # Set x axis to only first and last date

    plt.show()

    print("Q3 part 1 code finished")


# GENERAL METHODS

def main():
    part1()


if __name__ == "__main__":
    main()
