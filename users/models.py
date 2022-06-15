from django.db import models
from django.contrib.auth.models import User

class Username1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return self.user


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    bio = models.TextField()
    location = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    skill = models.TextField()
    pic = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
