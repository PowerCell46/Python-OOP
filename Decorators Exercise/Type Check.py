def type_check(searched_type):
    def something(func):
        def wrapper(argument):
            if type(argument) == searched_type:
                return func(argument)
            else:
                return f'Bad Type'
        return wrapper
    return something
