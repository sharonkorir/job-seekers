from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
import random

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.name)

# class Profile(models.Model):
#     '''
#     Profile model acts as blueprint for all profile instances
#     '''
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60, blank=True)
#     bio = models.TextField(max_length=200, blank=True)
#     profile_photo = CloudinaryField('image')
#     linkedIn_url = models.URLField(max_length = 150, null=True, blank=True)
    
#     def __str__(self):
#         return str(self.name)

class Resume(models.Model):
    '''
    CV model acts as blueprint for all project instances
    '''
    cv = models.FileField()
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str (self.profile.name)

class Pitch(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    pitch = models.TextField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.pitch

class Comment(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    pitch = models.ForeignKey(Pitch,on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.comment

RATE_CHOICES = [
  (1, '1'),
  (2, '2'),
  (3, '3'),
  (4, '4'),
  (5, '5'),
  (6, '6'),
  (7, '7'),
  (8, '8'),
  (9, '9'),
  (10, '10'),
]

class Rate(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(Resume, on_delete=models.CASCADE)
    conciseness = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    professionalism = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    flow = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return str(self.cv)