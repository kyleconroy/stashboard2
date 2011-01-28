"""
urls.py for Stashboard.

stashboard assumes that the it lives under /

Usage in your base urls.py:
(r'^/', include('stashboard.urls')),

"""

from django.conf.urls.defaults import *
from stashboard.views import IssueDetailView
from stashboard.views import RegionDetailView
from stashboard.views import ServiceListView
from stashboard.views import ServiceDetailView

urlpatterns = patterns('',
    (r'^$', ServiceListView.as_view()),
    (r'^issues/(?P<pk>\d+)$', IssueDetailView.as_view()),
    (r'^services/(?P<slug>[-\w]+)$', ServiceDetailView.as_view()),
    (r'^regions/(?P<slug>[-\w]+)$', RegionDetailView.as_view()),
)


