import pandas as pd
import random
import matplotlib.pyplot as plt

# The code in this function is a modified version of the code provided in the class example
def findStop(numbers: list, outputFileName: str, learnOptimal: bool):
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
    

def problem1():
    print("Executing code for scenario1.csv")
    s1FileContents = pd.read_csv('scenario1.csv').iloc[:,0].astype(float).tolist()
    findStop(s1FileContents, 'scenario1.png', False)
    

if __name__ == "__main__":
    print("Executing algorithm for problem 1\n")
    problem1()
