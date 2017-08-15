from __future__ import unicode_literals

from django.core.files.storage import get_storage_class
from django.db import models
from authen.models import User
from django.db.models import signals


class OverwriteStorage():
    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name):
        return name


def pic_path(instance, filename):
    path = "users/{}/profile{}".format(instance.user.username, filename[filename.rfind('.'):])
    storage = get_storage_class()()
    if storage.exists(path):
        storage.delete(path)
    return path


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, primary_key=True)
    photo = models.FileField(verbose_name="Profile Picture", upload_to=pic_path, max_length=255,
                             default='', blank=True)
    bio = models.TextField(default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)

    def __unicode__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):
    """Create profile for every new user"""
    if created:
        UserProfile.objects.create(user=instance)

signals.post_save.connect(create_profile, sender=User, weak=False, dispatch_uid="models.create_profile")
