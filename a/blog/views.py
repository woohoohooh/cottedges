from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm

def thanks(request):
    return render(request, 'blog/thanks.html')

def booking(request):
    bookings = Booking.objects.all()
    form = BookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            form = BookingForm()
    return render(request, 'blog/booking.html', {'form': form})

def map(request):
    bookings = Booking.objects.all()
    form = BookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            form = BookingForm()
    return render(request, 'blog/map.html', {'form': form})

