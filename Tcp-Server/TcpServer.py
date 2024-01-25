import socket
import threading


def handle_client(client_socket):
    while True:
        data = client_socket.recv(2048).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        client_socket.send(data.encode())  # send data to the client

    client_socket.close()


bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
server.listen(2)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

while True:
    client, addr = server.accept()
    print("Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
