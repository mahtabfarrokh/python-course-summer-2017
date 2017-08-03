import socket

TCP_IP= "127.0.0.1"
TCP_port = 5010
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_port))

sock.send(bytes(MESSAGE,"utf-8"))

data = sock.recv(BUFFER_SIZE)
sock.close()

print("received data: ", data)
