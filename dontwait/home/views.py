from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponse

from datetime import datetime, timedelta
import json

from .models import Court, Access

def home(request):
    return render(request, 'home/home.html', {"title":"home",})

def about(request):
    return render(request, "home/about.html", {"title":"about",})

def sticker(request, sg):
    return render(request, "sticker.html",{"slug":sg})

#Conditional renders
def court_home(request, court_slug):
    court = get_object_or_404(Court, slug=court_slug)
    return render(request, 'home/courthome.html', {"court":court, "title":court.name})

def court_claim(request, court_slug):
    court = get_object_or_404(Court, slug=court_slug)
    return render(request, 'home/courtclaim.html', {"court":court, "title":court.name})

@csrf_exempt
def court_claim_api(request, court_slug):
    court = get_object_or_404(Court, slug=court_slug)
    data = request.POST.dict()

    if not court.occupied():
        time = int(data['time'])
        time = time if time <= court.maxtime else court.maxtime
        court.booked = timezone.now() + timedelta(minutes=time)
        court.save()
        create_access_item(request, court, time)
        return HttpResponse(json.dumps({"status":200}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"status":204}), content_type="application/json")


def reset_time(request, court_slug):
    court = get_object_or_404(Court, slug=court_slug)
    court.booked = timezone.now()
    court.save()
    print("time reset!")
    return HttpResponse("Time reset!")


def handler404(request, exception):
    return render(request, '404.html', status=404)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def create_access_item(request, court, play_time):
    ip = get_client_ip(request)
    a = Access(ip=ip, court=court, play_time=play_time)
    a.save()
