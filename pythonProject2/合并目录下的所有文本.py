import os

dir_path = "./txt"
output_file = "./txt/ak47.txt"
with open(output_file,'w')as f:
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            with open(os.path.join(dir_path,filename))as f1:     #相关的os模块代码
                f.write(f1.read())