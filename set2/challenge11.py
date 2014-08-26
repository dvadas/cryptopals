#!/usr/bin/env python

import random

from Crypto.Cipher import AES

from util import randomBytes, bytes2str, pkcs7

def encryptWithRandomKey(data):
	key = bytes2str(randomBytes(16))

	if random.random() < 0.5:
		result = 'ECB'
		aes = AES.new(key, AES.MODE_ECB)
	else:
		result = 'CBC'
		iv = '\x00' * 16
		aes = AES.new(key, AES.MODE_CBC, iv)

	numBytesBefore = random.randrange(5, 10)
	numBytesAfter = random.randrange(5, 10)
	# print numBytesBefore, numBytesAfter
	bytesBefore = bytes2str(randomBytes(numBytesBefore))
	bytesAfter = bytes2str(randomBytes(numBytesAfter))
	
	input = bytesBefore + data + bytesAfter
	input = pkcs7(input, 16)
	# input = data
	output = aes.encrypt(input)
	return output, result

def main():
	for i in range(10):
		input = 'A' * 1024
		output, encryption = encryptWithRandomKey(input)
		print 'experiment', i, encryption
		# print len(output)
		
		result = 'CBC'
		for start in range(0, 32, 16):
			print start
			if output[start:start + 16] == output[start + 16:start + 16*2]:
				result = 'ECB'
				break
		print result

		if encryption != result:
			print 'failure!!!'
			break

if __name__ == '__main__':
	main()

