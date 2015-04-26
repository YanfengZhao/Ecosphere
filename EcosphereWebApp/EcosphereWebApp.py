
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import jinja2
import os
import json
import urllib2

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

		template_values = {'logoutURL': logoutURL}
		template = JINJA_ENVIRONMENT.get_template('usermain.html')

		self.response.write(template.render(template_values))

class SimulateWalk(webapp2.RequestHandler):
	def get(self):
		data = {'simulate_Walk':'True'}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response

		#print urllib2.urlopen("http://192.168.1.100:81/").read()

class StopAll(webapp2.RequestHandler):
	def get(self):
		data = {'stop':'all'}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response

class AnglePositionHandler(webapp2.RequestHandler):
	def post(self):
		angle1=self.request.get("angle1")
		angle2=self.request.get("angle2")
		angle3=self.request.get("angle3")
		position1=self.request.get("position1")
		position2=self.request.get("position2")
		position3=self.request.get("position3")
		data = {'angle1':angle1,'angle2':angle2,'angle3':angle3,'position1':position1,'position2':position2,'position3':position3}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/usermain',UserMain),
    ('/simulatewalk',SimulateWalk),
    ('/stopAll',StopAll),
    ('/anglePositionHandler',AnglePositionHandler)
], debug=True)