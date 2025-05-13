from datetime import datetime

from .models import MobilePhone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.

def index(request):
    # Show flights in the past
    mobiles = MobilePhone.objects.filter(year_of_production__lte=datetime.now().date())
    context = {'mobile_list': mobiles, 'app_name': 'Lab-3 DNICK'}
    return render(request, 'index.html', context)

def details(request, mobile_id):
    mobile = MobilePhone.objects.filter(id=mobile_id).first()
    context = {'mobile_data': mobile, 'app_name': 'Lab-3 DNICK'}
    return render(request, 'details.html', context)
