def person():
    money = 0
    
    def work():
        nonlocal money # 在内函数中使用了外函数的临时变量
        money += 100
        print(money)

    def overtime():
        nonlocal money
        money += 200
    
    def buy():
        nonlocal money
        money -= 50

    # 在外函数中返回了内函数，这个内函数就是闭包函数
    return work

res = person() # res = work
res() # res() = work()
res()
res()
res()
res()
res()


print(res.__closure__) # (<cell at 0x000001B1DB959DB0: int object at 0x000001B1DB889D30>,)
print(person.__closure__) # None
