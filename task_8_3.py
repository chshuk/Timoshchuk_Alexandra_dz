from functools import wraps


def type_logger(callback):

    @wraps(callback)
    def cube(*args):
        result = callback(*args)
        types = [f'{arg}: {type(arg)}' for arg in args]
        print(f'{callback.__name__}({", ".join(types)})')
        return result

    return cube


@type_logger
def calc_cube(*args):
    result = (arg ** 3 for arg in args)
    return result


cube_52 = calc_cube(5, 2, 3.4)
print(*cube_52, sep=', ')
