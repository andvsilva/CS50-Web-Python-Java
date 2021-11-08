

# Author: @andvsilva
# date 2021-11-07

# libraries
import ipaddress

#ip = '192.168.0.1'

#address = ipaddress.ip_address(ip)

#print(address + 200)

ip = '192.168.0.0/4'

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)


