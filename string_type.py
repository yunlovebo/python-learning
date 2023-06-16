# 转义字符
# \ 转义符、续行符

# \ 作为续行符的情况：
vars = '123' \
       '456'

print(vars) # 123456

# \ 作为转义符的情况：\n
vars = 'stay hungry, \n\nstay foolish'
print(vars)

# \r 光标位置
vars1 = 'stay hungry, \rstay foolish'
print(vars1) # stay foolish

# \t tabel键缩进
vars2 = 'stay hungry, \tstay foolish'
print(vars2) # stay hungry,    stay foolish

# \b 退格符
vars3 = 'stay hungry,\b\bstay foolish'
print(vars3) # stay hungrstay foolish

# \\ 反转义
vars4 = 'stay hungry,\\n stay foolish'
print(vars4) # stay hungry,\n stay foolish

# 想原样输出，而不是输出转义字符
vars5 = r'stay hungry, \tstay foolish'
print(vars5) # stay hungry, \tstay foolish


