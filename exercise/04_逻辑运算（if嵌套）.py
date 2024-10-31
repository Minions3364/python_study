has_ticket=True
knife_length=30
if has_ticket:            #if has_ticket==True: （这是我写的）
    print("车票通过，可以安检")
    if knife_length<20:
        print("安检通过")
    else:
        print("刀的长度不通过，有 %d 公分长！" % knife_length)
else:                               #else后面不用加has_ticket=Fasle: 了，这样会显示代码错误，直接else：就可以了
    print("大哥请买票")

