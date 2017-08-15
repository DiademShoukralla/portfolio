from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView

from .models import Business
from .forms import CreateBusinessForm


class ManageBusinessListView(ListView):
    template_name = 'business/manage_list.html'
    # will look into your templates folder for that path and file)
    context_object_name = "business_list"

    def get_context_data(self, **kwargs):
        context = super(ManageBusinessListView, self).get_context_data(**kwargs)
        context['title'] = 'Your Businesses'
        context['form'] = CreateBusinessForm()
        return context

    def get_queryset(self):
        return Business.objects.filter(employment__employee=self.request.user, employment__is_admin=True)


class ManageBusinessDetailView(DetailView):
    template_name = 'business/manage_detail.html'
    # will look into your templates folder for that path and file)
    context_object_name = "business"

    def get_context_data(self, **kwargs):
        context = super(ManageBusinessDetailView, self).get_context_data(**kwargs)
        context['title'] = "Manage " + self.kwargs['name']
        return context

    def get_object(self):
        return Business.objects.get(employment__employee=self.request.user, employment__is_admin=True,
                                    name=self.kwargs['name'])


class ViewBusinessDetailView(DetailView):
    template_name = 'business/view_detail.html'
    context_object_name = "business"

    def get_context_data(self, **kwargs):
        context = super(ViewBusinessDetailView, self).get_context_data(**kwargs)
        context['title'] = self.kwargs['name']
        return context

    def get_object(self):
        return Business.objects.get(name=self.kwargs['name'])


def create_business(request):
    if request.method == 'POST':
        print request.POST
        form = CreateBusinessForm(request.POST)
        print form.errors
        if form.is_valid():
            form.save(user=request.user)
            return HttpResponse("Good")
    print "Bad"
    return HttpResponse("Bad")
