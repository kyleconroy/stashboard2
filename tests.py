"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.utils import unittest

from stashboard.statusdashboard.models import Region
from stashboard.statusdashboard.models import Status
from stashboard.statusdashboard.models import Service

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

