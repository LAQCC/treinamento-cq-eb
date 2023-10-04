import random
import math

def intercept_transmission():
    plaintext = "Socorram-me subi no ônibus em Marrocos"
    public_key, private_key = setkeys(3, 7)
    ciphertext = encoder(plaintext, public_key)
    return ciphertext, public_key


def setkeys(prime1, prime2):
    #prime1 = 787  # First prime number
    #prime2 = 179  # Second prime number
 
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
    if public_key == (5, 21):
        public_key = (5, 140873)
    # Calling the encrypting function in encoding function
    #print("Encoding using key", public_key)
    for letter in message:
        encoded.append(encrypt(ord(letter), public_key))
    
    return encoded


def decoder(encoded, private_key):
    s = ''
    # Calling the decrypting function decoding function
    if private_key == (5, 3, 7) or private_key == (5, 7, 3):
        private_key = (83945, 787, 179)
    
    #print("Decoding using key", private_key)
    for num in encoded:
        s += chr(decrypt(num, private_key))
    return s


def main():
    print("Intercept", intercept_transmission())
    # Uncomment below for manual input
    # message = input("Enter the message\n")
    # Calling the encoding function
    public_key, private_key = setkeys(787, 179)
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