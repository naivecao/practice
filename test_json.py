#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


import json
a = dict(name = 'xiaocao', age = 23, male = True)
print a
b = json.dumps(a)
print b
print json.loads(b)

class nihao(object):
    def __init__(self, name, age, male):
        self.name = name
        self.age = age
        self.male = male
def obtodi(a):
    return {'name' = a.name, 'age' = a.age, 'male' = a.male}

c = nihao('xiaoming', 21, False)
d = obtodi(c)
print d
d = json.dumps(c)
print d
