def encrypt(text,s=0):
	result = ""
	#generates random key
	
	if s==0:
		from random import randint
		s=randint(1,9)
		del randint
	# traverse text
	for i in range(len(text)):
		char = text[i]
		if char==' ':
			result+= ' '
		# Encrypt uppercase characters
		elif (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return f"{s}{result}"

if __name__=="__main__":
	print(encrypt('Hello World'))
	print(encrypt(encrypt('Hello World!')))