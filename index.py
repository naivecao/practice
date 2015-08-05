#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


def application(environ, start_respone):
	start_respone('200 OK', [('Content-Type', 'text/html')])
	a = environ['PATH_INFO']
	b = environ['REQUEST_METHOD']
	c = a + b
	return c
	