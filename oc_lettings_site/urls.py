from django.contrib import admin
from django.urls import path, include

from . import views
from lettings.urls import urlpatterns as lettings_urls
from profiles.urls import urlpatterns as profiles_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include(lettings_urls)),
    path('', include(profiles_urls))
]



