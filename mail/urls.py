from django.urls import path
from . import views

urlpatterns = [
    path('send-emails/', views.index, name="index"),
]
