from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.OneToOneField(User, on_delete=models.CASCADE)
	thumbnail = models.ImageField(upload_to='thumbnails')
	title = models.CharField(max_length=100)
	caption = models.TextField()
	
	def __str__(self):
		return self.title