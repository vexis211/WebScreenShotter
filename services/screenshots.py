# coding=utf-8
from __builtin__ import staticmethod
import re
import urllib2
import urlparse

from google.appengine.api import files
from google.appengine.api import images

from google.appengine.api.taskqueue import taskqueue
from templating import BaseHandler

from services import blobs

import webscreenshots


__author__ = 'Jan Skalicky <hskalicky@gmail.com>'

service_uri = '/services/create-screenshot'
queue_name = "default"


class ScreenShotRequestManager(object):
    def __init__(self):
        pass

    @staticmethod
    def create(site_uri):
        taskqueue.add(url=service_uri, params={'site_uri': site_uri})

    @staticmethod
    def get_approx_requests_count():
        return taskqueue.QueueStatistics.fetch(taskqueue.Queue(queue_name)).tasks


class ScreenShotRequestHandler(BaseHandler):
    def post(self):
        site_uri = self.request.get('site_uri')
        screenshot_key = make_screenshot(site_uri)
        thumbnail_key = make_thumbnail(screenshot_key)
        screenshot_uri = '%s%s' % (blobs.service_uri_prefix, screenshot_key)
        thumbnail_uri = '%s%s' % (blobs.service_uri_prefix, thumbnail_key)

        #save
        webscreenshots.save_screenshot(site_uri, screenshot_uri, thumbnail_uri)


def download(uri):
    try:
        # create request
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) ' \
                     + 'AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        req = urllib2.Request(uri)  # .encode('utf-8')
        req.add_header('User-Agent', user_agent)
        # make request and get data
        response = urllib2.urlopen(req)
        content = response.read()
        mime = response.info().getheader('Content-Type')
        response.close()
        return mime, content
    except urllib2.URLError as e:
        return None


def get_first_img(site_uri):
    mime, html = download(site_uri)
    match = re.search('<img[^>]*src="([^<"]*)"', html)
    if not match:
        match = re.search("<img[^>]*src='([^<']*)'", html)
    if not match:
        return None
    image_rel_uri = match.group(1)
    image_uri = urlparse.urljoin(site_uri, image_rel_uri)
    return download(image_uri)


def make_screenshot(site_uri):
    #!!!!!!!!!!!!! GAE do not support html rendering -> for this example is downloaded first image on web !!!!!!!!!!!!!
    mime, image = get_first_img(site_uri)
    return save_image(mime, image)


def make_thumbnail(image_key):
    img = images.Image(blob_key=image_key)
    img.resize(width=80, height=80)
    # noinspection PyArgumentEqualDefault
    thumbnail = img.execute_transforms(output_encoding=images.PNG)

    return save_image('image/png', thumbnail)


def save_image(mime, image):
    file_name = files.blobstore.create(mime)
    with files.open(file_name, 'a') as f:
        f.write(image)
    files.finalize(file_name)
    return files.blobstore.get_blob_key(file_name)
