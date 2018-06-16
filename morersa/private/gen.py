import gmpy2

p = 0xFADEB267B75E4C39 # openssl prime -generate -bits 64 -hex
q = 0xC80814084DDD7751
n = p * q
f = (p - 1) * (q - 1)

print("n =", n)

e = 0x10001
d = gmpy2.invert(e, f)

print("e =", e)
print("d =", d)

flag = "too_small_rsa"
c = 0x746f6f5f736d616c6c5f727361 # codecs.encode(flag, hex)
ce = pow(c, e, n)
cd = pow(ce, d, n)

assert(cd == c)

print("encrypted_flag =", ce)

