"""from functools import reduce


def add(x, y):
    return x + y


sum = reduce(add, [i for i in range(10) if i % 2 != 0])

print(sum)


def fn1(x, y):
    return x * 10 + y


result = reduce(fn1, [1, 3, 5, 7, 9])
print(result)  # 13579"""


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)  # ['Adam', 'Lisa', 'Bart']

from functools import reduce


def prod(L):
    def multiply(x, y):
        return x * y

    return reduce(multiply, L)


print("3 * 5 * 7 * 9 =", prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print("测试成功!")
else:
    print("测试失败!")
    
    
def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(ch):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[ch]

    if '.' in s:
        integer_part, fractional_part = s.split('.')
        integer_value = reduce(fn, map(char2num, integer_part))
        fractional_value = reduce(fn, map(char2num, fractional_part)) / (10 ** len(fractional_part))
        print(integer_value, fractional_value)
        return integer_value + fractional_value
    else:
        return reduce(fn, map(char2num, s))
    

print('str2float(\'123.456\') =', str2float('123.456'))