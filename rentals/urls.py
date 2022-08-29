from django.urls import path
from . import views

urlpatterns = [
    path('places/',views.get_all_places),
]