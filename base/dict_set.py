# dict也称为map
# dict是用空间来换取时间的一种方法
# dict有以下几个特点：
# 1.查找和插入的速度极快，不会随着key的增加而变慢；
# 2.需要占用大量的内存，内存浪费多



# set和dict类似，也是一组key的集合，但不存储value。
# s = set([1, 2, 3]) ===> s = {1, 2, 3}
# 重复元素在set中自动被过滤
# s = {1, 1, 2, 2, 3, 3} ===> s = {1, 2, 3}

t = (1,2,3)
d = {t: 'a tuple as key'}
s = {t}
print(d)
print(s)

# t1 = (1,2,[3,4])
# d1 = {t1: 'a list as key'}
# s1 = {t1}
# print(d1) # TypeError: unhashable type: 'list'
# print(s1) # TypeError: unhashable type: 'list'


t2 = (1,)
d2 = {t2: 'a tuple with one element as key'}
s2 = {t2}
print(d2)
print(s2)
