from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Testimonial(models.Model):
    city = models.CharField(max_length=100)
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        output_size = (800, 600)
        width, height = img.size
        aspect_ratio = 4 / 3  # Desired aspect ratio (4:3)

        if width < height or width > 800 or height > 600:
            # Calculate the desired dimensions while maintaining the 4:3 aspect ratio
            desired_width = int(min(width, height * aspect_ratio))
            desired_height = int(desired_width / aspect_ratio)

            # Calculate the crop box to center the image
            left = (width - desired_width) // 2
            top = (height - desired_height) // 2
            right = left + desired_width
            bottom = top + desired_height

            # Crop the image
            img = img.crop((left, top, right, bottom))

            # Resize the cropped image to the desired output size
            img.thumbnail(output_size)

        img.save(self.image.path)