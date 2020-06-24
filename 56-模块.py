# 模块：通俗理解一个.py文件就是一个模块，模块是管理功能代码的
# 模块里面可以定义类，数据，全局变量，执行相应的功能代码操作

# 内置模块：就是python自己内部的模块，比如time、random
# 自定义模块：名字和变量名的定义很类似，都是由字母、数字、下划线组成，但是不能以数字开头，否则无法导入该模块


# 主模块：执行的这个模块就是主模块
from first_module import *
import second_module
# 使用模块中的功能代码
# print(g_num) first_module中g_num被限制使用
show()
stu = Student('德芙', 20)
stu.show_msg()

result = second_module.sum_num(1, 3)
print('自定义模块：', result)
# 查看模块名
print(__name__)

