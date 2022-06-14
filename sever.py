
import socket

severIp = '127.0.0.1'
port = 9999

sever = socket.socket()

sever.bind((severIp,port))
sever.listen(1)
print('Server is ready')

client,adder = sever.accept()
print('Client is connected')

msg = client.recv(1024)
print('Message received')
print(msg)

client.send(b'Hi Hi i\', sever. You\.re name is : ' +msg)
print('Message send')

client.close()
sever.close()