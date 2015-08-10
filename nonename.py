#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


print map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
def abc(x, y):
	return lambda: x * x + y * y

print abc(3, 4)