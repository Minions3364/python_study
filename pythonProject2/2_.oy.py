import random
b = random.randint(1,101)
counter = 0
while True:
    counter += 1
    a = int(input('a='))
    if a < b :
        print('小')
    elif a > b :
        print('大')
    else:
        print('猜对啦')
        break
    print('你总共猜了%d次' % counter)
    if counter > 5:
        print('caixu')