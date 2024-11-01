my_list = ["wkd", 777, True]
#循环控制变量通过下标索引来控制，默认为0
#每一次循环将下标索引变量+1
#循环条件：下标索引变量  ＜ 列表的元素数量
# 1、while 循环
index = 0
while index < len(my_list):
    element = my_list[index]
    index += 1
    print({element})

