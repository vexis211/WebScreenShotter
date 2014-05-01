# coding=utf-8
import webapp2

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'



class MainHandler(webapp2.RequestHandler):
    def post(self):
        self.response.write('Hello world!')
