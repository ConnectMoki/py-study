def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


foo = calc_sum(1, 2, 3, 4)

print(foo)  # 10


""" def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


f = inc()
print(f())  # 1
print(f())  # 2 """


def createCounter():
    n = 0

    def counter():
        nonlocal n
        n = n + 1
        return n

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print("测试通过!")
else:
    print("测试失败!")
