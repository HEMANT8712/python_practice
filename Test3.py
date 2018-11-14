# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 03:35:50 2017

@author: Administrator
"""

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
    

# Paste your code into this box
print("Please think of a number between 0 and 100!")
import math
mini = 0
maxi = 100
mid = 0
last_mid = -1
choice = ''
while (True):
    mid = math.floor((mini + maxi)/2)
    if(last_mid == mid):
        mid = last_mid + 1
    print ("Is your secret number " + str(mid) + "?")
    choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(choice == 'h'):
        maxi = mid
        last_mid = mid
    elif(choice == 'l'):
        mini = mid
        last_mid = mid
    elif(choice == 'c'):
        print("Game over. Your secret number was: " + str(mid))
        break
    else:
       print("Sorry, I did not understand your input.") 
   