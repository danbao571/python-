# 包：通俗理解包就是一个文件夹，只不过文件夹里面有一个__init__.py文件
# 包是管理模块的，模块是管理功能代码的
# --------import导入包里面的模块--------
# 假设有一个包名叫first_package里面有first和second两个模块
# import first_package.first   #****推荐该导入方法****
# import first_package.second
# 假设first里面有一个show方法
# 调用show方法
# first_package.first.show()

# -----------import导入包里面的模块设置别名------
# import first_package as one
# import second_package as two

# one.show()
# two.show_msg()

# ------from导入包名 import 模块名----------
# from first_package import first as one

# ---------from 包名.模块名 import 功能代码
# from first_package.first import show # 需要保证当前模块没有导入模块的功能代码


# ----------from 包名 import *----------
# from first_package import *
# 该方式不会导入包里面的模块，需要在__init__使用__all__去指定导入的模块


# import first_package
# first_package.first.show() # 会报错
# 直接导入包不会导入对应的模块，需要在init文件中自己导入（from first_package import first）

# 在init文件中可以使用在当前模块中导入模块（from.import first）

