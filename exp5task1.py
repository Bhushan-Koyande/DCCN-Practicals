'''
DCCN experiment 5 task 1
Group 6
Bhushan Koyande     24      2018130021
Shyam Mehta         30      2018130027
'''

import numpy as np

def check_even_parity(sequence):
    # check parity of input sequence
    ans = None
    for element in sequence: 
        if ans == None:
            ans = element
        else:
            ans = ans ^ element
    
    # return true if parity is even
    if(ans):
        return False
    else:
        return True
     
def rect_parity(codeword:np.ndarray, nrows:int, ncols:int):
    
    databits_length = nrows*ncols
    shape = ( nrows, ncols )
    data_bits = codeword[:databits_length].reshape( shape )
    
    R = codeword[databits_length:databits_length+nrows].tolist()
    C = codeword[databits_length+nrows:databits_length+nrows+ncols].tolist()
    
    print('Databits: ')
    print(data_bits)
    
    # find row wise parity
    row_sum = []
    for row in data_bits:
        if check_even_parity(row):
            row_sum.append(0)
        else:
            row_sum.append(1)
    
    # find column wise parity    
    col_sum = []
    for row in data_bits.transpose():
        if check_even_parity(row):
            col_sum.append(0)
        else:
            col_sum.append(1)

    print('Row Sum: ',row_sum)
    print('Column Sum: ',col_sum)
    
    print('Row parity bits: ',R)
    print('Column parity bits: ',C)
    
    row_error = 0
    col_error = 0
    row_flip = 0
    col_flip = 0

    # trying to find location of the error
    for i in range(nrows):
        if row_sum[i] != R[i]:
            print("Parity error in row {}".format(i+1))
            row_error += 1
            row_flip = i
    
    for i in range(ncols):
        if col_sum[i] != C[i]:
            print("Parity error in column {}".format(i+1))
            col_error += 1
            col_flip = i
    
    message_sequence = data_bits
    if row_error == col_error:
        # print(row_flip,col_flip)
        if row_error == 1:
            # correction : bit flip
            message_sequence[row_flip,col_flip] = not(data_bits[row_flip,col_flip])
        elif row_error == 0:
            # no error detected
            print('no correction is necessary')
        else:
            # conclude that error is uncorrectable
            print('uncorrectable error is detected')
    else:
        # conclude that error is uncorrectable
        print('uncorrectable error is detected')
        
    return message_sequence

def test_correct_errors():        
    nrows = 2
    ncols = 4
    codeword1 = np.array( [0, 1, 1, 0, 1, 1, 0, 1,
                        0,1, 
                        1, 0, 1, 1] )
    codeword2 = np.array( [1, 0, 0, 1, 0, 0, 1, 0,
                        1,1, 
                        1, 0, 1, 0] )  
    codeword3 = np.array( [0, 1, 1, 1, 1, 1, 1, 0,
                        1,1, 
                        1, 0, 0, 0] )  
    print('First Codeword')
    rect_parity(codeword1,nrows,ncols)
    
    print('\nSecond Codeword')
    rect_parity(codeword2,nrows,ncols)
    print('\nThird Codeword')
    rect_parity(codeword3,nrows,ncols)


if __name__ == "__main__":
    test_correct_errors()