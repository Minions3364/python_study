a = float(input(''))
b = float(input(''))
c = float(input(''))

if a + b > c and a + c > b and b + c > a :
    C = a + b + c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：%f' %(area))
else:
    print("不能构成三角形")