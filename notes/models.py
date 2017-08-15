from django.db import models
from login_logout.models import UserInfo
from django.db.models import ImageField, signals
from django.contrib.auth.models import Permission, User
##
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc
from datetime import datetime, timedelta
import os
############## NOTES ################## 
class Notes(models.Model):
	UserName = models.ForeignKey(User, on_delete=models.CASCADE)
	Tag = models.CharField(max_length=20)
	Note = models.TextField()
	my_date = models.DateTimeField(default=datetime.now())
	modified_date = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.UserName
############### EVents module ##########
class Event(models.Model):
	UserName = models.ForeignKey(User, on_delete=models.CASCADE)
	Tag = models.CharField(max_length=10)
	Description = models.TextField(max_length=100)
	#event_date = models.DateField()
	my_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return self.UserName
################ FILE HANDELING ####################
class Images(models.Model):
	UserName = models.ForeignKey(User, on_delete=models.CASCADE)
	Image_tag = models.CharField(max_length = 50)
	Image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.Image_tag
############### Document ###################
class Document(models.Model):
	UserName = models.ForeignKey(User, on_delete=models.CASCADE)
	docfile = models.FileField(upload_to='')
	#size =
	my_date = models.DateTimeField(default=datetime.now())
	modified_date = models.DateTimeField(default=datetime.now())
	#name, extension = (docfile.name).split(".")
	#name = docfile.name
	#extension = os.path.splitext(name)[1][1:]
	def extension(self):
		name, extension = os.path.splitext(self.docfile.name)
		return extension[1:]
	def name(self):
		name, extension = os.path.splitext(self.docfile.name)
		return name
	#def __str__(self):
	#	return self.docfile
################# HTML Calender #####################
class WorkoutCalendar(HTMLCalendar):
	def __init__(self, workouts):
		super(WorkoutCalendar, self).__init__()
		self.workouts = self.group_by_day(workouts)
	def formatday(self, day, weekday):
		if day != 0:
			cssclass = self.cssclasses[weekday]
			if date.today() == date(self.year, self.month, day):
				cssclass += ' today'
			if day in self.workouts:
				cssclass += ' filled'
				body = ['<ul>']
				for workout in self.workouts[day]:
					body.append('<li>')
					#body.append('<a href="%s">' % workout.get_absolute_url())
					body.append(esc(workout.Tag))
					body.append('</li>')
				body.append('</ul>')
				return self.day_cell(cssclass, '%d' % day)
			return self.day_cell(cssclass, day)
		return self.day_cell('noday', '&nbsp;')

	def formatmonth(self, year, month):
		self.year, self.month = year, month
		return super(WorkoutCalendar, self).formatmonth(year, month)

	def group_by_day(self, workouts):
		field = lambda workout: workout.start_date.day
		return dict(
			[(day, list(items)) for day, items in groupby(workouts, field)]
		)

	def day_cell(self, cssclass, body):
		return '<td class="%s">%s</td>' % (cssclass,body)

