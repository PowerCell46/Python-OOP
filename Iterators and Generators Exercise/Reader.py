def read_next(*args):
    for el in args:
        for item in el:
            yield item
