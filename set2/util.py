import random
import itertools

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

def hamming(str1, str2):
	if len(str1) != len(str2):
		raise ValueError('lengths do not match')

	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		value = ch1 ^ ch2
		while value > 0:
			if value & 1:
				diffs += 1
			value = value >> 1
	
	return diffs

def findKeysize(bytes, numBlocks=10, minSize=2, maxSize=40):
	distances = []
	for keysize in range(minSize, maxSize + 1):
		blocks = []
		for i in range(numBlocks):
			block = bytes[i * keysize:(i + 1) * keysize]
			blocks.append(block)

		total = 0
		count = 0
		for block1, block2 in itertools.combinations(blocks, 2):
			# print block1, block2
			distance = hamming(block1, block2)
			total += distance / float(keysize)
			count += 1

		avg = total / count
		# print keysize, avg
		distances.append((avg, keysize))

	distances.sort()
	return distances
