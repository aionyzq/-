from os import listdir, mkdir
from shutil import move
from time import time

path = input('请输入文件夹路径：')
e = listdir(path)
allList = []
path = path+'\\'
for i in e:

    r = i.split('.')
    print(i)
    if r[0] == '' or len(r) == 1:
        continue
    print('.'.join(r))
    allList.append('.'.join(r))
    name = '.'.join(r)
    try:
        mkdir(path+r[-1])
    except:
        try:
            move(path+name, path+r[-1])
        except FileExistsError:
            move(path+'('+str(time()*100000)+')'+name, path+r[-1])
        continue
    move(path+name, path+r[-1])
