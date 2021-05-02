from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),

    path("<slug:court_slug>", views.court_home, name="chome"),
    path("<slug:court_slug>/claim", views.court_claim, name="cclaim"),
    path("<slug:court_slug>/claim/api", views.court_claim_api, name="cclaim_api")
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns+= [
        path("<slug:court_slug>/reset", views.reset_time, name="reset"),
        path("sticker/", views.sticker, name="sticker"),
    ]

handler404 = views.handler404