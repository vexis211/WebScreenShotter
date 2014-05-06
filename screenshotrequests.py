# coding=utf-8
import sys
sys.path.insert(0, 'libs')

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
import enum
import webapp2
from templating import Templates

__author__ = 'Jan Skalicky <hskalicky@gmail.com>'


class ScreenShottingMode(enum.Enum):
    single_page = 0,
    whole_page_subtree = 1,


class RequestsHandler(webapp2.RequestHandler):
    def get(self):
        #TODO both vars
        requests = []
        approx_request_count = 0

        template_values = {
            'requests': requests,
            'approx_request_count': approx_request_count,
        }

        self.response.write(Templates.render('pages/requests.html', template_values))


class CreateRequestHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Templates.render('pages/create_request.html'))

    def post(self):
        site_url = self.request.get('site_url')
        mode = self.request.get('mode')

        if self.is_form_valid(site_url, mode):
            self.create_screenshot_request(site_url, mode)
            # render request list
            self.response.write(Templates.render('pages/requests.html'))
        else:
            template_values = {
                'site_url': site_url,
                'mode': mode,
            }
            # render create request with validation
            self.response.write(Templates.render('pages/create_request.html', template_values))

    @staticmethod
    def is_form_valid(site_url, mode):
        val = URLValidator(verify_exists=False)
        try:
            val(site_url)
        except ValidationError:
            return False

        if mode != ScreenShottingMode.single_page and \
           mode != ScreenShottingMode.whole_page_subtree:
            return False

        return True

    @staticmethod
    def create_screenshot_request(site_url, mode):
        #TODO
        pass
