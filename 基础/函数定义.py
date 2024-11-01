"""
def check() :
    print("hello world")

check()

def''' add(x ,y) :
    result=x + y
   return result           #这一步出错了，是print结果出来

def add(x , y) :         #定义的x , y  表示为形式参数  ，调用的7，8是实际参数【要一一对应】；传入参数可以是N个参数
    result = x + y
    print(f"x + y 的结果是：{result}")     #f是格式化输出，且定义完之后要调用，不然定义干嘛

add(7 ,8)

#案例练习：自动查核酸
def check(num , tem) :               #这个传入参数的定义不熟练，只用定义一个num或者tem就行了
    if tem <= 37.5 :
        print("体温正常")
    else:
        print(f"你的体温是{tem},需要隔离！")

check(2,36)

def check(tem) :
    if tem <=37.5:
        print(f"体温是{tem}度，请进！")
    else:
        print(f"体温是{tem}度，不正常！")
check(28)

 #程序中也讲究返回的结果
 #简单的代码
def add(x , y):
     result =x + y
     return result
#函数的返回值通过变量去接收
r = add(1,2)
print(r)
# 函数体在遇到return后就结束了，所以写在return后的代码不会执行

# 不写return，默认返回None值
def say_hi():
    print("你好呀")

result = say_hi()
print(result)
"""
"""
def check_age (age):                 #没写形式参数，后面直接输入实际参数所以报错了！！！！
    if age >18:                    #if判断age，上面的形式参数肯定要填上呀，否则判断从哪来的？？？
        return "success"
    else:
        return None

result = check_age (16)
if not result:
    print("未成年禁止进入papa")

#函数的嵌套调用
def func_a():
    print("1")
def func_b():
    print("2")
    func_a()
    print("3")
func_b()


#函数的变量作用域
#主要分为两类：局部和全局变量
#演示局部变量
"""
"""
def test_a():
    num= 100
    print(num)
test_a()
"""
"""
#print(num)            #NameError: name 'num' is not defined;出了定义的函数就没用了
#全局变量：函数体内、体外都能生效的变量，把变量定义到函数外面就可以了

#注：现在想在函数的内部去修改全局变量，         需要用到gobal
num = 200
def test_a():
    print(f"test_a:{num}")
def test_b():
    num = 500                    #此时，num 又变成了局部变量
    print(f"test_b:{num}")
test_a()
test_b()
print(num)

#如果想在函数内修改全局变量，就需要global
def test_a():
    print(f"test_a:{num}")
def test_b():
    global num
    num = 500                    #此时，num 又变成了局部变量
    print(f"test_b:{num}")
test_a()
test_b()
print(num)
#此时的输出：test_a:200；test_b:500；500  ，这就修改成功了
"""
#函数定义的综合练习
"""
money = 5000000
name =input("请输入你的名字：")#启动程序时输入，输入语句忘求了
def take(num):
    num=input("你要取的钱数目是：")
    print(num)
def left():
    result_a =money - num
    return result_a
"""
"""
input 语句
name = input（"你的名字是："）
print("你是：%s" % name)
"""
money = 5000000
name = None
name = input("你的名字是")
def query(show_header):
    if show_header:
        print("---查询余额---")
        print(f"{name},您的余额是{money}---")
def save(num):
    global money
    money += num
    print("存款")
    print(f"{name},您的余额是{money}yuan")
    query(False)
def get(num):
    global money
    money -= num
    print("取款")
    print(f"{name},您的余额是{money}yuan")
    query(False)
def main():
    print("---主菜单---")
    print(f"{name},欢迎，请选择操作")
    print("查询余额[输入1]")             #通过\t制表符对其输出
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("你的选择是：")
while True:
    key_board = main()
    if key_board == "1":
        query(True)
        continue
    elif key_board == "2":
        num = int(input("你要存多少钱，请输入："))
        save(num)
        continue
    elif key_board == "3":
        num = int(input("你要取多少钱，请输入："))
        get(num)
        continue
    else:
        print("退出")
        break


