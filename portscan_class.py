# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:端口实时监控工具        *
#*********************************************
import socket
import datetime
import telnetlib
#端口扫描主程序
#TCP扫描，syn模块
class portscan:
    def __init__(self,inputip,inputport):
        self.ip = inputip
        self.port = inputport
    def syn_portscan(self):
        ip = self.ip
        port = int(self.port)
        timeout = 0.1
        socket.setdefaulttimeout(timeout)  # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.connect((ip, port))
            print('INFO | IP {0} PORT {1} is open'.format(ip, str(port)))
            now = datetime.datetime.now()
            path = 'portscan_results/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '/tcpsyn'
            with open(path + '/result.txt', 'a+') as f:
                ip_true = ip.replace('.','_')
                ip_port = ip_true + '_' + str(port)
                f.write(ip_port)
                # f.write('{0} port {1} is open'.format(ip, port))
                f.write('\n')
                f.close()
        except Exception as e:
            print(('INFO | IP {0} PORT {1} is close'.format(ip, str(port))), '|', '失败原因：', e)
        finally:
            server.close()
    #telnet扫描模块
    def telnet_portscan(self):
        ip = self.ip
        port = int(self.port)
        try:
            tel = telnetlib.Telnet(ip, port, timeout=0.1)
            print(tel)
            print('INFO | IP {0} PORT {1} is open'.format(ip, str(port)))
            now = datetime.datetime.now()
            path = 'portscan_results/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '/telnet'
            with open(path + '/result.txt', 'a+') as f:
                ip_true = ip.replace('.','_')
                ip_port = ip_true + '_' + str(port)
                f.write(ip_port)
                # f.write('{0} port {1} is open'.format(ip, port))
                f.write('\n')
                f.close()
        except Exception as e:
            print(('INFO | IP {0} PORT {1} is close'.format(ip, str(port))), '|', '失败原因：', e)

#端口扫描功能正常
# a = portscan('127.0.0.1','135')
# a.telnet_portscan()
# a.syn_portscan()