# This script is to make the client - UDP

# First part to implement the client-server
# Author: @andvsilva
# date 2021-11-07

# libraries
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Client Socket was created successfully!')

host = 'localhost'
Port = 5433

message = "Starting the connection to the server."

try:
    #print('Client: ' + message)
    s.sendto(message.encode(), (host, 5432))
    
    data, server = s.recvfrom(4096)
    data = data.decode()
    print('Client: ' + data)
finally:
    print('Client: Close the connection! See you.')
    s.close()