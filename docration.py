#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


def abc(t):
	def abd(n):
		def abcd(*a, **b):
			print '%s %s():' % (t, n.__name__)
			return n(*a, **b)
		return abcd
	return abd

@abc('a')
def now():
	print 'This is now'

#now()

import functools
def log(func):
	@functools.wraps(func):
	def wrapper(*a, **b):
		print 'call %s():' % func.__name__
		return func(*a, **b)
	return wrapper