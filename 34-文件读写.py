# 文件访问模式
# 1.r:只读。文件不存在会崩溃
# 2.w:只写。
# 3.a:追加写
# 4.rb:以二进制方式读取文件数据
# 5.wb:以二进制方式写入文件数据
# 6.ab:以二进制方式追加写入文件数据
# 7.r+,w+,a+,支持读写
# 8.rb+，ab+，wb+ 支持二进制方式读写
# -----------------r模式-------------------

# 打开文件使用open函数
file = open("1.txt", "r", encoding="utf-8")  # 默认是r模式，r表示只读
# 读取文件中的数据
content = file.read()  # 读取文件中的所有数据
print(content)
# 关闭文件
file.close()

# --------------------w模式-----------------
# 提示：w模式：如果文件不存在，那么会创建一个文件并打开，然后写入数据
# 提示：w模式:如果文件存在，那么会把原有的数据清空，然后再写入
# 打开文件
# 提示：如果在windows开发python，那么需要指定编码格式
# 在mac和linux上编码模式默认是utf-8
file = open("1.txt", 'w', encoding="utf-8")
# 查看编码格式
print(file.encoding)
# 写入数据
file.write("ga")
# 文件多次写入不会覆盖前面的数据
file.write("在VR去")
# 关闭文件
file.close()


# ----------------a模式追加写入数据------------------
file = open("1.txt", 'a', encoding="utf-8")
file.write("ae")
file.close()

# 在python2里面不支持文件中有中文，需要指定编码格式
# _*_ coding:utf-8 _*_
# 在python3里面默认是支持中文的，使用utf-8编码的

# ------------------rb模式以二进制模式读取数据-------------
# 二进制模式不需要指定编码格式
file = open("1.txt", 'rb')
file_data = file.read()
# 对二进制数据进行utf-8解码,二进制到字符串叫解码
content = file_data.decode("utf-8")
print(content)
file.close()

# -------------------wb模式以二进制方式写入数据------------
file = open("1.txt", 'wb')
# 字符串到二进制叫编码
# 对字符串进行utf-8编码得到二进制数据
content = "jyhgklj哈 哈"
file_data = content.encode("utf-8")
file.write(file_data)
file.close()

# ---------------------ab模式追加写入数据-------------
file = open("1.txt", 'ab')
content = "hello 哈哈" # 一个中文占用三个字节，一个字母和数字占用一个字节
file_data = content.encode("utf-8")
file.write(file_data)
file.close()

# ---------------------r+读写-----------------
file = open("1.txt", 'r+', encoding="utf-8")
result = file.read()
print(result)
# 提示：写入数据不会清空数据，会把指定位置数据替换成写入的数据，其他数据不变
file.write("aff")
file.close()