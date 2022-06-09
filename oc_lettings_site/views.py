from django.shortcuts import render
from .models import Letting, Profile


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
def index(request):
    return render(request, 'index.html')


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)


# Sed placerat quam in pulvinar commodo.
def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac.
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
