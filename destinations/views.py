from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Destination,Packages,Info,Comment,Booking
from .forms import CommentForm,BookingForm


class DestinationsList(generic.ListView):
    # model = Destination
    queryset = Destination.objects.all()
    template_name = "destinations/index.html"
    paginate_by = 6

@login_required 
def my_booking(request):
    
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        booking_form = BookingForm(data=request.POST)
        
        if bookings.exists():
            # Render bookings if found
            return render(request, 'destinations/myBooking.html', {
                'bookings': bookings.all,
                'booking_form' : booking_form,
                })
        else:
            # if no bookings are found
            return render(request, 'destinations/no_bookings.html', {
                'message' : 'You have no bookings to show.',
                })

    return render(request, 'destinations/no_bookings.html', 
    {
        'message' : 'Plase log in to make the booking ',
        
    }
    )

# Package Detail page will call this method
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

# Info Detail page will calll this method 

def info_detail(request, slug):
    
    destinations = Destination.objects.all()
    destination = get_object_or_404(destinations, slug=slug)
    comments = destination.comments.all().order_by("-created_on")
    comment_count = destination.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.destination = destination
            comment.save()

            messages.add_message(
                request,messages.SUCCESS,
                'Comment submitted and awaiting approval!'
            )
    comment_form = CommentForm()

    return render(
        request,
        "destinations/info.html",
        {
            # "info" : destination,
            "destination": destination,
            "comments" : comments,
            "comment_count" : comment_count,
            "comment_form": comment_form,
        }
    )

#Editing a comment
def comment_edit(request, slug, comment_id):
    """
      view to edit comment
    """
    if request.method == "POST":
        queryset = Destination.objects.all()
        destination = get_object_or_404(queryset, slug=slug)
        info = destination.info
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm (data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.info = info
            info.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else :
            messages.add_message(request, messages.ERROR, 'Error on Update') 
        return HttpResponseRedirect(reverse('info_detail',args = [slug]))


# Deleting a comment
def comment_delete(request, slug, comment_id):
    
        queryset = Destination.objects.all()
        destination = get_object_or_404(queryset, slug=slug) 
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, "Comment Deleted! ")
        else:
            messages.add_message(request, messages.ERROR, "You can only delete your own comment! ")
        return HttpResponseRedirect(reverse('info_detail',args = [slug]))


# Editing the booking
def edit_booking(request,booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        if booking_form.is_valid():
            booking_form.save() 
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
    else:
         booking_form = BookingForm(instance=booking)
    # return HttpResponseRedirect(reverse('my_booking'))
    return render(request, 'destinations/edit_booking.html', 
                {   
                    'booking_form': booking_form, 
                    'booking': booking
                })

# Deleting the booking
def delete_booking(request,booking_id):   
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, "Booking Deleted!")
    return HttpResponseRedirect(reverse('my_booking'))


# Itinerary Detail page will call this method.
def itinerary_detail(request, package_id):

        queryset = Packages.objects.all()
        package = get_object_or_404(queryset, pk= package_id)

        bookings = package.bookings.all()
        # booking_count = package.bookings.filter(request.user).count()

        if request.method == "POST":
            print("Received a POST request")
            booking_form = BookingForm(data=request.POST)

            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.user = request.user
                booking.package = package
                booking.save()
                messages.add_message(request, messages.SUCCESS, 'Your booking is successfully submitted. One of our advisor will be contacted you very shortly!')
            else :
                messages.add_message(request, messages.ERROR, 'Error on Booking')
            return HttpResponseRedirect(reverse('itinerary_detail',args = [package_id]))
        booking_form = BookingForm()

        return render(
            request,
            "destinations/itinerary_detail.html",
            {
                'package' : package,
                'bookings' : bookings,
                # 'booking_count' : booking_count,
                'booking_form' : booking_form,
            }
    )