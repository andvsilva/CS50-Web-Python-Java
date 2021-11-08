# This script is one way to generate very strong passwords

# Author: @andvsilva
# date 2021-11-07

# libraries
import random, string

size_password = 64

chars = string.ascii_letters + string.digits + '!@#$%^&*()_-=+&?/.,`~"+'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size_password)))