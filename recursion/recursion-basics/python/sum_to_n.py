# Raspberry Pi Foundation
# Developed as part of Ada Computer Science
# 
# Usage licensed under CC BY-NC-SA 4.0

def sum_to_n(n):
    """Recursively calculates and returns the sum of all natural numbers from 1 to n inclusive"""
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n-1)


# This code will run if this file is executed directly
# (i.e. not called by another program)    
if __name__ =='__main__':
    n = 6
    result = sum_to_n(n)
    print(f"The sum of 1 to {n} is: {result}")
