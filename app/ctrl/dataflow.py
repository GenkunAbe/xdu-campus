# -*- coding: utf-8 -*-

import tornado.web
import sys
from model.dataflow import *
sys.path.append('..')

class DataflowCtrl(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        data = Dataflow()
        data = data.get_data_message(username, password)
        data_json = json.dumps(data)
        self.write(data_json)
