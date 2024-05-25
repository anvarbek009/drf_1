from rest_framework import serializers
from .models import CategorySigns,RoadSigns


class CategorSignsSerializer(serializers.Serializer):
    class Meta:
        model=CategorySigns
        fields='__all__'

class RoadSignsSerializer(serializers.Serializer):
    class Meta:
        model=RoadSigns
        fields='__all__'