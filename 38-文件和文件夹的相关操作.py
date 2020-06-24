# file = open("4.txt", 'w', encoding='utf-8')
# file.write('asd')
# file.close()

import os  #文件和文件夹操作相关的模块（py文件）
import shutil
# 重命名，提示：目标文件或文件夹要存在
# os.rename("1.txt", "01.txt")
# 创建文件夹
# os.mkdir("aaa")
# os.rename("aaa", 'bbb')
# 1.指定路径创建
# file = open("bbb/1.txt", 'w', encoding='utf-8')
# file.close()

# 2.切换到指定BBB目录创建，默认的路径是py文件操作得路径
# 查看操作目录的路径
# current_path = os.getcwd()
# print(current_path)
# # 切换到指定目录
# os.chdir("bbb")
# current_path = os.getcwd()
# print(current_path)

# file = open("2.txt", 'w', encoding="utf-8")
# file.close()

# 既可以修改文件夹也可以同时修改文件名
# os.renames("bbb/2.txt", "sss/3.txt")

# 查看目录下的文件名列表信息
file_name_list = os.listdir("bbb")
print(file_name_list)

os.chdir("bbb")
current_path = os.getcwd()
print(current_path)
# ".":表示当前目录，"..":表示上一级目录
file_name_list = os.listdir()  # os.listdir() = os.dir.listdir(".")
print(file_name_list)

# # 删除文件
# os.remove("sss/3.txt")
# # 删除文件夹
# os.rmdir("sss")
# # rmdir只能删除空目录

# 删除目录树
# shutil.rmtree("sss")

# 扩展
# 获取1.txt的绝对路径，从根目录（/，c\d\e\f等）算起的路径叫做绝对路径
# 相对路径：从当前目录算起的路径叫做相对路径。

abs_path = os.path.abspath("1.txt")
print(abs_path)

# 根据绝对路径获取路径中的文件名
file_name = os.path.basename(abs_path)
print(file_name)
# 1.txt

# 获取文件名和文件名后缀
file_name, file_extend = os.path.splitext(file_name)
print(file_name, file_extend)
# 1.txt