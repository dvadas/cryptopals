#!/usr/bin/env python

from util import pkcs7, str2bytes

input = 'YELLOW SUBMARINE'
padded = pkcs7(input, 20)
print padded

print str2bytes(padded)

