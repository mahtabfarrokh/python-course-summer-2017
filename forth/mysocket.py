import socket

UDP_IP= "127.0.0.1"
UDP_port = 5000

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

sock.bind((UDP_IP , UDP_port))
print("listen on :  ", UDP_IP,":" , str(UDP_port))

while True :
    data, addr = sock.recvfrom(1024)
    print("received message :" , data)