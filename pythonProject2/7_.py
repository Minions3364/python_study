#计算范围内所有的偶数
list=[]
def caixu(a,b):
    list = []
    for num in range (a, b+1):
        if num % 2 ==0:
            list.append(num)
    return list
print(caixu(1,100))

