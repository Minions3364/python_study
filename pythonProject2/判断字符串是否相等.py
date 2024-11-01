'''
s1= "abc"
s2 = "cba"
s3 = str(sorted(s2,reverse=False))
print(s3)
if s3 == s2:
    print(s3)
else:
    print("发生错误")
'''
s1= "abc"
s2 = "cba"
print(sorted(s1))
print(sorted(s2))
print(sorted(s1) == sorted(s2))    #直接在print 语句里进行相等比较，如果是对的输出True，反之为False；