
radius = float(input('半径是：'))
if radius != 0 :
    area = radius * radius * 3.14
else:
    area = 0
print(f'园的面积是%.2f' %area)
'''
在使用 print(f'园的面积是%d' % area) 时，%d 表示你希望输出一个 整数，即使 area 是浮点数，输出时也会被自动转换为整数
为了正确输出浮点数的面积，你可以使用 %.2f 来控制小数点后的位数，比如保留两位小数，或者直接使用 print(f'园的面积是{area}') 来输出完整的浮点数
'''


#用定义函数导入包的方式
import math
def aera(r):
    return round(math.pi * r * r, 2)    #这里的round （。。。。。，2）表示保留两位小数
print('aera是', aera(4))