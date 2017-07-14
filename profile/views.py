from django.shortcuts import render


def index(request):
    print request.user.is_authenticated()
    return render(request, "profile/profile.html", {'title': 'Profile'})
