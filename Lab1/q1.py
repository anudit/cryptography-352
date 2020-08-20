def encrypt(text, shift):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + shift - 65) % 26 + 65)
		else:
			result += chr((ord(char) + shift - 97) % 26 + 97)

	return result

def decrypt(text, shift):
    return encrypt(text, 26-shift)

text = input('Enter the Message: ')
s = int(input('Enter the Key: '))

print('Choose the following options')
print('1: Encrypt the message')
print('2: Decrypt the message')
ch = input('Choice: ')
if (int(ch) == 1):
	print(encrypt(text,s))
elif (int(ch) == 2):
	print(decrypt(text,s))
