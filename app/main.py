# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
from url import url

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id', '0')
        self.write('No.%s: Hello World!\r\n' % id)

app = tornado.web.Application([
    (r'/', MainHandler)
] + url)

if __name__ == '__main__':
    app.listen(5969)
    tornado.ioloop.IOLoop.instance().start()