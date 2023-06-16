'''
filter(func, iterable)
功能：过滤数据，把 iterable 中的每个元素拿到func中进行处理，如果返回True则保留，否则丢弃
参数：
    func 自定义函数
    iterable：可迭代的数据
返回：保留下来的数据组成的迭代器
'''

# 保留所有的偶数，丢弃所有的奇数
varlist = [1,2,3,4,5,6,7,8,9]

def myfunc(n):
    if n % 2 == 0:
        return True
    else:
        return False
it = filter(myfunc, varlist)
print(it, list(it)) # <filter object at 0x000002B0EA169840> [2, 4, 6, 8]

# 用lambda
it1 = filter(lambda n:True if n % 2 == 0 else False, varlist)
print(it1, list(it1)) # <filter object at 0x000001E6EDCE9DE0> [2, 4, 6, 8]
