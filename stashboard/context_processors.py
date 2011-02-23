from django.conf import settings as sett

def settings(request):

    my_dict = {
        'SITE_URL': sett.SITE_URL,
        'SITE_NAME': sett.SITE_NAME,
        'SITE_AUTHOR': sett.SITE_AUTHOR,
        'PUSH_URL': sett.PUBSUBHUBBUB_URL,
    }

    return my_dict
