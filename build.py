'''
向github推push代码时执行脚本
autor:jinyong pan
date: 2019-09-21
version:0.1
e-mail:1301914984@qq.com
'''
import os
import sys

basepath = os.path.abspath('.')
print ("开始恢复初始未安装状态......")
print()
print("-------------------------第一步-----------------------------")
print ("正在删除.\data\common.inc.php、config.cache.*.php等......")
print()
file10 = os.path.join(basepath,'data','common.inc.php')
file11 = os.path.join(basepath,'data','config.cache.bak.php')
file12 = os.path.join(basepath,'data','config.cache.inc.php')
if os.path.exists(file10):
    os.remove(file10)
    print ("操作成功：common.inc.php")
else:
    print ("不存在文件："+file10)
if os.path.exists(file11):
    os.remove(file11)
    print ("操作成功：config.cache.bak.php")
else:
    print ("不存在文件："+file11)
if os.path.exists(file12):
    os.remove(file12)
    print ("操作成功：config.cache.inc.php")
else:
    print ("不存在文件："+file12)
print()

print("-------------------------第二步-------------------------------")
print ("正在删除.\data\\admin_*.php......")
print()
path2 = os.path.join(basepath,'data')
list2 = os.listdir(path2)
for i in range(0,len(list2)):
    path = os.path.join(path2,list2[i])
    if os.path.isfile(path):
        fileName2 = os.path.basename(path)
        if fileName2[0:6]=='admin_':
            os.remove(path)
            print ("操作成功："+path+"\n")
        else:
            print ("不能删除文件："+fileName2+format("（文件未被处理）","->30"))
            
print()
print("------------------------第三步------------------------------------")
print("正在删除.\data\cache\*.inc....")
print()
path3 = os.path.join(basepath,'data','cache')
list3 = os.listdir(path3)
for i in range(0,len(list3)):
    path = os.path.join(path3,list3[i])
    if os.path.isfile(path):
        fileName3 = list3[i]
        path33 = os.path.join(path3,fileName3)
        if fileName3[-4:]=='.inc':
            os.remove(path33)            
            print ("成功删除文件："+path33+"\n")
        else:
            print ("不能删除文件："+fileName3+format("（文件未被处理）","->30"))    
print()
print("-------------------------第四步-------------------------------------")
print ("正在删除.\install\install_lock.txt......")
print()
file4 = os.path.join(basepath,'install','install_lock.txt')
if os.path.exists(file4):
    os.remove(file4)
    print ("操作成功")
else:
    print ("不存在文件："+file4)
print()


print("-------------------------第五步---------------------------------------")
print ("正在重命名.\install\index.phpbak......")
print()
file5 = os.path.join(basepath,'install','index.phpbak')
basepath5 = os.path.join(basepath,'install')
file51 = os.path.join(basepath5,'index.php')
if os.path.exists(file51):
    print ("文件已存在")
else:
    os.rename(file5,file51)
    print ("重命名成功："+file5+"\n"+"↓")
    print (file51)
print()

print("--------------------------第六步----------------------------------------")
print("正在处理初始管理目录admin.......")
print()
arrdir= []
arrfind = ['.git', 'article', 'articlelist', 'comment', 'data', 'detail', \
            'include', 'install', 'js', 'list', 'news', 'pic', \
            'templets', 'topic', 'topiclist', 'uploads', 'video', 'weixin',
            '文档','.vscode']
for x in os.listdir('.'):
    if os.path.isdir(x):
        arrdir.append(x)
print("正在查找要处理的管理目录......")
print()
founddir = list(set(arrdir).difference(set(arrfind)))
foundstr = ",".join(founddir)
dir60 = os.path.join(basepath,foundstr)
print("找到目录：“"+foundstr+"”")
print(dir60)
print()
print("正在试图重命名管理目录......")
print()
dir61 = os.path.join(basepath,'admin')
if os.path.exists(dir61):
    print ("已经存在名“admin”的文件夹")
else:
    os.rename(dir60,dir61)
    print ("文件夹重命名成功\r\n")

print()
print("--------------------------完成！--------------------------------------")
print("初始化处理完成！可以重新安装或发布了")
print()
