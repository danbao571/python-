# 类的定义需要使用class关键字，人是有特征和行为（动作）
# 类里面有属性（特征）和（行为）

# 定义学生类，这是旧式类，自己不主动继承object，在python3里面旧式类默认继承object。
# 在python2里面就没有父类。
class Student:
    # 类属性
    country = "中国"

    # 方法
    def show(self):
        print("哈哈，我是一个学生")

# 通过类创建对象，类好比一个模具，模具可以创建多个对象
student = Student()  # 类名(),表示创建了一个对象
# 调用方法，对象名.方法名
student.show()
# 查看Student类继承的父类
print(Student.__bases__)


# 新式类的定义
class Student(object):
    # 类属性
    country = "中国"

    # 方法
    def show(self):
        print("afsfaf")

print(Student.__bases__)
S1 = Student()
S1.show()