'''
内置高阶函数 reduce()
功能：
    每一次从 iterable 拿出两个元素，放入到func函数中进行处理，得出一个计算结果，
    然后把这个计算结果和iterable中的第三个元素，放入到func中继续运算
    得出的结果和之后的第四个元素，加入到func中继续运算，以此类推，直到最后的元素都参与了运算
参数：
    func：内置函数或自定义函数
    iterable：可迭代的数据
返回值：最终的运算处理结果
注意：使用 reduce 函数时，需要导入from functools import reduce
'''

from functools import reduce

# 问题1. [5,2,1,1] => 5211
varlist = [5, 2, 1, 1]
def myfunc(x, y):
    return x*10 + y
res = reduce(myfunc, varlist)
print(res, type(res)) # 5211 <class 'int'>

# 问题2. 把字符串的'456' ==> 456
# 要求不能使用int方法进行类型的转换
def myfunc(s):
    vardict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    return vardict[s]
iter1 = map(myfunc, '456') # [4, 5, 6]
print(list(iter1))
iter2 = reduce(lambda x,y:x*10+y, iter1, 1)
print(iter2)

