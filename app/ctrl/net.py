# -*- coding: utf-8 -*-

import tornado.web
import sys
sys.path.append('..')

class NetCtrl(tornado.web.RequestHandler):
    def get(self):
        self.write('Please Wait!\n')
