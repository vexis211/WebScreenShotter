# coding=utf-8
import datetime
from urlparse import urlparse
from google.appengine.ext import ndb

__author__ = 'Jan Skalicky <hskalicky@gmail.com>'


class WebScreenShot(ndb.Model):
    def __init__(self, site_uri, site_host_uri, created, image_ri, thumb_uri, **kwds):
        super(WebScreenShot, self).__init__(**kwds)
        self.site_uri = site_uri
        self.site_host_uri = site_host_uri
        self.created = created
        self.image_uri = image_ri
        self.thumb_uri = thumb_uri

    site_uri = ndb.StringProperty()
    site_host_uri = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    image_uri = ndb.StringProperty()
    thumb_uri = ndb.StringProperty()


def get_last_screenshots(count=10):
    query = WebScreenShot.query().order(-WebScreenShot.created)
    screenshots = query.fetch(count)
    return screenshots


def find_screenshots(host_uri, count=100):
    query = WebScreenShot.query(WebScreenShot.site_host_uri == host_uri) \
        .order(-WebScreenShot.created)
    screenshots = query.fetch(count)
    return screenshots


def save_screenshot(site_uri, image_uri, thumb_uri):
    site_host_uri = urlparse(site_uri).hostname
    created = datetime.datetime.now()
    shot = WebScreenShot(site_uri, site_host_uri, created, image_uri, thumb_uri)
    shot.put()