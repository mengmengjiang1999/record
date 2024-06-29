# 根据本文件夹下面的内容生成论文list

import os
import sys
import re

if __name__=="__main__":
    path = "./" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    
    files=sorted(files)
    
    text="Greybox Fuzzing of Distributed Systems.md"
    
    f=open("./AAApaperlist.md","w")
    cnt=1
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            if file[-3:]==".md":# 如果是md文件再打开
                if not (file=="AAApaperlist.md" or file=="其他.md"):
                    f.write("["+str(cnt)+"]"+file[:-3]+"\n")
                    cnt+=1
