'''
语法：
lambda [参数列表]:返回值
'''

# 封装一个函数做加法运算
# 1. 普通函数
def add(x, y):
    return x + y

print(add(2, 3))

# 2. 用lambda表达式来封装
res = lambda x, y: x + y
print(res(1, 2))

# lambda是一个表达式，因此不能写太复杂的逻辑，功能相对单一

# 1. 普通函数使用分支结构：
def func(gender):
    if gender == 'male':
        return '1'
    else:
        return '2'
    
print(func('male'))

# 2. lambda表达式使用分支结构：
# lambda 参数列表: 真区间 if 表达式判断 else 假区间
res1 = lambda gender: '1' if gender == 'male' else '2'

print(res1('female'))
