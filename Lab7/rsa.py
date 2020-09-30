from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   return key

   return public, private

def importKey(externKey):
   return RSA.importKey(externKey)

def getpublickey(priv_key):
   return priv_key.publickey()

def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

print('Rishabh')
rishabh = newkeys(1024);
rishabh_pub, rishabh_priv = rishabh, rishabh.publickey()
print(rishabh_pub, rishabh_priv)

print('Rahul')
rahul = newkeys(1024);
rahul_pub, rahul_priv = rahul, rahul.publickey()
print(rahul_pub, rahul_priv)

msg = 'Hello'

emsg = encrypt(msg, rishabh_pub)
dmsg = rishabh_priv.decrypt(emsg)

print(msg)
print(emsg)
print(dmsg)
print(emsg == dmsg)
