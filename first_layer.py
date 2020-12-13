from project.brick_constructor import BrickConstructor


# First layer class inherit another class which takes care of the second layer of brick
# First layer class will be responsible for creating the first layer of bricks and
# printing a string representation of the second layer in the console
class FirstLayer(BrickConstructor):
    # FirstLayer object is created taking r-'row' and c-'col' from user input as instance attributes
    def __init__(self, r, c):
        self.r = int(r)
        self.c = int(c)
        self.area = []
        # A two dimensional list is created from user input to represent first layer of bricks
        for _ in range(r):
            first_layer_bricks = input().split()
            # Loop that wil check if any brick from first layer span over 3 spaces
            for i, n in enumerate(first_layer_bricks):
                if i + 2 < self.c:
                    three_space_brick = first_layer_bricks[i] + first_layer_bricks[i + 1] + first_layer_bricks[i + 2]
                    if n * 3 == three_space_brick:
                        print("Bricks can't span over 3 spaces!")
                        exit()
            self.area.append(first_layer_bricks)

    # Class method which when called returns string representation of the area as per assignment rule .6
    def return_second_layer(self):
        # variable that counts each whole horizontal brick
        whole_brick_counter = 0
        # This bool will allow the program to place astrix accordingly since we wil be adding the
        # astrix symbols in to the two dimensional list
        placed_astrix = False
        # This code part will begin adding the astrix symbols under each horizontal and vertical brick
        for i_r, row in enumerate(self.area):
            for i_c, col in enumerate(row):
                # Since we are iterating through through two dimensional list and are adding symbols to
                # it we expect the length of it to grow, to compensate that a check is made so we don't get
                # "* *" between two whole bricks
                if placed_astrix:
                    placed_astrix = False
                    continue
                # From here up to line 59 all the astrix symbols will be added with in the two dimensional list
                if i_c + 1 < len(self.area[i_r]):
                    # part_one_c and part_two_c will represent the two parts of each brick
                    # this will let the program detect a whole brick and place the astrix symbols on each side
                    # or on one side only depending on where the brick is placed
                    part_one_c = str(self.area[i_r][i_c])
                    part_two_c = str(self.area[i_r][i_c + 1])
                    if part_one_c == part_two_c:
                        whole_brick_counter += 1
                        # If validation is passed a brick will be surounded by '*'
                        if i_c - 1 >= 0 and i_c + 2 < len(self.area[i_r]):
                            if self.area[i_r][i_c + 2] != '*':
                                self.area[i_r].insert(i_c + 2, '*')
                            if self.area[i_r][i_c - 1] != '*':
                                self.area[i_r].insert(i_c, '*')
                                placed_astrix = True
                        # If validation is passed '*' will be placed on right side of brick
                        elif i_c - 1 < 0 and i_c + 2 < len(self.area[i_r]):
                            if self.area[i_r][i_c + 2] != '*':
                                self.area[i_r].insert(i_c + 3, '*')
                                placed_astrix = True
                        # If validation is passed '*' will be placed on left side of brick
                        elif i_c - 1 >= 0 and i_c + 2 >= len(self.area[i_r]):
                            if self.area[i_r][i_c - 1] != '*':
                                self.area[i_r].insert(i_c, '*')

        # This code chunk will add the '*' outside of the two dimensional list in order to fully wrap each
        # brick with '*' as per .6 in assignment
        # Result variable will gather the whole string representation of the second layer
        result = f" {'* ' * self.c}\n"
        # Counter will be used to determine when to place a single' *' and when '  *"
        counter = 0
        # Whole_brick_counter will be used to place multiple '  *' to fully surround the bricks
        whole_brick_counter //= 2
        if self.r >= 4:
            whole_brick_counter //= 2
        whole_brick_counter -= 1
        # Program will iterate through the two dimensional list starting to place '*' symbols
        for i_li, line in enumerate(self.area):
            counter += 1

            for i_ch, ch in enumerate(line):
                if i_ch == 0:
                    result += '*'

                # Adds spaces between horizontal bricks
                result += str(ch)
                if i_ch == len(line) - 1:
                    result += '*'
                if i_ch + 1 < len(line):
                    ch_one = line[i_ch]
                    ch_two = line[i_ch + 1]
                    if ch_one == ch_two:
                        result += ' '

            if counter % 2 == 1:
                if self.c != 4:
                    result += f"\n   * *"
                    result += f"{' * *' * whole_brick_counter}\n"
                else:
                    result += f"\n   * *\n"
            elif counter % 2 == 0:
                result += f"\n {'* ' * self.c}\n"
        result += "\n"

        return result
