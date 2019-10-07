# Python3 循环语句
# Python中的循环语句有 for 和 while。
# while循环
# while 判断条件：
#     语句
a = 1
while a < 10:
    print(a)
    a += 2
# 同样需要注意冒号和缩进。另外，在 Python 中没有 do..while 循环。
# 以下实例使用了 while 来计算 1 到 100 的总和：
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

# 无限循环
# 我们可以通过设置条件表达式永远不为false来实现无限循环
# var = 1
# while var == 1:   # 表达式永远为true
#     num = int(input("请输出一个数字："))
#     print("你输入的数字是: ", num)
# print("Good bye!")
# 无限循环在服务器上客户端的实时请求非常有用。

# while 循环使用else语句
# while … else 在条件语句为 false 时执行 else 的语句块：
count = 0
while count < 5:
    print(count, "小于5")
    count = count + 1
else:
    print(count, "大于或等于5")

# 简单语句组
# 类似if语句的语法，如果while循环中只有一条语句，可以将该语句与while写在同一行中
# flag = 1
# while (flag): print("Python")

# for 语句
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串
# for循环的一般格式如下：
"""
for <variable> in <sequence>:
    <statements>
else:
    <statements>
"""
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

# 以下for循环实例中使用了break语句，break语句用于调出当前循环体
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == 'Runoob':
        print("菜鸟教程")
        break
    print("循环数据"+ site)
else:
    print("没有循环数据!")
print("完成循环!")

# range()函数 ，自动生成数列

# break和continue 语句及循环中的else子句
# break语句可以跳出for和while的循环体，如果你从for或while循环中终止，任何对应的循环else快将不执行。
for letter in 'Runoob':     # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)
var = 10
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!")

# continue 语句被用来告诉python跳过当前循环快中的剩余语句，然后继续进行下一轮循环
# !/usr/bin/python3

for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")

# 循环语句可以有else子句，它在穷尽列表（以for循环）或条件变为false（while循环）导致循环终止时被执行，但循环被break终止时不执行
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# pass语句
# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，如下实例
'''
实例
>>>while True:
...     pass  # 等待键盘中断 (Ctrl+C)
最小的类:

实例
>>>class MyEmptyClass:
...     pass
'''
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
