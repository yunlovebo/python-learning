# 内置函数-range()

'''
range()函数
功能：能够生成一个指定的数字序列
参数：
    start: 开始值，可选，包含，默认值0
    stop: 结束值，不包含
    [,step]： 步长，可选，默认值1
'''
res = range(10)
# print(res, type(res)) # range(0, 10) <class 'range'>
print(list(res)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in res:
    print(i) # 依次输出0-9

# print(next(res)) # TypeError: 'range' object is not an iterator
print(next(iter(res))) # 0

# 只写一个参数就是从0开始
res1 = range(10)

# 只有一个参数且为负数
res2 = range(-10)
print(res2) # range(0, -10)

# 传入步长
res3 = range(1, 10, 2)
print(list(res3)) # [1, 3, 5, 7, 9]

res4 = range(1, 10, 3)
print(list(res4)) # [1, 4, 7]

res = range(0, 10, -1)
print(list(res)) # []

# 倒序输出
res = range(10, 0, -1)
print(list(res)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

res = range(10, 0, -2)
print(list(res)) # [10, 8, 6, 4, 2]



