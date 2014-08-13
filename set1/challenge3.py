#!/usr/bin/env python

from util import getBytes

def scoreBytes(bytes):
	return sum(scoreChar(chr(byte)) for byte in bytes)

def scoreChar(char):
	if char < ' ':
		return -1
	elif char == ' ':
		return 1
	elif char < 'A':
		return 0
	elif char <= 'Z':
		return 1
	elif char < 'a':
		return 0
	elif char <= 'z':
		return 1
	elif char <= '~':
		return 0
	else:
		return -1

input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
bytes = getBytes(input)
print bytes

maxScore = None
for key in range(256):
	xored = [byte ^ key for byte in bytes]
	score = scoreBytes(xored)
	if maxScore < score:
		maxScore = score
		maxKey = key
		maxBytes = xored

print maxScore
print maxKey
print maxBytes

string = ''.join(map(chr, maxBytes))
print string

