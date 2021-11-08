# The code is to do the comparison between hashs

# Author: @andvsilva
# date 2021-11-07

# libraries
import hashlib

file1 = 'file1.txt'
file2 = 'file2.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The files are differents')
    print(f'The hash of the {file1} is: ', hash1.hexdigest())
    print(f'The hash of the {file2} is: ', hash2.hexdigest())
else:
    print('The files are equals')
    print(f'The hash of the {file1} is: ', hash1.hexdigest())
    print(f'The hash of the {file2} is: ', hash2.hexdigest())