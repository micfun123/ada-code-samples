# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def strip_start_and_end():
    """Demonstrates stripping characters from the start and end of a string"""
    my_string = "UIsaac Computer Science?"
    stripped_string = my_string.strip("U?")
    print(stripped_string)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    strip_start_and_end()
