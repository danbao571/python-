# 1.打开原文件读取数据
# rb模式：是比较通用的模式，可以兼容不同类型的文件
src_file = open('3.txt', 'rb')
# 读取文件中的全部数据
file_data = src_file.read()
# 2.打开目标文件准备写入数据
# 可以指定拷贝后的文件路径
dst_file = open("/Users/****/***/Desktop/3[副本].txt", 'wb')
# 把原文件中的数据写入到目标文件中
dst_file.write(file_data)
# 关闭文件
dst_file.close()
src_file.close()