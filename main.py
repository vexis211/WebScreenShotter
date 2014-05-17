#!/usr/bin/env python
# coding=utf-8
import webapp2
from screenshotrequests import RequestsHandler, CreateRequestHandler
from templating import Templates
from webscreenshots import get_last_screenshots, find_screenshots, get_screenshot_only_images


class MainHandler(webapp2.RequestHandler):
    def get(self):
        searching_uri = self.request.get('searchingUri')
        if searching_uri:
            screenshots = find_screenshots(searching_uri)
            template_values = {
                'screenshots': screenshots
            }
            self.response.write(Templates.render('parts/screenshot_table.html', template_values))
        else:
            screenshots = get_last_screenshots()
            template_values = {
                'screenshots': screenshots
            }
            self.response.write(Templates.render('pages/home.html', template_values))


class ImagesHandler(webapp2.RedirectHandler):
    def get(self):
        screenshots = get_screenshot_only_images()
        template_values = {
            'screenshots': screenshots
        }
        self.response.write(Templates.render('pages/images.html', template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Request', RequestsHandler),
    ('/Request/Create', CreateRequestHandler),
    ('/Images', ImagesHandler)
], debug=True)
