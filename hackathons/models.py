from __future__ import unicode_literals
import geocoder
from django.db import models
from django.template.defaultfilters import slugify
from datetime import date

class Hackathon(models.Model):
	name = models.CharField(max_length=255)
	school = models.CharField(max_length=255)
	date = models.DateTimeField()
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	slug = models.SlugField(blank=True)
	lat = models.CharField(max_length=255, blank=True)
	lon =  models.CharField(max_length=255,blank=True)
	url = models.URLField(max_length=500)

	class Meta:
		ordering = ['date']


	def save(self, *args, **kwargs):
		citystateString = str(self.city + ", " + self.state)
		g = geocoder.google(citystateString)
		self.slug = slugify(self.name)
		self.lat = g.lat
		self.lon = g.lng

		super(Hackathon, self).save(*args, **kwargs)


	def __unicode__(self):
		return str(self.name)

# Create your models here.
