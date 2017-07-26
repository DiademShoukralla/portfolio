from django.conf.urls import url
from .views import register, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^register/', register, name="register"),
]
