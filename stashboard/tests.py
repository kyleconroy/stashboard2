"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.utils import unittest

from stashboard.models import Region
from stashboard.models import Status
from stashboard.models import Service
from stashboard.models import LogEntry

class RegionTest(unittest.TestCase):

    def test_creation(self):
        region = Region(slug="us-east", name="U.S. East",
                        location="United States of America")
        self.assertEqual(region.name, "U.S. East")
        self.assertEqual(region.location, "United States of America")
        self.assertEqual(region.slug, "us-east")

class StatusTest(unittest.TestCase):

    def test_creation(self):
        status = Status(slug="down", name="Down", image="down.png",
                        description="The service is currently down")
        self.assertEqual(status.slug, "down")
        self.assertEqual(status.name, "Down")
        self.assertEqual(status.image, "down.png")
        self.assertEqual(status.description, "The service is currently down")

class ServiceTest(unittest.TestCase):

    def setUp(self):
        self.region = Region(slug="us-east", name="U.S. East",
                             location="United States of America")
        self.service = Service(slug="fake-service", name="Fake Service", 
                               description="This is fake, yo", region=self.region)

    def test_creation(self):
        self.assertEqual(self.service.slug, "fake-service")
        self.assertEqual(self.service.name, "Fake Service")
        self.assertEqual(self.service.region, self.region)
        self.assertEqual(self.service.description, "This is fake, yo")

    def test_feed_urls(self):
        (aa, an, iss) = self.service.feeds()
        self.assertEquals(aa["title"], "All Activity")
        self.assertEquals(aa["url"], "/feeds/services/fake-service/all-activity")

class LogEntryTest(unittest.TestCase):

    def setUp(self):
        self.region = Region(slug="us-east", name="U.S. East",
                        location="United States of America")
        self.service = Service(slug="fake-service", name="Fake Service", 
                               description="This is fake, yo", 
                               region=self.region)

    def test_creation(self):
        entry = LogEntry(url="/test/url", service=self.service,
                        description="The service has been changed from down to up")
        self.assertEqual(entry.url, "/test/url")
        self.assertEqual(entry.service, self.service)
        self.assertEqual(entry.description, 
                         "The service has been changed from down to up")

