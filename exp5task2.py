'''
DCCN experiment 5 task 2
Group 6
Bhushan Koyande     24      2018130021
Shyam Mehta         30      2018130027
'''

import numpy as np

def mod2(A:np.ndarray):
    # perform modulo-2 operation
    return np.mod(A,2)
    

def equal(a:np.ndarray, b:np.ndarray):
    # check if two arrays are equal
    return np.array_equal(a,b)

def syndrome_decode(codeword:np.ndarray,n:int,k:int,G:np.ndarray):
    q = n - k # Redundant Bits

    # G(k x n) = [I(k x k) : P(k x q)]
    mat_P = G[:,k:] # Parity Sub Matrix

    # Parity Check Matrix = H(q x n) = [trans(P(q x n) : I(q x q))]
    mat_P_transpose = np.transpose(mat_P)

    mat_H = np.concatenate((mat_P_transpose,np.identity(q)),axis=1)
    mat_H_transpose = np.transpose(mat_H)
    
    mat_S = mod2(np.dot(codeword,mat_H_transpose)) # Syndrome
    # print('H_transpose:\n',H_transpose)
    print('Syndrome:\n',mat_S)
    if equal(mat_S,np.zeros(q)) :
        print("...Passed")
        return f"Codeword: {codeword}"
    else:
        print(f"OOPS: Error detected {codeword} ...expected {np.zeros((1,q))} got {mat_S}")
        print("Corrected codeword :")
        for i,row in enumerate(mat_H_transpose):
            if equal(mat_S,row):
                codeword[i] ^= 1
                print(codeword)
                print('Identified dataword')
                return codeword[:-q]
        


'''
n = 7
k = 4
Generator_matrix = np.array([[1,0,0,0,1,1,1],
                             [0,1,0,0,1,1,0],
                             [0,0,1,0,1,0,1],
                             [0,0,0,1,0,1,1]],ndmin=2)
m = np.array([1,0,1,0])
print('Encoded dataword :\n',m)
for i in range(n):
    
    codeword = mod2(np.dot(m,Generator_matrix))
    transmitted_codeword = codeword
    print()
    print(i)
    print('~~~~~~~~~~~~~~~~~~~~~')
    print('Transmitted codeword:\n',transmitted_codeword)
    codeword[i]^=1
    print('Received codeword:\n',codeword)
    print(syndrome_decode(codeword,n,k,Generator_matrix))
    print()

codeword = mod2(np.dot(m,Generator_matrix))
transmitted_codeword = codeword
print()
print(n)
print('~~~~~~~~~~~~~~~~~~~~~')
print('Transmitted codeword:\n',transmitted_codeword)
print('Received codeword:\n',codeword)
print(syndrome_decode(codeword,n,k,Generator_matrix))
print('Deciphered dataword')
print(m)
'''