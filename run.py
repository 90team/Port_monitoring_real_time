# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:端口实时监控工具        *
#*********************************************


#--------------------/工具编写思路/--------------------
#1.开始并发
#--------------------/工具编写思路/--------------------


import os
import glob
import datetime
import subprocess

print('---------------------------------------------')
print('欢迎使用端口实时监控工具，本工具版本号：V3.0')
print('---------------------------------------------')
# ip伪线程设置
print('本软件默认开启所有IP并发扫描！请控制IP数量或者升级服务器配置以免宕机')
print('支持线程是：1、3、5、15、17、51、85、255、257、771、1285、3855、4369、13107、21845，请不要输入错误！')
thread = input('请输入端口扫描线程：')
thread = int(thread)
# 可以被整除：1、3、5、15、17、51、85、255、257、771、1285、3855、4369、13107、21845。
# ------------------------
# ip伪并发，65535切分模块
# ------------------------
def ip_ct(thread):
    print('INFO: The Thread is ' + str(thread))
    Number = int(65535 / thread)
    print(Number)
    i = 1
    dirpath = 'ports/'
    # 判断路径是否存在，然后判断文件是否存在，如果存在就将文件删除，如果路径不存在就创建目录
    if os.path.exists('ports'):
        if os.listdir('ports'):
            print('文件夹Ports已经存在，正在对文件进行清空...')
            for file in os.walk('ports'):
                print('os.walk返回对象' + str(file))
                for items in file[2]:
                    print('目标文件：' + items)
                    os.remove(dirpath + items)
                    print(items + '| 文件已删除')
        else:
            print('Ports目录已存在，且无文件！')
    else:
        os.mkdir('ports')
        print('Ports目录生成成功！')
    # 根据输入的port线程数目，然后对65535进行分割，然后生成文件，对文件进行列目录
    while i <= thread:
        count_original = Number * (i - 1)
        count = Number * i
        print('当前是生成第' + str(i) + '个线程')
        for port in range(count_original, count):
            with open('ports/port_' + str(i) + '.txt', 'a+') as f:
                f.write(str(port))
                f.write('\n')
                f.close()
        i += 1
    for filename in glob.glob(r'ports/*.txt'):
        print('文件：' + filename + '| 生成成功！')
    print('IP线程预分类模块完成！')
    #创建目录模块
def mkdir():
    now = datetime.datetime.now()
    path = 'portscan_results/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    # 去除首位空格
    # path = path.strip()
    # 去除尾部 \ 符号
    # path = path.rstrip("\\")
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False
ip_ct(thread)
mkdir()

for ip in open('hosts.txt','r'):
    listfile = os.listdir('ports')
    len_listfile = len(listfile)
    for x in range(0,len_listfile):
        for port in open('ports/'+ listfile[x],'r'):
            subprocess.Popen("python ./Real_Time_Port_Scaner.py " + ip + port)