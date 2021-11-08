# This script is to make the client - TCP

# First part to implement the client-server
# Author: @andvsilva
# date 2021-11-07

# libraries
import socket
import sys

print("#" * 60)
print("Setting the Client for the TCP...")
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("The connection does not work, :(")
        print(f"Error {e}")
        sys.exit()
    print("Socket was created successfully!")
    
    HostTarget = input("Type the Host or IP address to be connected: ")
    PortTarget = input("Type the Port to be connected: ")

    try:
        s.connect((HostTarget, int(PortTarget)))
        print(f"Client TCP was connected with sucess at the host - {HostTarget} and Port {PortTarget}")
        s.shutdown(2)
    except socket.error as e:
        print(f"The connection to the host {HostTarget} was not possible - Port {PortTarget}")
        print(f"Error: {e}")
        sys.exit()
        
if __name__ == '__main__':
    main()