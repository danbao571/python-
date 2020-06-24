# 装饰器本质上就是一个函数，可以对原函数的功能进行扩展，这样可以在不改变圆函数的定义及调用增加功能

def show():
    print("112321")

show()

# 装饰器-》 通过闭包完成装饰器
def decorator(new_func):

    def inner():
        print("-" * 10)
        new_func()
    # 返回的是闭包
    return inner

show = decorator(show)

show()

# ----------------------------------------

def decorator(new_func):

    def inner():
        print("-" * 10)
        new_func()
    # 返回的是闭包
    return inner

# 使用@decorator的时候装饰器里面的代码就会执行
@decorator  # 等价于show = decorator(show)
def show():
    print("112321")

show()