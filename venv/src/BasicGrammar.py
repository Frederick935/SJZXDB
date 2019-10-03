# Python 中单行注释以#开头
print("Hellow , Pathon!")
# 多行注释可以用过个#号，还有''' 和 """:
# 第一个注释
# 第二个注释
'''
第三个注释
第四个注释
'''
"""
第五个注释
第六个注释
"""
print("多行注释")
# Python最具特色的就是使用缩进来表示代码块，不需要使用{}.
# 缩进的空格数是可变的，但是同一个代码块必须包含相同的缩进空格数
if True:
    print("True")
else:
    print("False")
# 多行语句，可以使用反斜杠来实现多行语句
item_one = '1'
item_two = '2'
item_three = '3'
total = item_one + \
    item_two + \
    item_three
# 在[],{}或（）中的多行语句，不需要使用反斜杠
total = ['one', 'two',
         'three', 'four', 'five']
# 数字类型（number）
# Python 中数字有四种类型，整数、布尔型、 浮点数和复数
# int(整数) 如1 ，只有一种整数类型int，表示为长整数，没有Python2 中的Long。
# bool(布尔)如，True
# float(浮点型)，如1.23 ,3E-2
# complex(复数)，如1+2j，1.1+2.2j

# 字符串String
# Python 中单引号和双引号使用完全相同。
# 使用三引号（'''或"""）可以指定一个多行字符串
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义，比如 r"this is a line with \n"则\n会显示，并不是换行
# 按字面意义级联字符串，如"this" "is" "string" 会被自动转换成 this is string.
# 字符串可以用+运算符连接在一起，用*运算符重复。
# Python 中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# Python中的字符串不能改变
# Python没有单独的字符类型，一个字符就是长度为1的字符串。
# 字符串的截取的语法格式如下：变量[头下标：尾下标：步长]
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以有多行组成"""
# !/usr/bin/python3
str = 'Runoob'
print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[0])       # 输出字符串的第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始后的所有字符
print(str * 2)      # 输出字符串两次
print(str + '你好')  # 连接字符串
print('--------------------------------')
print('hellow\nrunoob')  # 使用反斜杠+n转义特殊字符
print(r'hellow\nrunoob')  # 在字符串前面添加一个r,表示原始字符串，不会发生转义

# 空行
# 函数之间或类的方法之前用空行分隔，表示一段新的代码的开始，类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不通，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会报错。但是空行的作用在于分隔两段
# 不同功能或含义的代码，便于日后代码的维护和重构。
# 空行也是程序代码的一部分

# 等待用户输入
# 执行下面的程序在按回车键后就会等待用户输入
# !/usr/bin/python3
# input("\n\n按下enter键后退出。")

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分好（;）分割
import sys ; x = 'runoob'; sys.stdout.write(x + '\n')

# 多个语句构成代码组
# 缩进相同的一组语句构成一个代码块，我们称之为代码组。
# 像if while def 和class 这样的复合语句，首行以关键字开始，以冒号（:）结束，该行之后的一行或多行代码构成代码组
# 我们将首行及后面的代码组称为一个子句（clause）
# if expression:
#     suite
# elif expression:
#     suite
# else:
#     suite

# Print输出
# Print默认输出是要换行的，如果要实现不换行需要在变量末尾加上 end="":
x = "a"
y = "b"
print(x)
print(y)
print('--------------')
print(x, end=" ")
print(y, end=" ")

# import 与from...import
# 在python中用import或者from...import 来导入相应的模块
# 将整个模块(somemodule)导入，格式为：import somemodule
# 从某个模块中导入某个函数格式为：form somemodule import somefunction
# 从某个模块中导入多个函数，格式为：from somemodule import firstfunc, secondfunc,thirdfunc
# 将某个模块中的全部函数导入，格式为：from somemodule import *

import  sys
print('==================Python import module=================')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n Python路径为：', sys.path)

from sys import argv, path   # 导入特定的成员

print('==================Python from import==============')
print('Path:', path)        # 因为已经导入path成员，所以此处应用时不需要加sys.path