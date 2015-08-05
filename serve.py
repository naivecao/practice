#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'

from wsgiref.simple_server import make_server
from index import application

httpd = make_server('', 8000, application)
print 'Starting port 8000 for HTTP Serving'
httpd.serve_forever()