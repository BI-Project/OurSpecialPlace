from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = (
            'id',
            'picture',
            'name',
            'natural_city',
            'static_dynamic',
            'mountain_sea',
            'history_modern',
            'save_flex',
            'accessibility',
            'dormitory_hotel',
            'season',
            'day_N_night',
            'age',
            'comment',
        )
