# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:57:58 2017

@author: Administrator
"""
"""BAsic Exmaple"""
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")
f.write("Data to be written")
f.close()
f = open("output.txt", "r")
print (f.read())
f.close()

"""Reading Between the Lines:- call .readline() on the file object, you'll 
get the first line of the file; subsequent calls to .readline() will return 
successive lines."""
my_file = open("output.txt", "r")
print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
my_file.close()

"""
PSA: Buffering Data
We keep telling you that you always need to close your files after you're
done writing to them. Here's why! During the I/O process, data is buffered: 
this means that it is held in a temporary location before being written to 
the file.Python doesn't flush the buffer—that is, write data to the file—until
 it's sure you're done writing. One way to do this is to close the file. 
 If you write to a file without closing, the data won't make it to the 
 target file.
 """
 
 # Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print (read_file.read())
read_file.close()

"""Automatic File Closing:-
The 'with' and 'as' Keywords
Programming is all about getting the computer to do the work. 
Is there a way to get Python to automatically close our files for us?
Of course there is. This is Python.
You may not know this, but file objects contain a special pair of 
built-in methods: __enter__() and __exit__(). The details aren't important,
 but what is important is that when a file object's __exit__() method is 
 invoked, it automatically closes the file. How do we invoke this method? 
 With with and as.The syntax looks like this:
     
     with open("file", "mode") as variable:
  # Read or write to the file
"""
with open("text.txt", "w") as textfile:
  textfile.write("Success!")
  
with open("text.txt", "w") as my_file:
  my_file.write("My Name is Hemant")
  
"""How to check file is closed:-
Python file objects have a closed attribute which is True when
the file is closed and False otherwise. By checking file_object.closed, 
we'll know whether our file is closed and can call close() on it if it's still open.
"""

with open("text.txt", "w") as my_file:
  my_file.write("My Nmae is Hemant")
  
if my_file.closed == "False":
  my_file.close()

print (my_file.closed)