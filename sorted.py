#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'

a = [1, 3, 678, 33, 9, 333]
#print sorted(a)
def abc(a, b):
	if a > b:
		return -1
	if a < b:
		return 1
	return 0
	
#print sorted(a, abc)

def abcd(a, b):
	c = a.upper()
	d = b.upper()
	if c < d:
		return -1
	if c > d:
		return 1
	return 0

b = ['bob', 'about', 'Zoo', 'Credit']
print sorted(b, abcd)