from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView
from stashboard.models import Announcement
from stashboard.models import Issue
from stashboard.models import Region
from stashboard.models import Status
from stashboard.models import Service
from stashboard.models import Update
from stashboard.models import LogEntry

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
        issues = Issue.objects.filter(service=self.object)
        context['issues'] = issues.filter(closed=None)

        announcements = Announcement.objects.filter(service=self.object)
        context['announcements'] = announcements.order_by("-created")

        return context

class StatusListView(ListView):

    model = Status
    context_object_name = "status_list"

class RegionListView(ListView):

    model = Region
    context_object_name = "region_list"

class AnnouncementFeed(ListView):

    context_object_name = "announcement_list"
    template_name = "stashboard/announcement_feed.html"
    queryset = Announcement.objects.order_by("-created")

class ServiceAnnouncementFeed(AnnouncementFeed):

    def get_queryset(self):
        service =  get_object_or_404(Service, slug=self.kwargs["slug"])
        return Announcement.objects.filter(service=service).order_by("-created")

class ActivityFeed(ListView):

    context_object_name = "log_list"
    template_name = "stashboard/activity_feed.html"
    queryset = LogEntry.objects.order_by("-opened")

class ServiceActivityFeed(ListView):

    def get_queryset(self):
        service =  get_object_or_404(Service, slug=self.kwargs["slug"])
        return LogEntry.objects.filter(service=service).order_by("-created")

class IssueFeed(ListView):

    context_object_name = "issue_list"
    template_name = "stashboard/issue_feed.html"
    queryset = Issue.objects.order_by("-opened")

class ServiceIssueFeed(IssueFeed):

    def get_queryset(self):
        service =  get_object_or_404(Service, slug=self.kwargs["slug"])
        return Issue.objects.filter(service=service).order_by("-opened")

