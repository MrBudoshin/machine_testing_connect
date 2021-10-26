from socket import *
import sys


sock = socket(AF_INET, SOCK_DGRAM)
host = sys.argv[1]
port = 12345
buf = 1024
addr = (host, port)
file_name = sys.argv[2]
sock.sendto(file_name.encode(), addr)
with open(file_name, 'rb') as ff:
    data = ff.read(buf)
    while data:
        if sock.sendto(data, addr):
            print("sending ...")
            data = ff.read(buf)
            print('send')
sock.close()
