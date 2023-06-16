'''
内置高阶函数 map(func, *iterables)
功能：对传入的每个可迭代数据中的每个元素放入到函数中进行处理，返回一个新的迭代器
参数：
    func 函数 自定义函数 | 内置函数
    iterables：可迭代的数据
返回值：新的迭代器
'''

# 问题1. 把一个字符串数字的列表转为整型的数字列表

# 方法1. 使用普通方法
varlist = ['1', '2', '3', '4'] # ==> [1,2,3,4]
newlist = []
for i in varlist:
    # print(i, type(i)) # 1...5 <class 'str'>
    newlist.append(int(i))
print(newlist) # [1, 2, 3, 4]

# 方法2. 使用map函数
res = map(int, varlist)
print(list(res)) # [1, 2, 3, 4]

# 问题2. [1,2,3,4] => [1,4,9,16]
varlist = [1,2,3,4]
def mayfunc(x):
    return x ** 2
res = map(mayfunc, varlist)
print(res) # <map object at 0x000001F6D62E9E40>
print(list(res)) # [1, 4, 9, 16]

# 使用lambda
res = map(lambda x:x**2, varlist)
print(list(res)) # 1, 4, 9, 16]

# 问题3 ['a', 'b', 'c', 'd'] => [65, 66, 67, 68]
varlist = ['a', 'b', 'c', 'd']
res = map(lambda x:ord(x.upper()), varlist)
print(list(res)) # [65, 66, 67, 68]
