import django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class NewPost(models.Model):

    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    developer=models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newpost_detail', kwargs={'pk': self.pk})


class AboutBlog(models.Model):
    application=models.CharField(max_length=200)
    developer=models.CharField(max_length=200)


