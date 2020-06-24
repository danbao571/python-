# 集合（set）：以大括号表现形式的数据集合，集合里面不能有重复数据，集合无序

# 集合根据下标获取数据和修改数据，可以添加和删除

my_set = {1, 4, 'abc', 'hello'}
print(my_set)
my_set.remove("abc")
my_set.add('bcd')
print(my_set)

# 添加数据
my_set.add(5)
print(my_set, type(my_set))

# my_set.remove('abc')
# my_set.discard('abcd')
# 总结：remove删除数据，数据必须存在，否则会奔溃；discard：删除数据，数据不存在会忽略，不会奔溃

# print(my_set)

for value in my_set:
    print(my_set)

# 定义空的集合时不能直接使用{}，否则是字典类型

my_set = set()
my_set.add(1)
print(my_set, type(my_set))

# 集合可以对容器类型数据去重
my_list = [1, 2, 3, 4, 4]
print(my_list)

my_set = set(my_list)
print(my_set)

my_list = list(my_set)
print(my_list)
