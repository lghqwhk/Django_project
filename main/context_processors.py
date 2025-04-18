from .models import Contacts



def footer(request):
    res = Contacts.objects.first()

    return {
        'address': '',
        'reservations': res.reservations if res else '',
        'opening_hours': ''
    }