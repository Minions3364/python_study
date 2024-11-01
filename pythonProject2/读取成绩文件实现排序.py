def read_file():
    result=[]
    with open("./stu_grade.txt",encoding="utf-8")as fin:
        for line in fin:
            line = line.strip()      # 使用 strip() 去除换行符和多余空白
            result.append(line.split(","))
    return result
def sort_data(data):
    return sorted(data,key=lambda x:int(x[2]),reverse=True)

def write_data(data):
    with open("stu_grade_output.txt","w")as f:
        for da in data:
            f.write(",".join(da) + "\n")
data=read_file()
print(data)
datas=sort_data(data)
print(datas)
write_data(data)
