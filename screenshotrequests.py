# coding=utf-8
import webapp2
from main import JINJA_ENVIRONMENT

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'



class RequestsHandler(webapp2.RequestHandler):
    def get(self):
        #TODO
        requests = []
        approx_request_count = 0

        template_values = {
            'requests': requests,
            'approx_request_count': approx_request_count,
        }

        template = JINJA_ENVIRONMENT.get_template('pages/home.html')
        self.response.write(template.render(template_values))


class CreateRequestHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('pages/home.html')
        self.response.write(template.render())

    def post(self):
        screenshots = get_last_screenshots()

        template_values = {
            'screenshots' : screenshots
        }

        template = JINJA_ENVIRONMENT.get_template('pages/home.html')
        self.response.write(template.render(template_values))
