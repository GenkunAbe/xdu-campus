import re
from xjtu_grade import *

class XjtuGradeParser():
    def __init__(self):
        pass

    def html_parser(self, html):
        lines = self.get_lines(html)
        grades = []
        for line in lines:
            grades.append(self.line_parser(line))
        return grades

    def get_lines(self, html):
        pattern = re.compile(r'<tr class.+?</tr>', re.S)
        return re.findall(pattern, html)

    def line_parser(self, line):
        pattern = re.compile(r'class="">\s*(.*?)\s*</td>', re.S)
        items = re.findall(pattern, line)
        grade = XjtuGrade()
        grade.term = items[0]
        grade.code = items[1]
        grade.name = items[2]
        grade.type = items[3]
        grade.status = items[4]
        grade.credit = items[6]
        grade.reason = items[7]
        grade.nature = items[8]
        grade.vaild = items[9]
        pattern = re.compile(r"'(.*?)'", re.S)
        marks = re.findall(pattern, items[5])
        if len(marks) == 0:
            grade.grades = {
            'main'      : items[5],
            'standard'  : '',
            'daily'     : '',
            'interim'   : '',
            'expr'      : '',
            'final'     : '',
            'other'     : ''
            }
        else:
            grade.grades = {
                'main'      : marks[1],
                'standard'  : marks[2],
                'daily'     : marks[3],
                'interim'   : marks[4],
                'expr'      : marks[5],
                'final'     : marks[6],
                'other'     : marks[7]
            }
        print grade
        return grade