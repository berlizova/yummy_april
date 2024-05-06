from django.shortcuts import render
from django.http import HttpResponse
from.models import DishCategory, Dish, Gallery
from .forms import ReservationForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.all()
        form = ReservationForm()

        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_gallery'] = 'Check <span>Our Gallery</span>'
        context['categories'] = categories
        context['gallery'] = gallery
        context['form'] = form

        return context

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful Reservation!')
            return redirect('main:index')


# Create your views here.
def index(request):
    categories = DishCategory.objects.filter(is_visible=True)
    for item in categories:
        for dish in item.dishes.filter(is_visible=True):
            print(dish.name)
        print(item.name)

    return HttpResponse('\n'.join(map(str, categories)))
