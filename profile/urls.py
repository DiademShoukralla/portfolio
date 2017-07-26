from django.conf.urls import url
from .views import index, update

urlpatterns = [
    url(r'^update/$', update, name='update'),
    url(r'^', index, name='index'),
]