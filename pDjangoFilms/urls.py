"""
URL configuration for pDjangoFilms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# pDjangoFilms/urls.py

from django.contrib import admin
from django.urls import path, include  # Incluye la función include
from DjangoFilmsApp import views

# indian
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', views.films_list, name='films_list'),  # Incluye las URLs de DjangoFilmsApp bajo el prefijo 'films/'
]

# indian
urlpatterns += staticfiles_urlpatterns()
