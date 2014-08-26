#!/usr/bin/env python

import base64

from Crypto.Cipher import AES

from util import randomBytes, bytes2str, str2bytes, pkcs7, findKeysize

class Encryptor(object):
	def __init__(self):
		self._key = bytes2str(randomBytes(16))
		
		extraText = '''
Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
		self._extraText = base64.standard_b64decode(extraText)
		self._aes = AES.new(self._key, AES.MODE_ECB)

	def encrypt(self, input):
		fullInput = input + self._extraText
		output = self._aes.encrypt(pkcs7(fullInput, 16))
		return output

def main():
	enc = Encryptor()
	output = enc.encrypt('A' * 1024)
	bytes = str2bytes(output)
	# print bytes
	keysizes = findKeysize(bytes)
	distance, keysize = keysizes[0]
	print keysize

	input = 'A' * (keysize - 1)
	chs = []
	print 'bytes'
	while True:
		block = len(chs) / keysize
		print len(chs), block, 'input:', input

		target = enc.encrypt(input)[block * keysize:(block + 1) * keysize]
		# print len(target)

		baseInput = input + ''.join(chs)
		for byte in range(256):
			ch = chr(byte)
			testInput = baseInput + ch
			test = enc.encrypt(testInput)[block * keysize:(block + 1) * keysize]
			if test == target:
				print ch, byte
				chs.append(ch)
				break
		else:
			print 'no byte found'
			break

		if len(input) == 0:
			input = 'A' * (keysize - 1)
		else:
			input = input[1:]

	print ''.join(chs)


if __name__ == '__main__':
	main()

