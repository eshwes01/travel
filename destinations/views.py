from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Destination, Packages, Comment, Booking
from .forms import CommentForm, BookingForm


class DestinationsList(generic.ListView):
    queryset = Destination.objects.all()
    template_name = "destinations/index.html"
    paginate_by = 6


@login_required
def my_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    booking_form = BookingForm(data=request.POST)

    if bookings.exists():
        return render(request, 'destinations/myBooking.html', {
            'bookings': bookings,
            'booking_form': booking_form,
        })
    else:
        return render(request, 'destinations/no_bookings.html', {
            'message': 'You have no bookings to show.',
        })


def package_detail(request, slug):
    destinations = Destination.objects.all()
    destination = get_object_or_404(destinations, slug=slug)

    if request.method == "POST":
        pass  # Add POST logic if needed

    return render(
        request,
        "destinations/package_detail.html", {
            "packages": destination.packages.all(),
            "co_name": "@ Travel Era",
            "destination": destination.title,
        }
    )


def info_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    comments = destination.comments.filter(approved=True)
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.destination = destination
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval!'
            )
            return HttpResponseRedirect(reverse('info_detail', args=[slug]))
    else:
        comment_form = CommentForm()

    return render(
        request,
        "destinations/info.html", {
            "destination": destination,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def comment_edit(request, slug, comment_id):
    destination = get_object_or_404(Destination, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.add_message(request, messages.ERROR,
                             'You are not allowed to edit this comment.')
        return HttpResponseRedirect(reverse('info_detail', args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment Updated and awaiting approval!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment.')

    return HttpResponseRedirect(reverse('info_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    destination = get_object_or_404(Destination, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment Deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comment!"
        )
    return HttpResponseRedirect(reverse('info_detail', args=[slug]))


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.user != request.user:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit this booking.")
        return HttpResponseRedirect(reverse('my_booking'))

    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
        else:
            messages.add_message(request,
                                 messages.ERROR, 'Error updating booking.')
    else:
        booking_form = BookingForm(instance=booking)

    return render(
        request, 'destinations/edit_booking.html', {
            'booking_form': booking_form,
            'booking': booking
        }
    )

# Deleting Booking from My Booking page
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.user != request.user:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to delete this booking.")
        return HttpResponseRedirect(reverse('my_booking'))

    booking.delete()
    messages.add_message(request, messages.SUCCESS, "Booking Deleted!")
    return HttpResponseRedirect(reverse('my_booking'))

# This method will carry out as itenerary detail display page 
def itinerary_detail(request, package_id):
    package = get_object_or_404(Packages, pk=package_id)
    bookings = package.bookings.all()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.package = package
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking is successfully submitted!'
            )
            return HttpResponseRedirect(reverse
                                    ('itinerary_detail', args=[package_id]))
        else:
            messages.add_message(request, messages.ERROR, 'Error on Booking')

    booking_form = BookingForm()

    return render(
        request, "destinations/itinerary_detail.html", {
            'package': package,
            'bookings': bookings,
            'booking_form': booking_form,
        }
    )
