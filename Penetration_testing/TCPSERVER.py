import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = '192.168.254.19'
port = 4444
s.bind((host, port))

s.listen(3)

while True:
    clientsocket, address = s.accept()
    print("[+] Recieved Connection from %s" % str(address))

    message = 'Hello! Thank your for connecting'
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
