# Raspberry Pi Foundation
# Developed as part of Ada Computer Science
# 
# Usage licensed under CC BY-NC-SA 4.0


# First example
def conv(a):
   b = a / 9.81 * 3.711
   return b


# Second example
GRAVITY_ON_EARTH = 9.81
GRAVITY_ON_MARS = 3.711

def calculate_weight_on_mars(weight_on_earth):
   weight_on_mars = weight_on_earth / GRAVITY_ON_EARTH * GRAVITY_ON_MARS
   return weight_on_mars


def main():
    """Execute both subroutines and output the results"""

    weight = 35.7
    print(conv(weight))
    print(calculate_weight_on_mars(weight))


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
