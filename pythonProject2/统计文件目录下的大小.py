import os
#print(os.listdir("./path"))     打印当前目录下的所有文件和文件夹名称
sum_size = 0
for file in os.listdir("./path"):
    if os.path.isfile("./path/" + file):
        sum_size += os.path.getsize("./path/" + file)

print(sum_size)
'''在 os.path.isfile() 中，如果直接使用 os.path.isfile("./path" + file)，则路径会变成 ./pathfile1.txt，而不是 ./path/file1.txt。

为避免手动处理路径分隔符，推荐使用 os.path.join() 函数，这样可以根据系统自动添加正确的分隔符:
for file in os.listdir("./path"):
    file_path = os.path.join("./path", file)
    if os.path.isfile(file_path):
        sum_size += os.path.getsize(file_path)

'''