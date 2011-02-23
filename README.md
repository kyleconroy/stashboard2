# STASHBOARD

## Installation 

    pip install stashboard
    
## Setup
    
You'll need to add a few things to your `settings.py` file. Add stashboard to the installed apps

    INSTALLED_APPS = (
        ....
        'stashboard',
    )

Next, add the stashobard context processor

    TEMPLATE_CONTEXT_PROCESSORS = (
        ....
        "stashboard.context_processors.settings",
    )
    
And finially some specific settings

    SITE_NAME = "<title>"
    SITE_URL = "http://example.com"
    SITE_AUTHOR = "Kyle Conroy"
    PUBSUBHUBBUB_URL = "http://pubsub.example.com"
    
Stashboard assumes that it will be at the root of SITE_URL. Lastly, update the `urls.py` to include the stashboard urls

    urlpatterns = patterns('',
        ....
        (r'^', include('stashboard.urls')),
    )
    
And you're done!
    
## Running

Make sure to run your management commands before getting started

    ./manage.py syncdb
    ./manage.py loaddata services issues announcements updates 

To test it out, run

    ./manage.py runserver
    
