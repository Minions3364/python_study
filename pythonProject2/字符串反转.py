k=input('请输入= ')
#print(k[::-1])               直接对字符串进行切片操作，-1是步长


m_list=[]
for i in k:
    m_list.append(i)

m_list.sort(reverse=True)
print("".join(m_list)) #这样列表就变成了字符串
