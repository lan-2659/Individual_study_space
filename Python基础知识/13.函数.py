# 函数的形参定义自左至右的顺序为：位置形参，星号元组形参，命名关键字参数，双星号字典形参
# 命名关键字参数必须采用关键字传参的形式
# 当函数作为参数传入另一个函数时，不要带括号
# 函数名后面加括号代表运行函数，不加括号代表这个函数的地址
'''
函数式编程思想:
    封装 --- 函数本身
    继承 --- 将核心逻辑提取出来封装为一个或者多个函数，将这些函数作为参数传入原函数
    多态 --- 可能会将核心逻辑封装为多个函数，由这些函数共同作用得到结果
'''


#定义函数(使用关键字def)
'''
def 函数名(参数1, 参数2, ……, 参数3='默认值'):      # 可以把函数设置成不需要参数, 也可以设置多个参数
    函数体                                     # 设置了默认值的参数叫(缺省参数/默认实参),设置默认值时等号两边不要留空白
    return 返回值                               # return语句可以放在函数中的任意一个地方, 建议一个函数返回一个值就好
                                              # return语句会直接结束函数的执行
def 函数名(参数1, 参数2, ……, *形参名):            # '*'号会让Python生成一个名为'形参名'的元组, 这个元组会接收传入的所有实参(不限制数量)
    函数体                                     # '**'会生成一个字典, 给这个字典传参数时需要按照用dict()创建字典时的格式
                                              # 除了带*的参数，其它参数都可以设置默认值
''' 



# 形参和实参
'''
函数名后定义的参数叫 形参
我们向函数传递的具体参数叫 实参
'''

# 位置实参 & 关键字实参
'''
调用函数时，实参如果与形参按照顺序一一对应，这种实参叫位置实参
位置实参的顺序很重要，搞错顺序很可能会导致函数调用出错

关键值实参是传递给函数的名值对                          # 使用关键值形参时等号左右两边不带空号
关键值实参就是在调用函数时直接给形参赋值

示例：
def favorite_books(book_1, book_2, book_3):
    print('My favorite books are {}, {} and {}'.format(book_1, book_2, book_3))

book1 = 'hello'
book2 = 'world'
book3 = 'python'

favorite_books(book1, book2, book3)                               # 用位置实参调用函数，必须注意实参传递顺序
favorite_books(book_2=book2, book_3=book3, book_1=book1)    # 用关键字实参调用函数，不需要注意实参传递顺序
'''


# 生成器
'''
用 yield 关键字返回数据的函数就是生成器
生成器返回数据时，只会在需要时生成，且一次返回一个
可用 for 循环来循环函数，以获取全部数据
这个生成器属于可迭代对象
'''


# 闭包
"""
    闭包三大要素：
        内部函数
        访问外部函数变量
        返回内部函数
    作用：
        外部函数执行过后 栈帧不会被释放 等待内部函数调用
    优点：逻辑连续，当闭包作为另一个函数调用参数时，避免脱离当前逻辑而单独编写额外逻辑。
    缺点：由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，所以不能滥用闭包
        
闭包连续性案例：
def give_money(money):
    print('给你%d元'%money)
    
    def buy_thing(thing,price):
        nonlocal money
        money -= price
        print('你购买了%s,还剩%d元'%(thing,money))
    
    return buy_thing

buy_thing = give_money(1000)
buy_thing('书',500)
buy_thing('水果',100)
buy_thing('水果',100)

"""


# 装饰器
'''
# 装饰器是一个函数，主要作用是来用包装另一个函数、类方法或类本身
# 系统在执行带装饰器的函数时，会抛弃原本函数的运行逻辑，执行装饰器函数中的运行逻辑
# 需要注意，自定义装饰器函数时，需要把装饰器函数定义在使用装饰器的函数上面

# -----------这是基本装饰器----------------
from time import time 

def new_fun(fn):                    # 装饰器这里的形参必加，这个形参会接收原函数整体
    print("hhhhhh")
    def wrapper(*args,**kwargs):    # 约定成俗装饰器中的内置函数叫wrapper
        start = time()
        print(fn(*args,**kwargs))
        end = time() - start
        print("执行时间：", end)
        return "内置函数返回语句"
    return wrapper   # 这里不要加括号，加了括号代表直接执行这个函数，拿不到外面传入的参数
        
            # 加入装饰器后，原函数不会执行，会执行装饰器函数
@new_fun    # 加装饰器原理：原函数整体传给装饰器(不包括参数)，参数会传给内置函数
def old_fun(*args):   # 加入装饰器后原函数本身就拿不到传入的参数了，原函数只能去装饰器的内置函数中拿参数
    print(args)
    return sum(args)
    
    
print(old_fun(1, 2, 3, 45, 66, 77, 42))
print(old_fun(1, 2, 3, 45, 66, 77, 42))
# 只有第一次调用会执行全部装饰器代码，后面调用时只执行内置函数代码
# 调用函数时，函数的返回内容就是，装饰器的内置函数返回的内容



# 带参数的装饰器（这个一般是三层嵌套函数，最外层返回装饰器，中间返回内置函数）
def repeat(num):        # 这里接收装饰器参数
    def decorator(func):        # 这里接收原函数
        def wrapper(*args, **kwargs):       # 这里接收原函数的参数
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 调用被装饰的函数
greet("Alice")  # 调用被装饰的函数
# 与基本装饰器一样的逻辑，所有外层代码都只执行一次，接下来再次调用原函数就会只会执行装饰器返回的内置函数



# 类装饰器
class MyDecorator:
    def __init__(self, func):   # 需要在这里接收原函数
        self.func = func

    def __call__(self, *args, **kwargs):    # 原函数的参数回传到这里，每次调用原函数都只会执行这个函数
        print("Something is happening before the function is called.")
        result = self.func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

@MyDecorator  # 应用类装饰器
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Charlie")  # 调用被装饰的函数



# 多个装饰器执行顺序：从下往上（装饰器链）
'''


# 特别注意当你用自己写的装饰器去装饰类时，一定要在内置函数中把生成的类的实例返回


# 闭包与装饰器在调用上的不同
'''
# 闭包的调用与装饰器不同
# 闭包的原函数调用一次就好
# 闭包调用时需要定义一个参数接收返回的内置函数函数
# 然后用该参数调用内置函数，就可以实现逻辑循环

# 但是装饰器不需要专门定义参数接收返回的内置函数
# 带装饰器的函数可以一直调用
# 只有第一次调用时会执行全部的装饰器函数
# 之后的调用都只会执行内置函数
'''

# 补充
"""
def test(a, b, *, c, d):     # *号表示后面参数必须用关键字传参
    print(a, b, c, d)

test(1, 2, c=3, d=4)    # 由于c、d没有默认参数且c、d前面有单独的*号，所以必须用关键字传参
"""