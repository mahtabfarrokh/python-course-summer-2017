import socket

UDP_IP= "127.0.0.1"
UDP_port = 5000
Message = "Hello world :D"


print("UDP IP : ", UDP_IP)
print("UDP Port:", UDP_port)
print("message :", Message)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(Message, "utf-8"), (UDP_IP, UDP_port))