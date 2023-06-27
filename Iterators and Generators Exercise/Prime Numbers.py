def get_primes(list):
    for number in list:
        prime = True
        for divider in range(2, number - 1):
            if number % divider == 0:
                prime = False
                break
        if prime and number > 1:
            yield number
