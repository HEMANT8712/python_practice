# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 00:46:42 2017

@author: Administrator
"""

# Reverse Cipher- Encryption and Decryption

message = input("Enter the string to encrpyt/decrypt using Reverse Cipher:\n")
translated = ''
i = len(message) - 1
while i >= 0:
     translated = translated + message[i]
     print(i, message[i], translated)
     i = i - 1
print("Output String is: " + translated)



# Caesar Cipher

# http://inventwithpython.com/hacking (BSD Licensed)

# the string to be encrypted/decrypted

message = 'You can show black is white by argument, said Filby,but you will never convince me.'
# the encryption/decryption key
key = 8
# tells the program to encrypt or decrypt
mode = 'encrypt' # set to 'encrypt' or 'decrypt'
# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# stores the encrypted/decrypted form of the message
translated = ''
# capitalize the string in message
message = message.upper()
# run the encryption/decryption code on each symbol in the message string
for symbol in message:
     if symbol in LETTERS:
         # get the encrypted (or decrypted) number for this symbol
         num = LETTERS.find(symbol) # get the number of the symbol
         if mode == 'encrypt':
             num = num + key
         elif mode == 'decrypt':
             num = num - key
         # handle the wrap-around if num is larger than the length of

         # LETTERS or less than 0

         if num >= len(LETTERS):
             num = num - len(LETTERS)
         elif num < 0:
             num = num + len(LETTERS)
         # add encrypted/decrypted number's symbol at the end of translated
         translated = translated + LETTERS[num]

     else:
         # just add the symbol without encrypting/decrypting
         translated = translated + symbol

# print the encrypted/decrypted string to the screen
print(translated)





# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)


message = 'GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''
    # The rest of the program is the same as the original Caesar program:
    # run the encryption/decryption code on each symbol in the message
    for symbol in message:
         if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key
            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)
            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]
         else:
             # just add the symbol without encrypting/decrypting
             translated = translated + symbol
    # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))