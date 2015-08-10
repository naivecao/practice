#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


# Advanced features of slice
L = ['a', 'b', 'c', 'd', 'e']
M = 'abcdef'
print M[:3][:2]
# Advanced features of iterate
N = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f'}
for key, value in N.iteritems():
	print key, '--', value
for key, value in enumerate(['a', 'c', 'd']):
	print key, '--', value
# Advanced features of list generator
g = (x * x for x in range(1, 12) if x % 2 == 1)
for i in g:
	print i