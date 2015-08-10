#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


def abcd(*s):
	def abc():
		a = 0
		for n in s:
			a = a + n
		return a
	return abc

a = abcd(1, 3, 5, 7, 9)
print a
print a()