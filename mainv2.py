""" Objective: Traverse a matrix of integers in a spiral pattern and append the integers to a 1-dimensional array in order.
Example:
    input = [
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
    ]
    output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] """

def main():
    input_1 = [
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
    ]

    input_2 = [
    [ 1,  2,  3,  4,  5],
    [14, 15, 16, 17,  6],
    [13, 20, 19, 18,  7],
    [12, 11, 10,  9,  8],
    ]

    input_3 = [
    [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
    [22, 23, 24, 25, 26, 27, 28, 29, 30, 11],
    [21, 20, 19, 18, 17, 16, 15, 14, 13, 12], 
    ]
    
    input_4 = [
    [ 1, 2],
    [ 4, 3]
    ]

    print(solve(input_1))

def solve(input):
    output = []
    dist_x = len(input[0]) - 1
    dist_y = len(input) - 1
    x = 0
    y = 0
    direction = 1
    length = len(input[0]) * len(input)

    # We loop until we return
    while True:
        # We move around the spiral:
        for i in range(2):
            # X axis
            for j in range(dist_x):
                # Check to see if we're done
                if len(output) >= length:
                    return output
                output.append(input[y][x])
                x += direction
            # Y axis
            for j in range(dist_y):
                # Check to see if we're done
                if len(output) >= length:
                    return output
                output.append(input[y][x])
                y += direction
            # Swap the direction for the next loop
            direction = - direction
        # Check to see if we're done
        if len(output) >= length:
            return output
        # After each loop, the distance must go down by 2.
        dist_x -= 2
        dist_y -= 2
        # This moves us into the correct position for the start of the next loop.
        y += direction
        x += direction

if __name__ == "__main__":
    main()
