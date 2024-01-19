import pandas as pd

def problem1():
    fileContents = pd.read_csv('scenario1.csv')
    print(fileContents)

if __name__ == "__main__":
    print("Executing algorithm for problem 1\n")
    problem1()
