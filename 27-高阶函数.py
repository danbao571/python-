# 高阶函数：当一个函数的参数可以接收另外一个函数或者返回一个函数，那么这样的函数就叫高阶函数
# 高阶函数针对的是接收或者返回的是函数，那么类似于这样的函数统称高阶函数

def sum_num(num1, num2):
    result = num1 + num2
    return result

# 高阶函数，因为接收的参数是一个函数
def calc_num(num1, num2, new_func):
    value = new_func(num1, num2)
    return value

result = calc_num(1, 2, sum_num)
print(result)

# 高阶函数，还可以返回一个函数
def test(new_func):
    new_func()
    def inner():
        print("我是内部函数")
    return inner

def show_msg():
    print("sadd")


new_func = test(show_msg)
new_func()