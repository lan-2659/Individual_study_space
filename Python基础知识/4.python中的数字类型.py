# int类型
"""
x = -10
print(x)    # 十进制的整数数字

x = 0o10
print(x)    # 八进制的整数数字

x = 0x12ff12
print(x)    # 十六进制的整数数字

x = 0b110
print(x)    # 二进制的整数数字

print(1_00_00_00)  # 可以在数字中加入下划线提高可读性，不会影响数字大小

注意：调用print()函数时，如果参数是整数(无论几进制)，都默认输出十进制的整数数字
"""


# 进制转换
"""
int(整型数字)     # 返回一个十进制整数
int(字符串, 字符串中数字进制（默认为10）)    # 返回一个十进制整数

bin()          # 返回一个二进制数字符串，开头:0b
oct()          # 返回一个八进制数字符串，开头:0o
hex()          # 返回一个十六进制数字符串，开头:0x
bin()、oct() 和 hex() 它们只能接收整型数字（十进制、二进制、八进制、十六进制都可以）作为参数
"""


# float类型
"""
x = 1.2
print(x)    # 正常浮点数

x = 10.
print(x)    # 整数后面只要带了小数点就会被判定为浮点数，如果没有小数部分系统会自动帮你在小数部分加个0

x = .9        # 小数点前面没有数字，系统会自动帮你在整数部分加个0
print(x)

注意0和0.0是不一样的，一个是整数，一个是浮点数
"""


# 浮点数与整数之间的转换
"""
float(字符串|浮点数|整数(任意进制))         # 返回一个浮点数，如果小数部分没有数字则会自动帮你补一个0
int(浮点数)      # 返回一个十进制整数，小数部分会被直接丢弃（并非四舍五入）

round(浮点数|整数, 保留小数位数（默认不保留小数，如果原数字小数位数不足则直接输出原数字）)   # 四舍六入，五看齐（即奇变偶不变）

import math
math.ceil(x)    # 返回大于x的最小整数
math.floor(x)   # 返回小于x的最大整数
"""


# 科学计数法、π和自然常量e
"""
x = 1e3     # 1乘以10的3次方
x = 2e03    # 2乘以10的3次方
x = 1.56e-2     # 1.56乘以10的-2次方
x = 1.34e-02    # 1.34乘以10的-2次方
x = 1.34e+2     # 1.34乘以10的2次方
print(x)
注意：e 后面必须是整数（这个整数可以是0开头）

import math
x = math.pi  # 返回数学常量π（圆周率）约等于3.1415926
print(x)
x = math.e   # 返回自然常量e，约等于2.72
print(x)
"""


# 复数类型
"""
x = 1 + 2j  # 直接创建复数
print(x)

x = complex(1, 2)   # 通过conplex()函数创建复数，虚部数字可以不填，默认为0
print(x)
"""
