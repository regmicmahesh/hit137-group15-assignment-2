# Program: encryption_program.py
# Author: Gallage Achintha Methsara Fernando
# Student ID: S390909

# This program encrypts and decrypts text using a custom encryption algorithm.
# The encryption algorithm is as follows:
# - Shift the text by n * m for lowercase letters a-m
# - Shift the text by -(n + m) for lowercase letters n-z
# - Shift the text by -n for uppercase letters A-M
# - Shift the text by m^2 for uppercase letters N-Z

# The decryption algorithm is as follows:
# - Shift the text by -(n * m) for lowercase letters a-m
# - Shift the text by (n + m) for lowercase letters n-z
# - Shift the text by n for uppercase letters A-M
# - Shift the text by -(m ** 2) for uppercase letters N-Z


########################################################
# Functions
########################################################

def shift_within_range(c, shift, start, end):
    """ shifts a character by given value in [start, end] range """

    # Example: shift_within_range('a', 1, 'a', 'm') -> 'b'
    #           range_size = 122 - 97 + 1 = 26
    #           normalized = 97 - 97 = 0
    #           shifted = (0 + 1) % 26 = 1
    #           return chr(97 + 1) = 'b'
 
    range_size = ord(end) - ord(start) + 1
    abs_shift = ord(c) - ord(start)
    shifted = (abs_shift + shift) % range_size # % range_size to wrap around given range.
    return chr(ord(start) + shifted)

def encrypt_text(text, n, m):
    """ encrypts text using the encryption algorithm """
    
    # had to use a list to append the encrypted characters to a string
    encrypted = []

    for c in text:
        if 'a' <= c <= 'm':
            shift = n * m
            encrypted.append(shift_within_range(c, shift, 'a', 'm'))
        elif 'n' <= c <= 'z':
            shift = -(n + m)
            encrypted.append(shift_within_range(c, shift, 'n', 'z'))
        elif 'A' <= c <= 'M':
            shift = -n
            encrypted.append(shift_within_range(c, shift, 'A', 'M'))
        elif 'N' <= c <= 'Z':
            shift = m ** 2
            encrypted.append(shift_within_range(c, shift, 'N', 'Z'))
        else:
            encrypted.append(c)
    return ''.join(encrypted)

def decrypt_text(text, n, m):
    """ decrypts text using the decryption algorithm """
    
    decrypted = []
    for c in text:
        if 'a' <= c <= 'm':
            shift = -(n * m)
            decrypted.append(shift_within_range(c, shift, 'a', 'm'))
        elif 'n' <= c <= 'z':
            shift = (n + m)
            decrypted.append(shift_within_range(c, shift, 'n', 'z'))
        elif 'A' <= c <= 'M':
            shift = n
            decrypted.append(shift_within_range(c, shift, 'A', 'M'))
        elif 'N' <= c <= 'Z':
            shift = -(m ** 2)
            decrypted.append(shift_within_range(c, shift, 'N', 'Z'))
        else:
            decrypted.append(c)
    return ''.join(decrypted)

def verify_decryption(original, decrypted):
    """ returns true if the decryption works """
    return original == decrypted



########################################################
# Main Program
########################################################

n = int(input("Enter value for n: "))
m = int(input("Enter value for m: "))

with open("raw_text.txt", "r") as file:
    raw_text = file.read()

encrypted = encrypt_text(raw_text, n, m)

with open("encrypted_text.txt", "w") as file:
    file.write(encrypted)

decrypted = decrypt_text(encrypted, n, m)
if verify_decryption(raw_text, decrypted):
    print("decryption works!")
else:
    print("decryption failed!")


