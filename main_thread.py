# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:端口实时监控工具        *
#*********************************************

#----------------------/main_judge/---------------------------
#1.创建扫描目录
#2.传入IP伪线程
#3.传入IP进行扫描
#4.判断IP端口是否存在，异常就发邮件
#5.功能待补充
#--------------------/------------------/--------------------
import judge_class
import portscan_class
import datetime
import time
import os
def Main_Thread(s,p,u,q_s,q_p,q_u,ip,port,scanclass):
    a = judge_class.judge(s,p,u,q_s,q_p,q_u)
    a.sayit()
    ss = portscan_class.portscan(ip,port)
    # a.mkdir()
    # a.ip_ct(thread)
    if scanclass == '1':
        ss.syn_portscan()
        # 获取扫描结果中的端口和IP
        listsvn = []
        now = datetime.datetime.now()
        listfile = os.listdir('portscan_results/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '/telnet')
        len_listfile = len(listfile)
        for tm in range(0,len_listfile):
            for file in open(listfile[tm]):
                listsvn.append(file)
        if listsvn:
            for second in listsvn:
                ret = a.fderror(second)
                if ret == '0':
                    if a.mail('发现异常端口：' + second) == '1':
                        print('邮件发送完毕，如果收件箱未发现邮件，那么邮件可能在垃圾箱！')
                    elif a.mail_two('发现异常端口：' + second) == '1':
                        print('邮件发送完毕，如果收件箱未发现邮件，那么邮件可能在垃圾箱！')
                    else:
                        now = datetime.datetime.now()
                        nowtime = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
                        print('邮箱资源用尽,时间是：' + nowtime)
                        print('邮箱资源用尽,时间是：' + nowtime, file=open('Warning.txt', 'a+'))
                elif ret == '1':
                    print('不存在异常端口，无需发送邮件！')
        else:
            print('无端口开放,无法发送邮件！')
    else:
        ss.telnet_portscan()
        # 获取扫描结果中的端口和IP
        listtel = []
        now = datetime.datetime.now()
        listfile = os.listdir('portscan_results/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '/telnet')
        len_listfile = len(listfile)
        for tm in range(0,len_listfile):
            for file in open(listfile[tm]):
                listtel.append(file)
        if listtel:
            for second in listtel:
                ret = a.fderror(second)
                if ret == '0':
                    if a.mail('发现异常端口：' + second) == '1':
                        print('邮件发送完毕，如果收件箱未发现邮件，那么邮件可能在垃圾箱！')
                    elif a.mail_two('发现异常端口：' + second) == '1':
                        print('邮件发送完毕，如果收件箱未发现邮件，那么邮件可能在垃圾箱！')
                    else:
                        now = datetime.datetime.now()
                        nowtime = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
                        print('邮箱资源用尽,时间是：' + nowtime)
                        print('邮箱资源用尽,时间是：' + nowtime, file=open('Warning.txt', 'a+'))
                elif ret == '1':
                    print('不存在异常端口，无需发送邮件！')
        else:
            print('无端口开放,无法发送邮件！')
    print('检测完毕....')
    print('1000秒之后结束进程！')
    time.sleep(1000)
    exit()