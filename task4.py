def author(name='unknown user'):
    def decorator(func):
        def new_func(*args, **kwargs):
            new_func._author = name
            return func(*args, **kwargs)

        return new_func

    return decorator

@author('sfdsdf')
def add2(num: int) -> int:
    return num+2

print(add2(0))
print(add2._author)