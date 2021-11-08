import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        os.system(f'ping -c 1 {ip}')
        print('-' * 60)
        time.sleep(3)
