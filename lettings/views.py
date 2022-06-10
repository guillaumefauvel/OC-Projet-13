from django.shortcuts import render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}

    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }

    return render(request, 'lettings/lettings.html', context)