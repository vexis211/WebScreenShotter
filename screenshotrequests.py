# coding=utf-8
import sys
from urlparse import urlparse

sys.path.insert(0, 'libs')

from services.screenshots import ScreenShotRequestManager
from django.core.validators import URLValidator
import webapp2
from templating import Templates

__author__ = 'Jan Skalicky <hskalicky@gmail.com>'


class RequestsHandler(webapp2.RequestHandler):
    def get(self):
        # requests = self.get_waiting_requests()

        # approx_request_count = requests.count()
        approx_request_count = ScreenShotRequestManager.get_approx_requests_count()

        template_values = {
            # 'requests': requests,
            'approx_request_count': approx_request_count,
        }

        self.response.write(Templates.render('pages/requests.html', template_values))

        # def get_waiting_requests(self):
        #     return []


class CreateRequestHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Templates.render('pages/create_request.html'))

    def post(self):
        site_uri = self.request.get('site_uri')

        if self.is_form_valid(site_uri):
            ScreenShotRequestManager.create(site_uri)
            # render request list
            self.redirect('/Request')
        else:
            template_values = {
                'site_uri': site_uri,
                'site_uri_errors': 'This is not valid URL! Please check and try to submit again.'
            }
            # render create request with validation
            self.response.write(Templates.render('pages/create_request.html', template_values))

    @staticmethod
    def is_form_valid(site_uri):
        val = URLValidator(verify_exists=False)
        try:
            val(site_uri)
        except:  # TODO not nice :-)
            return False

        return True