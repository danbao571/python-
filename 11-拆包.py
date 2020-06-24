# 拆包：把容器类型（字符串，列表，元组，字典，集合）中美一个数据使用不同变量进行保存

my_str = 'sacf'
# 注意点：变量个数要个容器里的数据个数一致
a, b, c, d = my_str
print(a, b, c, d)

my_list = [1, 5]
num1, num2 = my_list
print(num1, num2)

my_tuple = (1, 5)
num1, num2 = my_tuple
print(num1, num2)

my_dict = {'name': 'Benson', 'age': 12}.values()
key1, key2 = my_dict
print(key1, key2)

my_set = {3, 5}
num1, num2 = my_set
print(num1, num2)
