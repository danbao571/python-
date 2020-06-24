import sys
# 递归函数：在函数里面再调用函数本身就是递归函数
# 递归函数的特点：1传递，2回归

def calc_num(num):
    # 计算1的阶乘的时候不需要往下传递，需要返回结果
    if num == 1:
        return 1
    else:
        return num * calc_num(num-1)

result = calc_num(6)
print(result)

# 不能无限递归调用，默认次数是1000
# 获取默认递归次数
result = sys.getrecursionlimit()
print(result)
# 设置递归次数
sys.setrecursionlimit(1100)