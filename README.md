# STASHBOARD

## Installation 

    pip install stashboard
    
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
    PUSH_URL = "http://pubsub.example.com"
    
Stashboard assumes that it will be at the root of SITE_URL
    
    
