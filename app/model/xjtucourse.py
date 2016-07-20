# -*- coding: utf-8 -*-

import json

class XjtuGrade:

    def __init__(self):
        self.term       =   None
        self.code       =   None
        self.name       =   None
        self.type       =   None
        self.status     =   None
        self.credit     =   None
        self.reason     =   None
        self.nature     =   None
        self.vaild      =   None
        self.grades     =   {
            'main'      : 100,
            'standard'  : 100,
            'daily'     : 100,
            'interim'   : 100,
            'expr'      : 100,
            'final'     : 100,
            'other'     : 100
        }

    def __str__(self):
        dic = {
            'term' : self.term,
            'code' : self.code,
            'name' : self.name,
            'type' : self.type,
            'stauts' : self.status,
            'credit' : self.credit,
            'reason' : self.reason,
            'nature' : self.nature,
            'vaild' : self.vaild,
            'grades' : self.grades,
        }
        return json.dumps(dic)

class XjtuCourse:
    
    def __init__(self):
        self.name       =   None
        self.teacher    =   None
        self.classroom  =   None
        self.time       =   None




        


