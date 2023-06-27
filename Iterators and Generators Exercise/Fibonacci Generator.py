def fibonacci():
    list = [0, 1]
    yield list[-2]
    yield list[-1]
    while True:
        yield list[-1] + list[-2]
        list.append(list[-1] + list[-2])
