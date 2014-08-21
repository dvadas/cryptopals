#!/usr/bin/env python

from Crypto.Cipher import AES
import base64

fd = open('challenge7.txt')
input = fd.read()
fd.close()

# print input
data = base64.standard_b64decode(input)
# print data

aes = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
decrypted = aes.decrypt(data)
print len(decrypted)
print decrypted
for i in range(0, len(decrypted), 16):
	print decrypted[i:i+16].replace('\n', '\\n')
print [ord(ch) for ch in decrypted[-10:]]

bytes = [ord(ch) for ch in data]
for i in range(0, len(bytes), 16):
	print bytes[i:i+16]


