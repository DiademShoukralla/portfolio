from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.db.models import signals

from authen.models import User


class Business(models.Model):
    name = models.CharField(_('name'), max_length=30, primary_key=True)
    email = models.EmailField(_('email address'), max_length=30)
    description = models.CharField(_('description'), max_length=200, blank=True)
    street_address = models.CharField(_('street address'), max_length=30, blank=True)
    city = models.CharField(_('city'), max_length=30, blank=True)
    country = models.CharField(_('country'), max_length=30, blank=True)
    area_code = models.CharField(_('area code'), max_length=3, blank=True)
    number = models.CharField(_('phone number'), max_length=7, blank=True)

    def __unicode__(self):
        return self.name


class Employment(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = (('business', 'employee'),)

    def __unicode__(self):
        return "{} works at {}".format(str(self.employee), self.business.name)


def create_business(sender, instance, created, **kwargs):
    """Create employment link when business is added"""
    if created:
        print "hi"
        Employment.objects.create(business=sender, employee=sender.user, is_admin=True)

# signals.post_save.connect(create_business, sender=Business, weak=False, dispatch_uid="models.create_business")
