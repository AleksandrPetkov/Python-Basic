from functools import wraps


class UnexpectedTypeException(Exception):
    pass


def expected(*expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if not isinstance(func_result, expected_types):
                raise UnexpectedTypeException(f'Was expecting types: {expected_types}')
            else:
                print(func(*args, **kwargs))
        return wrapper
    return decorator


@expected(int, str)
def my_func(value):
    return value


my_func(2.5)  #error


