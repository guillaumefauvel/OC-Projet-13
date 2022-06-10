from django.contrib import admin

from .models import Address
from lettings.models import Letting
from profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
