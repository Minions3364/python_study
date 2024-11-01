#定义元组
t1= ()
t3=tuple()
t2=(1,2,"wkd",True)
#定义单个元素元组，元素后面要再加个逗号
t4=("hello")
print({type(t4)})   #这是字符串
t4=("hello",)     #这是元组
#元组也可以嵌套
t5=((1,2,3),(4,5,6))
#从嵌套元组中取数据，写法和列表一样
num = t5[1][2]
print({num})

t7=("蔡徐坤",18,["sing","jump","basketball"])
index = t7.index(18)
print(f"学生年龄的下标是{index}")
name= t7[0]
print(f"学生的姓名是{name}")
del t7[2][2]
t7[2].append("coding")
print(t7)