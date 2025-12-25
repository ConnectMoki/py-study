from abstest import my_abs

# print(my_abs('a'))
# print(abs('a'))


# pass
def nop():
    pass


age = 20
if age >= 18:
    pass

# 返回多个值

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)

r = move(100, 100, 60, math.pi / 6)

print(x, y)
print(r)  # r是一个tuple

#

import math


def quadratic(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2


print("quadratic(2, 3, 1) =", quadratic(2, 3, 1))
print("quadratic(1, 3, -4) =", quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print("测试失败")
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print("测试失败")
else:
    print("测试成功")

# 函数的参数


def power(x, n=2):
    return x**n


print(power(5, 3))
print(power(5))


def enroll(name, gender, age=6, city="Beijing"):
    print("name:", name)
    print("gender:", gender)
    print("age:", age)
    print("city:", city)


enroll("Sarah", "F")
enroll("Bob", "M", 7)
enroll("Adam", "M", city="Tianjin")


# 默认参数有坑


def add_end(L=[]):
    L.append("END")
    return L


print(add_end([1, 2, 3]))

print(add_end(["x", "y", "z"]))

print(add_end())  # 第一次调用， ['END']
print(add_end())  # 第二次调用， ['END', 'END']

# Python函数在定义的时候，默认参数L的值就被计算出来了，
# 即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。


def add_end(L=None):
    if L is None:
        L = []
    L.append("END")
    return L


print(add_end())
print(add_end())


# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))


def calc(*numbers):
    print(numbers)  # numbers接收的是一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
nums = [1, 2, 3]
print(calc(*nums))  # *nums表示把nums这个list的所有元素作为可变参数传进去


# 关键字参数
def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


person("Michael", 30)
person("Bob", 35, city="Beijing")
person("Adam", 45, gender="M", job="Engineer")

extra = {"city": "Beijing", "job": "Engineer"}
person("Jack", 24, city=extra["city"], job=extra["job"])
person("Jack", 24, **extra)


# 命名关键字参数
def person(name, age, **kw):
    if "city" in kw:
        # 有city参数
        pass
    if "job" in kw:
        # 有job参数
        pass
    print("name:", name, "age:", age, "other:", kw)


person("Jack", 24, city="Beijing", addr="Chaoyang", zipcode=123456)


def person(name, age, *, city, job):
    print(name, age, city, job)


person("Jack", 24, city="Beijing", job="Engineer")


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# person('Jack', 24, 'Beijing','Engineer') 这个会报错
person("Jack", 24, city="Beijing", job="Engineer")


def person(name, age, *, city="Beijing", job):
    print(name, age, city, job)


person("Jack", 24, job="Engineer")


def f1(a, b, c=0, *args, **kw):
    print("a =", a, "b =", b, "c =", c, "args =", args, "kw =", kw)


def f2(a, b, c=0, *, d, **kw):
    print("a =", a, "b =", b, "c =", c, "d =", d, "kw =", kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, "a", "b")
f1(1, 2, 3, "a", "b", x=99)

f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {"d": 99, "x": "#"}

f1(*args, **kw)

args = (1, 2, 3)
kw = {"d": 88, "x": "#"}
f2(*args, **kw)


def mul(x, *y):
    result = x
    print(y)
    for i in y:
        result = result * i
    return result


print("mul(5) =", mul(5))
print("mul(5, 6) =", mul(5, 6))
print("mul(5, 6, 7) =", mul(5, 6, 7))
print("mul(5, 6, 7, 9) =", mul(5, 6, 7, 9))

if mul(5) != 5:
    print("mul(5)测试失败!")
elif mul(5, 6) != 30:
    print("mul(5, 6)测试失败!")
elif mul(5, 6, 7) != 210:
    print("mul(5, 6, 7)测试失败!")
elif mul(5, 6, 7, 9) != 1890:
    print("mul(5, 6, 7, 9)测试失败!")
else:
    try:
        mul()
        print("mul()测试失败!")
    except TypeError:
        print("测试成功!")
