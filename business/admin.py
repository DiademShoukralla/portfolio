from django.contrib import admin

# Register your models here.
from business.models import Business, Employment

admin.site.register(Business)
admin.site.register(Employment)
