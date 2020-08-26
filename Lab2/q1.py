def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None
	else:
		return x % m

def affine_encrypt(text, key):
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
				+ ord('A')) for t in text.upper().replace(' ', '') ])

def affine_decrypt(cipher, key):
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
					% 26) + ord('A')) for c in cipher ])


inp = input('Enter the values of a & b (Key):')
a_b = inp.split(' ')
a_b[0] = int(a_b[0])
a_b[1] = int(a_b[1])

text = input('Enter the plaintext:')
enc = affine_encrypt(text, a_b)
dec = affine_decrypt(enc, a_b)

print(f'Encrypted Text: {enc}')

print(f'Decrypted Text: {dec}')
