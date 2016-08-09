# -*- coding: utf-8 -*-

"""

	This module has two classes.
	
	Class Ids auto login and return vaild cookie
	for further operation by given username & password.

	If Website require verification code, ask user to
	fill the code.

    Class LoginErr inherit Error class
    LoginErr may be raised when it is a wrong 
    username or password.

"""

import cookielib
import urllib
import urllib2
import re

urls = {
    'ids' : 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp',
    'dataids' : 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fpayment.xidian.edu.cn%2Fpages%2Fcaslogin.jsp',
    'data' : 'http://zyzfw.xidian.edu.cn/'
}

class Ids():

    def __init__(self):
        pass
        
    # paras:
    #     usr       : username
    #     psw       : password
    # return:
    #     cookie    : a vaild cookie for further operation.
    #                 if need verification code, return None.
    #     codepic   : a pic if need verification code, else None.
    # Error:
    #     LoginErr  : raise LoginErr when the username or password
    #                 is wrong.       
    def get_ids_cookie(self, usr, psw, type):

        # Get Login Page
        if type == 'ids':
            html = self.get_page('ids')
        elif type =='dataids':
            html = self.get_page('dataids')
        if (self.has_code(html)):
            # If need verification code
            pic = self.get_pic(html)
            return None, pic

        # Get Hidden Values
        pattern = re.compile(r'"hidden" name=".*?" value="(.*?)"',re.S)
        values = re.findall(pattern, html)
        self.lt = values[0]
        self.exe = values[1]
        self._even = values[2]
        self.rm = values[3]

        # Try Login
        postdata = urllib.urlencode({
            'username' : usr,
            'password' : psw,
            'lt':self.lt,
            'execution':self.exe,
            '_eventId':self._even,
            'rmShown':self.rm
        })

        request = urllib2.Request(
            url = urls['ids'],
            data = postdata)
        result = self.opener.open(request)
        # html = result.read().decode('gbk')
        # print html
        # try:
        #     # 如果解码失败了，一般都是账号密码错了
            
        # except:
        #     raise LoginErr
        
        # # 如果没有触发异常，那么就算是成功了
        return self.cookies, None



    def get_data_cookie(self, usr, psw, ver):

        # Get Login Page
        html = self.get_page('data')
        if (self.has_code(html)):
            # If need verification code
            pic = self.get_pic(html)
            return None, pic

        # Get Hidden Values
        pattern = re.compile(r'name="csrf-token" content="(.*?)"', re.S)
        value = re.findall(pattern, content)
        self.csrf = value[0]
        
        pattern = re.compile(r'"hidden" name=".*?" value="(.*?)"', re.S)
        value = re.findall(pattern, content)
        self._csrf = value[0]

        postdata = urllib.urlencode({
            'loginform-username' : usr,
            'loginform-password':psw,
            'loginform-verifycode':ver,
            'csrf-token':self.csrf,
            '_csrf':self._csrf
        })

        request = urllib2.Request(
            url = urls['data'],
            data = posydata)
        result = self.opener.open(request)

        # Try Login
        try:
            # 如果解码失败了，一般都是账号密码错了
            pass
        except:
            raise LoginErr
        
        # 如果没有触发异常，那么就算是成功了
        return self.cookie, None


    # This function return raw html text for further operation
    # return:
    #     html      : Login page html text
    def get_page(self, type):
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        if type == 'ids':
            response = self.opener.open(urls['ids'])
        elif type == 'data':
            response = self.opener.open(urls['data'])
        elif type == 'dataids':
            response = self.opener.open(urls['dataids'])

        content = response.read().decode('utf-8')
        return content


    # Just like self.get_cookie()
    # 下面三个先不写吧
    def get_cookie_code(self, usr, psw, code):
        # Try Login
        try:
            # 如果解码失败了，一般都是账号密码错了
            pass
        except:
            raise LoginErr
        
        # 如果没有触发异常，那么就算是成功了
        return self.cookie, None

    # paras:
    #     html      : raw html text
    # return:
    #     flag      : True if the html has verification code
    def has_code(self, html):
        return False

    # paras:
    #     html      : raw html text
    # return:
    #     pic       : The verification code picture
    def get_pic(self, html):
        return None


#class LoginErr(Error):    