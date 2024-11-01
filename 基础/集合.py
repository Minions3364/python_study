#集合添加新元素的用法
set={"wkd",777,True}
set.add(888)
print(set)
#移除元素
set.remove(777)
print(set)
#set.pop()                 随机取出
#取出两个集合的差集（取出集合1和集合2的差集【集合1有但集合2没有的】）
set1={1,2,3}
set2={1,4,5}
new_set= set1.difference(set2)           #语法
print(new_set)
#在集合1内，删除和集合2相同的元素         语法：set1.difference_update(set2)
set1.difference_update(set2)
print(set1)
#2个集合合并
set3=set1.union(set2)       #语法
print(set3)