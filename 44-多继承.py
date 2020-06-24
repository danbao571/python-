class A(object):
    def show(self):
        print('我是A类')


class B(object):
    def show_info(self):
        print('我是B类')

        # show()方法先被A使用
        def show(self):
            print('我是c类')


class C(A, B):
    pass


c = C()
c.show()
c.show_info()
# 在python里面方法的调用会遵循mro，类继承顺序，决定了方法调用时的查找顺序
print(C.mro())
