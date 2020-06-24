# 定义一个装饰器函数（无返回值）
def decorator(func):
    def inner(num1, num2):
        print('计算结果如下：')
        func(num1, num2)
    return inner

@decorator # =>  sun_num = decorator(sun_num)
def sum_num(num1, num2):
    result = num1 + num2
    print(result)

sum_num(1, 2)

# -------------------------------------------
# 定义一个装饰器函数(有返回值)
def decorator(func):
    def inner(num1, num2):
        print('计算结果如下：')
        return func(num1, num2)
    return inner

@decorator # =>  sun_num = decorator(sun_num)
def sum_num(num1, num2):
    result = num1 + num2
    return result

result = sum_num(1, 2)
print(result)