from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

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

    def feeds(self):
        fs = []
        for f in ["All Activity", "Announcements", "Issues"]:
            url = "/feeds/services/%s/%s" % (self.slug, slugify(f))
            fs.append({"title": f,"url": url})
        return fs

    def archives(self):
        fs = []
        for f in ["All Activity", "Announcements", "Issues"]:
            url = "/archives/services/%s/%s" % (self.slug, slugify(f))
            fs.append({"title": f,"url": url})
        return fs


class Announcement(models.Model):
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
        closed  -- datetime: The date and time this issue was closed
        service -- Service: The service this annoucement is for
    """
    service = models.ForeignKey(Service)
    title = models.CharField(max_length=100)
    description = models.TextField()
    opened  = models.DateTimeField(auto_now_add=True)
    closed  = models.DateTimeField(null=True, blank=True)
    resolution  = models.TextField(null=True, blank=True)

    def __unicode__(self):
        if self.closed:
            return unicode("Resolved: %s" % self.title)
        else:
            return unicode("Open: %s" % self.title)

    def is_closed(self):
        if self.closed:
            return True
        else:
            return False


class Update(models.Model):
    """An issue update
        Properties:
        description   -- string: The description of this servier
        issue -- Issue: The Issue this update is for
        created  -- datetime: The date and time this update was created
    """
    issue = models.ForeignKey(Issue)
    created  = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __unicode__(self):
        return unicode("UPDATE on Issue ") + unicode(self.issue)


class LogEntry(models.Model):
    """ An archival entry into the log
        url -- url: The url to display in the log
        service -- Service: The service this annoucement is for
        description -- string: The description of this log entry
    """
    created  = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service)
    url = models.CharField(max_length=150)
    description = models.TextField()





