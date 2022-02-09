from django.contrib import admin
from .models import NewPost
from .models import AboutBlog

# Register your models here.
admin.site.register(NewPost)
admin.site.register(AboutBlog)