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
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
    ]

    output = solve(input)
    print(output)

def solve(input):
    x = 0
    y = 0
    x_lower_bound = 0
    y_lower_bound = 0
    x_upper_bound = len(input[0]) - 1
    y_upper_bound = len(input) - 1
    output = []

    for i in range(20):
        output, x, y, y_lower_bound = move(input, output, x, y, "right", y_lower_bound, x_upper_bound)
        output, x, y, x_upper_bound = move(input, output, x, y, "down", x_upper_bound, y_upper_bound)
        output, x, y, y_upper_bound = move(input, output, x, y, "left", y_upper_bound, x_lower_bound)
        output, x, y, x_lower_bound = move(input, output, x, y, "up", x_lower_bound, y_lower_bound)
    
    return output

def move(input, output, x, y, mode, bound_to_change, bound):
    while True:
        output.append(input[y][x])
        print(output)
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

        if axis == bound:
            print("turning")
            bound_to_change += direction
            break

    return output, x, y, bound_to_change
    

    """
    def move(axis, other_axis, direction, turning_point):
        output.append(input[y][x])
        print(output)
        axis += direction
        if axis == turning_point:
            turning_point -= direction
            return False
        return True

    x = 0
    y = 0
    x_bounds = [0, len(input[0]) -1]
    y_bounds = [0, len(input) -1]
    keep_looping = True

    #while keep_looping:
    for i in range(20):
        keep_looping = move(x, y, 1, x_bounds[1])
        keep_looping = move(y, x, 1, y_bounds[1])
        keep_looping = move(x, y, -1, x_bounds[0])
        keep_looping = move(y, x, -1, y_bounds[0])

    print(output)
    

    
    while True:
        # move in x axis
        while True:
            print("x")
            output.append(input[y][x])
            print(output)
            x += direction
            if x in x_bounds:
                print("turning x")
                if direction == 1:
                    y_bounds[0] += direction
                if direction == -1:
                    y_bounds[1] += direction
                break
        while True: 
            print("y")
            output.append(input[y][x])
            print(output) 
            y += direction
            if y in y_bounds:
                print("y is: " + str(y))
                print("turning y")
                if direction == 1:
                    x_bounds[1] -= direction
                if direction == -1:
                    x_bounds[0] -= direction
                break
    """

def old_main():
    input = [
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
    ]
    output=[]

    x = 0
    y = 0
    len_x = len(input[0])
    len_y = len(input)
    wraps = 0
    direction = 1
    stop = False
    """    
    for i in input[y]:
        output.append(i)
        x = input[y].index(i)

    y += 1

    for i in input[y:]:
        output.append(i[x])
        y = input.index(i)
    
    x -= 1

    for i in input[y][x::-1]:
        output.append(i)
        x = input[y].index(i)

    y -= 1

    for i in input[y:0:-1]:
        output.append(i[x])
        y = input.index(i)

    x += 1
    """
    for i in range(10):
        for j in range(2):
            output, x, y, direction, wraps, stop = move_x(input, output, x, y, direction, wraps)
            if stop:
                break
            output, x, y, direction, wraps, stop = move_y(input, output, x, y, direction, wraps)
            if stop:
                break
        #wraps += 1

    print(output)
    print(x)
    print(y)

def move_x(input, output, x, y, direction, wraps):
    end = ((len(input[y]) - (wraps * (- direction))) * direction) + direction
    input_slice = input[y][x:end:direction]
    print(input_slice)

    if len(input_slice) == 0:
        print("done")
        return (output, x, y, direction, wraps, True)

    for i in input_slice:
        output.append(i)
        x = input[y].index(i)

    y += direction
    return (output, x, y, direction, wraps, False)

def move_y(input, output, x, y, direction, wraps):
    if direction == -1:
        wraps += 1
    end = ((len(input) - (wraps * (- direction))) * direction) + direction
    print(end)
    input_slice = input[y:end:direction]
    print(input_slice)

    if len(input_slice) == 0: 
        print("done")
        return (output, x, y, direction, wraps, True)

    for i in input_slice:
        output.append(i[x])
        y = input.index(i)

    x -= direction
    direction = (- direction)

    return (output, x, y, direction, wraps, False)

if __name__ == "__main__":
    main()
