import socket

HOST = "127.0.0.1"
PORT = 63999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket1:
    socket1.bind((HOST, PORT))
    socket1.listen()
    con1, adr1 = socket1.accept()
    with con1:
        print("From " + adr1)
        while True:
            data1 = con1.recv(1024)
            if not data1:
                break
            con1.sendall(data1)
