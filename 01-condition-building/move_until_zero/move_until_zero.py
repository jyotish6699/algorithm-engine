# we will move untill zero for all categories
# 1. top to down 

def top_to_bottom():
    n = 10  
    while n != 0:
        print(n)
        n-=1

# top_to_bottom()

# Initial state?	n = 10
# Continue while?	n != 0
# State change?	n -= 1
# Boundary?	0
# Termination?	n becomes 0

def divide_until_zero():
    n = 577876
    while n != 0:
        print(n)
        n //= 10

divide_until_zero()