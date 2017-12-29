"""
	book/models.py
data models for a simplified library. books

"""
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	copyright = models.IntegerField(default=2017) 
	num_availible = models.PositiveIntegerField(validators=[MinValueValidator(0)])
	def __str__(self):
		return "{} by {}".format(self.title, self.author)

	def get_absolute_url(self):
    		"""
    		Returns the url to access a particular instance of the model.
    		"""
    		return reverse('book-detail', args=[str(self.id)])


