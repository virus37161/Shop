from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from shop_app.models import *
from django.views.generic import ListView
from shop_app.filters import ClothFilterByCategory
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string

class ListCloth (ListView):
    model = Cloth
    template_name = 'main.html'
    context_object_name = 'clothes'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClothFilterByCategory(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['categories'] = Category.objects.all()
        context['new_arrivals'] = self.request.GET.get('new') == 'True'
        return context


@login_required
def add_basket(request, pk):
    user = request.user
    cloth = Cloth.objects.get(id=pk)
    cloth.basket.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/main/'))

@login_required
def remove_basket(request, pk):
    user = request.user
    cloth = Cloth.objects.get(id=pk)
    cloth.basket.remove(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/main/basket/'))


class UserBasket (LoginRequiredMixin, ListView):
    model = Cloth
    template_name = 'user_basket.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClothFilterByCategory(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Cloth.objects.filter(basket=self.request.user.id)
        return context
