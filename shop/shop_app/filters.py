from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter,CharFilter,ModelChoiceFilter, BooleanFilter
from shop_app.models import Cloth
import django_filters

class ClothFilterByCategory(FilterSet):



    class Meta:
        model = Cloth
        fields = ['category', 'new']



