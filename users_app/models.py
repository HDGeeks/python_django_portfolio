from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
 we dont have models for Auth coz django got that covered .
 Thanks , i guess , wink wink .

"""


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_pic = models.ImageField(default='default.jpg',
                                upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
