# 定义全局变量

# 定义不可变类型全局变量
g_num = 10
print("函数外：", id(g_num))

def modify():
    #声明要修改全局变量
    global g_num
    g_num = 1
    print("modify", g_num)
    print('函数内：', id(g_num))

modify()
print(g_num)

# 定义可变类型全局变量
g_list = [3, 5]
print("函数外：", id(g_list))

def modify():
    # 在原有数据的基础上添加了一个数据
    # 如果只是修改数据，那么这里可以不需要加上global
    # g_list.append(4)
    # 加上global表示内存地址要发生改变(内外都会改变但还是一样)
    # global g_list
    g_list.append(4)
    print("modify:", g_list)
    print('函数内：', id(g_list))

modify()

print(g_list)