from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test



def is_manager(user):
    return user.groups.filter(name='Manager').exists()
@login_required(login_url='login')
@user_passes_test(is_manager )

def index(request):
    return HttpResponse('Manager page')
