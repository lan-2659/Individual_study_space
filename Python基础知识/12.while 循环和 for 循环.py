# # # python中只提供了两种循环一个是while循环，一个是for-in循环


# while语法结构
"""
while 循环条件:
    循环体
"""
# while循环中最重要的三个部分：1、循环变量 2、循环条件 3、循环增量
# while循环的结束方法：
# 1、条件为 False
# 2、遇到 break


# for-in循环：(遍历)
"""
for 自定义的变量 in 可迭代对象：  # for循环本质是根据索引号取值，若可迭代对象发生变化，for循环根据索引号获取的值与原来相比会有变化
    循环体
"""


# break 和 continue
"""
break：循环中一旦遇到break就会跳出当前循环，执行当前循环后的语句   

continue：结束本次循环，继续下次循环
"""


# 循环语句中的else语句：
"""
可以在循环后面加上else语句
如果循环正常结束就会执行else语句

如果是因为break语句退出循环，就不会执行else语句
"""
