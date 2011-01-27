from django.views.generic import ListView
from stashboard.models import Region, Status, Service

class ServiceListView(ListView):

    model = Service
    context_object_name = "service_list"

class StatusListView(ListView):

    model = Status
    context_object_name = "status_list"

class RegionListView(ListView):

    model = Region
    context_object_name = "region_list"



