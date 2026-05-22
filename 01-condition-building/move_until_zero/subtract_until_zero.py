"""Problem Statement — Robot Battery Drain

An autonomous robot starts with a battery level of N.

Each movement operation consumes exactly 7 battery units.

Print the battery level after every movement until the battery becomes less than or equal to 0.

Example
Input:
30

Output:
30
23
16
9
2"""

def Battery_Drain(n):
    
    while(n>0):
        print(n)
        n -= 7

Battery_Drain(30)

# Time Complexity ---------
# Iterations = n/7
# O(n/7)→O(n) -> linear time
# because constants are ignored in Big-O.

# space complexity --------
# only one variable n is used, no extra memory grows with input 
# O(1) -> constant space