from project.no_solution_exists import NoSolutionExists


# Class is not instantiated but instead has only one purpose at this point,
# to hold the method used to lay the second layer of bricks which will be usd by it's child class
class BrickConstructor:

    # Class method which when called, starts laying second layer bricks as per the assignment example,
    # starting from left to right for upper bricks and then from right to left on the bottom ones
    # While arranging second layer layout method takes in consideration that no brick can span over 3 cols or rows
    # as per assignment rule .4
    # This method works with horizontally placed bricks from the first layer as per assignment example
    def second_layer_brick_constructor(self, area, rows, cols):

        # Variable which keeps track on current brick
        brick_counter = 0

        # Iterates over rows in first layer of bricks
        for row in range(0, rows, 2):

            # Iterating left to right on first layer of bricks
            for col in range(cols - 1, -1, -1):
                # Checks if the column number provided by the user is even
                if cols % 2 == 0:
                    # Full_brick holds the two column indexes needed to lay each new brick
                    full_brick = [col - 2, col - 1]
                    # Splits brick column indexes in two variables keeping the code cleaner
                    brick_part_one = full_brick[0]
                    brick_part_two = full_brick[1]
                    # Checks first part of brick doesn't go out of index while traversing left
                    if brick_part_one >= 0:
                        if col % 2 == 1:
                            # Adds one brick to brick counter
                            brick_counter += 1
                            # Puts brick in child class which holds area of bricks
                            area[row][brick_part_one] = brick_counter
                            area[row][brick_part_two] = brick_counter
                # No solution is possible if columns are not an even number thus raising and error
                else:
                    raise NoSolutionExists("-1 No solution exists")

            # This code part is made to be used with even count of rows only
            # It puts a vertical brick on the far LEFT side as per assignment example
            # The if statement checks if row number provided by user is even
            if row + 1 < rows:
                # Add one to brick counter
                brick_counter += 1
                # Puts vertical brick to far left side of area
                area[row][0] = brick_counter
                area[row + 1][0] = brick_counter
            # Raises an error if rows number is not even
            else:
                raise NoSolutionExists("-1 No solution exists")


            # Iterating right to left on first layer of bricks
            for col in range(cols):
                # Checks if the column number provided by the user is even
                if cols % 2 == 0:
                    # Full_brick holds the two column indexes needed to lay each new brick
                    full_brick = [col + 1, col + 2]
                    # Splits brick column indexes in two variables keeping the code cleaner
                    brick_part_one = full_brick[0]
                    brick_part_two = full_brick[1]
                    # Checks first part of brick doesn't go out of index while traversing right
                    if brick_part_two < cols:
                        if col % 2 == 0:
                            # Adds one brick to brick counter
                            brick_counter += 1
                            # Puts brick in child class which holds area of bricks
                            area[row + 1][brick_part_one] = brick_counter
                            area[row + 1][brick_part_two] = brick_counter
                # No solution is possible if columns are not an even number thus raising and error
                else:
                    raise NoSolutionExists("-1 No solution exists")

            # This code part is made to be used with even count of rows only
            # It puts a vertical brick on the far RIGHT side as per assignment example
            # The if statement checks if row number provided by user is even
            if row + 1 < rows:
                brick_counter += 1
                area[row][cols - 1] = brick_counter
                area[row + 1][cols - 1] = brick_counter
            # Raises an error if rows number is not even
            else:
                raise NoSolutionExists("-1 No solution exists")
