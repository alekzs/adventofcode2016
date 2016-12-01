def solve(input):
    directions = [0, 1, 2, 3] # 0 - North, 1 - East, 2 - South, 3 - West
    currentDirection = 0
    path = {0: 0, 1: 0, 2: 0, 3: 0}
    steps = input.split(", ")
    for step in steps:
        turnDirection = step[0]
        turnDistance = int(step[1:])
        if turnDirection == "R":
            currentDirection += 1
        else:
            currentDirection -= 1
        directionKey = directions[currentDirection % 4]
        path[directionKey] += turnDistance

    # Calculate the total distance by cancelling out the opposite directions
    totalDistance = abs(path[0] - path[2]) + abs(path[1] - path[3])
    print "DONE", totalDistance

input = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5"

solve(input)
