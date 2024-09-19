from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Destination

# Create your views here.
class DestinationsList(generic.ListView):
    
    # model = Destination
    queryset = Destination.objects.all()
    template_name = "destinations/index.html"
    paginate_by = 3

    
    def dest_list(request, slug):
        dataset= Destination.objects.all()


        if request.method == "POST":
            print("Received the POST request")

        return render(
            request,
            "destinations/index.html",
            {

            }
        )