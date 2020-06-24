# continue：结束本次循环，然后可以继续下次循环，整个循环不一定结束

# break：跳出当前循环，当前循环执行结束

# 提示：continue和break不能单独使用，只能在循环语句中使用

num = 1

while num <= 5:
    if num == 2:
        num += 1
        # 执行continue结束本次循环，continue后面的代码不会执行
        continue
    print(num)
    num += 1
else:
    print("循环数据结束")

num = 1

while num <= 5:
    if num == 2:
        num += 1
        # 执行break结束当前循环，break后面代码也不会执行
        break
    print(num)
    num += 1
else:
    # 如果循环语句里面执行了break那么else不会执行
    print("循环数据结束")

print('----------------')

for value in range(1, 5):
    if value == 2:
        # 结束本次循环
        continue
    print(value)
else:
    print("循环数据结束")
print('----------------')

for value in range(1, 5):
    if value == 2:
        break
    print(value)
else:
    print("循环数据结束")

# 总结： 循环语句里面只要不执行break那么就是执行else语句

name = input("请输入姓名：")
for value in['张三', '李四']:
    if value == name:
        print(value)
        break
else:
    print("没有这个人")
