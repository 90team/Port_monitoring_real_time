# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:端口实时监控工具        *
#*********************************************

#--------------------/工具编写思路/--------------------
#1.写入邮箱账号 授权码
#2.设置IP伪线程
#3.设置扫描类型
#4.开始根据IP循环扫描
#--------------------/工具编写思路/--------------------
import main_thread

def run(ip,port):
    print('采用126邮箱和QQ邮箱代理服务器发送邮件！')
    #126邮箱设置
    sender = 'hacker9090@126.com'
    sender_password = 'jnfNKJFNAK1561'
    user = '2698392815@qq.com'
    #Q邮箱设置
    q_serder = 'jiu0-sec@qq.com'
    q_sender_password = 'jktcdnwwmxccgbfh'
    q_user = '2698392815@qq.com'
    #扫描类型
    print(' 1: SYN  \n   2: Telnet')
    scanclass = input('请输入扫描类型：')
    main_thread.Main_Thread(sender, sender_password, user, q_serder, q_sender_password, q_user, ip, port, '1')
    # for i in open('hosts.txt','r'):
    #     listfile = os.listdir('hosts')
    #     len_listfile = len(listfile)
    #     for x in range(0,len_listfile):
    #         for y in open(listfile[x],'r'):
    #             main_thread.Main_Thread(sender,sender_password,user,q_serder,q_sender_password,q_user,i,y,thread,scanclass)