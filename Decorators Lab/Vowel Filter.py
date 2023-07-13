def vowel_filter(function):
    def wrapper():
        input_list = function()
        vowels = ["a", "o", "e", "y", "u", "i"]
        result = list(filter(lambda x: x.lower() in vowels, input_list))
        return result

    return wrapper
