# Raspberry Pi Foundation
# Developed as part of Ada Computer Science
# 
# Usage licensed under CC BY-NC-SA 4.0

def show_error():
    """Example of an if/elif statement to match the error code"""
    error_code = input("Enter the error code: ")
    
    if error_code == "400":
        print("Bad request")
    elif error_code == "401":
        print("Unauthorised request")
    elif error_code == "403":
        print("Forbidden request")
    elif error_code == "404":
        print("Page not found")
    elif error_code == "408":
        print("Timeout error")
    else:
        print("Unknown error")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    show_error()
