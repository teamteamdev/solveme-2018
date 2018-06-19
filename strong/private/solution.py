ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEF"

# number to letter
def letter(i):
    return ALPHABET[i]

# letter to number
def number(s):
    return ALPHABET.find(s)

# shift letters
def shiftlettersback(s, key):
    new_alphabet = shifttext(ALPHABET, key)
    
    # < table = str.maketrans(ALPHABET, new_alphabet)
    table = str.maketrans(new_alphabet, ALPHABET)
    
    return s.translate(table)

# shift string
def shifttext(s, key):
    key = ord(key) % 32
    
    return s[key:] + s[:key]

def shifttextback(s, key):
    # < key = len(s)
    key = len(s) - (ord(key) % 32)
    
    return s[key:] + s[:key]

# xor letters
def letter_xor(s, key):
    key = (ord(key) + ord(key)) % 32
    
    result = ""
    
    for let in s:
        result += letter(number(let) ^ key)
    
    return result

# some magic   
def half(s):
    result = ""
    for i in s:
        # < if 2 * number(i) >= 32:
        if number(i) % 2 == 1:
            # < result += letter(2 * number(i) - 31)
            result += letter((number(i) + 31) // 2)
        else:
            # < result += letter(2 * number(i))
            result += letter(number(i) // 2)
    return result
    
def decrypt(s, key):
    # < return double(letter_xor(shifttext(shiftletters(s, key), key), key))
    return shiftlettersback(shifttextback(letter_xor(half(s), key), key), key)

non_secret = input()
for key in ALPHABET:
    print(key, decrypt(non_secret, key))
