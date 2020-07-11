from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    # The following fields are declared by Django by default.
    # I have mentioned them just so that there is no doubt.

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # The following fields are the custom fields.

    bio = models.TextField(blank=True)
    headline = models.CharField(max_length=300)
    following = models.IntegerField(default=0)
    articles = models.IntegerField(default=0)
    profile_picture = models.URLField(blank=True)


class Story(models.Model):
    class Meta:
        verbose_name_plural = "Stories"

    story_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    date_published = models.DateField()
    reading_duration = models.IntegerField()
    thumbnail = models.URLField()
