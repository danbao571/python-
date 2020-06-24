# 1.打开原文件读取数据
# rb模式：是比较通用的模式，可以兼容不同类型的文件
src_file = open('3.txt', 'rb')
dst_file = open("3[副本].txt", 'wb')
# 循环读取文件中的数据
while True:
    file_data = src_file.read(1024)
    # 判断数据是否读取完成
    # if len(file_data) > 0:
    # 判断二进制类型是否有数据
    if file_data:
        # 表示有数据
        # 把原文件中的数据写入到目标文件
        dst_file.write(file_data)
    else:
        print("数据读取完成：", file_data)
        break
# 关闭文件
dst_file.close()
src_file.close()