import socket

TCP_IP= "127.0.0.1"
TCP_port = 5020
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_port))

while True:
    command = input("Enter your command: ")
    if command == "exit":
        break
    elif command == "send":
        message = input("Enter your message: ")
        sock.send(bytes(message,"utf-8"))
        data = sock.recv(BUFFER_SIZE)
        print("answer: ", data.decode("utf-8"))

sock.close()
