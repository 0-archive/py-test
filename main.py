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
    output=[]

    location = input[0][0]
    x = 0
    y = 0
    len_x = len(input[0])
    len_y = len(input)
    direction = "right"
    
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



    print(output)
    print(x)
    print(y)

if __name__ == "__main__":
    main()
