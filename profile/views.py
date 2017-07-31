from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import capfirst
from .models import UserProfile


@login_required(login_url=reverse_lazy('login'))
def index(request):
    return render(request, "profile/profile.html", {'title': 'Profile'})


def update(request):
    user = request.user
    if request.method == "POST" and user.is_authenticated():
        first_name = request.POST.get('first_name', None)
        if first_name:
            user.first_name = capfirst(first_name)
            user.save()
            return HttpResponse(user.first_name)
        last_name = request.POST.get('last_name', None)
        if last_name:
            user.last_name = capfirst(last_name)
            user.save()
            return HttpResponse(user.last_name)
        myfile = request.FILES.get('photo', None)
        if myfile:
            u_p = UserProfile.objects.get(user=user)
            u_p.photo = myfile
            u_p.save()
            return HttpResponseRedirect(reverse_lazy("profile:index"))
    return HttpResponse("")
