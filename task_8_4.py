from functools import wraps


def val_checker(verbosity):
    def type_logger(callback):
        @wraps(callback)
        def cube(*args):
            result = callback(*args)
            types = [f'{arg}: {type(arg)}' for arg in args]
            for arg in args:
                if verbosity(arg):
                    print(f'{callback.__name__}({", ".join(types)})')
                    return result
                else:
                    raise ValueError(f'wrong value {arg}')

        return cube
    return type_logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


cube_4 = calc_cube(4)
print(cube_4)
cube_3 = calc_cube(-3)
print(cube_3)
