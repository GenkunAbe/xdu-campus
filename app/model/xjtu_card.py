import re
import urllib
import urllib2
import cookielib
import cStringIO

from PIL import Image, ImageEnhance
from pytesseract import *


class XjtuCard:

	def __init__(self):
		# URL for login
		self.loginUrl = 'https://cas.xjtu.edu.cn/login?service=http://card.xjtu.edu.cn:8050/Account/CASSignIn'
		# URL of grades
		self.cardUrl = 'http://card.xjtu.edu.cn/CardManage/CardInfo/Transfer'
		# URL of pay
		self.payUrl = 'http://card.xjtu.edu.cn/CardManage/CardInfo/TransferAccount'
		# URL of check code
		self.codeUrl = 'http://card.xjtu.edu.cn/Account/GetCheckCodeImg?rad='
		# URL of keyboard layout
		self.keyboardUrl = 'http://card.xjtu.edu.cn/Account/GetNumKeyPadImg'
		# Simulating Browser
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'
		}
		self.cookies = cookielib.CookieJar()
		self.postdata = urllib.urlencode({})
		
		# Generate opener
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

	# Get grades page
	def get_page(self, lt, exe):

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

		# Get card page
		result = self.opener.open(self.cardUrl)
		return result.read()

	# get the keys for login
	def get_keys(self):
		result = self.opener.open(self.loginUrl)
		html = result.read().decode('utf-8')
		pattern = re.compile(r'type="hidden".+value="(.+?)"')
		values = re.findall(pattern, html)
		return values[0], values[1]

	def pay(self, psw, check_code, amt):
		self.postdata = urllib.urlencode({
			'password' : psw,
			'checkCode' : check_code,
			'amt' : amt,
			'fcard' : 'bcard',
			'tocard' : 'card',			
			'bankno' : '',
			'bankpwd' : ''
		})
		request = urllib2.Request(
			url = self.payUrl,
			data = self.postdata,
			headers = self.headers
		)
		result = self.opener.open(request)
		return result.read()
    

	def get_code_pic(self, html):
		pattern = re.compile(r'rad=(\d+)"')
		rad = re.findall(pattern, html)[0]
		result = self.opener.open(self.codeUrl + rad)
		with open('1.gif', 'wb') as f:
			f.write(result.read())

	def get_encoded_psw(self, psw):
		result = self.opener.open(self.keyboardUrl)
		stream = cStringIO.StringIO(result.read())
		img = Image.open(stream)
		img = ImageEnhance.Brightness(img).enhance(1.1)
		new_img = Image.new('L', (130, 25))
		for j in range(10):
			tmp = img.crop((6+j*30, 3, 19+j*30,28))
			new_img.paste(tmp, (j*13,0))
		ss = image_to_string(new_img, lang='num')
		ans = ''
		for i in psw:
			for j in range(len(ss)):
				if i == ss[j]:
					ans += str(j)
		return ans[::-1]


if __name__ == '__main__':
	xjtu = XjtuCard()
	lt, exe = xjtu.get_keys()
	html = xjtu.get_page(lt, exe)
	xjtu.get_code_pic(html)
	raw_psw = input('Enter your password: ')
	code = input('Enter check Code: ')
	amt = input('Enter amount of money: ')
	psw = xjtu.get_encoded_psw(raw_psw)	
	result = xjtu.pay(psw, code, '%.2f' % float(amt))
	print result

