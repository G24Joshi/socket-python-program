import socket
s=socket.socket(type=socket.SOCK_DGRAM)
host="127.0.0.1"
port=5000

s.bind((host,port))
print("server listening...")


while True:
    data.address=s.recvfrom(1024)
    print("got data from :", address)
    print(data.decode())
    s.sendto(b"Hello I am UDP SErver",address)
    break
s.close()