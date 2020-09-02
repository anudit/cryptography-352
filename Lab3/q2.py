def create_cipher( text, key ):
    answer = ""
    p = 0
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p==len(key):
            p = 0
    return answer

KEY = '100111001011'
plain_text = '001011010111'

print(f"Plain Text:{plain_text}")
cipher_text = create_cipher(plain_text, KEY)
print(f"Cipher text: {cipher_text}")
decrypt = create_cipher(cipher_text, KEY)
print("Decrypt: "+decrypt)
