#Huseyn Mammadov
from textwrap import wrap
import sys

from matplotlib.pyplot import get
def encrypt(plaintext, key):
    plaintext = format(plaintext, '012b')
    key = format(key, '09b')
    s1 =    [
                ["101", "010", "001", "110", "011", "100", "111", "000"],
                ["001", "100", "110", "010", "000", "111", "101", "011"] 
            ]
    s2 =    [
                ["100", "000", "110", "101", "111", "001", "011", "010"],
                ["101", "011", "000", "111", "110", "010", "001", "100"]
            ]
    
    blocks = wrap(plaintext,12) 
    key_12 = key * 2
    key_4 = [key_12[0:8], key_12[1:9], key_12[2:10], key_12[3:11]]

    ciphertext = ""
    
    for i in range(0,len(blocks)):
        block = blocks[i]
        left = block[:len(block)//2]
        right = block[len(block)//2:]
        for j in range (4):
            temp_l = left
            k = key_4[j]
            left = right
            right = expand(right)
            right = xor(right,k,8)
            right1 = right[:len(right)//2]
            right2 = right[len(right)//2:] 
            s1row = int(right1[0])
            s1col = int(right1[1:],2)
            s2row = int(right2[0])
            s2col = int(right2[1:],2)
            s1total = s1[s1row][s1col]
            s2total = s2[s2row][s2col]
            f = s1total + s2total
            right = xor(temp_l,f,6)
        ciphertext += left + right
    
 
    if len(ciphertext) == 0: return 0
    else: ciphertext = int(ciphertext, 2)
        
    return ciphertext
        
def expand(t):

    result = t[0] + t[1] + t[3] + t[2] + t[3] + t[2] + t[4] + t[5]
    return result

def xor(s1, s2, n):
    res = "0" 
    n1 = int(s1,2)
    n2 = int(s2,2)
    result = bin(n1^n2)[2:]
    #result = bin(n1^n2)[3:].zfill(8)
    res_len = len(result)
    temp = n-res_len
    res = res * temp
    result = res + result
    return result


def decrypt(ciphertext,key):
    ciphertext = format(ciphertext, '012b')
    key = format(key, '09b')
    
   
    s1 =    [
                ["101", "010", "001", "110", "011", "100", "111", "000"],
                ["001", "100", "110", "010", "000", "111", "101", "011"] 
            ]
    s2 =    [
                ["100", "000", "110", "101", "111", "001", "011", "010"],
                ["101", "011", "000", "111", "110", "010", "001", "100"]
            ]
   
    blocks = wrap(ciphertext,12)
    key_12 = key * 2
    key_4 = [key_12[0:8], key_12[1:9], key_12[2:10], key_12[3:11]]

    plaintext = ""
    for i in range(len(blocks)):
        block = blocks[i]
        left = block[:len(block)//2]
        right = block[len(block)//2:]
        
        for j in reversed(range(4)):
            temp_r = left
            next_r_expanded = expand(temp_r)
            v = xor(next_r_expanded,key_4[j],8)
            right1 = v[:len(v)//2]
            right2 = v[len(v)//2:] 
            s1row = int(right1[0])
            s1col = int(right1[1:],2)
            s2row = int(right2[0])
            s2col = int(right2[1:],2)
            s1total = s1[s1row][s1col]
            s2total = s2[s2row][s2col]
            f = s1total + s2total
            left = xor(right,f,6)
            right = temp_r
        plaintext = left + right + plaintext
    
    if len(plaintext) == 0: return 0
    else: plaintext = int(plaintext, 2)
  
    return plaintext

def findPairs(plaintext,ciphertext):
    lst_e = []
    lst_d = []
    my_list = [dict() for x in  range(512)]
    for i in range(len(my_list)):
        lst_e.append(encrypt(plaintext,i))
        lst_d.append(decrypt(ciphertext,i))
    my_dict = dict() 
    for index,value in enumerate(lst_e):
        my_dict[index] = value
    my_dict2 = dict() 
    for index,value in enumerate(lst_d):
        my_dict2[index] = value
    res = []
    for key, value in my_dict.items():
        for key2, value2 in my_dict2.items():
            if value==value2:
                res.append((key,key2))
    print("Number of pairs: " +str(len(res)))
    my_dict3 = dict() 
    for index,value in enumerate(res):
        my_dict3[index] = value
    print(my_dict3.values())
    return my_dict3


a = int(sys.argv[1])  
b = int(sys.argv[2])
c = int(sys.argv[3])  
d = int(sys.argv[4])

lst1 = findPairs(a,b)
lst2 = findPairs(c,d)
#print(type(lst1))
#print(type(lst2))




def findCommon(a,b):
    final = {}
    for item in a.values():
        if item in b.values():
            final[item]=b.get(item)
    
    print("There is only one pair which is : "+ str(len(final)))
    print("Key pair is: " + str(final))

result = findCommon(lst1,lst2)


    

'''
plaintext/ciphertext pairs 0/247; 4095/2808
'''



'''
Plaintext  	Key	Ciphertext
0	    0	1323 
0	    85	1097
0	    170	1973
0	    255	599
0	    341	3631
0	    511	1726
1365	0	2249
1365	85	2699
1365	170	2799
1365	255	1567
1365	341	1867
1365	511	769
2730	0	3326
2730	85	2086
2730	170	2228
2730	255	3266
2730	341	1296
2730	511	1846
4095	0	2369
4095	85	317
4095	170	464
4095	255	1793
4095	341	2122
4095	511	2772
'''






