# Python3集合
# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('caaaaa' in basket)

# # 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)    # 集合a中包含而集合b中不包含的元素
print(a | b)      # 集合a或b中包含的所有元素
print(a & b)      # 集合a和b中都包含了的元素
print(a ^ b)      # 不同时包含于a和b的元素
# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 集合的基本操作
# 添加元素
# s.add(x)
# 将元素x添加到是、集合s中，如果元素已存在，则不进行任何操作
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
# s.update( x ) x 可以有多个，用逗号分开。
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)
thisset.update([1, 4], [5, 6])
print(thisset)
thisset.update({'abc': 456, 'Name': 'Facebook'})
print(thisset)

# 移除元素
# s.remove( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)
# 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
"""
>>> thisset.remove("Facebook")   # 不存在会发生错误
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Facebook'
>>>
"""

# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
# s.discard( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")     #不存在不会发生错误
print(thisset)
# thisset = set(("Google", "Runoob", "Taobao"))
# s.pop()
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
X = thisset.pop()
print(X)
# 多次执行测试结果都不一样。
# 然而在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）。
"""
>>>thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
>>> thisset.pop()
'Facebook'
>>> print(thisset)
{'Google', 'Taobao', 'Runoob'}
>>>
"""
# 计算集合元素个数
# len(s)
# 计算集合 s 元素个数。
"""
>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> len(thisset)
3
"""
# 清空集合
# s.clear()
# 清空集合 s。
"""
>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.clear()
>>> print(thisset)
set()
"""

# 判断元素是否在集合中存在
# x in s
# 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。
"""
>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> "Runoob" in thisset
True
>>> "Facebook" in thisset
False
>>>
"""

# 集合内置方法完整列表
"""

方法	描述
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
"""