from rest_framework import serializers
from app.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    """
    ProviderSerializer class to serialize/deserialize the Provider class
    """

    class Meta:
        model = Provider
        fields = '__all__'


class PolygonSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize/deserialize the ServiceArea class
    """

    class Meta:
        model = ServiceArea
        fields = '__all__'


class FilterServiceAreaSerializer(serializers.ModelSerializer):
    """
    FilterServiceAreaSerializer class used for showing the specific details of polygon to the Users
    """
    class Meta:
        model = ServiceArea
        fields = ['provider', 'name', 'price']
