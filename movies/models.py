from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
#name = models.CharField(max_length=200
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    event_name = models.CharField(max_length=50, blank=True)

    # def __str__(self):
    #     return User.first_name + " " + User.last_name

