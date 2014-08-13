#!/usr/bin/env python

import base64
import itertools
import sys

from ascii import scoreBytes
from util import hamming, bytes2str

def crackXor(bytes):
	maxScore = None
	for key in range(256):
		xored = [byte ^ key for byte in bytes]
		score = scoreBytes(xored)
		if maxScore < score:
			maxScore = score
			maxKey = key
			maxBytes = xored
	
	return maxKey, maxBytes, maxScore

fd = open('challenge6.txt')
data = fd.read()
fd.close()
print data[:64]

bytes = [ord(ch) for ch in base64.standard_b64decode(data)]
print bytes[:64]

NUM_BLOCKS = int(sys.argv[1])
distances = []
for keysize in range(2, 40):
	blocks = []
	for i in range(NUM_BLOCKS):
		block = bytes[i * keysize:(i + 1) * keysize]
		blocks.append(block)

	total = 0
	count = 0
	for block1, block2 in itertools.combinations(blocks, 2):
		distance = hamming(block1, block2)
		total += distance / float(keysize)
		count += 1

	avg = total / count
	# print keysize, avg
	distances.append((avg, keysize))

distances.sort()
distances = distances[:3]
print distances

for distance, keysize in distances[:1]:
	print keysize
	blocks = []
	start = 0
	for start in range(0, len(bytes), keysize):
		block = bytes[start:start + keysize]
		blocks.append(block)
	print 'blocks:', len(blocks)
	
	groups = list(itertools.izip_longest(*blocks))
	print 'groups:', len(groups)
	print len(groups[0])

	key = []
	decrypted = []
	for group in groups:
		group = list(group)
		while group[-1] is None:
			group.pop()
		
		maxKey, maxBytes, maxScore = crackXor(group)
		key.append(maxKey)
		decrypted.append(maxBytes)
	
	print bytes2str(key)
	
	decBlocks = list(itertools.izip_longest(*decrypted))
	print len(decBlocks)
	print len(decBlocks[0])
	decBytes = []
	for block in decBlocks:
		decBytes.extend(block)
	while decBytes[-1] is None:
		decBytes.pop()
	# print decBytes

	print bytes2str(decBytes)

