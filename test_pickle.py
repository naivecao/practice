#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


try:
    import cPickle as pickle
except ImportError:
    import pickle

a = dict(name = 'xiaoming', age = 20, male = True)
with open('dump.txt', 'wb') as f:
    pickle.dump(a, f)
with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
print d
