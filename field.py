from project.first_layer import FirstLayer


class Field:
    # R0w_input wee take the user input
    row_col = list(map(int, input().split()))
    # User input will be split between rows and cols to be used in building the area of bricks
    rows = row_col[0]
    cols = row_col[1]
    # First layer object is created
    f = FirstLayer(rows, cols)

    # If user input is equal to more than 100 total bricks program will end as per .4 in assignment rules
    if rows > 10 or cols > 10:
        exit()
    else:
        # Calling second layer brick building method
        f.second_layer_brick_constructor(f.area, f.r, f.c)
        # Printing string representation of second layer if one is found
        print(f.return_second_layer())
