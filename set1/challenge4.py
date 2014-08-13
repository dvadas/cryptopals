#!/usr/bin/env python

from util import getBytes
from ascii import scoreBytes

maxScore = None
for line in open('challenge4.txt'):
	line = line.strip()
	bytes = getBytes(line)

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


