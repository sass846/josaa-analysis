from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="home"),
  path("about/", views.about, name="about"),
  path("contact/", views.contact, name="contact"),
  path("institutes/", views.institutes, name="institutes"),
  path("seats/", views.seats, name="seats"),
  path("analysis/", views.analysis, name="analysis"),
]