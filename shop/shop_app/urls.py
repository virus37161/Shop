
from django.urls import path
from django.contrib.auth.views import TemplateView
from shop_app.views import ListCloth, add_basket, UserBasket, remove_basket

urlpatterns = [
    path ('main/', ListCloth.as_view(), name='main'),
    path('main/cloth/add/<int:pk>/', add_basket),
    path('main/cloth/remove/<int:pk>/', remove_basket),
    path ('main/basket/', UserBasket.as_view(), name='basket'),

]