class Student():
    def show(self):
        print("我是德芙")

# 创建对象
student = Student()

# 动态添加对象属性
student.name = "德芙"
student.age = 18


# 获取数据对应的属性
print(student.name, student.age)


# 修改属性
student.name = "流火之月"
print(student.name, student.age)

student.show()
