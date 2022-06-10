from django.shortcuts import render
from lettings.models import Letting
from profiles.models import Profile


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
def index(request):
    return render(request, 'index.html')

