import itertools

def solution():
    def integers():
        number = 0
        while True:
            number += 1
            yield number

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return list(itertools.islice(seq, n))
    
    return (take, halves, integers)
