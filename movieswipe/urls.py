"""
URL configuration for movieswipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from back import views as back_views
from ..back.views.movie_viewset import MovieViewSet
from ..back.views.vote_viewset import VoteViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", back_views.index),
    path("api/v1/votes/", VoteViewSet.as_view(), name="vote"),
    path("api/v1/movies/", MovieViewSet.as_view(), name="movie"),
]
