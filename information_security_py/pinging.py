import os

print("#" * 60)

ip_ou_host = input("Type the IP or the host to be verified: ")

print("-" * 60)

os.system(f'ping {ip_ou_host}')

