#!/usr/bin/env python
# coding=utf-8

import webapp2
from screenshotrequests import RequestsHandler, CreateRequestHandler
from templating import Templates
from webscreenshots import get_last_screenshots

class MainHandler(webapp2.RequestHandler):
    def get(self):
        screenshots = get_last_screenshots()

        template_values = {
            'screenshots': screenshots
        }
        self.response.write(Templates.render('pages/home.html', template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Request', RequestsHandler),
    ('/Request/Create', CreateRequestHandler)
], debug=True)
