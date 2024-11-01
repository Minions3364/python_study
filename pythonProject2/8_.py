# 删除列表中的元素
lista= [3,5,7,9,11,13]
listb= [7,9]
def dele(lista,listb):
    for num in listb:
        lista.remove(num)
    return lista
print(dele(lista,listb))

lista= [3,5,7,9,11,13]
listb= [7,9]
data=[num for num in lista if num not in listb]      #一行代码搞定  ，{“列表推导式”}
print(data)

listc=[1,2,3,1,2]
lis=[]
[lis.append(item) for item in listc if item not in lis ]           #列表推导式的正确用法应该是返回一个新列表，而不是依赖 append()
print(lis)

listc=[1,2,3,1,2]
listd=list(set(listc))
print(listd)