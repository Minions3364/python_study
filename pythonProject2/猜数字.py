import random

a = int(input('请输入 '))
for i in range(0,101):
    count = 0
    if a < i:
        print("猜小了")
    elif a > i:
        print("猜大了")
    else:
        print("猜对了")
    count +=1
print(f"猜对了{count}次")
