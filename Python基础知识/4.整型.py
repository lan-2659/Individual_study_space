
# int类型
# 对应占位符：%d    
# %3d 表示这个整型有三位，不足则用空格补全，若原数值超出3位则按照实际输出
# %03d 表示这个整型有三位，不足则用0补全，若原数值超出3位则按照实际输出
'''x=001     错误,此类型不能以0开头'''
x=1
print('%03d' % x)    #可以这样输出001
        # 注意位数限定数前要么什么都不放，要么放0

# int类型转换为float类型时若无小数部分会自动生成一位小数，小数部分为0