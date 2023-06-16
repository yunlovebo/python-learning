'''
内置高阶函数 sorted()
运行原理：把可迭代数据里面的元素，一个一个的拿出来，放到key这个函数中进行处理，并按照函数中return的结果进行排序，返回一个新的列表
功能：排序
参数：
    iterable 可迭代的数据
    reverse  可选，是否反转，默认为False=不反转
    key      可选，函数，可以是自定义函数，也可以是内置函数
返回值：排序后的结果
'''

arr = [3, 7, 1, -9, 20, 10]

# 不传默认值，从小到大排列
res = sorted(arr) # [-9, 1, 3, 7, 10, 20]
print(res)
print(arr) # 不改变原数组

res1 = sorted(arr, reverse=True) # [20, 10, 7, 3, 1, -9]
print(res1)

# key使用内置函数
res2 = sorted(arr, key=abs) # [1, 3, 7, -9, 10, 20]
print(res2)

# 使用自定义函数
arr1 = [3,2,4,6,5,7,9]
def func(num):
    '''
    按照return的结果从小到大排序
    3 1
    2 0
    4 0
    6 0
    5 1
    7 1
    9 1
    '''
    print(num, num % 2)
    return num % 2
res3 = sorted(arr1, key=func) # [2, 4, 6, 3, 5, 7, 9]
print(res3)

# 自定义key函数使用lambda表达式
res4 = sorted(arr1, key=lambda x:x%2) # [2, 4, 6, 3, 5, 7, 9]
print(res4)


