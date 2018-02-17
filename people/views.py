from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import People

def index(request):
    all_people = People.objects.all()
    context = {'all_people': all_people}
    return render(request, 'people/index.html', context)

def detail(request, name):
    person = get_object_or_404(People, name=name)
    return render(request, 'people/detail.html', {'person': person})
