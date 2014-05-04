# coding=utf-8
import datetime
from google.appengine.ext import ndb

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'


class WebScreenShot(ndb.Model):
    def __init__(self, site_uri, site_sec_dom_uri, created, image_ri, thumb_uri):
        self.siteUri = site_uri
        self.siteSecondDomUri = site_sec_dom_uri
        self.created = created
        self.imageUri = image_ri
        self.thumbUri = thumb_uri

    siteUri = ndb.StringProperty()
    siteSecondDomUri = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    imageUri = ndb.StringProperty()
    thumbUri = ndb.StringProperty()


def get_last_screenshots(count=10):
    query = WebScreenShot.query().order(-WebScreenShot.created)
    screenshots = query.fetch(count)
    return screenshots


def find_screenshots(second_dom_uri, count=100):
    query = WebScreenShot.query(WebScreenShot.siteSecondDomUri == second_dom_uri) \
        .order(-WebScreenShot.created)
    screenshots = query.fetch(count)
    return screenshots


def save_screenshot(site_uri, image_uri, thumb_uri):
    site_sec_dom_uri = 'TODO'
    created = datetime.datetime.now()
    shot = WebScreenShot(site_uri, site_sec_dom_uri, created, image_uri, thumb_uri)
    shot.put()