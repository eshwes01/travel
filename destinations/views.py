from django.shortcuts import render,get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Destination,Packages

# Create your views here.
class DestinationsList(generic.ListView):
    
    # model = Destination
    queryset = Destination.objects.all()
    template_name = "destinations/index.html"
    paginate_by = 3


def package_detail(request, slug):

    # dataset= Packages.objects.all()
    # package = get_object_or_404(dataset, slug=slug)

    destinations= Destination.objects.all()
    # packages = Packages.objects.all()
    destination = get_object_or_404(destinations, slug=slug)
    
    print("Package Detail page.")

    if request.method == "POST":
        print("Received the POST request")

    return render(
        request,
        "destinations/package_detail.html",
        {
            "packages" : destination.packages.all(), 
            "co_name" : "Travel Era",
            "destination" :destination.title
        }
    )