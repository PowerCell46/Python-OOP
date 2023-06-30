def cache(func):
    log = {}
    
    def wrapper(num):
        if num not in wrapper.log:
            wrapper.log[num] = func(num)
        return wrapper.log[num]
    
    wrapper.log = {}
    return wrapper
