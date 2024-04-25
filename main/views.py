from django.shortcuts import render
from django.http import HttpResponse
from.models import DishCategory


# Create your views here.
def index(request):
    categories = DishCategory.objects.all()

    return HttpResponse('\n'.join(map(str, categories)))
