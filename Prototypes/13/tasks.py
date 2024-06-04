from ipaddress import *

def task2():
    ip_net = ip_network("192.168.32.176/255.255.255.240") # Дана сеть IP адреса и Маска
    cnt = 0 

    for i in ip_net:
        b = bin(int(i))[2:]
        if b.count('1') % 2 != 0:
            cnt += 1
            print(i)
            
    print(cnt)

task2()

def task4():
    ip_nt = ip_network('252.67.33.87/255.255.0.0', False) # Дан узел IP адреса и Маска
    cnt = 0

    for i in ip_nt:
        right = bin(int(i))[-16:].count("1")
        left = bin(int(i))[:-16].count("1")
        if right > left:
            cnt += 1

    print(cnt)
