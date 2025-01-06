from django.db import models
from django.contrib.auth.models import User


	# Create your models here.
class Topic(models.Model):
	"""A Topic the user is learning about"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)		
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
 
	def __str__(self):
		return self.name

class Entry(models.Model):
	"""Something Specific Learned About A Topic"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def _str_(self):
		"""Return a simple string representing the entry"""
		return f"{self.text[:50]}..."