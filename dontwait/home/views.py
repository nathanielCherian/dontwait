from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponse

from datetime import datetime, timedelta
import json

from .models import Court

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, "home/about.html")

def court_home(request, court_slug):
    court = get_object_or_404(Court, slug=court_slug)
    return render(request, 'home/courthome.html', {"court":court})

def court_claim(request, court_slug):
    court = get_object_or_404(Court, slug=court_slug)

    return render(request, 'home/courtclaim.html', {"court":court,})

@csrf_exempt
def court_claim_api(request, court_slug):
    court = get_object_or_404(Court, slug=court_slug)
    data = request.POST.dict()

    if not court.occupied():
        time = int(data['time'])
        time = time if time <= court.maxtime else court.maxtime
        print(time)
        court.booked = timezone.now() + timedelta(minutes=time)
        court.save()
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
