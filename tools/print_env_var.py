# coding=utf-8
__author__ = 'Jan Skalicky <hskalicky@gmail.com>'

import os
import webapp2


class PrintEnvironmentHandler(webapp2.RequestHandler):
    def get(self):
        for name in os.environ.keys():
            self.response.out.write("%s = %s<br />\n" % (name, os.environ[name]))