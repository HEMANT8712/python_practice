# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:26:36 2017

@author: Administrator
"""

def reverse(string):
  lgth= len(string)
  reverse_str = ""
  while(lgth > 0):
    reverse_str = reverse_str + string[lgth-1]
    lgth -= 1
  return reverse_str

print (reverse("Python!"))

x= [10, 8, 6,4,2]
print("Hello!")
for item in x:
   print( item)
   


