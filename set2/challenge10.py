#!/usr/bin/env python

from Crypto.Cipher import AES
import base64

from util import xor

fd = open('10.txt')
input = fd.read()
fd.close()

# print input
data = base64.standard_b64decode(input)
# print data

# Doing it automatically
iv = '\x00' * 16
aes = AES.new('YELLOW SUBMARINE', AES.MODE_CBC, iv)
decrypted = aes.decrypt(data)
# print decrypted

# Doing it by hand
aes = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)

prevBlock = iv
blockSize = 16
encBlocks = []
for i in range(0, len(decrypted), blockSize):
	block = decrypted[i:i + blockSize]
	block = xor(block, prevBlock)
	encBlock = aes.encrypt(block)
	# print encBlock
	encBlocks.append(encBlock)

	prevBlock = encBlock

encData = ''.join(encBlocks)
print encData == data



