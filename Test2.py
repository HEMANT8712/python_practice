# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:07:44 2017

@author: Administrator
"""
#Count of Vowel in string
s = 'azcbobobegghakl'
string = "aeiou"
count = 0
for item in s:
   for vowel in string:
      if (item == vowel):
        count = count + 1
        break
 
print("Number of Vowel =" + str(count))

#Number of times substring occur
s = 'azcbobobegghakl'
count = 0
for index,item in enumerate(s):
      print( index)
      if (s[index:index+3] == "bob"):
        count = count + 1
 
print("Number of times bob occurs is =" + str(count))

#Longest substring in alphabetical order
s = 'bcdabc'
lst = []
for index,item in enumerate(s):
   string = s[index]
   temp = index
   for letter in s[index+1:len(s)]:
      x = ord(s[temp])
      y = ord(letter)
      if (x <= y):
        string = string + letter
        temp = temp + 1        
      else :
        break
   lst.append(string)

print (lst)
string = lst[0]
for index,ans in enumerate(lst):
    if (len(string) < len(lst[index])):
        string = lst[index]
    elif(len(string) == len(lst[index])):
        for item in range(len(string)):
            a = ord(string[item])
            b = ord(lst[index][item])
            if (a > b):
               string = lst[index]
               break
 
print ("Longest substring in alphabetical order" + str(':') +string)               
    
