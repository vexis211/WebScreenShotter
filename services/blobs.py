# coding=utf-8
import urllib
from google.appengine.ext.blobstore import blobstore
from google.appengine.ext.webapp import blobstore_handlers

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'

service_uri_prefix = "/services/blobs/"


class BlobServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)