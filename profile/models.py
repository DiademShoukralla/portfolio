from __future__ import unicode_literals

from django.db import models

from authen.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    photo = models.FileField(verbose_name="Profile Picture", upload_to="profiles", max_length=255,
                             default='', blank=True)
    bio = models.TextField(default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)
