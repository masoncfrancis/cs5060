import pandas as pd
import random
import matplotlib.pyplot as plt


def findStop(numbers: list, outputFileName: str, learnOptimal: bool):
    # The code in this function is a modified version of the code provided in the class example
    len_candidates = 100
    solution_found_count = {}
    optimal_solution_found_count = {}
    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(0, 999):
        candidates = random.sample(numbers, len_candidates)
        optimal_candidate = max(candidates)

        for i in range(1, len_candidates):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    solution_found_count[str(i)] += 1
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i)] += 1
                    
                    break

    plt.figure(figsize=(30, 6))  # Adjust the size as needed

    x, y = zip(*optimal_solution_found_count.items())

    plt.plot(x,y)
    # plt.show()
    plt.savefig(outputFileName, bbox_inches='tight')
    print("Graph file saved as " + outputFileName)
    
    if learnOptimal:
        maxKey = str(max(optimal_solution_found_count, key=optimal_solution_found_count.get))
        return {maxKey: optimal_solution_found_count[maxKey]}
    else:
        return {'37': optimal_solution_found_count['37']}
    

def problem1(fileName: str):
    print("\nExecuting problem 1 code for " + fileName)
    s1FileContents = pd.read_csv('scenario1.csv').iloc[:,0].astype(float).tolist()
    s1Result37 = findStop(s1FileContents, fileName + '-37.png', False)
    s1ResultOptimalFound = findStop(s1FileContents, fileName + '-optimal.png', True)
    print("Optimal Solution Found Count at 37%: " + str(s1Result37['37']))
    computedPercent = list(s1ResultOptimalFound)[0]
    print("Optimal Stopping Point found at " + computedPercent +  "%. Count: " + str(s1ResultOptimalFound[computedPercent]))
    

def problem2():
    pass


if __name__ == "__main__":

    # Problem 1
    print("Executing algorithm for problem 1")
    problem1('scenario1.csv')
    problem1('scenario2.csv')

    # Problem 2
    print("Executing algorithm for problem 2")

