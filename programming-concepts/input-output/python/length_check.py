# Raspberry Pi Foundation
# Developed as part of Ada Computer Science
# 
# Usage licensed under CC BY-NC-SA 4.0

def main():
    valid_booking = False
    booking = input("Enter your booking reference: ")

    if len(booking) == 8:
        valid_booking = True


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
