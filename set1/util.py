
def getBytes(string):
	decoded = string.decode('hex')
	return [ord(ch) for ch in decoded]
