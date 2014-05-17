# coding=utf-8
import datetime
from urlparse import urlparse
from google.appengine.ext import ndb

__author__ = 'Jan Skalicky <hskalicky@gmail.com>'


class WebScreenShot(ndb.Model):
    site_uri = ndb.StringProperty()
    site_host_uri = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    image_uri = ndb.StringProperty()
    thumb_uri = ndb.StringProperty()


def get_last_screenshots(count=10):
    query = WebScreenShot.query().order(-WebScreenShot.created)
    screenshots = query.fetch(count, read_policy=ndb.EVENTUAL_CONSISTENCY)
    return screenshots


def get_screenshot_only_images(count=100):
    query = WebScreenShot.query().order(-WebScreenShot.created)
    screenshots = query.fetch(count, read_policy=ndb.EVENTUAL_CONSISTENCY,
                              projection=[WebScreenShot.image_uri, WebScreenShot.thumb_uri])
    return screenshots


def find_screenshots(uri, count=100):
    site_host_uri = urlparse(uri).hostname
    if not site_host_uri:
        site_host_uri = uri
    query = WebScreenShot.query(WebScreenShot.site_host_uri == site_host_uri) \
        .order(-WebScreenShot.created)
    screenshots = query.fetch(count)
    return screenshots


def save_screenshot(site_uri, image_uri, thumb_uri):
    site_host_uri = urlparse(site_uri).hostname
    created = datetime.datetime.now()

    shot = WebScreenShot(site_uri=site_uri, site_host_uri=site_host_uri,
                         created=created, image_uri=image_uri, thumb_uri=thumb_uri)
    shot.put()