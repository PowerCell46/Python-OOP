def even_numbers(function):

    def wrapper(numbers): # TODO: Implement
        return list(filter(lambda x: x % 2 == 0, numbers))

    return wrapper
