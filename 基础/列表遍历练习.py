list= [1,2,3,4,5,6,7,8,9,10]
def list_while():
    list_1=[]
    i = 0
    while i < len(list):
        element = list[i]
        if element %2 == 0:
            list_1.append(element)
        i += 1
    print(f"{list_1}")

list_while()


def list_for():
    list2=[]
    index = 0
    for element in list:
        if element %2 == 0:
            list2.append(element)
        index += 1
    print(list2)
list_for()