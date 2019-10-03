# Python 基础数据类型
# Python 中的变量不需要申明，每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
# 在Python中，变量就是变量，它没有类型，我们所说的“类型”是变量所指的内存中对象的类型
# 等号=用来给变量赋值
# 等号=运算符左边是一个变量名，等号预算福邮编是存储在变量中的值
# !/usr/bin/python3
counter = 100       # 整形变量
miles = 1000.0      # 浮点型变量
name = "runoob"     # 字符串
print(counter)
print(miles)
print(name)

# 多个变量赋值
# Python允许同时为多个变量赋值
# a = b = c = 1
# 以上实例，创建一个整形对象，值为1，从后向前赋值，三个变量被赋予相同的数值。
# 也可以为多个对象指定多个变量。
# a, b, c = 1, 2, "Runoob"
# 以上实例，两个整形对象1和2的分配给变量a和b，字符创对象“Runoob”分配给变量c。

# 标准数据类型
# Python3 中有六个标准的数据类型：
# Number(数字)
# String(字符串)
# List(列表)
# Tuple(元组)
# Set(集合)
# Dictionary(字典)
# Python3的六个标准数据类型中：
# 不可变数据（3个）：Number(数字)、String(字符串)、Tuple(元组)
# 可变数据（3个）：List(列表)、Dictionary(字典)、Set(集合)

# Number(数字)
# Python3 支持 int 、float、bool、complex(复数)。
# 在Python3中，只有一种整数类型int，表示为长整型，没有Python2中的Long
# 像大多数语言一样，数据类型的赋值和计算都是很直观的
# 内置的type()函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
# 此外还可以用isinstance来判断
e = 111
print(isinstance(a, int))
# isinstance 和 type 的区别在于：
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型
'''
>>> class A:
...     pass
... 
>>> class B(A):
...     pass
... 
>>> isinstance(A(), A)
True
>>> type(A()) == A 
True
>>> isinstance(B(), A)
True
>>> type(B()) == A
False
'''
# 注意：在Python2中是没有布尔型的，它用数字0表示False，用1表示true，到Python3中，把True和False定义成关键字了，但他们的值
# 还是1和0，他们可以和数字相加
# 当指定一个值时，Number对象就会被创建
# var1 = 1
# var2 = 2
# 也可以使用del语句删除一些对象应用。
# del语法的语句是：
# del var1[, var2[, var3[...., varn]]]
# 可以通过使用del语句删除单个或多个对象
# del var
# del var_a, var_b
# 数值预算
print(5+4)      # 加法
print(4.3-2)    # 减法
print(3*7)      # 乘法
print(2/4)      # 除法，得到一个浮点数
print(2//4)     # 除法，得到一个整数
print(17 % 3)     # 取余
print(2**5)     # 乘方
# 注意
# Python可以同时为多个变量赋值，如a,b=1,2
# 一个变量可以通过赋值指向不同类型的对象
# 数值的除法包含两个预算法：/返回一个浮点数，//返回一个整数
# 在混合计算中，Python会把整数类型转换成浮点数。

# String（字符串）

# List(列表)
# List(列表)是Python中使用最频繁的数据类型
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字、字符串甚至可以包含列表（所谓嵌套）
# 列表是写在方括号[]之间，用逗号分隔开的元素列表
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
# 列表的截取的语法格式：变量[头下标:尾下标]
# 索引值以0位开始值，-1位从末尾的开始位置。
t = ['a', 'b', 'c', 'd', 'e']
print(t[1:3])
print(t[3:])
print(t[:4])
print(t[:])

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

# 与Python字符串不一样的是，列表中的元素是可以改变的。
'''
>>>a = [1, 2, 3, 4, 5, 6]
>>> a[0] = 9
>>> a[2:5] = [13, 14, 15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 将对应的元素值设置为 [] 
>>> a
[9, 2, 6]
'''
'''
List写在方括号之间，元素用逗号隔开
和字典一样，List可以被索引和切片
List可以使用+操作符进行凭借
List中的元素是可以改变的。
'''
# Python列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引1到索引4的位置并设置为步长2（间隔一个位置）来截取字符串
letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']
print(letters[1:4:2])
print(letters[-4:-1])
# 如果第三个参数为负数表示逆向读取，一下实例用于翻转字符串
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    print(inputWords)
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = '，'.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob Python MY'
    rw = reverseWords(input)
    print(rw)

# Tuple（元组）
# 元组（Tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开
# 元组中的元素类型也可以不相同
tuple11 = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple11)      # 输出完整元组
print(tuple11[0])   # 输出元组的第一个元素
print(tuple11[1:3]) # 输出从第二个元素开始到第三个元素
print(tuple11[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple*2)  # 输出两次元组
print(tuple11 + tinytuple)  # 连接元组
# 元组与字符串类似，可以被索引切下标索引从0开始，-1位从末尾开始的位置。也可以进行截取。
# 其实也可以把字符串看做一种特殊的元组
# 虽然元组的元素不可改变，但它可以包含可变的对象，比如list列表
tupleandlist = ('abcd', 786, 2.23, ['c', 'h', 'e', 'c', 'k', 'i', 'o'], 70.2)
print(tupleandlist)
# 构造包含0个或1个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()       # 空元组
tup2 = (20,)    # 一个元素，需要在元素后面添加逗号
# string list 和tuple都属于sequence(序列)
'''
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''

# Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成，构成集合的事务或对象称作元素或成员
# 基本功能是进行成员关系测试和删除重复元素
# 可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
# 创建格式：
# parame = {value1, value2,....}
# 或者set(value)
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复元素的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# Set可以进行集合运算
a1 = set('abracadabra')
b1 = set('alacazam')
print(a1)
print(a1-b1)    # a和b的差集
print(a1|b1)    # a和b的并集
print(a1&b1)    # a和b的交集
print(a1^b1)    # a和b中不同时存在的元素

# Dictionary（字典）
# 字典（Dictionary）是Python中另一个非常有用的内置数据类型
# 列表是有序的对象集合，字典是无序的对象集合，两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
# 字典是一种映射类型，字典用{}表示，它是一个无序的键（key）:值（value）的集合
# 键（key）必须使用不可变类型
# 在同一个字典中，键（key）必须是唯一的
dict1 = {}
dict1['one'] = "1_菜鸟教程"
dict1[2] = "2_菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict1['one'])     # 输出键为'one' 的值
print(dict1[2])          # 输出键为2 的值
print(tinydict)         # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())    # 输出所有值
# 构造函数dict()可以直接从键值对序列中构建字典如下：
dict2 = dict([('Runoob', 1), ('google', 2), ('taobao', 3)])
print(dict2)
dict3 = {x: x**2 for x in (2, 4, 6)}
print(dict3)
dict4 = dict(Runoob=1, Google=2, Taobao=3)
print(dict4)
'''
另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。

注意：

1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
'''

# Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
'''

int(x [,base])
将x转换为一个整数

float(x)
将x转换到一个浮点数

complex(real [,imag])
创建一个复数

str(x)
将对象 x 转换为字符串

repr(x)
将对象 x 转换为表达式字符串

eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)
将序列 s 转换为一个元组

list(s)
将序列 s 转换为一个列表

set(s)
转换为可变集合

dict(d)
创建一个字典。d 必须是一个 (key, value)元组序列。

frozenset(s)
转换为不可变集合

chr(x)
将一个整数转换为一个字符

ord(x)
将一个字符转换为它的整数值

hex(x)
将一个整数转换为一个十六进制字符串

oct(x)
将一个整数转换为一个八进制字符串
'''
