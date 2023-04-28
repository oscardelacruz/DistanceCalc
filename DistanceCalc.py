import numpy as np
import pandas as pd
import seaborn as sns


def calcEuclidean(p1, p2):
    # calculating the distance
    # between two points, based on the euclidean distance
    # formula.

    d = 1
    # // todo code here
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    # formula for euclidean
    d = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return d


def calcManhattan(p1, p2):
    d = 1

    # / / todo code here
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]
    # formula for manhattan distance
    d = abs((x2 - x1) + abs(y2 - y1))

    return d


def main():
    point1 = (3, 4)  # features on a 2-dim plane
    point2 = (8, 9)  # features on a 2-dim plane

    distance = calcEuclidean(point1, point2)
    print("The Distance is = ", distance)

    # verify
    dist = np.linalg.norm(np.array((point1)) - np.array((point2)))
    print("The distance is = ", distance)

    distance = calcManhattan(point1, point2)
    print("The Distance is = ", distance)


# -  -  - main - - -
main()
