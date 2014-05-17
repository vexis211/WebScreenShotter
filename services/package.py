# coding=utf-8
import webapp2

from services import screenshots, blobs
from services.blobs import BlobServeHandler
from services.screenshots import ScreenShotRequestHandler


__author__ = 'Jan Skalicky <hskalicky@gmail.com>'

app = webapp2.WSGIApplication([
    (screenshots.service_uri, ScreenShotRequestHandler),
    (blobs.service_uri_prefix + '([^/]+)?', BlobServeHandler)
], debug=True)
