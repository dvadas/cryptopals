#!/usr/bin/env python

import base64

hexData = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print hexData

decoded = hexData.decode('hex')
print decoded

base64Data = base64.standard_b64encode(decoded)
print base64Data

target = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
if base64Data == target:
    print 'success'
else:
    print 'failure'
