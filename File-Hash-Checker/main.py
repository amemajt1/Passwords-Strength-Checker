#Second project to improve my python and cybersecurity skills - File Hash Checker 
#Hashing → is a method that takes any type of data (word, file, full message, etc.) and converts it into a short, fixed-length of letters and numbers.
#this result is called - HASH CODE
#File hash checker takes a file and generates a unique hash code - "fingerprint" for that file. I will focus on MD5 and SHA256 


#1 - import the lbraries 

#Hashlib library - used to create hashes of data. 
import hashlib 

from tkinter import * 

#2 - ask user for the file 

file_name = input("Enter the file name: ")

#3 - read file in binary mode 
#Hash functions operate on bytes - I opened the file in binary mode to ensure I was hashing the exact contents of the file 
#without any text encoding or line-ending conversions.


with open(file_name, "rb") as file:
    data = file.read()

md5_hash = hashlib.md5(data).hexdigest()
sha256_hash = hashlib.sha256(data).hexdigest()

print(md5_hash)
print(sha256_hash)

#4 - compute MD5 + SHA256 hash
#5 - display results through Tkinter GUI 
