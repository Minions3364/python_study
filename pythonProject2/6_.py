list=[124,5,65476,76,5756,7568]
def sum_list():
    result = 0
    for num in list:
        result += num
    return result
print(sum_list())
"""八嘎！！！
for num in range(list[0],list[6]):   怎么会有这样的写法！！！
改成 for num in list:    就行了  
循环逻辑错误：你使用了 range(list[0], list[6])，这只是在两个数字之间生成一个范围，而不是遍历列表中的所有元素。如果要遍历列表的所有元素，你应该直接遍历 my_list 而不是生成一个范围
"""