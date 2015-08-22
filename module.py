#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


import sys
def test():
	args = sys.argv
	return args

print __name__
print test()

try:
	import cStringIO as StringIO
except ImportError:
	import StringIO

sys.path.append('../')
print sys.path