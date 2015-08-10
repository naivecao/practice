#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'

def abc(x):
	return x % 2 == 1

print filter(abc, [1, 2, 3, 4, 5, 6])