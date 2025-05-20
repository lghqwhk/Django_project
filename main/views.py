from django.shortcuts import render, redirect
from .models import Category, Items, Specials
from .forms import ReservationForm
from django.contrib import messages
import logging


def index(request):
    categories = Category.objects.filter(is_visible=True)
    reservation = ReservationForm(request.POST or None)

    if request.method == "POST" and reservation.is_valid():
        reservation.save()
        messages.success(request, 'Your reservation has been saved. Wait for a call.')
        return redirect('home')

    context = {
        'categories': categories,
        'reservation': reservation,
    }

    return render(request, 'index.html', context=context)


def specials_view(request):
    specials = Specials.objects.filter(is_visible=True).order_by('sort')
    return render(request, 'specials.html', {'specials': specials})



logger = logging.getLogger(__name__)
logger.debug("This view was reached!")

