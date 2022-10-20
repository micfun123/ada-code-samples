# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def palindrome(word):
    """Recursively determines whether a word is a palindrome. Returns a Boolean."""
    length = len(word)
    if length == 0 or length == 1:
        return True
    elif word[0] == word[length - 1]:
        new_word = word[1 : length - 1]
        return palindrome(new_word)
    else:
        return False


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    test_word = 'kayak'
    is_palindrome = palindrome(test_word)
    print (f"{test_word}: {is_palindrome}")
