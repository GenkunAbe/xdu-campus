# -*- coding: utf-8 -*-

import requests
import re
import sys
from requests import Request, Session
import shutil

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

