# 异常：当前使用python解释器去执行代码时，遇到了错误，在控制台输出错误信息
# 代码遇到异常会中止执行
# name = '张三'
# name + 10


# 提示：多数异常类都是继承Exceotion
try:
    num1 = input('请输入一个数字：')
    num2 = input('请输入另一个数字：')

    result = int(num1) + int(num2)
    print(result)
except ValueError as e:  # 表示异常对象
    print(e, type(e))

try:
    name = 'zs'
    del name

    # 在try里面如果执行代码遇到了异常那么不会在执行try语句里面的代码，会执行except里的代码
    print(name)
    result = 1/0
    print(result)
# except (NameError, ZeroDivisionError) as e:
except NameError as e:
    print(e, type(e))
except ZeroDivisionError as e:
    print(e, type(e))
else:
    print('代码没有异常会执行else')
finally:
    print('有没有异常都会执行')