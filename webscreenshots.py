# coding=utf-8
from argparse import _StoreTrueAction
from google.appengine.ext import ndb

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'


class WebScreenShot(ndb.Model):
    uri = ndb.StringProperty()
    secondDomUri = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    imageUri = ndb.StringProperty()
    thumbnailUri = ndb.StringProperty()