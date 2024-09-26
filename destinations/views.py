from django.shortcuts import render,get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Destination,Packages,Info


class DestinationsList(generic.ListView):
    # model = Destination
    queryset = Destination.objects.all()
    template_name = "destinations/index.html"
    paginate_by = 6


def package_detail(request, slug):

    # dataset= Packages.objects.all()
    # package = get_object_or_404(dataset, slug=slug)

    destinations= Destination.objects.all()
    destination = get_object_or_404(destinations, slug=slug)

    if request.method == "POST":
        print("Received the POST request")

    return render(
        request,
            "destinations/package_detail.html",
        {
            "packages" : destination.packages.all(), 
            "co_name" : "@ Travel Era",
            "destination" :destination.title
        }
    )

def info_detail(request, slug):
    
    destinations = Destination.objects.all()
    destination = get_object_or_404(destinations, slug=slug)
    comments = destination.comments.all().order_by("-created_on")
    comment_count = destination.comments.filter(approved=True).count()

    return render(
        request,
        "destinations/info.html",
        {
            # "info" : destination,
            "destination": destination,
            "comments" : comments,
            "comment_count" : comment_count,
        }
    )

def itinerary_detail(request, package_id):
  
    package = get_object_or_404(Packages, pk= package_id)

    return render(
        request,
        "destinations/itinerary_detail.html",
        {
            'package' : package
        }
    )