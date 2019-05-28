import socket
s = socket.socket()

#获取本机名称
hostname=socket.gethostname()
#获取本机IP
ip=socket.gethostbyname(hostname)
port = 8050

s.bind((ip,port))

s.listen(5)
c,addr = s.accept()   #c—客户套接字
print('Got connection from',addr)
while True:
    msg = c.recv(1024).decode()
    print(msg)
    if int(msg) > 0:
        c.send('Continue'.encode())
    else:
        c.send('Stop'.encode())
        #c.close()
        break
			
