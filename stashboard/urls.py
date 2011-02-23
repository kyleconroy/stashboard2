"""
urls.py for Stashboard.

stashboard assumes that the it lives under /

Usage in your base urls.py:
(r'^/', include('stashboard.urls')),

"""

from django.conf.urls.defaults import *
from stashboard.views import IssueDetailView
from stashboard.views import RegionDetailView
from stashboard.views import DefaultRegionView
from stashboard.views import ServiceDetailView
from stashboard.views import ActivityFeed
from stashboard.views import AnnouncementFeed
from stashboard.views import IssueFeed
from stashboard.views import ServiceActivityFeed
from stashboard.views import ServiceAnnouncementFeed
from stashboard.views import ServiceIssueFeed

urlpatterns = patterns('',
    (r'^$', DefaultRegionView.as_view()),
    (r'^issues/(?P<pk>\d+)$', IssueDetailView.as_view()),
    (r'^services/(?P<slug>[-\w]+)$', ServiceDetailView.as_view()),
    (r'^regions/(?P<slug>[-\w]+)$', RegionDetailView.as_view()),
    (r'^feeds/all-activity$', ActivityFeed.as_view()),
    (r'^feeds/issues$', IssueFeed.as_view()),
    (r'^feeds/announcements$', AnnouncementFeed.as_view()),
    (r'^feeds/services/(?P<slug>[-\w]+)/announcements$', ServiceAnnouncementFeed.as_view()),
    (r'^feeds/services/(?P<slug>[-\w]+)/issues$', ServiceIssueFeed.as_view()),
    (r'^feeds/services/(?P<slug>[-\w]+)/all-activity$', ServiceActivityFeed.as_view()),
)


