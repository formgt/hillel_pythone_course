def pow(x):
    return x**2


def some_gen_creator(begin, end, func):
    def inner_gen():
        current = begin
        for _ in range(end):
            yield current
            current = func(current)

    return inner_gen


my_gen_func = some_gen_creator(2, 4, pow)
gen = my_gen_func()
print(list(gen))
