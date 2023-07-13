def reverse_text(string):
    for index in range(len(string) - 1, -1, -1):
        yield string[index]
