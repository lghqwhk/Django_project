from .models import Contacts



def footer(request):
    res = Contacts.objects.first()

    return {
        'address': res.address if res else'',
        'reservations': res.reservations if res else '',
        'opening_hours': res.opening_hours if res else''
    }