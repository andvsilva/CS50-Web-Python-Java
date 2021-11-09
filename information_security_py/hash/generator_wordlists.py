# Generator of wordlists

# Author: @andvsilva
# date 2021-11-08

import itertools

string = input("String to be permutated: ")

results = itertools.permutations(string, len(string))

j=1
for i in results:
    print(f'# {j} -> ' + ''.join(i))
    j += 1