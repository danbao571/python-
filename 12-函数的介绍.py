# 函数：就是某一个功能的代码的实现，使用函数可以对代码进行复用

# def 函数名（参数【可选】）
#    功能代码的实现

# 定义函数， 不会调用
def show():
    print('sadbfas')
# 调用函数
show()

# 函数的四种类型

# 无参数无返回值
def show():
    print("asdni")

show()

# 有参数无返回值
def show(name, age):
    print("我叫%s, 年龄：%d" % (name, age))

show("张三丰", 18)

# 无参数有返回值
def return_value():
    msg = "好好学习，天天向上"
    return msg
resule = return_value()
print(resule)

# 有参数有返回值
def show_msg(name, age):
    msg = '我叫:%s 年龄：%d' % (name, age)
    return msg
resule = show_msg("李四", 18)
print(resule)