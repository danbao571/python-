# 函数的嵌套
# 返回函数：在函数里面返回一个函数

def show():
    def inner():
        print("神仔")
    # 返回了一个函数
    return inner

# 获取返回的函数
new_func = show()
# 执行返回的函数
new_func()

def calc(operation):
    if operation == '+':
        def sum_num(num1, num2):
            result = num1 + num2
            return result
        return sum_num

    if operation == '-':
        def jq_num(num1, num2):
            result = num1 - num2
            return result
        return jq_num

new_func = calc('-')

result = new_func(1, 4)
print(result)