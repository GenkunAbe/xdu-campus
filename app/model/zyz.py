# -*- coding: utf-8 -*-

import requests
import re
import sys
from requests import Request, Session
import shutil
import pickle
from cookielib import LWPCookieJar 

url = 'http://zyzfw.xidian.edu.cn/'

class Zyzfw:
    def __init__ (self):
        self.s = requests.session()

    def dataflow_login(self, usr, psw):
        html = self.s.get(url).text
        ver_patten = re.compile(r'<img id="loginform-verifycode-image" src="(.*?)"', re.S)
        ver_url = url + re.findall(ver_patten, html)[0]
        result = self.s.get(ver_url, stream = True)
        with open("ver.jpg", 'wb') as f:
            result.raw.decode_content = True
            shutil.copyfileobj(result.raw, f)
        ver = input('please input the ver: ')
        
        patten = re.compile(r'"hidden" name="_csrf" value="(.*?)"', re.S)
        value = re.findall(patten, html)
        _csrf = value[0]

        postdata = {
            '_csrf' : _csrf,
            'LoginForm[username]' : usr,
            'LoginForm[password]' : psw,
            'LoginForm[verifyCode]' : ver,
            'login-button' : ''
        }

        self.s.post(url, data = postdata)
        return self.s
        # result = self.s.get('http://zyzfw.xidian.edu.cn/home/base/index')
        # print result.text

    def dataflow_login_get(self, usr, psw):
        html = self.s.get(url).text
        ver_patten = re.compile(r'<img id="loginform-verifycode-image" src="(.*?)"', re.S)
        ver_url = url + re.findall(ver_patten, html)[0]

        result = self.s.get(ver_url, stream = True)
        result.raw.decode_content = True

        patten = re.compile(r'"hidden" name="_csrf" value="(.*?)"', re.S)
        value = re.findall(patten, html)
        _csrf = value[0]
        postdata = {
            '_csrf' : _csrf,
            'LoginForm[username]' : usr,
            'LoginForm[password]' : psw,
            'login-button' : ''
        }
        #save postdata and self.s
        f = open('postdata.dat', 'wb')
        pickle.dump(postdata, f, True)
        f.close()
        self.s.cookies = LWPCookieJar('cookies')
        self.s.cookies.save()

        return result.content

    def dataflow_login__post(self, ver):
        #load postdata and self.s
        self.s.cookies = LWPCookieJar()
        self.s.cookies.load('cookies')
        postdata = pickle.load(open('postdata.dat', 'r'))
        postdata['LoginForm[verifyCode]'] = ver
        result = self.s.post(url, data = postdata)
        return self.s

if __name__ == '__main__':
    usr = sys.argv[1]
    psw = sys.argv[2]
    zyzfw = Zyzfw()
    pic = zyzfw.dataflow_login_get(usr, psw)
    with open('pic.jpg', 'wb') as f:
        f.write(pic)
    ver = raw_input('ver: ')
    
    zyzfw2 = Zyzfw()
    result = zyzfw2.dataflow_login__post(ver)
    print result


