import __name__equals__main__
def fact(n):
    '''
        Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods. It’s specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, the docstring should describe what the function does, not how.
        Example of doc string.
        The function accepts a num and return its factorial.
    '''
    if (n == 1): 
        return 1
    return n * fact(n-1)

print(fact(900))