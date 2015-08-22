#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


# Debug
def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r == (-1):
		print 'Error'
	else:
		pass

try:
	print 'Try..'
	r = 10 / 0
	print 'Result:', r
except ZeroDivisionError, e:
	print 'except:', e
finally:
	print 'finally...'
print 'END'