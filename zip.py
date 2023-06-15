# 内置函数zip

'''
参数：&iterables, 任意个的可迭代对象
返回值：返回一个元组的迭代器
'''

var1 = '1234'
var2 = ['a', 'b', 'c', 'd']
var3 = ('A', 'B', 'C', 'D')
# 调用zip函数，组成新的元组迭代器
res = zip(var1, var2, var3)
print(res, type(res)) # <zip object at 0x000001E3D6346900> <class 'zip'>

# 提取迭代器数据的方法：next()、list()、for循环
'''
下面的循环输出：
('1', 'a', 'A')
('2', 'b', 'B')
('3', 'c', 'C')
('4', 'd', 'D')
'''
# for i in res:
#     print(i)

# 用list的方法提取迭代器数据：
print(list(res)) # [('1', 'a', 'A'), ('2', 'b', 'B'), ('3', 'c', 'C'), ('4', 'd', 'D')]

v1 = [1,2,3,4]
v2 = [22,33,44,55]
res = zip(v1, v2)
print(list(res)) # [(1, 22), (2, 33), (3, 44), (4, 55)]


# 与*zip结合
x = [1,2,3]
y = [4,5,6]
zipped = zip(x, y)

# 拆开
print(list(zipped)) # [(1, 4), (2, 5), (3, 6)]

# 又回去了
x2, y2 = zip(*zip(x, y))
print(x2, y2) # (1, 2, 3) (4, 5, 6)


xx = [1,2,3]
yy = [4,5,6]
print(*zip(xx, yy)) # (1, 4) (2, 5) (3, 6)
