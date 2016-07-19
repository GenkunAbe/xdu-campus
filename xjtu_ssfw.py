# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re
from HTMLParser import HTMLParser
from xjtu_grade_parser import *

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

# A HTML Parser to get direct URL
class HTMLParserForUrl(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.url = None

	def handle_starttag(self, tag, attrs):
		if tag == "a" and ('class', 'popup-with-zoom-anim') in attrs:
			self.url = attrs[2][1][8:-3]


class XJTU:

	def __init__(self):
		# URL for login
		self.loginUrl = 'https://cas.xjtu.edu.cn/login?service=http%3A%2F%2Fssfw.xjtu.edu.cn%2Findex.portal'
		# URL of grades
		self.gradeUrl = 'http://ssfw.xjtu.edu.cn/index.portal?.pn=p1142_p1144_p1156'
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
			'username':'zdzhu',
			'password':'zdzhu123456',
			'lt':lt,
			'execution':exe,
			'_eventId':'submit',
		})

		# POST data
		request  = urllib2.Request(
			url = self.loginUrl,
			data = self.postdata,
			headers = self.headers)
		result = self.opener.open(request)
		# Get direct URL
		html = result.read().decode('utf-8')
		hp = HTMLParserForUrl()
		hp.feed(html)
		hp.close()

		# Direct URL
		result = self.opener.open(hp.url)

		# Get grades page
		result = self.opener.open(self.gradeUrl)
		return result.read()

	# get the keys for login
	def getKey(self):
		result = self.opener.open(self.loginUrl)
		html = result.read().decode('utf-8')
		hp = HTMLParserForKey()
		hp.feed(html)
		hp.close()
		return hp.lt, hp.execution

if __name__ == '__main__':
	xjtu = XJTU()
	lt, exe = xjtu.getKey()
	html = xjtu.getPage(lt, exe)
	xjtuGradeParser = XjtuGradeParser()
	xjtuGradeParser.html_parser(html)