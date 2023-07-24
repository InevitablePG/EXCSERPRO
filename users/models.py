from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
 
	def save(self):
		super().save()
		
		img = Image.open(self.image.path)
		output_size = (300, 300)
		width, height = img.size
		if (width == height) and (width > 300 or height > 300):
			img.thumbnail(output_size)
			
		elif (width != height) and (width > 300 or height > 300):
	        # Crop the image to a square and resize to 300x300
	        min_dim = min(width, height)
	        max_dim = max(width, height)
	        left = (max_dim - min_dim) // 2
	        right = left + min_dim
	        top = 0
	        bottom = min_dim
	        img = img.crop((left, top, right, bottom))
	        img.thumbnail(output_size)
		
		else:
	        # Crop the image to a square
	        min_dim = min(width, height)
	        max_dim = max(width, height)
	        left = (max_dim - min_dim) // 2
	        right = left + min_dim
	        top = 0
	        bottom = min_dim
	        img = img.crop((left, top, right, bottom))
			
		img.save(self.image.path)