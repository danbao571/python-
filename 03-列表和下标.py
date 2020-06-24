# 列表： 以括号表现形式的数据集合，  比如：[1,4]

my_list = [1, 1.2, "asd", "神仔", True]

# 获取列表中的数据可以根据下标获取
value = my_list[0]
print(value)

# python中的下标其实就是一个编号，可以根据编号找到某个数据，在python中可以有正数和负数下标
# 正数下标：默认从零开始，0：表示一个元素， 负数下标：-1便是倒数第一个数据

result = my_list[-1]
print(result)

result = my_list[-4]
print(result)

result = my_list[3]
print(result)

# 列表的增删改查
my_list = []  # 一个空的列表


# 向列表增加一个指定数据
my_list.append(1)
print(my_list)
my_list.append("阿兴")
print(my_list)

my_list1 = ["图仔", "as"]
my_list.append(my_list1)
print(my_list)


# 向列表插入指定数据
my_list.insert(1, '峰哥')
print(my_list)

# extend:把列表中数据放进大列表（扩展一组数据）
my_list.extend(my_list1)
print(my_list)

# 修改数据
my_list[0] = '鸠华'
print(my_list)

# 删除数据
# remove删除指定数据
my_list.remove("鸠华")
print(my_list)

# 根据下标删除指定数据
del my_list[0]
print(my_list)

# 注意点：下标要合法

# 根据下标删除并返回指定数据（返回的是删除的数据）
my_list = ['你好', '西华', 'asd']
# 切片
result = my_list[1:3]
print(result)
# pop不指定下标默认删除倒数第一个数据
result = my_list.pop()
print(result, my_list)

result = my_list.pop(0)
print(result, my_list)

# 判断指定数据是否在列表中
my_list = ['你好', '西华', 'asd']

result = '西华' in my_list
print(result)

result = '西华' not in my_list
print(result)

index = my_list.index('你好')
print(index)

# 根据指定数据获取数据在列表中的个数
count = my_list.count('芒果')