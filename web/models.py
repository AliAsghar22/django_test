from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):

	text = models.CharField(max_length=255)

	date = models.DateTimeField()

	amount = models.BigIntegerField()

	user = models.ForeignKey(User)

	def __str__(self):
		return '%s, %s' % (self.text,self.date)

class Income(models.Model):

	text = models.CharField(max_length=255)

	date = models.DateTimeField()

	amount = models.BigIntegerField()

	user = models.ForeignKey(User)

	def __str__(self):
		return '%s, %s' % (self.text,self.date)