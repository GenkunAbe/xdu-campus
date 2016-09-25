# -*- coding: utf-8 -*-


"""

	This module has some classes.
	
	Class Ids auto login and return vaild cookie
	for further operation by given username & password.


"""

import re
import json
from zyz import *
from datacharge import *

dataurls = {
    'datamessage' : 'http://zyzfw.xidian.edu.cn/home/base/index',
    'datacharge' : 'http://payment.xidian.edu.cn/netdetails511',
    'northcampus' : 'http://payment.xidian.edu.cn/utildetails518',
    'zy' : 'http://payment.xidian.edu.cn/utildetails512',
    'ht' : 'http://payment.xidian.edu.cn/utildetails513',
    'dx' : 'http://payment.xidian.edu.cn/utildetails514'
}

class Dataflow:

    def __init__(self):
        pass

    def get_data_message(self, usr, psw):
        data = {}
        zyz = Zyzfw()
        s = zyz.dataflow_login(usr, psw)
        datahtml = s.get(dataurls['datamessage']).text
        bodypatten = re.compile(r'<tbody>\s*.*?\s*</tbody>', re.S)
        databody = re.findall(bodypatten, datahtml)
        datamessagepatten = re.compile(r'<td>(.*?)</td>', re.S)
        datamessage = re.findall(datamessagepatten, databody[0])
        datamessage.pop(0)
        for i in range(4):
            datamessage.pop(i + 2)
        datamessage.pop(5)
        message = []
        for i in range(4):
            message.append(datamessage[i])
        data['message'] = message
        return data
    
    def  domitorycharge(self, usr, psw, subpaypro, summary, domitorytype):
        datacharge = Datazyz()
        s, link = datacharge.charge_login(usr, psw)
        s.get(link)
        result = s.get(dataurls[domitorytype]).text
        postdata = {
            "subpayproId" : subpaypro,
            "summary" : summary
        }
        posturl = "http://payment.xidian.edu.cn/utSubProjectCreateOrder"
        result = s.post(posturl, data  = postdata)
        result = json.loads(result.text)
        result = s.get('http://payment.xidian.edu.cn/showUserSelectPayType23' + str(result['payOrderTrade']['id']))
        html = result.text
        p = re.compile(r'<input type="hidden".*?value=[\'|\"](.*?)[\'|\"].*?/>', re.S)
        values = re.findall(p, html)
        data = {
            'payType':'01',
            'orderno':values[4],
            'orderamt':values[5],
            'struts.token.name':values[6],
            'token':values[7]
        }
        result = s.post('http://payment.xidian.edu.cn/onlinePay', data=data)
        html = result.text
        p = re.compile('<input type="hidden" name="(.+?)" value="(.+?)"/>', re.S)
        values = re.findall(p, html)
        postdata = dict(values)

        result = s.post('https://mapi.alipay.com/gateway.do?_input_charset=utf-8', data=postdata)
        # with open('result.html', 'w') as f:
        #     f.write(result.text.encode('utf8'))
        # print result.text
        return result.text


    def datacharge(self):
        pass

    


if __name__ == '__main__':
    # usr = sys.argv[1]
    # psw = sys.argv[2]
    usr = '14030188026'
    psw = '030540'   
    charge = Data()
    charge.domitorycharge(usr, psw, '3', '14030188026', 'ht')
    


   
        


