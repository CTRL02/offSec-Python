import socket
target_host = "0.0.0.0"
target_port = 9999
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Sock_STREAM indicate tcp
# connect the client
client.connect((target_host,target_port))
# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #any messege that the server should recieve upon connection
# receive some data
response = client.recv(4096) 
print (response)
