# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 01:38:17 2017

@author: Administrator
"""

#List Comprehensiion

c = ['C' for x in range(5) if x < 3]
print (c)

cubes_by_four = [(x**3) for x in range(1,11) if((x**3)%4) == 0]
                                                
print (cubes_by_four)

#List Slicing (start:END:step)

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print (l[2:9:2])

to_five = ['A', 'B', 'C', 'D', 'E']

print (to_five[3:])
# prints ['D', 'E'] 

print (to_five[:2])
# prints ['A', 'B']

print (to_five[::2])
# print ['A', 'C', 'E']

letters = ['A', 'B', 'C', 'D', 'E']
print (letters[::-1])
#print ['E', 'D', 'C', 'B', 'A']. Reverse a list

#anonymous function- work as basic funtion with no name
my_list = range(16)
print (filter(lambda x: x % 3 == 0, my_list))

squares = [x**2 for x in range(1,11)]
print (filter(lambda x:(x > 30) and (x<70), squares))

# Left Bit Shift (<<)  
print (0b000001 << 2 == 0b000100 )# (1 << 2 = 4))
print (0b000101 << 3 == 0b101000)# (5 << 3 = 40)       

# Right Bit Shift (>>)
print(0b0010100 >> 3 == 0b000010) #(20 >> 3 = 2)
print(0b0000010 >> 2 == 0b000000) #(2 >> 2 = 0)

# Bitwise And
print (bin(0b1110 & 0b101))

#Bitwise OR
print (bin(0b1110 | 0b101))

#Bitwise Xor
print (bin(0b1110 ^ 0b101))

#Bitwise Not
print (~1)
print (~2)
print (~3)
print (~42)
print (~123)


#Bitmasking
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print ("Bit was on")
  
# Turing it on 
  a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7
print (desired)

#Fliping the bits
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1
print (desired)

#Slip and slide (use the left shift (<<) and 
#right shift (>>) operators to slide masks into place.)
a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask
print (desired)

