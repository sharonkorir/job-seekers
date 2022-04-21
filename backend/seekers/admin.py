from django.contrib import admin
from .models import Profile, Rate, Resume, Pitch, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Pitch)
admin.site.register(Resume)
admin.site.register(Comment)
admin.site.register(Rate)