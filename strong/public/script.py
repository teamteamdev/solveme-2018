ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEF"

# number to letter
def letter(i):
    return ALPHABET[i]

# letter to number
def number(s):
    return ALPHABET.find(s)

# shift letters
def shiftletters(s, key):
    new_alphabet = shifttext(ALPHABET, key)
    
    table = str.maketrans(ALPHABET, new_alphabet)
    
    return s.translate(table)

# shift string
def shifttext(s, key):
    key = ord(key) % 32
    
    return s[key:] + s[:key]

# xor letters
def letter_xor(s, key):
    key = (ord(key) + ord(key)) % 32
    
    result = ""
    
    for let in s:
        result += letter(number(let) ^ key)
    
    return result

# some magic
def double(s):
    result = ""
    for i in s:
        if 2 * number(i) >= 32:
            result += letter(2 * number(i) - 31)
        else:
            result += letter(2 * number(i))
    return result
    
def encrypt(s, key):
    return double(letter_xor(shifttext(shiftletters(s, key), key), key))

secret = input()
key = input()
print(encrypt(secret, key))
