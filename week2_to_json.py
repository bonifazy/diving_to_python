from functools import wraps
from json import dumps


def to_json(func):
    @wraps(func)  # Не забудьте про сохранение корректного имени декорируемой функции.
    def wrapped(*args, **qwargs):
        return dumps(func(*args, **qwargs))  # convert args to json
    return wrapped  # loopback


@to_json
def get_arg():
    return 3.14


@to_json
def get_list():
    return ['one', 'two', 'three']


@to_json
def get_all():
    return [1, 2, 3], {4: 'four', 5: 'five'}


if __name__ == "__main__":
    print(get_arg(), get_list(), get_all())
    # 3.14 ["one", "two", "three"] [[1, 2, 3], {"4": "four", "5": "five"}]
