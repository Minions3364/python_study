my_list = ["wkd",777,True]
print(my_list)
print(type(my_list))         #['wkd', 777, True] ,<class 'list'>

#嵌套列表
your_list = [[1,2,3] , ["a", "b", "c"]]
print(your_list)
print(your_list[0])
print(your_list[1])
print(your_list[-1])
print(your_list[1][0])             #通过下标索引取数据，一定不要超出范围

#查找下标索引
index = my_list.index("wkd")
print({index})

#修改特定位置的值
my_list[0]="kb"
print(my_list[0])
print(my_list)

#列表插入元素     语法：列表.insert（下标，元素），在指定的下标位置，插入指定的元素
my_list.insert(1,666)
print(my_list)
#追加元素        语法：列表.append（元素），将指定元素，追加到列表的尾部
my_list.append(888)
print(my_list)
#追加一批元素    语法：列表.extend(其他数据容器），将其他数据的内容取出，依次追加到列表尾部
my_list.extend(your_list)
print(my_list)
#列表元素的删除    语法：del列表【下标】；或者 列表.pop（下标）{不仅能删除，还能将元素作为返回值得到}
del my_list[3]
print(my_list)

element =my_list.pop(2)
print(my_list,{element})
#删除某元素在列表中的第一个匹配项        语法：列表.remove（元素）     【记住是第一个匹配项】
my_list.append(888)
print(my_list)
my_list.remove(888)
print(my_list)
#清空列表
your_list.clear()
print(your_list)
#统计某元素在列表内的数量        语法：列表count（元素）
my_list.count(888)
print(my_list.count(888))
#统计列表中有多少个元素    语法：len（列表）
count = len(my_list)
print({count})

#内容练习
first_list = [21,25,21,23,22,20]
first_list.append(31)
print(first_list)
second_list = [29,33,30]
first_list.append(second_list)
print(first_list)
ele1 =first_list.pop(0)
print({ele1})
ele2 =second_list.pop(-1)
print({ele2})
index = first_list.index(31)
print({index})



