
def getBytes(string):
	decoded = string.decode('hex')
	return [ord(ch) for ch in decoded]

def bytes2str(bytes):
	return ''.join(chr(byte) for byte in bytes)

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

