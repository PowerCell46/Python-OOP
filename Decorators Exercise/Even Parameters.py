def even_parameters(func):
    def wrapper(*args):
        try:
            even_numbers = list(filter(lambda x: x % 2 == 0, args))
        except TypeError:
            even_numbers = []
        # print(even_numbers)
        if len(even_numbers) == len(args):
            return func(*args)
        else:
            return 'Please use only even numbers!'
    return wrapper
