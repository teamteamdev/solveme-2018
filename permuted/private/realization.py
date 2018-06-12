def encrypt(s, key):
    while len(s) % 4 != 0:
        s += " "
    
    x = key
    BLOCK_SIZE = 4
    
    result = ""
    
    for block in range(len(s) // BLOCK_SIZE):        
        data = list(s[block*4:(block+1)*4])
        
        for i in range(BLOCK_SIZE - 1, 0, -1):
            x = (11027 * x + 367367) % i
            data[i], data[x] = data[x], data[i]
        
        result += "".join(data)
    
    return result

def decrypt(s):
    for key in [2, 1, 0]:
        x = key
        printed = False
        BLOCK_SIZE = 4
        
        result = ""
        
        for block in range(len(s) // BLOCK_SIZE):        
            data = list(s[block*4:(block+1)*4])
            perm = [i for i in range(BLOCK_SIZE)]
            recovered = [None for _ in range(BLOCK_SIZE)]
            
            for i in range(BLOCK_SIZE - 1, 0, -1):
                x = (11027 * x + 367367) % i
                perm[i], perm[x] = perm[x], perm[i]
            
            for i in range(BLOCK_SIZE):
                recovered[perm[i]] = data[i]
            
            result += "".join(recovered)
        
        print(result)
        
        
flag = "sto_is_secure_nobody_can_see_it"
key = 0x31337 + 0x1337

enc = encrypt(flag, key)
print(enc)
decrypt(enc)