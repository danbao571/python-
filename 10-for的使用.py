# 获取容器类型（字符串，元组，列表，字典，集合）中的每一个数据使用for循环是最简单的

my_str = 'alas'
for value in my_str:
    print(value)

# 循环遍历时候下标和数据都需要可以使用enumerate
my_list = ['苹果', '神仔']
for value in my_list:
    print(value)

my_list = enumerate(['苹果', '神仔'])
for value in my_list:
    print(value[0], value[1], type(value))

# index,value获取的是元组中的每一个值，就是拆包
for index, value in enumerate(['苹果', '神仔']):
    print(index, value)

# 遍历字典默认是遍历key
for key in {'name': 'Benson', 'age': 21}:
    print(key)
# 取value
for key in {'name': 'Benson', 'age': 21}.values():
    print(key)
# 取key和value
for key, value in {'name': 'Benson', 'age': 21}.items():
    print(key, value)
for item in {'name': 'Benson', 'age': 21}.items():
    print(item)
