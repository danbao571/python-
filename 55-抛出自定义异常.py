# 自定义异常
class CustomException(Exception):
    def __init__(self, content):
        self.content = content

    # 表示抛出异常显示的异常描述信息
    def __str__(self):
        return "我是自定义异常，因为数据不是a，异常数据为：%s" % self.content

# 这里的异常是系统抛出的，然后系统会指定异常信息
# a = 10
# del a
# print(a)


content = input('输入一个数据：')
if content != 'a':
    # 抛出自定义异常
    raise CustomException(content)
    # raise NameError("name a is not defined")
    # raise只能抛出异常类型
