from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetr ullamcorper non id est.
def index(request):
    return render(request, 'index.html')
