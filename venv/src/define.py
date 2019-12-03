# Python3 函数
# 函数是组织好的，可以重复使用的，用来实现单衣，或相关联功能的代码段
# 函数能提高应用的模块性，和代码的重复利用率。自己创建函数，叫用户自定义函数
# 定义一个函数
# 函数代码块以def关键词开头，后接函数标识符名称或圆括号（）
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以可以用于定义参数
# 函数的第一行语句可以选择性的使用文档字符串-用于存放函数说明
# 函数内容以冒号起始，并且缩进
# return[表达式]结束函数，选择性地返回一个值给调用方，不带表达式的return相当于返回None
# Python 定义函数使用 def 关键字，一般格式如下：
'''
def 函数名（参数列表）:
    函数体
'''
# 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
def hello():
    print("Hello World")

hello()

# 更复杂点的应用，函数中带上参数变量:
# 计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 5
h = 4
print("width =" ,w , "height =", h ,"area =",area(w,h))

# 函数调用
# 定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构
# 这个函数的基本结构完成之后，可以通过另一个函数调用执行，可可以直接从Python命令提示符执行
# 如下实例调用了printmu()函数
# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return

# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

# 参数传递
# 在python中，类型属于对象，变量是没有类型的
# a=[1,2,3]
# a="Runoob"
# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
# 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
# python 函数的参数传递：
# 不可变类型：类似C++的值传递，如整数、字符串、元组。如 fun(a),传递的指示a的值，没有影响a对象本省。比如在fun（a）内部修改a的值，只是修改另一个赋值的对象，不会影响a本身
# 可变类型：类似C++的引用传递，如列表，字典。如fun(la),则是将la真正的传过去，修改后fun外部的la也会受影响
# python中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
# python 传不可变对象实例
def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)  # 结果是 2
'''
实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，
在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。
'''
# 传可变对象实例
# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
def changme(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值: ", mylist)
    return
# 调用changme函数
mylist = [10,20,30]
changme(mylist)
print("函数外取值: ", mylist)

# 参数
'''
以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数
'''
# 必选参数
# 必选参数须以正确的顺序传入参数。调用时的数量必须和声明时的一样。
# printmu()函数，必须传入一个参数，不然会出现语法错误

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
# 使用关键字参数允许函数调用时参数的顺序与申明的不一致，因为Python解释器能够参数名匹配参数值
# 以下实例在函数 printme() 调用时使用参数名：
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

# 调用printme函数
printme(str="菜鸟教程")

# 以下实例中演示了函数参数的使用不需要使用指定顺序：
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")

# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：

def printinfo(name, age = 35):
    print("名字: " ,name)
    print("年龄：", age)
    return
printinfo(age=50,name="runoob")
print("-----------------------")
printinfo(name="runoob")

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2中参数不通，声明时不会命名，基本语法如下：
# def functionname([formal_args,] * var_args_tuple):
#     "函数_文档字符串"
#     function_suite
#     return [expression]
# 加了星号*的参数会以元组（tuple）的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    # 打印任何传入的参数
    print("输出：")
    print(arg1)
    print(vartuple)
printinfo(70,60,50)
# 如果再函数调用时没有指定参数，它就是一个空元祖，我们也可以不向函数传递任未命名的变量。如下实例：
def printinfo1(agr1, *vartuple):
    # 打印任何传入的参数
    print("输出：")
    print(agr1)
    for var in vartuple:
        print(var)
    return

printinfo1(10)
printinfo1(170,50,60)

# 还有一种就是参数带两个**语法基本如下：
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了两个星号**的参数会以字典的形式导入。
def printinfo2(arg1, **vardict):
    print("输出：")
    print(arg1)
    print(vardict)
printinfo2(1,a=2,b=3)

# 声明函数时，参数中星号*可以单独出现，例如
# def f(a,b,*,c):
#     return a+b+c

# 如果星号* 单独出现，参数必须用关键字传入
def f(a,b,*,c):
    return a+b+c
# f(1,2,3)  报错
print(f(1,2,c=3))

# 匿名函数
# Python使用lambda来创建匿名函数、。
# 所谓匿名，意即不再使用def语句这样标准的形式定义一个函数。
# lanbda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
# lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
# lambda函数的语法只包含一个语句，如下：
# lambda [arg1[,arg2,...........argn]]:expression

sum = lambda arg1,arg2:arg1+arg2
print("相加后的值为：",sum(10,20))
print("相加后的值为：",sum(20,20))

# return 语句
# return【表达式】语句用于退出函数，选择性的向调用方法返回一个表达式，不带参数值的return语句返回None，之前的例子都没有示范如何返回
# 数值，一下实例演示了return语句的用法；
def sum(arg1 , arg2):
    total=arg1 + arg2
    print("函数内：", total)
    return total
total = sum(10,20)
print("函数外：",total)

# 强制位置参数
# Python3.8中新增了一个函数行参语法/用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式
# 在以下的例子中，形参a和b必须使用指定位置参数，C或D可以是位置形参或关键字形参，而e或f要求为关键字形参：
# def f(a,b, / ,c,d,*,e,f):
#     print(a,b,c,d,e,f)

# 以下使用方法是正确的
"""
f(10,20,30,d=40,e=50,f=60)
"""
# 以下使用方法会发生错误：
'''
f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式

'''
