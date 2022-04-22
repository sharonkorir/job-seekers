from django.contrib import admin
from .models import User, Rate, Resume, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Resume)
admin.site.register(Comment)
admin.site.register(Rate)