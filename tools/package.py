# coding=utf-8
import webapp2
from tools.print_env_var import PrintEnvironmentHandler

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'

app = webapp2.WSGIApplication([
    ('/tools/print-env-var', PrintEnvironmentHandler)
], debug=True)
