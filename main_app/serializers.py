from rest_framework import serializers
from .models import *

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourExperience
        fields = '__all__'

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGuide
        fields = '__all__'