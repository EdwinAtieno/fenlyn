import django_filters
from .models import *
class OrderFilter(django_filters.FilterSet):
        model = Destination.desc
        fields = '__all__'
