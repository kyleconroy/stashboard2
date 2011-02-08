from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView
from stashboard.models import Annoucement
from stashboard.models import Issue
from stashboard.models import Region
from stashboard.models import Status
from stashboard.models import Service
from stashboard.models import Update

class RegionDetailView(DetailView):

    context_object_name = "region"
    model = Region

    def get_context_data(self, **kwargs):
        context = super(RegionDetailView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.filter(region=self.object)
        context['statuses'] = Status.objects.all()
        return context

class DefaultRegionView(RegionDetailView):

    def get_object(self):
        return Region.objects.all()[0]

class IssueDetailView(DetailView):

    context_object_name = "issue"
    model = Issue

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        # Get the object we're querying
        context['updates'] = Update.objects.filter(issue=self.object)
        return context

class ServiceDetailView(DetailView):

    context_object_name = "service"
    model = Service

    def get_object(self):
        return get_object_or_404(Service, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        # Get the object we're querying
        context['issues'] = Issue.objects.filter(service=self.object).filter(closed=None)
        context['announcements'] = Annoucement.objects.filter(service=self.object)
        return context

class StatusListView(ListView):

    model = Status
    context_object_name = "status_list"

class RegionListView(ListView):

    model = Region
    context_object_name = "region_list"



