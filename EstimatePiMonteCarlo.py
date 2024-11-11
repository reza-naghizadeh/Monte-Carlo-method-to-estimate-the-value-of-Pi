import random
import math


# Generating the points and finding if they are inside the circle or no
def checkPoint(square, circle):
    # Amount of point that we generate
    iteration = int(1e11)
    # Inside circle and square point counters
    insideCircle = 0
    insideSquare = 0
    # For loop to generate point and find distance
    for i in range(0, iteration):
        x = random.uniform(square[0], square[1])
        y = random.uniform(square[0], square[1])
        # Distance finder
        point = math.sqrt((x ** 2) + (y ** 2))
        # counter // checking with distance
        if point <= circle:
            insideCircle += 1
        insideSquare += 1

    return insideSquare, insideCircle


# Compute the pi value
def pi(insideSquare, insideCircle):
    # because we compute the quarter of circle the formula looks like this
    piScore = 4 * (insideCircle / insideSquare)

    return piScore


if __name__ == '__main__':
    # Setting the square and circle
    square = [0, 10]
    # Circle radius
    circle = 10

    # Generate the points and check if they are inside the circle or no
    insideSquare, insideCircle = checkPoint(square, circle)

    # Compute the pi
    piScore = pi(insideSquare, insideCircle)

    print(f"The score estimated for pi = {piScore}")

