"""python中 "=" 是用于变量对值的引用, 可以让多个变量引用同一个值"""

""" 最重要的是值不是变量！！！ """
# 值一旦改变，引用该值的变量中的内容就会改变


x = 123  # 为x增加123的引用
print(id(x))  # 输出123的地址
print(type(x))  # 输出123的类型
print(x)  # 输出123


a, b, c = 1, 2, 3  # 可以这样为a,b,c赋值
a = b = c = 1  # 可以这样为a,b,c赋值
"""
a = 1, b = 2, c = 3  # 但是不可以这样为a,b,c赋值
注意："," 代表元组
a = 1, b = 2, c = 3 被电脑理解成了 a = (1, b) = (2, c) = 3
这导致了语法上的混乱，所以Python不允许这样写。

不过允许这样写：a = 1; b = 2; c = 3
"""

del a  # 删除变量a，即解除a对2的引用

a, b = 1, "1"
print(a == b)  #'=='符号只比较两个对象的值和类型
print(a is b)  #'is'符号除了比较值和类型外还要比较地址

c = 1 + 2j  # 这里的c是复数
print(c)
