from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	thumbnail = models.ImageField(upload_to='thumbnails')
	title = models.CharField(max_length=100)
	caption = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})