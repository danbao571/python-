# 列表生成器（列表推导式）：一般使用for循环快速创建一个列表，最终要获取一个列表

# 正常创建列表
my_list = []
for i in range(1, 6):
    my_list.append(i)
print(my_list)

# 列表推导式创建列表
my_list = [i for i in range(1, 6)]
print(my_list)

my_list =[value * 2 for value in range(1, 6)]
print(my_list)

my_list = [len(value) for value in ['asd', 'asdfg', '神仔']]
print(my_list)

my_list = [value for value in range(1, 11) if value % 2 == 0]
print(my_list)


