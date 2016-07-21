# -*- coding: utf-8 -*-

import tornado.web
import sys
sys.path.append('..')

class TableCtrl(tornado.web.RequestHandler):
    def get(self):
        self.write('Please Wait!\n')
