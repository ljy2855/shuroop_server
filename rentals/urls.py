from django.urls import path
from . import views

urlpatterns = [
    path('places/',views.get_all_places),
    path('borrow/<int:id>/',views.borrow_umbrella),
    path('return/<int:id>/',views.return_umbrella),
]