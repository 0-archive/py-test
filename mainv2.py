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
    output = []
    dist_x = len(input[0]) - 1
    dist_y = len(input) - 1
    x = 0
    y = 0
    direction = 1
    length = len(input[0]) * len(input)

    while True:
        for i in range(2):
            for j in range(dist_x):
                output.append(input[y][x])
                x += direction
            for j in range(dist_y):
                output.append(input[y][x])
                y += direction
            direction = - direction
        dist_x -= 2
        dist_y -= 2
        y += direction
        x += direction
        if dist_x <= 0 and dist_y <= 0:
            break

    return output

if __name__ == "__main__":
    main()
