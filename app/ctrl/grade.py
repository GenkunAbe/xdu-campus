# -*- coding: utf-8 -*-

import tornado.web
import sys
sys.path.append('..')
from model.xdujwxt import XDU

class GradeCtrl(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username', '15020881062')
        password = self.get_argument('password', '881062')
        xdu = XDU()
        lt, exe = xdu.getKey()
        page = xdu.getPage(username, password, lt, exe)
        self.write(page)
