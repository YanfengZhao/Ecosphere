
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
		user = users.get_current_user()
		if user:
			self.redirect('/usermain')
			url = None
		else:
			url = users.create_login_url('/')
		template_values = {'url': url}
		template = JINJA_ENVIRONMENT.get_template('main.html')

		self.response.write(template.render(template_values))

class UserMain(webapp2.RequestHandler):
	def get(self):
		logoutURL = users.create_logout_url('/')
		self.response.write('<a href="%s">logout</a>' %logoutURL)
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/usermain',UserMain)
], debug=True)