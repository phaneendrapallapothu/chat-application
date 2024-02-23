from django_filters import rest_framework as filters

from chatter.models import Room


class RoomFilterSet(filters.FilterSet):
    order = filters.OrderingFilter(fields=("created", "name"))

    class Meta:
        model = Room
        fields = {"name": ["icontains"]}
