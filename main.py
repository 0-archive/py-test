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
    input = [
    [ 1,  2,  3,  4,  5],
    [14, 15, 16, 17,  6],
    [13, 20, 19, 18,  7],
    [12, 11, 10,  9,  8],
    ]

    print(solve(input))

def solve(input):
    x = 0
    y = 0
    x_lower_bound = 0
    y_lower_bound = 0
    x_upper_bound = len(input[0]) - 1
    y_upper_bound = len(input) - 1
    output = []
    length = len(input[0]) * len(input)

    # Loop until finished, going right, down, left, and up.
    while len(output) < length:
        output, x, y, y_lower_bound = move(input, output, x, y, "right", y_lower_bound, x_upper_bound, length)
        output, x, y, x_upper_bound = move(input, output, x, y, "down", x_upper_bound, y_upper_bound, length)
        output, x, y, y_upper_bound = move(input, output, x, y, "left", y_upper_bound, x_lower_bound, length)
        output, x, y, x_lower_bound = move(input, output, x, y, "up", x_lower_bound, y_lower_bound, length)
    
    return output

def move(input, output, x, y, mode, bound_to_change, bound, length):
    while True:
        # If the output is already the correct length, stop.
        if len(output) >= length:
            break
        # Else add the current digit to the output
        output.append(input[y][x])
        # Set the necessary info based on what direction we're going
        if mode == "right":
            x += 1
            axis = x
            direction = 1
        elif mode == "left":
            x -= 1
            axis = x 
            direction = -1
        elif mode == "down":
            y += 1
            axis = y
            direction = -1
        elif mode == "up":
            y -= 1
            axis = y
            direction = 1

        # If we're at the boundary, move the bound that needs to be changed
        # and then break.
        if axis == bound:
            bound_to_change += direction
            break

    return output, x, y, bound_to_change

if __name__ == "__main__":
    main()
