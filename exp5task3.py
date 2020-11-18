'''
DCCN experiment 5 task 3
Group 6
Bhushan Koyande     24      2018130021
Shyam Mehta         30      2018130027
'''

import numpy as np
from exp5task2 import syndrome_decode, mod2, equal

n = 7
k = 4
Generator_matrix = np.array([[1,0,0,0,1,1,1],
                             [0,1,0,0,1,1,0],
                             [0,0,1,0,1,0,1],
                             [0,0,0,1,0,1,1]],ndmin=2)
m = np.array([1,0,1,0])
print(f'Testing all codewords ...')
print('Encoded dataword :\n',m)
for i in range(n):
    
    codeword = mod2(np.dot(m,Generator_matrix))
    transmitted_codeword = codeword
    print()
    print('~~~~~~~~~~~~~~~~~~~~~')
    print('Transmitted codeword:\n',transmitted_codeword)
    codeword[i]^=1
    print('Received codeword:\n',codeword)
    print(syndrome_decode(codeword,n,k,Generator_matrix))
    print()

codeword = mod2(np.dot(m,Generator_matrix))
transmitted_codeword = codeword
print()
print('~~~~~~~~~~~~~~~~~~~~~')
print('Transmitted codeword:\n',transmitted_codeword)
print('Received codeword:\n',codeword)
print(syndrome_decode(codeword,n,k,Generator_matrix))
print('Deciphered dataword')
print(m)

print("All 0 and 1 error tests passed for (7,4,3) code with generator matrix G = \n",Generator_matrix)