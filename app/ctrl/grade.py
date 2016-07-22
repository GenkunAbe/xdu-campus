# -*- coding: utf-8 -*-

import tornado.web
import sys
import json
sys.path.append('..')
from model.jwxt import *

class GradeCtrl(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username', '15020881062')
        password = self.get_argument('password', '881062')
        jwxt = Jwxt()
        grade = jwxt.get_grade(username, password)
        grade_json = json.dumps(grade, cls=CourseEncoder)
        self.write(grade_json)
