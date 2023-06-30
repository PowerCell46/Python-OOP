def number_increment(numbers):
    
    def increase():
        nums = list(map(lambda x: x + 1, numbers))
        return nums

    return increase()
