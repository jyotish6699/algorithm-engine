"""
Problem: File Compression System

A cloud storage service continuously compresses a file before archiving it.

Each compression operation reduces the current
file size to half using integer division.

Given the initial file size in MB,
print the file size after every compression step
until the size becomes 0.

Example:
Input: 100

Output:
100
50
25
12
6
3
1
"""

def compression_file(n):
    
    while(n!=0):
        print(n)
        n //= 2

compression_file(100)

# time complexity --------
# O(n/2) = O(n) -> linear time 
# because iteration is half for each iteration so n/2 each iteration

# space complexity --------
# O(1) because only n vaiable is used so, if n will grow still one variable memory use 

