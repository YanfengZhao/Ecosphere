
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
		data = {'work_Mode':'1'}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response

class Videos(webapp2.RequestHandler):
	def get(self):
		data = {'work_Mode':'2'}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response

class Images(webapp2.RequestHandler):
	def get(self):
		data = {'work_Mode':'3'}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response

class ServosMove(webapp2.RequestHandler):
	def get(self):
		data = {'work_Mode':'4'}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response

class StopAll(webapp2.RequestHandler):
	def get(self):
		data = {'work_Mode':'9'}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response

class AnglePositionHandler(webapp2.RequestHandler):
	def post(self):
		servoX=self.request.get("servoX")
		servoY=self.request.get("servoY")
		servoZ=self.request.get("servoZ")
		motorX=self.request.get("motorX")
		motorY=self.request.get("motorY")
		motorZ=self.request.get("motorZ")
		servoSpeedX=self.request.get("servoSpeedX")
		servoSpeedY=self.request.get("servoSpeedY")
		servoSpeedZ=self.request.get("servoSpeedZ")
		motorSpeedX=self.request.get("motorSpeedX")
		motorSpeedY=self.request.get("motorSpeedY")
		motorSpeedZ=self.request.get("motorSpeedZ")

		new_servo_request_finish = "1"
		new_motor_request_finish = "1"
		if servoX != "0" or servoY != "0" or servoZ != "0" or servoSpeedX != "0" or servoSpeedY != "0" or servoSpeedZ != "0":
			new_servo_request_finish = "0"
		if motorX != "0" or motorY != "0" or motorZ != "0" or motorSpeedX != "0" or motorSpeedY != "0" or motorSpeedZ != "0":
			new_motor_request_finish = "0"
		
		data = {'servoX':servoX,'servoY':servoY,'servoZ':servoZ,'motorX':motorX,'motorY':motorY,'motorZ':motorZ,
		"servoSpeedX":servoSpeedX,"servoSpeedY":servoSpeedY,"servoSpeedZ":servoSpeedZ,"motorSpeedX":motorSpeedX,"motorSpeedY":motorSpeedY,
		"motorSpeedZ":motorSpeedZ,"new_servo_request_finish":new_servo_request_finish,"new_motor_request_finish":new_motor_request_finish, "work_Mode":"0"}
		header = { 'Content-Type' : "application/json"}
		req = urllib2.Request('http://192.168.1.100:81/',data=json.dumps(data))
		response = urllib2.urlopen(req)
		print response


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/usermain',UserMain),
    ('/simulatewalk',SimulateWalk),
    ('/stopAll',StopAll),
    ('/anglePositionHandler',AnglePositionHandler),
    ('/videos',Videos),
    ('/images',Images),
    ('/servosMove',ServosMove)
], debug=True)