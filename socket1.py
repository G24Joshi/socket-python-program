import socket
s=socket.socket()     #create a socket object. socket module has socket class
host="127.0.0.1"
port=5000

s.bind((host,port))

s.listen()
print("server listening...")


while True:
    con,address=s.accept()
    print("got connection from :",address)
    con.send(b"Hello I am TCP Server")
    data=con.recv(1024).decode()   #data jo aayega wo bhi bites me ayaega to use decode krenge
    print(data)
    con.close()
    break
s.close()