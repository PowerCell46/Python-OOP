def tags(html_tag):
    def innerFunc(func):
        def wrapper(*args):
            return f'<{html_tag}>{func(*args)}</{html_tag}>'
        return wrapper
    return innerFunc
