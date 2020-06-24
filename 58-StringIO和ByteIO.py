# ----------StringIO-------------
# 把字符串数据写入到内存
import io
from io import BytesIO
# StringIO的操作和文件写入和读取的操作很类似
str_io = io.StringIO()

# 向内存写入数据
str_io.write('hello')
str_io.write('world')

# 获取数据
# content = str_io.getvalue()
# print(content)

# 设置文件指针的位置到文件开头
str_io.seek(0)
# 默认全部读取
# read(2):读取指定长度（2）
result = str_io.read()
print(result)

# --------------ByteIO---------------------
byte_io = BytesIO()

# 向内存写入数据
byte_io.write('哈哈'.encode('utf-8'))
# 读取数据，获取写入到内存中的全部数据
data = byte_io.getvalue()
print(data)

content = data.decode('utf-8')
print(content)