# 匿名函数：顾名思义就是函数没有名字，使用lambda关键字定义的函数就是匿名函数

result = (lambda x, y: x+y)(1, 2)
print(result)

# 一般使用变量保存匿名函数
dunc = lambda x, y: x+y
result = dunc(1, 4)
print(result)

# 匿名函数简单应用
def is_os(num):
    if num % 2 == 0:
        return True
    else:
        return False
result = is_os(1)
print(result)

new_func = lambda num: True if num % 2 == 0 else False

result = new_func(3)
print(result)

# 对字典列表排序
my_list = [{'name': '神仔', 'age': 20}, {'name': '阿兴', 'age': 19}]
# item：表示列表中每一项字典数据
# item["age"]:表示子典中age对应的value值
# sort排序默认从小到大进行，倒序在后面加reverse = True
my_list.sort(key=lambda item: item["age"], reverse=True)
print(my_list)

# 使用普通函数
def get_value(item):
    return item["age"]

my_list.sort(key=get_value, reverse=True)
print(my_list)