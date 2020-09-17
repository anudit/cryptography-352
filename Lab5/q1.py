import random, sys, os, rabinMiller

def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def generateKey(keySize):

   print('Generating p prime...')
   p = rabinMiller.generateLargePrime(keySize)
   print('Generating q prime...')
   q = rabinMiller.generateLargePrime(keySize)
   n = p * q

   print('Generating e that is relatively prime to (p-1)*(q-1)...')
   while True:
      e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
      if gcd(e, (p - 1) * (q - 1)) == 1:
         break

   print('Calculating d that is mod inverse of e...')
   d = findModInverse(e, (p - 1) * (q - 1))
   publicKey = (n, e)
   privateKey = (n, d)
   return (publicKey, privateKey)


bits = 512
publicKey, privateKey = generateKey(bits)

print(f'\n------------ RSA-{bits} PUBLIC KEY ---------------')
print("[N]", publicKey[0])
print("[E]", publicKey[1])
print(f'-----------------------------------------------')

print(f'\n------------ RSA-{bits} PRIVATE KEY ---------------')
print("[N]", privateKey[0])
print("[D]", privateKey[1])
print(f'-----------------------------------------------')
