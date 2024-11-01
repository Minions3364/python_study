#对列表进行简单的排序
#怎么原地排序？是升序还是降序？
lista =[2,5,1,4,3]
listb =['e','b','a','c','d']
listc=list(set(lista))
listd=list(set(listb))
print(listc)
print(listd)
"""
def re_se(lista):
    for item in lista:
        if item <
"""
lista =[2,5,1,4,3]
lista.sort(reverse=True)                 #list.sort()  列表排序的用词
listb=sorted(lista, reverse=True)        #reverse=True 实现降序的功能 ，如果是升序，reverse=False
print(lista)
print(listb)


#复杂列表，元素是字典或者元组
listk=[{'c':1},{'a':2},{'b':22}]
listg=sorted(listk,key=lambda x:list(x.keys())[0])
#lambda x: list(x.keys())[0] 表示我们对每个字典的键进行排序。
# 在每个字典中，x.keys() 会返回键名的列表，list(x.keys())[0] 获取第一个键。
print(listg)