import matplotlib.pyplot as plt
import numpy as np


def getMineralValue(areaNum: int):
    # Giving credit where credit is due:
    # I designed this function myself, but I had GitHub Copilot help me write the code
    # faster than it would take to type it out. So it is my own work, but completed faster
    # using GitHub Copilot.

    if areaNum == 1:
        return np.random.beta(2, 2) + 1
    elif areaNum == 2:
        return np.random.beta(3, 7) * 3
    elif areaNum == 3:
        return np.random.normal(2.4, 1.8)
    elif areaNum == 4:
        return np.random.uniform(-1, 4)
    elif areaNum == 5:
        return np.random.normal(0, 9)
    elif areaNum == 6:
        return np.random.beta(7, 3) + 2
    elif areaNum == 7:
        return np.random.uniform(0, 4)
    elif areaNum == 8:
        return np.random.beta(3, 7) * 2
    elif areaNum == 9:
        return np.random.normal(2, 1.4)
    elif areaNum == 10:
        return np.random.normal(1.3, 7)


# PART 1 METHODS

def part1():
    pass


def main():
    part1()


if __name__ == "__main__":
    main()
