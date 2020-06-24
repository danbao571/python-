  # 字符串定义：  只要使用引号（'xx',"xx","""jjj""",'''xxx'''）引起来的数据就叫做字符串

my_list = 'hello'

# 根据指定数据查找对应的下标(索引）
result = my_list.index("e")

print(result)

# 根据指定数据查找对应的下标（索引）
result = my_list.find("h")
print(result)

# find 和 index的区别，find找不到指定数据返回-1，index如果没有找到那么报错。

# 统计字符串长度（个数）
result = len(my_list)
print(result)


# 统计某个字符串出现的次数
result = my_list.count("l")
print(result)

# 替换指定数据
result = my_list.replace("l", 'x')
print(result)

# 分割数据
my_str = "神仔,阿兴,图仔,峰哥"
result = my_str.split(',')
print(result)

# 判断是否以指定数据开头，结尾（endswith）
my_url = "http://www.baidu.com"
result = my_url.startswith("http")
print(result)

# 需求：把字符串以指定字符串分割数据成三部分
my_str = "aaabbbccc"
result = my_str.partition("bbb")
print(result)

# join:根据指定字符串拼接数据，前提是最终的数据是字符串
# 指定字符串数据（以.连接神仔啊）
flag_str ="."
my_str = "神仔啊"
result = flag_str.join(my_str)
print(result)

# 去除空格
my_str = ' hello '
result = my_str.strip()
print(result)
# 去除前面空格
my_str = ' hello '
result = my_str.lstrip()
print(result)
# 去除后面空格
my_str = ' hello '
result = my_str.rstrip()
print(result)



