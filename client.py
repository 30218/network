
from http import client
import socket

severIp = '127.0.0.1'
port = 9999

sever = socket.socket()
sever.connect((severIp,port))

print('Server is connect')

print("이름을 입력하세요 (ex:Jang)")
msg = input()

client.send(bytes(msg,'utd-8'))
print("Message send")
msg = client.recv(1024)
print("Message received")
print(msg)

client.close()