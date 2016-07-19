	# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re
from HTMLParser import HTMLParser

# A HTML Parser to get the keys for login
class HTMLParserForKey(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.lt = None
		self.execution = None

	def handle_starttag(self, tag, attrs):
		if tag == "input" and ('type', 'hidden') in attrs:
			if ('name', 'lt') in attrs:
				self.lt = attrs[2][1]
			elif ('name', 'execution') in attrs:
				self.execution = attrs[2][1]

class XDU:

	def __init__(self):
		# URL for login
		self.loginUrl = 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp'
		# URL of grades
		self.gradeUrl = 'http://jwxt.xidian.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo'
		# Simulating Browser
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
		self.cookies = cookielib.CookieJar()
		self.postdata = urllib.urlencode({})
		# Generate opener
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

	# Get grades page
	def getPage(self, lt, exe):

		# Generate POST data
		self.postdata = urllib.urlencode({
			'username':'15020881062',
			'password':'881062',
			'submit':'',
			'lt':lt,
			'execution':exe,
			'_eventId':'submit',
			'rmShown':'1'
		})

		# POST data
		request  = urllib2.Request(
			url = self.loginUrl,
			data = self.postdata,
			headers = self.headers)
		result = self.opener.open(request)

		# Get grades page
		result = self.opener.open(self.gradeUrl)
		print result.read().decode('gbk')

	# get the keys for login
	def getKey(self):
		result = self.opener.open(self.loginUrl)
		html = result.read().decode('utf-8')
		hp = HTMLParserForKey()
		hp.feed(html)
		hp.close()
		return hp.lt, hp.execution

if __name__ == '__main__':
	xdu = XDU()
	lt, exe = xdu.getKey()
	xdu.getPage(lt, exe)