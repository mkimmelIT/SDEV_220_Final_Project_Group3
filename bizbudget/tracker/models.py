from django.db import models


class TrackerUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	department = models.CharField(max_length=10)
	position = models.CharField(max_length=60)
	email = models.EmailField('User Email')


	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Tracker(models.Model):
	department = models.CharField('Department', max_length=10)
	date =  models.DateTimeField('Request Date') 
	requester = models.ManyToManyField(TrackerUser)
	description = models.CharField(max_length=120)
	quantity = models.PositiveIntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)


	def __str__(self):
		return self.department