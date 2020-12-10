from django.db import models

from django.contrib.auth.models import User

from PIL import Image
# Create your models here.

class UserProfile(models.Model):
	user_id=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="pic/")
	dob=models.DateField(null=True)
	address=models.TextField()

	def __str__(self):
		return self.user.username