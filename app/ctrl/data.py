# -*- coding: utf-8 -*-

import tornado.web
import sys
from model.dataflow import *
sys.path.append('..')

class VerCtrl(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        data = Dataflow()
        data = data.get_data_ver(username, password)
        self.write(data)


class DatachargeCtrl(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        subpaypro = self.get_argument('subpaypro')
        summary = username
        domitorytype = self.get_argument('domitorytype')
        data = Dataflow()
        data = data.domitorycharge(username, password, subpaypro, summary, domitorytype)
        data_json = json.dumps(data)
        self.write(data_json)


class DataflowCtrl(tornado.web.RequestHandler):
    def get(self):
        ver = self.get_argument('ver')
        data = Dataflow()
        data = data.get_data_message(ver)
        data_json = json.dumps(data)
        self.write(data_json)

