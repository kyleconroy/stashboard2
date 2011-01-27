from django.db import models

# Create your models here.
class Region(models.Model):
    """ A geographical location 

        Properties:
        location      -- string: The location of this region
        name          -- string: The name of this region
        slug          -- string: The slug for this region
    """
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class Status(models.Model):
    """The status of a service

        Properties:
        name        -- string: The friendly name of this status
        slug        -- stirng: The identifier for the status
        description -- string: The state this status represents
        image       -- string: Image in /images/status
    """
    slug = models.SlugField(unique=True)
    description = models.TextField()
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

class Service(models.Model):
    """A service for Stashaboard to track.

        Properties:
        name          -- string: The name of this service
        description   -- string: The description of this servier
        status        -- Status: The current status of the service
        slug          -- string: The key of this service
        region        -- Region: The region in which this service is located 
    """
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    region = models.ForeignKey(Region)
    status = models.ForeignKey(Status)
