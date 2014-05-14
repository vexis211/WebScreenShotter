# coding=utf-8
from __builtin__ import staticmethod
import urllib2

from google.appengine.api.taskqueue import taskqueue
from webapp2 import RequestHandler

import webscreenshots


__author__ = 'Jan Skalicky <hskalicky@gmail.com>'

service_uri = '/services/create-screenshot'
queue_name = "default"


class ScreenShotRequestManager:
    def __init__(self):
        pass

    @staticmethod
    def create(site_uri):
        taskqueue.add(url=service_uri, params={'site_uri': site_uri})

    @staticmethod
    def get_approx_requests_count():
        return taskqueue.QueueStatistics.fetch(taskqueue.Queue(queue_name)).tasks


class ScreenShotRequestHandler(RequestHandler):
    def post(self):
        site_uri = self.request.get('site_uri')
        screenshot = make_screenshot(site_uri)
        thumbnail = make_thumbnail(screenshot)
        #save
        screenshot_uri = save_screenshot(screenshot)
        thumbnail_uri = save_thumbnail(thumbnail)
        webscreenshots.save_screenshot(site_uri, screenshot_uri, thumbnail_uri)


@staticmethod
def download_page(site_uri):
    try:
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = {'User-Agent': user_agent}
        return urllib2.urlopen(site_uri, headers)
    except urllib2.URLError:
        return None


@staticmethod
def make_screenshot(site_uri):
    return ''  #TODO


@staticmethod
def make_thumbnail(image):
    return ''  #TODO


@staticmethod
def save_screenshot(screenshot):
    return ''  #TODO


@staticmethod
def save_thumbnail(thumbnail):
    return ''  #TODO



