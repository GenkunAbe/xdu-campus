# -*- coding: utf-8 -*-

"""

	This module has two classes.
	
	Class Ids auto login and return vaild cookie
	for further operation by given username & password.

	If Website require verification code, ask user to
	fill the code.

    Class LoginErr inherit Error class
    LoginErr may be raised when it is a wrong 
    username or password.

"""

class Ids():

    def __init__(self):
        # TODO
        pass

    # paras:
    #     usr       : username
    #     psw       : password
    # return:
    #     cookie    : a vaild cookie for further operation.
    #                 if need verification code, return None.
    #     codepic   : a pic if need verification code, else None.
    # Error:
    #     LoginErr  : raise LoginErr when the username or password
    #                 is wrong.       
    def get_cookie(self, usr, psw):

        # Get Login Page
        html = self.get_page()
        if (self.has_code(html)):
            # If need verification code
            pic = self.get_pic(html)
            return None, pic

        # Get Hidden Values
        self.lt = 
        self.exe = 

        # Try Login
        try:
            # 如果解码失败了，一般都是账号密码错了
            pass
        except:
            raise LoginErr
        
        # 如果没有触发异常，那么就算是成功了
        return self.cookie, None


    # This function return raw html text for further operation
    # return:
    #     html      : Login page html text
    def get_page(self):
        self.cookie = 
        return html


    # Just like self.get_cookie()
    # 下面三个先不写吧
    def get_cookie_code(self, usr, psw, code):
        # Try Login
        try:
            # 如果解码失败了，一般都是账号密码错了
            pass
        except:
            raise LoginErr
        
        # 如果没有触发异常，那么就算是成功了
        return self.cookie, None

    # paras:
    #     html      : raw html text
    # return:
    #     flag      : True if the html has verification code
    def has_code(self, html):
        return False

    # paras:
    #     html      : raw html text
    # return:
    #     pic       : The verification code picture
    def get_pic(self, html):
        return None


class LoginErr(Error):
    
    

    