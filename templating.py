# coding=utf-8
import os
import jinja2
import webapp2

__author__ = 'Jan Skalicky<hskalicky@gmail.com>'


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja_env(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True)

    def render_response(self, _template, values=None):
        if not values:
            values = {}
        # Renders a template and writes the result to the response.
        rendered = self.jinja_env.get_template(_template).render(values)
        self.response.write(rendered)