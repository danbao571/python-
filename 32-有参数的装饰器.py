def get_decorator(char):
    # 定义一个装饰器
    def decorator(func):
        def inner():
            print(char*10)
            func()
        return inner
    return decorator

# 把@后面的操作相当于执行了一个函数，返回了一个装饰器
@get_decorator('4')   # 有参数的装饰器
def show():
    print('12341')

show()