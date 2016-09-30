# -*- coding: utf-8 -*-

import re
import sys
import requests
import shutil
from requests import Request, Session

url = 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fpayment.xidian.edu.cn%2Fpages%2Fcaslogin.jsp'

class Datazyz:
    def __init__(self):
        self.s = requests.session()

    def charge_login(self, usr, psw):
        html = self.s.get(url).text
        pattern = re.compile(r'"hidden" name=".*?" value="(.*?)"',re.S)
        values = re.findall(pattern, html)
        self.lt = values[0]
        self.exe = values[1]
        self._even = values[2]
        self.rm = values[3]

        postdata = {
            'username' : usr,
            'password' : psw,
            'lt':self.lt,
            'execution':self.exe,
            '_eventId':self._even,
            'rmShown':self.rm
        }
        result = self.s.post(url, data = postdata)
        html = result.text
        if(html.find('captchaResponse') != -1):
            pattern = re.compile(r'"hidden" name=".*?" value="(.*?)"',re.S)
            values = re.findall(pattern, html)
            self.lt = values[0]
            self.exe = values[1]
            self._even = values[2]
            self.rm = values[3]
            result = self.s.get("http://ids.xidian.edu.cn/authserver/captcha.html", stream = True)
            with open("ver.jpg", 'wb') as f:
                result.raw.decode_content = True
                shutil.copyfileobj(result.raw, f)
            ver = raw_input('please input the ver: ')
            postdata = {
                'username' : usr,
                'password' : psw,
                'lt':self.lt,
                'execution':self.exe,
                '_eventId':self._even,
                'rmShown':self.rm,
                'captchaResponse':ver
            }
            result = self.s.post(url, data = postdata)
            print result.text
        pattern = re.compile(r'href="(.+?)"', re.S)
        link = re.findall(pattern, result.text)[0]
        link = 'http://payment.xidian.edu.cn' + link
        
        return self.s, link

if __name__ == '__main__':
    usr = sys.argv[1]
    psw = sys.argv[2]
    datazyz = Datazyz()
    datazyz.charge_login(usr, psw)


