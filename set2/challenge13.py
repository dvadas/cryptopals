#!/usr/bin/env python

from collections import namedtuple

def parseKeyValues(string):
	keyValues = string.split('&')
	result = {}
	for keyValue in keyValues:
		key, value = keyValue.split('=')
		result[key] = value

	return result

def serialiseKeyValues(keyValues):
	parts = ['%s=%s' % (key, value) for key, value in keyValues.iteritems()]
	return '&'.join(parts)

def escape(field):
	return field.replace('&', '').replace('=', '')

Profile = namedtuple('Profile', ['email', 'uid', 'role'])

profiles = []
def makeProfile(email):
	profile = Profile(email, len(profiles), 'user')
	profiles.append(profile)
	return profile

def serialiseProfile(profile):
	# safeEmail = profile.email
	safeEmail = escape(profile.email)
	keyValues = profile._asdict()
	keyValues['email'] = safeEmail
	return serialiseKeyValues(keyValues)

def deserialiseProfile(string):
	keyValues = parseKeyValues(string)
	return Profile(**keyValues)

def main():
	# string = 'foo=bar&baz=qux&zap=zazzle'
	# print parseKeyValues(string)
	
	profile1 = makeProfile('foo@bar.com&role=admin')
	print profile1
	serialised = serialiseProfile(profile1)
	print serialised
	profile2 = deserialiseProfile(serialised)
	print profile2


if __name__ == '__main__':
	main()


