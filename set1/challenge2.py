#!/usr/bin/env python

input1 = '1c0111001f010100061a024b53535009181c'
input2 = '686974207468652062756c6c277320657965'

def getBytes(string):
	decoded = string.decode('hex')
	return [ord(ch) for ch in decoded]

bytes1 = getBytes(input1)
bytes2 = getBytes(input2)
xored = [byte1 ^ byte2 for byte1, byte2 in zip(bytes1, bytes2)]
print xored
string = ''.join(map(chr, xored))
print string
output = string.encode('hex')
print output

target = '746865206b696420646f6e277420706c6179'
if output == target:
    print 'success'
else:
    print 'failure'

