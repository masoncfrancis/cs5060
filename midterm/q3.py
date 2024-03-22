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
    # get plotting stuff initialized
    fix, axs = plt.subplots(2, 2)

    # read in AAPL
    appleFrame = readCsv('data/AAPL.csv')
    appleCloseDict = getCloseDict(appleFrame)
    appleHighLowDiffDict = getHighLowDiffDict(appleFrame)

    # plot AAPL Close values
    axs[0, 0].plot(appleCloseDict.keys(), appleCloseDict.values())
    axs[0, 0].set_xlabel("Date")
    axs[0, 0].set_ylabel("Value ($)")
    axs[0, 0].set_title("AAPL Closing Values")

    # plot AAPL High/Low difference values. To calculate, high-low=value was used
    axs[0, 1].plot(appleHighLowDiffDict.keys(), appleHighLowDiffDict.values())
    axs[0, 1].set_xlabel("Date")
    axs[0, 1].set_ylabel("Value ($)")
    axs[0, 1].set_title("AAPL High/Low Difference")

    # read in TSLA
    teslaFrame = readCsv('data/TSLA.csv')
    teslaCloseDict = getCloseDict(teslaFrame)
    teslaHighLowDiffDict = getHighLowDiffDict(teslaFrame)

    # plot TSLA Close values
    axs[1, 0].plot(teslaCloseDict.keys(), teslaCloseDict.values())
    axs[1, 0].set_xlabel("Date")
    axs[1, 0].set_ylabel("Value ($)")
    axs[1, 0].set_title("TSLA Closing Values")

    # plot TSLA High/Low difference values. To calculate, high-low=value was used
    axs[1, 1].plot(teslaHighLowDiffDict.keys(), teslaHighLowDiffDict.values())
    axs[1, 1].set_xlabel("Date")
    axs[1, 1].set_ylabel("Value ($)")
    axs[1, 1].set_title("TSLA High/Low Difference")

    plt.show()


# GENERAL METHODS

def main():
    part1()


if __name__ == "__main__":
    main()
