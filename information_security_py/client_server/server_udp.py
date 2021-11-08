# This script is to make the server - UDP

# client-server
# Author: @andvsilva
# date 2021-11-07

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket was created successfully.')

host = 'localhost'

port = 5432

s.bind((host, port))

message = '\nServer: I will set the connection now!'

print("listening...")
while 1:
    data, end = s.recvfrom(4096)
    
    if data:
        print('Server sending the message to the client...')
        s.sendto(data + (message.encode()), end)
    