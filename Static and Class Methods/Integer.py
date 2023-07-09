import math


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) != float:
            return 'value is not a float'

        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numbers_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}

        current_biggest = value[0]
        result = roman_numbers_dictionary[current_biggest]
        keeper = 0

        for index in range(1, len(value)):
            current_roman_number = value[index]

            if roman_numbers_dictionary[current_roman_number] == roman_numbers_dictionary[current_biggest]:
                if keeper > 0:
                    keeper += roman_numbers_dictionary[current_roman_number]
                else:
                    result += roman_numbers_dictionary[current_roman_number]

            elif roman_numbers_dictionary[current_roman_number] > roman_numbers_dictionary[current_biggest]:

                if roman_numbers_dictionary[current_roman_number] > result:
                    result = roman_numbers_dictionary[current_roman_number] - result

                else:
                    result += roman_numbers_dictionary[current_roman_number] - keeper
                    keeper = 0
                current_biggest = current_roman_number

            elif roman_numbers_dictionary[current_roman_number] < roman_numbers_dictionary[current_biggest]:
                there_is_not_a_bigger_number = True
                for i in range(index + 1, len(value)):
                    if roman_numbers_dictionary[value[i]] > roman_numbers_dictionary[current_roman_number]:
                        keeper += roman_numbers_dictionary[current_roman_number]
                        current_biggest = current_roman_number
                        there_is_not_a_bigger_number = False
                        break
                if there_is_not_a_bigger_number:
                    result += roman_numbers_dictionary[current_roman_number]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if float(value) != float and type(value) == str:
            value = float(value)
            return cls(int(value))
        else:
            return f'wrong type'
