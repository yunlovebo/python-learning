# 迭代器

# range()  返回一个可迭代的对象，左闭右开
# rang(10) -> 0-9
# range(2, 10) -> 2-9
# range(10. 3, -1) -> 10->4

# arr = ['a', 'b', 1, 2, 3, 4, 5]
# for i in arr:
#     print(i)

# 循环次数过多时，应使用迭代器
# for i in range(1, 100000000000):
#     print(i)

# iter() 把可迭代的对象，转为一个迭代器对象

f4 = ['赵四', '刘能', '小沈阳', '宋小宝']

# 遍历方式：

# 1. for循环
# for i in f4:
#     print(i)

# 2. 把可迭代对象转为迭代器对象
res = iter(f4)
# print(res, type(res)) # <list_iterator object at 0x000001C71EEE9A20> <class 'list_iterator'>

# 迭代器取值方案

# 1. 使用next()函数去调用迭代器对象
r = next(res)
print(r) # 赵四

print(next(res)) # 刘能
print(next(res)) # 小沈阳
print(next(res)) # 宋小宝
# print(next(res)) # StopIteration，数据取完了

# 2. 使用list取值
f4_1 = ['赵四', '刘能', '小沈阳', '宋小宝']
res1 = iter(f4_1)
r1 = list(res1)
print(r1) # ['赵四', '刘能', '小沈阳', '宋小宝']

# 3. 使用for循环
f4_2 = ['赵四', '刘能', '小沈阳', '宋小宝']
res2 = iter(f4_2)

# 赵四
# 刘能
# 小沈阳
# 宋小宝
for i in res2:
    print(i)
# print(next(res2)) # StopIteration，上面的for循环已经取完迭代器里的值，导致这里报错


# 检测迭代器和可迭代对象的方法
from collections.abc import Iterator, Iterable

varstr = '123456'
res = iter(varstr)


# type() 函数返回当前数据的类型
# isinstance() 检测一个数据是不是一个指定的类型
r1 = isinstance(varstr, Iterable) # True
r2 = isinstance(varstr, Iterator) # False
r3 = isinstance(res, Iterable) # True
r4 = isinstance(res, Iterator) # True
print(r1, r2, r3, r4)

