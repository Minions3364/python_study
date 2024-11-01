#字符串也不可被修改
#替代法
my_str = "蔡徐坤唱跳rap"
new_str = my_str.replace("rap","你干嘛")
print({new_str})
#字符串的分割；  按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中； 注意：字符串本身不变，而是得到了一个列表对象
str1= "蔡徐坤 唱 跳"
str1_list = str1.split(" ")
print(str1_list)



str2 = "itheima itcast buxuegu"
count = str2.count("it")
print({count})
new_str2= str2.replace(" ","l")
print({new_str2})
str2_list = new_str2.split("l")

print(str2_list)
