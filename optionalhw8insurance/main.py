import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def makePlots(frame):
    premium = frame["Monthly.Premium.Auto"]

    claimAmount = frame["Total.Claim.Amount"]
    plt.plot(claimAmount.tolist(), premium.tolist(), linestyle='None', marker='o', label="Men")
    plt.title("Claim Amounts vs. Premiums")
    plt.xlabel("Claim Amount")
    plt.ylabel("Monthly Premium")
    plt.show()

    complaints = frame["Number.of.Open.Complaints"]
    plt.plot(complaints.tolist(), premium.tolist(), linestyle='None', marker='o', label="Men")
    plt.title("Complaints vs. Premiums")
    plt.xlabel("Open Complaints")
    plt.ylabel("Monthly Premium")
    plt.show()

    sns.scatterplot(x="Vehicle.Class", y="Monthly.Premium.Auto", data=frame)
    plt.title("Premiums by Vehicle Class")
    plt.xlabel("Vehicle Class")
    plt.ylabel("Monthly Premium")
    plt.show()

    sns.scatterplot(x="Coverage", y="Monthly.Premium.Auto", data=frame)
    plt.title("Premiums by Coverage")
    plt.xlabel("Coverage")
    plt.ylabel("Monthly Premium")
    plt.show()

    sns.scatterplot(x="Education", y="Monthly.Premium.Auto", data=frame)
    plt.title("Premiums by Education Level")
    plt.xlabel("Education Level")
    plt.ylabel("Monthly Premium")
    plt.show()

    sns.scatterplot(x="EmploymentStatus", y="Monthly.Premium.Auto", data=frame)
    plt.title("Premiums by Employment Status")
    plt.xlabel("Employment Status")
    plt.ylabel("Monthly Premium")
    plt.show()


def getFrame():
    return pd.read_csv('dataset.csv')


def createModel(frame):
    # I received help on this part on how to use SciKit-Learn to make a model
    # using the Phind search engine

    x = frame[['Total.Claim.Amount', 'Vehicle.Class', 'Coverage', 'Education', 'EmploymentStatus']]
    y = frame['Monthly.Premium.Auto']

    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2)


def main():
    frame = getFrame()
    makePlots(frame)
    createModel(frame)


if __name__ == "__main__":
    main()
