from django.db import models
from django.contrib.auth.models import User
from users.models import Profile



class Gold(models.Model):
    name = models.CharField(max_length=20)
    gram = models.FloatField()
    price = models.FloatField()
    prob = models.FloatField()
    picture = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.ForeignKey(Gold, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    test = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text

