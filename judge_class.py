# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:端口实时监控工具        *
#*********************************************


#判断主程序

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime
import time

#集合了判断功能
class judge:
    #设置126邮箱基本参数
    sender = ''
    pwd = ''
    user =''
    #s设置QQ邮箱基本参数
    q_sender = ''
    q_pwd = ''
    q_user = ''
    #定义构造方法，定义构造类逻辑没有问题
    def __init__(self,s,p,u,q_s,q_p,q_u):
        #设置126邮箱的授权码
        self.sender = s
        self.pwd = p
        self.user = u
        #设置QQ邮箱的授权码等
        self.q_sender = q_s
        self.q_pwd = q_p
        self.q_user = q_u
    def sayit(self):
        print('设置完毕->发件人邮箱地址1是：%s  |  邮箱授权码1是：%s  |  收件人邮箱地址1是：%s' % (self.sender, self.pwd, self.user))
        print('设置完毕->发件人邮箱地址2是：%s  |  邮箱授权码2是：%s  |  收件人邮箱地址2是：%s' % (self.q_sender, self.q_pwd, self.q_user))
    #判单端口是否异常功能板块，逻辑没问题，功能实现：字符串相减
    def fderror(self, second):
        list3 = []
        for i in open('reResult.txt', 'r'):
            list3.append(i.strip('\n'))
        print('原始IP_端口列表是：'  +  str(list3))
        list_i = []
        for i in second:
            if i not in list3:
                list_i.append(i)
        # if len(str(list_i)) == 2:
        #     print('不存在异常端口')
        # else:
        #     print('异常IP_端口列表是：'  +  str(list_i))
        if list_i:
            now = datetime.datetime.now()
            nowtime = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
            print(nowtime + '异常IP_端口列表是：' + str(list_i), file=open('Abnormal_ports.txt', 'a+'))
            print('异常IP_端口列表是：'  +  str(list_i))
            return '0'
        else:
            print('未发现端口异常')
            return '1'
    #发送邮件，两个邮箱逻辑代码没问题
    def mail(self,i):
        try:
            msg = MIMEText(i, 'plain', 'utf-8')
            sender_name = 'M9KJ-TEAM'
            msg['From'] = formataddr([sender_name, self.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            my_name = 'M9KJ-TEAM'
            msg['To'] = formataddr([my_name, self.user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = '[外网资产]端口监控-端口存在异常'  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL('smtp.126.com', 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.sender, self.pwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender, [self.user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            time.sleep(2)
            print('等待2秒关闭链接。。。')
            server.quit()  # 关闭连接
            ret = '1'
        except Exception as e:
            print(e)
            ret = '0'
        return ret
    def mail_two(self,i):
        try:
            msg = MIMEText(i, 'plain', 'utf-8')
            sender_name = 'M9KJ-TEAM'
            msg['From'] = formataddr([sender_name, self.q_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            my_name = 'M9KJ-TEAM'
            msg['To'] = formataddr([my_name, self.q_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = '[外网资产]端口监控-端口存在异常'  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.q_sender, self.q_pwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.q_sender, [self.q_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            time.sleep(2)
            print('等待2秒关闭链接。。。')
            server.quit()  # 关闭连接
            ret = '1'
        except Exception as e:
            print(e)
            ret = '0'
        return ret
'''
#邮箱部分测试完毕，无异常
s = judge('hacker9090@126.com','jnfNKJFNAK1561','2698392815@qq.com','jiu0-sec@qq.com','jktcdnwwmxccgbfh','2698392815@qq.com')
s.sayit()
if s.mail('出现问题') == '1':
    print('邮件发送完毕，如果收件箱未发现邮件，那么邮件可能在垃圾箱！')
elif s.mail_two('出现问题') == '1':
    print('邮件发送完毕，如果收件箱未发现邮件，那么邮件可能在垃圾箱！')
else:
    now = datetime.datetime.now()
    nowtime = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' +str(now.second)
    print('邮箱资源用尽,时间是：' + nowtime)
    print('邮箱资源用尽,时间是：' + nowtime,file=open('Warning.txt','a+'))
#判断功能正常
s = judge('hacker9090@126.com','jnfNKJFNAK1561','2698392815@qq.com','jiu0-sec@qq.com','jktcdnwwmxccgbfh','2698392815@qq.com')
s.fderror(['10_10_10_10_80',])

#创建目录功能逻辑正常
s = judge('hacker9090@126.com','jnfNKJFNAK1561','2698392815@qq.com','jiu0-sec@qq.com','jktcdnwwmxccgbfh','2698392815@qq.com')
s.mkdir()

s = judge('hacker9090@126.com','jnfNKJFNAK1561','2698392815@qq.com','jiu0-sec@qq.com','jktcdnwwmxccgbfh','2698392815@qq.com')
s.fderror(['10_10_10_10_80'])
a = s.fderror(['10_10_10_10_80'])
print(a)
'''

'''
案例：
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

# 实例化类
p = people('runoob',10,30)
p.speak()
执行以上程序输出结果为：
runoob 说: 我 10 岁。
'''