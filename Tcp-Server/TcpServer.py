import socket
import threading
bind_ip = "0.0.0.0"
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port)) #Create the server listening port and address
server.listen(5) 
print ("[*] Listening on %s:%d" % (bind_ip,bind_port))
# this is our client-handling thread
def handle_client(client_socket): 
 # print out what the client sends
 request = client_socket.recv(1024)
 print ("[*] Received: %s" % request)
 # send back a packet
 client_socket.send(b"ACK!") #Response sent to the tcp client
 client_socket.close()
while True:
 client,addr = server.accept() 
 print ("[*] Accepted connection from: %s:%d" % (addr[0],addr[1])) #addr[0] will be the client ip address and addr[1] will be the port of the client
 # spin up our client thread to handle incoming data
 client_handler = threading.Thread(target=handle_client,args=(client,))
 client_handler.start()
