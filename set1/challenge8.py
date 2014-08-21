#!/usr/bin/env python

from collections import defaultdict

from util import getBytes

for line in open('challenge8.txt'):
	line = line.strip()
	bytes = getBytes(line)
	# print bytes

	blocks = defaultdict(int)
	for i in range(0, len(bytes), 16):
		block = tuple(bytes[i:i+16])
		blocks[block] += 1
	
	sortedBlocks = sorted(blocks.iteritems(), key=lambda (block, count): count, reverse=True)

	block, count = sortedBlocks[0]
	# Duplicate blocks means that plaintext was repeated
	if count > 1:
		print line
		print bytes
		for block, count in sortedBlocks:
			print count, block


