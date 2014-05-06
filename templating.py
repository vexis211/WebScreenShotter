# coding=utf-8
import os
import jinja2

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'


class Templates(object):
    def __init__(self):
        pass

    JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

    @staticmethod
    def render(path, values=None):
        if not values:
            values = {}

        template = Templates.JINJA_ENVIRONMENT.get_template(path)
        return template.render(values)