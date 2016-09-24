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
import sys
import requests
import Cookie
from requests import Request, Session


urls = {
    'ids' : 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp',
    'dataids' : 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fpayment.xidian.edu.cn%2Fpages%2Fcaslogin.jsp',
}



class AddCookieHandle(urllib2.BaseHandler):
    def __init__(self, cookieValue):
        self.cookieValue = cookieValue
    
    def http_request(self, req):
        if not req.has_header('Cookie'):
            req.add_unredirected_header('Cookie', self.cookieValue)
        else:
            cookie = req.get_header('Cookie')
            req.add_unredirected_header('Cookie', self.cookieValue + '; ' + cookie)
        return req


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
        
        html = self.get_page('ids')
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

    


    def get_page(self, type):
        self.cookies = cookielib.CookieJar()
        r = requests.get(urls['ids'])
        return r.text


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
