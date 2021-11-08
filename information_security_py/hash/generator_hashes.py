# Generator of hashes

# Author: @andvsilva
# date 2021-11-07

# libraries
import hashlib

string = input("Type the string to generate the hash: ")

menu = int(input('''#### MENU Choose one type of hash ### 
             1) MD5 
             2) SHA1
             3) SHA256
             4) SHA512
             Type the number of the hash to be generated: ''')
           )

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print("The hash MD5 of the string is: ", result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print("The hash SHA1 of the string is: ", result.hexdigest())
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print("The hash SHA256 of the string is: ", result.hexdigest())
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print("The hash SHA512 of the string is: ", result.hexdigest())
else:
    print('Something is wrong, please, check if the input was type correctly.')