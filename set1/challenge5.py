#!/usr/bin/env python

import itertools

from util import getBytes

input = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

bytes = [ord(ch) for ch in input]
print bytes

def repeatingKeyXor(key, bytes):
	repeatingKey = itertools.cycle(key)
	return [keyByte ^ byte for keyByte, byte in zip(repeatingKey, bytes)]

key = [ord(ch) for ch in 'ICE']
encrypted = repeatingKeyXor(key, bytes)
print encrypted

string = ''.join(map(chr, encrypted))
output = string.encode('hex')
print output

target = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
print target

if output == target:
    print 'success'
else:
    print 'failure'
