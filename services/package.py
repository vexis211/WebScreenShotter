# coding=utf-8
import webapp2

from services import screenshots
from services.screenshots import ScreenShotRequestHandler


__author__ = 'Jan Skalicky <hskalicky@gmail.com>'

app = webapp2.WSGIApplication([
    (screenshots.service_uri, ScreenShotRequestHandler)
], debug=True)
