from django.contrib import admin
from django.urls import path, include

from . import views
from lettings.urls import urlpatterns as lettings_urls
from profiles.urls import urlpatterns as profiles_urls


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include(lettings_urls)),
    path('', include(profiles_urls)),
    path('sentry-debug/', trigger_error),
]
