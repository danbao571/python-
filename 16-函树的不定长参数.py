# 函数的不定长参数：1不定长位置参数，2不定长关键字参数

# 不定长参数：调用函数时不确定传入多少个参数，可能是0个或多个

# 定义一个不定长位置参数(*args）
def sun_num(*args):
    # 提示：args：会把调用函数传入的位置参数封装到一个元组里面，如果没有传入参数那么是一个空元组
    print(args, type(args))

    # 计算结果变量
    resule = 0
    for value in args:
        resule += value

    return resule


# 调用不定长位置参数的函数
vaule = sun_num(1, 4, 5, 6)
print(vaule)

# 注意：*args表示定义的函数时不定长位置参数，调用函数时只能按位置参数传参
# -----------------------不定长关键字函数的定义及调用---------------------------

# 定义不定长关键字参数函数，**kwargs：表示的就是一个不定长关键字参数
def show_msg(**kwargs):
    # kwargs：会把函数调用的关键字参数封装到字典里面
    print(kwargs, type(kwargs))

    for key, value in kwargs.items():
        print(key, value)
show_msg(a = 1, b = 8)
