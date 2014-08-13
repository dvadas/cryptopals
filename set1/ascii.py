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
