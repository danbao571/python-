# 局部变量：在函数内定义的变量叫局部变量，局部变量只能在函数内使用，不能再函数外使用

def show():
    # 局部变量
    score = 100
    print("分数", score)
show()

# 全局变量：在函数外定义的变量叫全局变量，全局变量可以在不同函数内使用

score = 100

def show():
    # 修改全局变量
    global score   #表示要对全局变量score进行数据的修改
    score = 99
    print('分数:', score)
show()

def show():
    print('分数:', score)
show()
