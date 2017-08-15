
from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.

class UserInfo(models.Model):
	UserName = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	FullName = models.CharField(max_length=50)
	BirthDate = models.DateField()
	Email = models.EmailField(max_length=70,blank=False,unique=True)
	Gender = models.CharField(max_length=1)
	ProfilePic = models.ImageField(upload_to='ProfilePic/')
	Quote = models.CharField(max_length=200)

	def __str__(self):
		return self.FullName

