1. 高阶函数：
        1. 闭包
            1. 闭包的特点：
                1. 在外函数中定义了局部变量，并且在内部函数中使用了这个局部变量
                2. 在外函数中返回了内函数，返回的内函数就是闭包函数
                3. 主要在于保护了外函数中的局部变量，既可以被使用，又不会被破坏
            2. 如何检测一个函数是否为闭包函数？
                1. 函数名.__closure__ 如果是闭包函数返回cell
        2. lambda表达式(匿名函数)
            1. 在python中使用lambda表达式定义匿名函数
            2. lambda表达式仅仅是一个表达式，不是一个代码块，所以lambda又称为一行代码的函数
            3. lambda表达式也有形参，并且不能访问除了自己的形参之外的任何数据，包括全局变量
    2. 迭代器（迭代器 == 迭代器对象）
        1. 定义：迭代器是一个能被next()函数调用，并不断返回下一个值的对象，称为迭代器（iterator 迭代器对象）
        2. 特点：
            1. 迭代器是python中最具特色的功能之一，是访问集合元素的一种方式
            2. 迭代器是一个可以记住访问遍历的位置的对象
            3. 从集合的第一个元素开始访问，直到集合中的所有元素被访问完毕
            4. 迭代器只能从前往后一个一个的遍历，不能后退
        3. 使用
            1. 循环次数过多时，应使用迭代器
            2. 可迭代对象 vs 迭代器对象
                1. iter()：传入可迭代对象，返回一个迭代器对象
                2. 可迭代对象：str、list、tuple、dict、set、range
                3. 注意：迭代器对象一定是一个可以迭代的对象，但是可迭代对象不一定是迭代器对象
            3. 迭代器取值方案
                1. next() 调用一次获取一次，直到数据被取完
                2. list() 使用list函数直接取出迭代器中的所有数据
                3. for 使用for循环遍历迭代器的数据
            4. 迭代器取值特点：取出一个少一个，直到都取完，最后再获取就会报错
            5. 检测迭代器和可迭代对象的方法：使用isinstance方法
                1. 迭代器一定是一个可迭代的对象
                2. 可迭代的对象不一定能是一个迭代器
