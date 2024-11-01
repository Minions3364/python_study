"""
def get_jc(number):
    result = 1
    while number > 0:                               #while 循环 结束时  要记得return 接受返回值
        result *= number
        number -= 1
    return result
print(get_jc(6))
"""


def is_sushu(number):
    if number < 2:
        return False
    for i in range(2,int(number  ** 0.5 + 1)):
        if number  % i ==0:
            return False
    return True

list=[]
for number in range(1,31):
    if is_sushu(number):
        list.append(number)
print(list)

