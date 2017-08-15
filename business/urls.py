from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ManageBusinessListView as MbLv, ManageBusinessDetailView as MbDv, ViewBusinessDetailView as VbDv
from .views import create_business as cb

urlpatterns = [
    url(r'^manage/$', login_required(MbLv.as_view()), name="manage"),
    url(r'^manage/create/$', login_required(cb), name='create'),
    url(r'^manage/(?P<name>[\w-]+)/$', login_required(MbDv.as_view()), name='detail'),
    url(r'^(?P<name>[\w-]+)/$', VbDv.as_view(), name='view'),
]
