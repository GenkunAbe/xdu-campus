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
import sys


def list_decode(items):
    ans = []
    for i in range(len(items) - 1):
        ans.append(items[i])
    patten = re.compile(r'">(.+?)&nbsp;', re.S)
    grade = re.findall(patten, items[-1])[0]
    ans.append(grade)
    return ans
     

class Jwxt:

    def __init__(self):
        self.s = requests.session()


    # paras:
    #     usr       : username
    #     psw       : password
    # return:
    #     grades    : a dict which has all grades.
    def get_grade(self, usr, psw):
        gradeurl = "http://jwxt.xidian.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo"
        grade = {}
        ids = Ids()
        self.s = ids.ids_login(usr, psw)
        html = self.s.get(gradeurl).text
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
            grade[re.findall(headpatten, term)[0]] = courses
        
        return grade


    # paras:    
    #     usr       : username
    #     psw       : password
    # return:
    #     grades    : a dict which has all course table
    def make_addpatten(self, year, term, classnumber):
        return "http://jwxt.xidian.edu.cn/bjKbInfoAction.do?oper=bjkb_xx&xzxjxjhh="+ year + "-" + term + "-1&xbjh=" + classnumber + "&xbm=" + classnumber + "&xzxjxjhm=" + year
    
    

    def get_week(self, weeks):
        result = [0 for i in range(21)]
        p0 = re.compile(u'[\u4e00-\u9fa5]*')
        weeks = p0.sub('', weeks)
        p1 = re.compile(r',')
        items = re.split(p1, weeks)
        for item in items:
            p2 = re.compile(r'-')
            num = re.split(p2, item)
            if len(num) == 2:
                for i in range(int(num[0]), int(num[1]) + 1):
                    result[i] = 1
            else:
                result[int(num[0])] = 1
        return result
        

    def get_table(self, usr, psw, year, term, classnumber):
        table = {}
        address = self.make_addpatten(year, term, classnumber)
        ids = Ids()
        self.s = ids.ids_login(usr, psw)
        tableHtml = self.s.get(address).text
        #每节课包含的所有课程
        periodPatten = re.compile(r'<td width="12%" >\s*.*?\s*<tr bg', re.S)
        period = re.findall(periodPatten, tableHtml)
        
        courses = []    #存储每节课的课程
        for course in period:   #从每节课中提取出课程

            coursepatten = re.compile(r'<td width="12%" valign="top">.*?</td>', re.S)
            items = re.findall(coursepatten, course)
            for item in items:
                patten = re.compile(r' (.*?)<br>')
                its = re.findall(patten, item)
                for i in range(len(its)):
                    
                    coursemessagepatten = re.compile(r'(.*?)\(.*?,(.*?),(.*?),(.*?)\)', re.S)
                    coursemessagelist = re.findall(coursemessagepatten, its[i])
                    coursemessagelist[0] = list(coursemessagelist[0])
                    weeks = self.get_week(coursemessagelist[0][3])
                    coursemessagelist[0][3] = weeks
                    its[i] = coursemessagelist[0]
                   
                courses.append(its)
                
            if courses != [[],[],[],[],[],[],[]]:
                headpatten = re.compile(r'<td width="12%" >(.*?)</td>', re.S)
                
                table[re.findall(headpatten, course)[0]] = courses
                
            courses = []

        return table


if __name__ == '__main__':
    usr = sys.argv[1]
    psw = sys.argv[2]
    jwxt = Jwxt()
    table = jwxt.get_table(usr, psw, '2016-2017', '1', '1403018')
    print table