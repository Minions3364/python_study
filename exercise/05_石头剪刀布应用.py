#导入随机工具包
#注意：在导入工具包的时候，应该将导入的语句，放在文件的顶部
#因为，这样可以方便下边的代码，在任何需要的时候，使用工具包中的工具
import random
player = int(input("石头是（1） 剪刀是（2） 布是（3）:"))
computer = random.randint(1, 3)
print('玩家选择的拳头是%d - 电脑出的拳是%d' % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("弱爆了")
elif player == computer:
    print("真是一场酣畅淋漓的战斗，再来！")
else:
    print("电脑你这个老六，我不服！")
