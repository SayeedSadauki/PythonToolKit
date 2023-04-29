import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.254.19'
port = 4444

clientsocket.connect((host, port))

message = 'Hello from client!'
clientsocket.send(message.encode('ascii'))

response = clientsocket.recv(1024)
print(response.decode('ascii'))

clientsocket.close()
