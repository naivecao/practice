#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


class Mail(object):
	def __init__(self):
		self.user = ('naivecao@outlook.com', 'xiaocao8023')
		self.stmp = ('smtp-mail.outlook.com', 25, True, 'TLS')
		self.pop = ('pop-mail.outlook.com', 995, 'TLS')
		print 'start'

	def write(content):
		from email.mime.text import MIMEText
		MIMEText(content, _subtype='plain', _charset='utf-8')
	
	def send(self, text, addr = None):
		import smtplib
		serve = smtplib.SMTP(self.stmp[0], self.stmp[1])
		#serve.set_debuglevel(1)
		#serve.login(self.user[0], self.stmp[1])
		#serve.sendmail(self.user[0], [addr], text.as_string())
		#serve.quit

	def receive():
		return None
		
	def __del__(self):
		print 'end'
		return None

		
mail = Mail()
#mail.send()
a = 'a'
mail.write(a)