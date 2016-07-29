# -*- coding: utf-8 -*-

import tornado.web
import sys
import json
sys.path.append('..')
from model.jwxt import Jwxt

class TableCtrl(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username', '123456789')
        password = self.get_argument('password', '888888')
        jwxt = Jwxt()
        table = jwxt.get_table(username, password, '2016-2017', '1', '1403018')
        table_json = json.dumps(table)
        self.write(table_json)
