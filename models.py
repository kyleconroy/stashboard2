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

    def __unicode__(self):
        return unicode(self.name)

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

    def __unicode__(self):
        return unicode(self.name)

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

    def __unicode__(self):
        return unicode(self.name)

class Annoucement(models.Model):
    """A service announcement
        Properties:
        message -- string: A Markdown formatted message
        title   -- string: The title of the annoucement
        created -- datetime: The date and time this annoucement was created
        service -- Service: The service this annoucement is for
    """
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service)

    def __unicode__(self):
        return unicode(self.title)

class Issue(models.Model):
    """A service announcement
        Properties:
        description   -- string: The description of this servier
        title   -- string: The title of the annoucement
        opened  -- datetime: The date and time this issue was opened
        closed  -- datetime: The date and time this issue was opened
        service -- Service: The service this annoucement is for
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    opened  = models.DateTimeField(auto_now_add=True)
    closed  = models.DateTimeField(null=True, blank=True)
    service = models.ForeignKey(Service)

    def __unicode__(self):
        if self.closed:
            return unicode("Resolved: {0}".format(self.title))
        else:
            return unicode("Open: {0}".format(self.title))


class Update(models.Model):
    



