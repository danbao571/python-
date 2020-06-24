# 定义必须参数使用关键字传参的函数
def show(address, sex, *, name, age):
    print(address, sex)
    print("我叫：%s 年龄:%d" % (name, age))

show('上海', '男', name='神仔', age=19)
show(address='上海', sex='男', name='神仔', age=19)
