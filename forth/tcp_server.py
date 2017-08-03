import socket

TCP_IP= "127.0.0.1"
TCP_port = 5020

BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_port))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print("Conection address: ", addr)

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break;
        print("received data: ", data)
        temp = data.decode("utf-8")
        temp += " salam"
        conn.send(bytes(temp, "utf-8")) #echo

    conn.close()