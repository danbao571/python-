# 带@的类或方法为语法糖，☞那些没有给计算机语言添加新功能，而只是对人类来说更“甜蜜”的语法。

class Student(object):
    def __init__(self):
        self.__score = 100

    # 把方法改成对应的属性
    # 获取值
    @property
    def get_score(self):
        return self.__score
    # 设置值
    @get_score.setter
    def set_score(self, score):
        self.__score = score


stu = Student()
# score = stu.get_score()
# print(score)
#
# stu.set_score(99)
# score = stu.get_score()
# print(score)

score = stu.get_score  # 调用get_score时没有（），以为其改为属性调用。
print(score)
stu.set_score = 80
score = stu.set_score
print(score)
