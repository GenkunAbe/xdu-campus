# -*- coding: utf-8 -*-


"""

	This module has some classes.
	
	Class Ids auto login and return vaild cookie
	for further operation by given username & password.


"""

from ids import *
import cookielib
import urllib
import urllib2
import re
import json


urls = {
    'grade': 'http://jwxt.xidian.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo',
    'table': 'http://jwxt.xidian.edu.cn/xkAction.do?actionType=6'
}

class Course:
    def __init__(self, items):
        pattern = re.compile(r'">(.+?)&nbsp;')
        grade = re.findall(pattern, items[6])[0]
        
        self.data = [
            items[0].decode('gbk').encode('utf-8'), 
            items[1].decode('gbk').encode('utf-8'), 
            items[2].decode('gbk').encode('utf-8'), 
            items[3].decode('gbk').encode('utf-8'), 
            items[4].decode('gbk').encode('utf-8'), 
            items[5].decode('gbk').encode('utf-8'), 
            grade.decode('gbk').encode('utf-8')
        ]
    def __str__(self):
        s =  '[%s, %s, %s, %s, %s, %s, %s]' % (self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6])
        return s

class CourseEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, Course):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj)  


     

class Jwxt:

    def __init__(self):
        self.cookie = cookielib.CookieJar()


    # paras:
    #     usr       : username
    #     psw       : password
    # return:
    #     grades    : a dict which has all grades.
    def get_grade(self, usr, psw):
        grade = {}
        ids = Ids()
        self.cookies, pic = ids.get_ids_cookie(usr, psw)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        result = self.opener.open(urls['grade'])
        html = result.read()
        patten = re.compile(r'<a name=".*?" />.*?<td height="21"', re.S)
        terms = re.findall(patten, html)
        for term in terms:
            pattern = re.compile(r'<tr.*?;">(.*?)</tr>', re.S)
            subjects = re.findall(pattern, term)
            
            courses = []
            for subject in subjects:
                pattern = re.compile(r'<td.*?">\s*(.*?)\s*</td>', re.S)
                items = re.findall(pattern, subject)
                course = Course(items)
                course = json.dumps(course, cls=CourseEncoder)  
                courses.append(course)
            
            headpatten = re.compile(r'<a name="(.*?)" />.+?<td height="21"', re.S)
            grade[re.findall(headpatten, term)[0].decode('gbk').encode('utf-8')] = courses

            
        for (key, value) in grade.items():
            print key
            for course in value:
                print course
                
        print grade
        
        
        return grade
    # paras:    
    #     usr       : username
    #     psw       : password
    # return:
    #     grades    : a dict which has all course table
    def get_table(self, usr, psw):
        return table
