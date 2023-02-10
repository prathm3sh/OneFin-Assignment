from django.contrib import admin
from django.urls import path, include

from movie.views import (
    MoviesListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('movies/', MoviesListView.as_view(), name='movies-list')
]
