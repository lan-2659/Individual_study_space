# 集合中的元素必须是不可变的数据，集合中不存在相同的元素：集合中保存的数据一定不同
# 特别注意集合是无序的，不能进行索引


# 创建集合
"""
set_x = set()           # 创建空集合

set_x = {1, 2, 3, 4, 4}     # 集合中不会存在重复的值，创建成功后会自动移除重复的部分

set_x = set((1, 2, 3, 4))   # 用set()函数创建集合，可以传入可迭代对象，这个函数会把可迭代对象中的每一个元素，转换为集合中的元素

注意：set_x = {} 这样创建出来的是字典，不是集合
"""


# 集合间的基本运算：(可以连用)
"""
(并)   | : set_x = set1 | set2      set3中的元素为set1和set2中的全部元素
(交)   & : set_x = set1 & set2      set3中的元素为set1和set2种都包含的元素
(差)   - : set_x = set1 - set2      set3中的元素为set1中包含而set2中不包含的
(异或) ^ : set_x = set1 ^ set2      set3中的元素为set1和set2中各自独有的元素
"""


# 集合常用API
"""
set_x.add(2)      # 向set_x中添加数字2，如果set_x中已经存在2，则不会添加

del set_x               # 删除set_x这个集合
set_x.remove(2)         # 从set_x中移除数字2，如果集合中没有2会报错
set_x.discard(2)        # 从set_x中移除数字2，如果集合中没有2不会报错
set_x.pop()             # 从set_x中随机移除一个元素，并返回移除元素的值

len(set_x)              # 获取set_x长度(即集合中的元素个数)

set_x.clear()           # 清空set_x中的元素

set_x.issubset(set_y)   # 判断set_x是否是set_y的子集，返回一个布尔值
set_x.isdisjoint(set_y) # 判断set_x和set_y是否没有交集（即两个集合没有共同元素），返回一个布尔值
"""
