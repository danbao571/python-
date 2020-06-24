# 缺省参数： 在函数定义时就一直有值，这样的参数就叫缺省参数

def sum_num(num1, num2=4):
    result = num1 + num2
    return result
# 没有给函数的第二个参数传值，那么使用默认值（缺省值）
value = sum_num(1)
# value = sum_num(1, 3)
print(value)