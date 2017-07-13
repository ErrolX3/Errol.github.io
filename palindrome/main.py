#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os 
import jinja2
import random
import urllib
import urllib2
import json

from google.appengine.ext import ndb


jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))

class Student(ndb.model):
    name = ndb.StringProperty()
    grade = ndb.IntegerProperty()

def is_palindrome(word):
  first_half = None
  second_half = None
 
  if len(word) % 2 == 0:
    first_half = len(word) / 2
    second_half = len(word) / 2
 
  else:
    first_half = (len(word) / 2) + 1
    second_half = len(word) / 2
    print first_half
    print second_half

    first_half = word[:first_half]  
    second_half = word[second_half:]
    second_half = second_half[::-1]

    print first_half
    print second_half 

 
  if first_half == second_half:
     return word + ' is a palindrome!'
  else:
     return word + ' is not a palindrome...'
  
is_palindrome('kayak')
is_palindrome('race car')
is_palindrome('katniss evedreen')



class FortHandler(webapp2.RequestHandler):
	def get(self):
		fortunes = [ 
		'good',
		'bad',
		'mysterious'
		]
		
		rand_fortune = random.choice(fortunes)
		all_fortunes= fortunes
		template = jinja_environment.get_template(
			'fortune.html')
		self.response.write(template.render(
			{
			 'fortune': rand_fortune,
			 'all_fortunes': fortunes,
			
			}))


class EmailsHandler(webapp2.RequestHandler):
    def get(self):

        emails = [
          {'title': 'help', 'sender': 'fakeaccount@gmail.com'},
          {'title': 'money pls', 'sender': 'fakeaccount@gmail.com'},
          {'title': 'hey!', 'sender': 'a_friend@gmail.com'},
          {'title': 'spam', 'sender': 'fakeaccount@gmail.com'},
          {'title': 'day 11 hmwk', 'sender': 'drb@hampton.edu'},
        ]
        template = jinja_environment.get_template(
            'emails.html')
        self.response.write(template.render(
            {
                'emails': emails,
            }))


class SumHandler(webapp2.RequestHandler):
   def get(self):
    	num1 = self.request.get('num1')
    	num2 = self.request.get('num2')

    	sum_of_nums= int(num1) + int(num2)

	template = jinja_environment.get_template('sum.html')
    	self.response.write(template.render({
    		'num1': num1,
    		'num2': num2,
    		'sum' : sum_of_nums,
    		}))


class PalindromeHandler(webapp2.RequestHandler):
    def get(self):
        palindrome_output = is_palindrome('racecar')
        template = jinja_environment.get_template(
        	'palindrome.html')
        self.response.write(template.render(
             {
            'palindrome': palindrome_output,
            'word': 'racecar'
             }))
        	

class MovieHandler(webapp2.RequestHandler):
   def get(self):        	
        name = self.request.get('name')
        length = self.request.get('length')
        num_reviews = self.request.get('num_reviews')
        stars = self.request.get('stars')
        template = jinja_environment.get_template(
            'movie.html')
        self.response.write(template.render(
            {
            'name': name,
            'length': length,
            'num_reviews': num_reviews,
            'stars': stars,
            }))


class MadLibsHandler(webapp2.RequestHandler):
    def get(self):
		template = jinja_environment.get_template('madlibs_input.html')
		self.response.write(template.render())
    def post(self):
		character_name= self.request.get('characterName')
		adjective = self.request.get('adj')
		template = jinja_environment.get_template('madlibs_output.html')
		self.response.write(template.render({
			'name': character_name,
			'adjective':adjective
			}))

class MyLibsHandler(webapp2.RequestHandler):
    def get(self):
		template = jinja_environment.get_template('mylib_input.html')
		self.response.write(template.render())
    def post(self):
		name= self.request.get('characterName')
		quality = self.request.get('Qual')
		template = jinja_environment.get_template('mylib_output.html')
		self.response.write(template.render({
			'name': name,
			'quality':quality,
			}))
	
'''
class MainHandler(webapp2.RequestHandler):
	def get(self):
		response= urllib2.urlopen('https://randomuser.me/api/?results=10')
		content = response.read()
		content_dictionary = json.loads(content)
		template = jinja_environment.get_template('random_user.html')
		self.response.out.write(template.render({
			'content' : content_dictionary
			}))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        giphy_data_source = urllib2.urlopen(
            "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        self.response.write(gif_url)
'''

class GifHandler(webapp2.RequestHandler):
    def get(self):
        sQuery = self.request.get('sQuery')
        base_url = 'http://api.giphy.com/v1/gifs/search?'
        url_params = {'q': sQuery, 'api_key': 'dc6zaTOxFJmzC', 'limit' :5}
        #content = response.read()
        content = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
        content_dictionary = json.loads(content)
        template = jinja_environment.get_template('gif.html')
        self.response.out.write(template.render({
            'content' : content_dictionary,
            }))


class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('search.html')
        self.response.out.write(template.render())

 
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('student_input.html')
        self.response.write(template.render())
 
    def post(self):
        name_from_form = self.request.get('studentName')
        grade_from_form=self.request.get('studentGrade')
        grade_from_form= int(grade_from_form)


        student_model = Student(name=name_from_form, grade=grade_from_form)
        student_model.put()

        template = jinja_environment.get_template('student_added.html')
        self.response.write(template.render(
            {
              'name': name_from_form
            }
            ))
 
class ListHandler(webapp2.RequestHandler):
    def get(self):
        students_query = Student.query().order(-Student.grade)
        list_of_students = students_query.fetch(limit=2)

        template = jinja_environment.get_template('list.html')
        self.response.write(template.render({
            'students':list_of_students,
            }))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/palindrome', PalindromeHandler),
    ('/fort', FortHandler),
    ('/emails', EmailsHandler),
    ('/sum', SumHandler),
    ('/movie',MovieHandler),
    ('/mlb',MadLibsHandler),
    ('/myL',MyLibsHandler),
    ('/gif',GifHandler),
    ('/search',SearchHandler),
    ('/list',ListHandler)
], debug=True)
