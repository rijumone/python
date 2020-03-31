"""
call function with args reversed
"""

def reverse_args(func, *args):
    """
        args: function
        return: new function with reversed args
    """
    def wrapper_function(*args):
        tpl = args[::-1]
        return func(*tpl)
    
    return wrapper_function

@reverse_args
def test_foo(*args):
    print(args)

if __name__ == '__main__':
    
    test_foo('a', 'b', 'c') 