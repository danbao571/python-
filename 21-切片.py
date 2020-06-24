# 切片：根据下标的范围获取一部分数据，比如：列表，字符串可以使用切片

my_str = 'hello'

result = my_str[1]
print(result)

# 切片使用格式
# 数据【起始下标：结束下标：步长】
# 提示：起始下标默认0，结束下标不包含，步长默认1

result = my_str[1:3]
print(result)

# 使用负数切片方式
result = my_str[-1:0:-1]
print(result)
