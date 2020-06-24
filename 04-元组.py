# 元组：以小括号表现形式的数据集合， 比如：（1,2,'asc'）
# 元组也可以存放任意数据
# 元组只能根据下标获取数据，不能直接对元组进行数据修改
my_tuple = (1, 4, ['sad', '萨达'])
print(my_tuple)

value = my_tuple[0]
print(value)

# 通过列表修改元组数据
# 获取列表
my_list = my_tuple[2]
# 根据列表修改数据
my_list[1] = 2
print(my_tuple)

# 注意点：如果元组中只有一个元素，那么需要加上一个逗号
my_tuple = (5,)

print(my_tuple, type(my_tuple))


# 判断数据是否存在
my_tuple = (5, 10)
result = 5 in my_tuple
print(result)

# 数据在元组中的位置
index = my_tuple.index(5)
print(index)

# 数据在元组中出现的次数
result = my_tuple.count(10)
print(result)
