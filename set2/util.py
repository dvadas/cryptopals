import random

def pkcs7(input, blockSize):
	length = len(input)
	leftover = length % blockSize
	if leftover == 0:
		return input

	paddingLength = blockSize - leftover
	return input + '\x04' * paddingLength

def str2bytes(string):
	return [ord(ch) for ch in string]

def bytes2str(string):
	return ''.join(chr(ch) for ch in string)

def xor(string1, string2):
	bytes1 = str2bytes(string1)
	bytes2 = str2bytes(string2)

	outBytes = [byte1 ^ byte2 for byte1, byte2 in zip(bytes1, bytes2)]
	return bytes2str(outBytes)

def randomBytes(length):
	return [random.randrange(2**8) for i in range(length)]

