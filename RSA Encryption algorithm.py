import random
from math import gcd

# ---------- PRIME GENERATION ----------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime():
    while True:
        p = random.randint(20, 100)
        if is_prime(p):
            return p

# ---------- KEY GENERATION ----------
def generate_keys():
    p = get_prime()
    q = get_prime()
    while q == p:
        q = get_prime()

    n = p * q
    phi = (p-1)*(q-1)

    e = 17
    while gcd(e, phi) != 1:
        e += 2

    d = pow(e, -1, phi)
    return (e, n), (d, n)

# ---------- ENCRYPT / DECRYPT CHARACTER-WISE ----------
def encrypt_text(text, pub):
    e, n = pub
    return [pow(ord(ch), e, n) for ch in text]

def decrypt_text(cipher_list, priv):
    d, n = priv
    return ''.join(chr(pow(c, d, n)) for c in cipher_list)

# ---------- MAIN ----------
public_key, private_key = generate_keys()

text = input("Enter your text: ")

cipher = encrypt_text(text, public_key)
plain  = decrypt_text(cipher, private_key)

print("\nEncrypted:", cipher)
print("Decrypted:", plain)