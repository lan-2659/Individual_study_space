# 字符串是可迭代对象

# 创建字符串
"""
# 单引号创建
str_ = ''

# 双引号创建
str_ = ""

# 三引号多用于创建多行字符串
str_ = '''hello!
world!'''
"""


# 字符串转义与不转义
"""
str_ = 'hello\nworld'   # \n表示换行
print(str_)

str_ = 'hello\tworld'   # \t表示制表符
print(str_)

str_ = 'hel\'lo\' world'    # \'表示转义单引号
print(str_)

str_ = r'C:\Windows\notepad.exe'    # 字符串界定符前加r/R,任何字符都不转义,输出时会按原样输出
print(str_)
"""


# 字符串的运算
"""
new_str = 'hello' + 'world'      # 用'+'连接字符串返回一个新字符串
print(new_str)

new_str = 'hello''world'         # 两个或以上字符串如果紧邻在一起，会自动连接
print(new_str)

new_str = 'hello' * 2            # 重复字符串两次，并返回一个新字符串
print(new_str)
"""


# 字符串切片
""" 
切片的语法是：str[start:end:step]
注意：切片时遵循左闭右开的原则，str[start:end]的end是开区间，不包含end
第三个参数是步长(默认为1)，步长为正时表示正向遍历，步长为负时表示反向遍历
切片时会先根据步长的正负判断区间[start:end)是否可以进行正向或反向遍历，如果不行则会直接返回一个空字符串
切片的原理是先切后取，如果判断可以遍历，则会从切下来的部分中start所在方向的那一端开始取值
并将取到的值组成一个新的字符串并返回

print (str1[0])                  # 通过索引输出字符串第一个字符
print (str1[2:5])                # 输出从第三个开始到第五个的字符
print (str1[0:-1])               # 输出第一个到倒数第二个的所有字符
print (str1[::-1])               # 输出字符串倒序
"""


# 字符串中的占位符
"""
%s: 字符串占位符
%d: 整数占位符
%f: 浮点数占位符
%x: 十六进制数占位符
%o: 八进制数占位符
%b: 二进制数占位符
%g: 根据数值大小自动选择普通浮点数或科学计数法，通常更简洁
%e/%E: 科学计数法占位符，将传入数字用科学计数法表示，可以 "%.2e" 这样来指定保留几位小数(默认6位小数)(整数位数指定了无效，始终为1位)
%%: 输出一个%
"""


# 字符串的格式化表达式
"""
使用占位符
str = 'hello %s' % 'world'
print(str)

str = '我今年%09d' % 18888888888888888     # 这里指定输出数字至少为9位，位数不足9位则用0补全，位数超出则原样输出
print(str)                                 # 注意这里的填充字符要么不指定（不指定就不会填充），要么指定为0

str = '这件衣服价格是：%.2f' % 123.456789   # 这里保留两位小数
print(str)

str = 'hello %s %d' % ('world', 12)     # 注意使用两个以上占位符时，传的数据需要使用小括号括起来并使用逗号隔开
print(str)


在字符串前加f进行格式化
str = f'hello world {数据|变量|函数}'
输出时不会输出 {} ，只会输出 {} 中的数据、变量值或函数结果

可以在 {} 中进行对数值或变量的操作，如数值之间的运算、两个变量的连接

可以在 {} 中对数字进行规范化，如：
str = f'这个足球场的面积为：{123.456789:j^7.2f} 公顷'  # j是填充符，^表示居中，7表示输出整体数字的最少位数，.2f表示保留两位小数
print(str)

数字规范化格式：f'{num:j>22.4f}'
                    ':'后的内容: 填充符号 对齐方式 整体数字的最少位数 小数部分保留位数
                    对齐方式:
                        < 左对齐
                        > 右对齐
                        = 符号对齐（将符号（正数符号不显示）放在最左侧，而数字部分则右对齐）
                        ^ 居中
                    整体数字的位数 = 整数部分位数 + 小数点(小数点算一位) + 小数部分位数 + 符号(符号算一位，正数无符号)
                    整体数字的位数如果小于整体数字的最少位数，则会根据你的对齐方式用填充符号填充；如果大于则原样输出
                    选择填充符号后必须选择对齐方式
                    浮点型部分保留位数必须按格式写：.xf(x为你想要保留的位数)
                    其余部分想加就加
"""


# 字符串对象的常见API
"""
str1.upper()                     # 将str1中的小写字母转成大写字母, 返回一个字符串
str1.lower()                     # 将字符串str1中的大写字母转小写字母, 返回一个字符串
str1.swapcase()                  # 将str1中的大小写互换, 返回一个字符串

str.rstrip('字符串')              # 会删除字符串的右边指定字符串, 不指定会默认删除空白, 返回一个字符串
str.lstirp('字符串')              # 会删除字符串的左边指定字符串, 不指定会默认删除空白, 返回一个字符串
str.strip('字符串')               # 会删除字符串两边的全部指定字符串, 不指定会默认删除空白, 返回一个字符串

bool_str = str.isdigit()            # 判断是否是全数字，返回一个布尔值
bool_str = str.isalpha()            # 判断是否全是字母，返回一个布尔值

bool_str = str.startswith('指定字符串')     # 判断字符串是否以指定字符串开头，返回一个布尔值
bool_str = str.endswith('指定字符串')      # 判断字符串是否以指定字符串结尾，返回一个布尔值

str.split('分割符', 分割次数)       # 会返回一个列表，可以不指定分割符和分割次数，默认分割符为空格，默认分割次数为无限次

str.replace('待替换字符', '替换字符', 次数) # 会返回一个字符串，如果不指定次数，会将所有待替换字符替换掉

str.title()                        # 将字符串中每个单词首字母改成大写, 返回一个字符串

str.count('指定字符串')     # 返回字符串中指定字符串出现的次数

str.find('指定字符串', start=None, end=None)      # 返回字符串中指定字符串第一次出现的起始位置，找不到返回-1，可以指定起始位置和结束位置(即查找范围)
"""
