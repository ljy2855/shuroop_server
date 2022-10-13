from django.urls import path
from . import views

urlpatterns = [
    path('places/',views.get_all_places),
    path('place/<int:id>/',views.get_place),
    path('borrow/<int:id>/',views.borrow_umbrella),
    path('return/<int:id>/',views.return_umbrella),
    path('places/search/<str:keyword>/',views.search_places),
    path('places/search/',views.get_searched_places),
    path('places/favorite/',views.get_favorite_places),
    path('places/search/add/<int:id>/',views.add_searched_place),
    path('places/favorite/add/<int:id>/',views.add_favorite_place),
    path('places/search/remove/<int:id>/',views.remove_searched_place),
    path('places/favorite/remove/<int:id>/',views.remove_favorite_place),
]