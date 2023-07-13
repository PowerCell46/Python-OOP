def multiply(times):
    def decorator(function): # TODO: Implement
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return times * result
        return wrapper
    return decorator
