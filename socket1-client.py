import socket
s=socket.socket()     #create a socket object. socket module has socket class
host="127.0.0.1"
port=5000

s.connect((host,port))
data=s.recv(1024).decode()
print(data)
s.send(b"hello I am TCP Client")
s.close()