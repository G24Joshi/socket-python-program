import socket
s=socket.socket(type=socket.SOCK_DGRAM)
host="127.0.0.1"
port=5000

s.sendto(b"Hellow I am UDP Client",(host,port))
data,address=s.recvfrom(1024)
print("got data from :",address)
print(data.decode())
s.close()