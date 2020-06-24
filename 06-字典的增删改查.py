# 定义空的字典
my_dict = {}
print(my_dict)

# 增加键值对
my_dict["name"] = "张三"
my_dict["age"] = 22
my_dict["sex"] = '男'
my_dict["address"] = '北京'
print(my_dict)

# 修改键值对，key存在就是修改键值对
my_dict["address"] = '上海'
print(my_dict)

# 删除键值对
del my_dict['age']
print(my_dict)

# 随机删除键值对返回key和value(字典无序)
# value = my_dict.popitem()

# 指定key删除键值对，返回key对应value
value = my_dict.pop('sex')
print(value, my_dict)

# 判断key是否存在
result = "age" in my_dict
print(result)

result = "age" in my_dict.keys()
print(result)

# 获取字典中所有的value
result = "张三" in my_dict.values()
print(result)