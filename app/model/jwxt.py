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


def list_decode(items):
    ans = []
    for i in range(len(items) - 1):
        ans.append(items[i].decode('gbk').encode('utf-8'))
    pattern = re.compile(r'">(.+?)&nbsp;')
    grade = re.findall(pattern, items[-1])[0]
    grade = grade.decode('gbk').encode('utf-8')
    ans.append(grade)
    return ans
     

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
                # course = Course(items)
                # course = json.dumps(course, cls=CourseEncoder)  
                # courses.append(course)
                courses.append(list_decode(items))
                
            
            headpatten = re.compile(r'<a name="(.*?)" />.+?<td height="21"', re.S)
            grade[re.findall(headpatten, term)[0].decode('gbk').encode('utf-8')] = courses
        
        return grade


    # paras:    
    #     usr       : username
    #     psw       : password
    # return:
    #     grades    : a dict which has all course table
    def get_table(self, usr, psw):
        return table
