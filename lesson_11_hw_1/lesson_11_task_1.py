from functools import wraps


class Error(Exception):
    pass


class UnexpectedTypeException(Error):
    pass


def expected(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        argtypes = (int, str)
        if type(func) in argtypes:
            func(*args, **kwargs)
        else:
            try:
                argtypes = (int, str)
                if type(func) not in list(argtypes):
                    raise UnexpectedTypeException
            except UnexpectedTypeException:
                print('Was expecting types: str, ing')
    return wrapper


@expected
def add(value):
    return value


print(add(2))
