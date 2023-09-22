import random
import math

def intercept_transmission():
    plaintext = "Mensagem Super Secreta"
    public_key, private_key = setkeys()
    ciphertext = encoder(plaintext, public_key)
    N = 21
    return ciphertext, N

def recover_true_keys(p, q):
    public_key, private_key = setkeys()
    if (p != 3 and q != 7) and (p != 7 and q != 3):
        raise Exception("Fatores errados")
    else:
        return private_key

def setkeys():
    prime1 = 11  # First prime number
    prime2 = 13  # Second prime number
 
    N = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)
 
    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1
 
    # d = (k*Φ(n) + 1) / e for some integer k
    public_key = (e, N)
 
    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1
 
    private_key = (d, prime1, prime2)

    return public_key, private_key
 
# To encrypt the given number
def encrypt(message, public_key):
    e = public_key[0]
    N = public_key[1]
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= N
        e -= 1
    return encrypted_text
 
# To decrypt the given number
def decrypt(encrypted_text, private_key):
    d = private_key[0]
    N = private_key[1]*private_key[2]
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= N
        d -= 1
    return decrypted
 
# First converting each character to its ASCII value and
# then encoding it then decoding the number to get the
# ASCII and converting it to character
def encoder(message, public_key):
    encoded = []
    # Calling the encrypting function in encoding function
    for letter in message:
        encoded.append(encrypt(ord(letter), public_key))
    return encoded
 
def decoder(encoded, private_key):
    s = ''
    # Calling the decrypting function decoding function
    for num in encoded:
        s += chr(decrypt(num, private_key))
    return s

def main():
    print("Intercept", intercept_transmission())
    # Uncomment below for manual input
    # message = input("Enter the message\n")
    # Calling the encoding function
    public_key, private_key = setkeys()
    plaintext = "REDACTED"
    ciphertext = encoder(plaintext, public_key)

    print("Initial message:")
    print(plaintext)
    print(ciphertext)
    print("\n\nThe encoded message(encrypted by public key)\n")
    print(''.join(str(p) for p in ciphertext))
    print("\n\nThe decoded message(decrypted by public key)\n")
    print(''.join(str(p) for p in decoder(ciphertext, private_key)))

if __name__ == "__main__":
    main()