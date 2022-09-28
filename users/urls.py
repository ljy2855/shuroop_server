from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_with_password),
    path('check/token/',views.check_token),
    path('sign-up/',views.sign_up),
    path('check/id/',views.check_id),
    path('pay/',views.pay),
]
