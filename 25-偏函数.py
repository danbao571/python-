import functools
# 偏函数：通俗理解指明函数的参数偏爱某个值这样的函数叫做偏函数

def show(num1, num2, num3=1):
    result = num1 + num2 + num3
    return result

result = show(1, 3)

print(result)

# 定义一个偏函数
def show2(num1, num2, num3=2):
    result = show(num1, num2, num3)
    return result

result = show2(1, 3)

print(result)

# --------------------------------------

# 指明函数的参数设置为某个值
new_func = functools.partial(show2, num2=3)
result = new_func(4)

print(result)

# 指明内置函数的参数偏爱某个值，生成一个偏函数

new_func = functools.partial(int, base=2) # 以二进制为基础把数据转化成十进制
result = new_func('11111111')
print(result)