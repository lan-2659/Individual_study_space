# Python内置函数range(start,stop,step)
'''
作用：生成指定范围的序列
优点：所有range对象存储空间都相同，因为仅仅只需要存储start,stop,step三个数据，只有当用到range对象时才会去计算序列中的相关元素
start   开始的数值（默认为0）
stop    停止的数值(不包括该值，且没有默认值)
step    步长（默认为1）, 不能为0或负数, 为0会报错
'''
# range()函数只有三种用法
# 1、range(stop)
# 2、range(start,stop)
# 3、range(start,stop,step)


# sorted(可迭代对象, key=函数, reverse=True)
# 传入的函数会对每一个可迭代对象元素使用，用于选出比较的值
# 只有序列中待排值类型相同才能排，结果会返回一个按照从小到大排列的'列表'（数字在前，字母在后）
'''
示例:
str_ = 'asdjs1112345  !@#dn￥%……&*（）——+'#字符串
print(sorted(str_))

list_ = list('hello world!')#列表
print(sorted(list_))

tuple_ = tuple('asjdhb')#元组
print(tuple_)
print(sorted(tuple_))

dict_ = {'Alice': '2341', 'Beth': '9102', 'Cecil': 3258}#字典
print(sorted(dict_).items())

set_ = set(('bcsegdhf'))#集合
print(sorted(set_))
'''


# min(可迭代对象，key = 函数)
# 传入的函数会对每一个可迭代对象元素使用，用于选出比较的值
'''
这个函数会选出可迭代对象中最小的那一个
或者排序最靠前的一个
'''


# max(可迭代对象, key = 函数)
# 传入的函数会对每一个可迭代对象元素使用，用于选出比较的值
'''
这个函数会选出可迭代对象中最大的那一个
或者排序最靠后的一个
'''


# 拷贝知识
'''
1、直接赋值
变量都指向同一个对象，当对象改变时对导致指向该对象的变量的变化

2、copy()浅层拷贝
数据.copy()
变量指向不同的表层对象，但还指向同一个子对象

3、copy.deepcopy()深层拷贝          # 要先导入copy模块
copy.deepcopy(数据)
变量指向不同的表层对象和子对象

4、字符串、列表、元组的切片方式复制也是浅层拷贝
'''


#bit_count()方法
'''
python 3.10 以上可用

返回一个数转换成二进制后1的个数
'''


# enumerate()
'''
可以对列表，字符串，元组使用
返回索引序号和值
序号在前，值在后
'''


# abs()
'''
abs(i - j)    返回计算结果的绝对值
'''


# map()函数
'''
map(函数, 可迭代对象)           会将接收到的函数应用到可迭代对象的每一个元素上，然后返回一个迭代器
'''


# filter()函数
'''
filter(判断函数，可迭代对象) 
    会对可迭代对象中的所有元素使用判断函数
    （判断函数的返回值只能是True或False）
    会将所有符合条件的元素打包成一个迭代器返回
'''


# zip()函数
'''
是一个内置函数，用于将多个可迭代对象作为参数，将对应的元素打包成元组，然后返回由这些元组组成的迭代器
'''


# join()方法
'''
'分隔符'.join(可迭代对象)   返回一个字符串，将可迭代对象中的元素连接成一个字符串，且每个元素之间以分隔符分开
'''


# chr()
'''
将一个ASCll码或是Unicode码转换成对应字符
chr(65) --> 'A'
'''


# ord()
'''
将一个字符转换成ASCll码或是Unicode码
ord('A')  --> 65
'''

# iter() 函数
'''
iter(可迭代对象) 
    返回一个可迭代对象的迭代器
    这个迭代器只能往前取值，不能后退，即只能用一次
    可以对迭代器对象进行循环
    迭代器对象可以用 next(迭代器对象) 语句返回下一个元素
    若下一个元素不存在，会触发 StopIteration 异常
    注意 next() 方法只能对迭代器对象使用
    
迭代器：访问可迭代对象的工具
迭代器对象：就是迭代器来源的那个可迭代对象
'''


# count()函数
'''
可迭代对象.count(元素)
    返回一个数字，代表这个元素在可迭代对象中的数量
'''
