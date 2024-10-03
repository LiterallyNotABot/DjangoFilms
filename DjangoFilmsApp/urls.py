from django.urls import path
from . import views

from DjangoFilmsApp import views
urlpatterns = [
    path('', views.films_list, name='films_list'),
]