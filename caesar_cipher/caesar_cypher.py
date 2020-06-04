# solution from here https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

def encrypt(plain_text_phrase, numeric_shift_key):
    encrypted_key = ""
    for char in plain_text_phrase:
        # for each character in our plain_text_phrase parameter
        # isalpha() methods returns “True” if all characters in the string are alphabets, otherwise, it returns “False”.
       if char.isalpha():
           # Check to see if the character is an alphabet
           # The ord() function returns an integer representing the Unicode character.
           # Adds the value of our character's integer value to our numeric_shift_key parameter
            shifted_string = ord(char) + numeric_shift_key
            # while the sum is greater than z's integer value, subtract 26 until we're in the range of alphabet values
            while shifted_string > ord('z'):
                shifted_string -= 26
            # The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
            # Turns our checked shifted_string value into an alphabet letter
            final = chr(shifted_string)
            # Concatenates our final outputs into our encrypted_key variable
            encrypted_key += final
    return encrypted_key

print(encrypt('abc', 100))


def decrypt(encrypted_text, numeric_shift_key):
    return encrypt(encoded, -key)

decrypt((encrypt('abc', 100)), -100)