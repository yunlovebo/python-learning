# 内置函数：数学相关

print(abs(-99.99)) # 99.99

print(sum([1,2,3])) # 6

print(max([1,2,3])) # 3
print(max((1,2,3))) # 3
print(min([1,2,3])) # 1
print(min(1,2,3)) # 1


print(pow(2,3)) # 8

print(round(3.1415926, 2)) # 3.14
print(round(0.5)) # 0
print(round(1.5)) # 2
print(round(2.5)) # 2
print(round(3.5)) # 4
print(round(4.5)) # 4
print(round(5.5)) # 6
print(round(6.5)) # 6
print(round(-0.5)) # 0
print(round(-1.5)) # -2
print(round(-2.5)) # -2
print(round(-3.5)) #- 4
print(round(-4.5)) # -4
print(round(-5.5)) # -6
print(round(-6.5)) # -6

print(bin(123)) # 0b1111011
print(int(0b1111011)) # 123
print(oct(123)) # 0o173
print(hex(123)) # 0x7b
print(int(0x366)) # 870

# 将字符转为ASCII
r = ord('a')
print(r) # 97

# 将ASCII转为字符
r= chr(65)
print(r) # A
