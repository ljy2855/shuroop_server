from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('get/',views.get_notices),
    path('delete/all/',views.delete_all_notices),
    path('delete/',views.delete_notice),
]