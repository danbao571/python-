# 闭包：在函数嵌套的情况下，内部函数使用了外部函数的参数或者变量
# 并把这个内部函数返回，那么返回的内部函数可以称为闭包（对应的就是一个函数）

def show():
    num = 10
    def inner():
        print(num)
    return inner
new_func = show()


new_func()

# 通过闭包可以生成不同的函数
def hello(msg, count):
    def return_msg():
        result = msg * count
        return result
    return return_msg

new_func1 = hello("a", 2)
result = new_func1()
print(result)

new_func2 = hello("b", 2)
result = new_func2()
print(result)