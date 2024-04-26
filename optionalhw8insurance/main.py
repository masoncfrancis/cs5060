import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


def main():
    # import the csv
    frame = pd.read_csv('dataset.csv')

    length = len(frame)

    # plot values

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

    # Develop linear regresion models


if __name__ == "__main__":
    main()
