# 正则表达式是一个特殊的字符序列
# 正则表达式原理从左到右一个字符一个字符的匹配

"""
贪婪匹配（尽可能多地匹配）
非贪婪匹配（尽可能少地匹配）


简单的正则表达式：
"hqyj"  "华清远见"  "来来来ll7887"     必须和这些字符串相同才会匹配


复杂一点的：

"[hqyj]"  匹配"h"或者"q"或者"y"或者"j"字符, 即括号中的单个字符

"[hqyj]牛"    匹配"h牛"或者"q牛"或者"y牛"或者"j牛"

"[^hqyj]"   匹配除了 "h"、"q"、"y"、"j" 之外的字符, 即括号外的单个字符

"[a-z]"     括号内匹配的内容可以是一个范围

"[0-9]"     括号内匹配的内容可以是一个范围

"."     匹配任意字符

\d      匹配任何十进制数字；相当于类 [0-9]
\D      与 \d 相反，匹配任何非十进制数字的字符；相当于类 [^0-9]


\s      匹配任何空白字符（包含空格、换行符、制表符等）
\S      与 \s 相反


\w      匹配字母、数字、下划线[a-zA-Z0-9_]
\W      于 \w 相反


\b      匹配一个位置，该位置是单词的开始或结束。它不匹配任何字符
\B      匹配一个位置，该位置不是单词的开始或结束。它不匹配任何字符


数量控制：(如果仅匹配一个字符，且允许0次，那么每一个字符都会匹配，匹配不上的会返回一个 "")
*       重复0次或者更多次，贪婪匹配
+       重复1次或者更多次，贪婪匹配
?       重复1次或者0次，非贪婪匹配
{n}     重复n次,n是数字，贪婪匹配
{n,}    重复n次或者更多次，贪婪匹配
{n,m}   重复n到m次，贪婪匹配


() 用于分组 (捕获)
    "hq(yj)"    按照 "hqyj" 进行匹配，但拿到结果后只要 "yj" 部分，即捕获分组
    (?:re)这种表达式就不会单独提取这一部分，即非捕获分组，大多用于 re 中包含 "|" 的选择


在限制数据格式时可以用 "|" 来进行选择，选择内容必须全部放在 () 中


^开始
    "^hqyj\d+"      有 ^ 在re开头，表示匹配字符串的开头。


$结尾
    "hqyj\d+$"      有 $ 在re结尾，表示匹配字符串的结尾。


当 ^ 和 $ 一起使用时，它们表示匹配整个字符串，即字符串的开始和结束之间的内容必须完全符合正则表达式


由于正则表达式中 * . \  {} () 等等符号具有特殊含义,如果你指定的字符正好就是这些符号,需要用\进行转义

"""


# re模块
"""
re.findall("re",text)    # 遍历字符串，找到正则表达式匹配的所有位置，并以列表的形式返回。
        # 如果给出的正则表达式中包含子组，就会把子组的内容单独返回，如果有多个子组就会以元组的形式返回。
    
re.finditer("re", text)     #与 re.findall("re",text) 效果一样，但返回一个迭代器

re.search('re', text)    # 从头扫描整个字符串，一旦成功匹配字符串，就停止，并返回一个对象，否则返回none
        # 可以直接输出对象，查看匹配位置，和匹配内容
    
re.sub("re","替换内容", text)   # 替换匹配成功的字符，返回字符串

re.split("re", text)        # 根据匹配内容对字符串进行切割，返回一个列表
"""


"""
前瞻断言（Lookahead） && 后顾断言（Lookbehind）

前瞻断言用于判断当前位置之后的字符是否符合某个条件。它分为两种类型：
    正向前瞻断言（Positive Lookahead）：(?=pattern)
        用于判断当前位置之后的字符是否匹配 pattern。如果匹配成功，则整个表达式成功；否则失败。
        示例：匹配后面跟着数字的字母：(?=[0-9])[a-zA-Z]。
    负向前瞻断言（Negative Lookahead）：(?!pattern)
        用于判断当前位置之后的字符是否不匹配 pattern。如果不匹配成功，则整个表达式成功；否则失败。
        示例：匹配后面不是数字的字母：(?![0-9])[a-zA-Z]。

后顾断言用于判断当前位置之前的字符是否符合某个条件。它也分为两种类型：
    正向后顾断言（Positive Lookbehind）：(?<=pattern)
        用于判断当前位置之前的字符是否匹配 pattern。如果匹配成功，则整个表达式成功；否则失败。
        示例：匹配前面是数字的字母：(?<=[0-9])[a-zA-Z]。
    负向后顾断言（Negative Lookbehind）：(?<!pattern)
        用于判断当前位置之前的字符是否不匹配 pattern。如果不匹配成功，则整个表达式成功；否则失败。
        示例：匹配前面不是数字的字母：(?<![0-9])[a-zA-Z]。
        
使用场景
正向前瞻：用于匹配某个模式后面跟着特定内容的情况。例如，匹配价格（数字后面跟着货币符号）：\d+(?=€)。
负向前瞻：用于匹配某个模式后面不跟着特定内容的情况。例如，匹配不是价格的数字：\d+(?!€)。
正向后顾：用于匹配某个模式前面有特定内容的情况。例如，匹配美元金额（前面有 $ 符号）：(?<=\$)\d+。
负向后顾：用于匹配某个模式前面没有特定内容的情况。例如，匹配不是美元金额的数字：(?<!\$)\d+。

注意事项
后顾断言在某些正则表达式引擎中可能不支持，例如早期的JavaScript版本。
使用前瞻和后顾断言时，要注意它们不会消耗字符，即匹配成功后，匹配的“游标”不会移动。
这些断言在处理复杂的匹配需求时非常有用，但可能会增加正则表达式的复杂性和计算成本。
"""
