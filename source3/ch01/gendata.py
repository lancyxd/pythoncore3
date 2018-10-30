#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
#from sys import maxint
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

for i in range(randrange(3, 4)):
    maxint=2**32
    dtint = randrange(maxint)	# pick date
    print('dtint:',dtint)  #dtint
    dtstr = ctime(dtint)	# date string   Wed Mar  2 16:28:05 2067
    llen = randrange(4, 7)	# login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)	# domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    print ('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
	dom, choice(tlds), dtint, llen, dlen))

#Tue Apr  6 01:22:47 1982::ziqek@aokbpsvx.org::386875367-5-8