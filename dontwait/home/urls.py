from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

DEBUG = True

urlpatterns = [
    path("", views.home, name="home"),

    path("<slug:court_slug>", views.court_home, name="chome"),
    path("<slug:court_slug>/claim", views.court_claim, name="cclaim"),
    path("<slug:court_slug>/claim/api", views.court_claim_api, name="cclaim_api")
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if DEBUG:
    urlpatterns+= [
        path("<slug:court_slug>/reset", views.reset_time, name="reset"),
    ]

handler404 = views.handler404