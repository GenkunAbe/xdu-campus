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
        grade = "http://jwxt.xidian.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo"
        grade = {}
        ids = Ids()
        self.cookies, pic = ids.get_ids_cookie(usr, psw)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        result = self.opener.open(grade)
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
    def make_addpatten(self, year, term, classnumber):
        return "http://jwxt.xidian.edu.cn/bjKbInfoAction.do?oper=bjkb_xx&xzxjxjhh="+ year + "-" + term + "-1&xbjh=" + classnumber + "&xbm=" + classnumber + "&xzxjxjhm=" + year
    
    
    def get_table(self, usr, psw, year, term, classnumber):
        table = {}
        address = self.make_addpatten(year, term, classnumber)
        ids = Ids()
        self.cookies, pic = ids.get_ids_cookie(usr, psw)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        result = self.opener.open(address)
        tableHtml = result.read().decode('gbk')
    
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
                for it in its:
                    print it
                    coursemessagepatten = re.compile(r'(.*?)\(.*?,(.*?),(.*?),(.*?)\)', re.S)
                    coursemessagelist = re.findall(coursemessagepatten, it)
                    print coursemessagelist
                    for i in coursemessagelist:
                        print i 
                    weeks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    count = 0
                    for weeknumber in coursemessagelist[2]:
                        if weeknumber <= '20' and weeknumber >= '1':
                            weeks[int(wekknumber)] = 1
                        
                        elif weeknumber == '-':
                            suite
                            for i = int(coursemessagelist[2],index(weeknumber) - 1) + 1 in range(coursemessagelist[2],index(weeknumber) + 1 - coursemessagelist[2],index(weeknumber) - 1 )
                                weeks[i] = 1
                        else:
                            pass
                        count += 1
                    
                    coursemessagelist[2] = weeks
                    weeks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    count = 0
                courses.append(its)
            if courses != [[],[],[],[],[],[],[]]:
                headpatten = re.compile(r'<td width="12%" >(.*?)</td>', re.S)
                
                table[re.findall(headpatten, course)[0]] = courses
                
            courses = []

        return table
