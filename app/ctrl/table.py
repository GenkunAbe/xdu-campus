# -*- coding: utf-8 -*-

import tornado.web
import sys
import json
sys.path.append('..')
from model.jwxt import Jwxt

class TableCtrl(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        year = self.get_argument('year')
        term = self.get_argument('term')
        classnumber = self.get_argument('classnumber')
        jwxt = Jwxt()
        table = jwxt.get_table(username, password, year, term, classnumber)
        table_json = json.dumps(table)
        self.write(table_json)
