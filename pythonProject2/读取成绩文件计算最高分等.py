def read_file():
    result=[]
    with open("./stu_grade.txt") as f:
        for line in f:
            line =line.strip()
            filed=line.split(',')
            result.append(int(filed[-1]))
    max_result=max(result)
    min_result=min(result)
    avg_result=sum(result)/len(result)
    return max_result,min_result,avg_result

data=read_file()
print(data)