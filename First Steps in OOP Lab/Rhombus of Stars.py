def rhombus_of_stars(side_of_the_rhombus):
    result_list = []
    middle_row = []

    for i in range(side_of_the_rhombus * 2 - 1):
        if i % 2 == 0:
            middle_row.append("*")
        else:
            middle_row.append(" ")
    result_list.append(middle_row)
    # Creating the middle row with a for cycle

    left_index = 0
    right_index = len(middle_row) - 1
    while left_index != right_index:
        new_list = []
        for index in range(0, len(middle_row)):
            if index < left_index or index > right_index:
                new_list.append(middle_row[index])
            elif left_index <= index <= right_index:
                if middle_row[index] == "*":
                    new_list.append(" ")
                else:
                    new_list.append("*")
        left_index += 1
        right_index -= 1
        middle_row = new_list  # We create every new row and append it to the result list
        result_list.append(middle_row)

    for i in range(len(result_list) - 1, 0, -1):
        print("".join(result_list[i]))  # We print the upper side of the figure

    for el in result_list:
        print("".join(el))  # We print the lower side of the figure


rhombus_of_stars(int(input()))
