"""
urls.py for Stashboard.

stashboard assumes that the it lives under /

Usage in your base urls.py:
(r'^/', include('stashboard.urls')),

"""

from django.conf.urls.defaults import *
from stashboard.views import ServiceListView

urlpatterns = patterns('',
    (r'^services$', ServiceListView.as_view()),
)


