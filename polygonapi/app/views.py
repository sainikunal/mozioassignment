from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon as PolygonGeometry, Point as PointGeometry

from app.serializers import ProviderSerializer, PolygonSerializer, FilterServiceAreaSerializer
from app.models import Provider, ServiceArea
# Create your views here.


class ProviderCreate(generics.ListCreateAPIView):
    """
    ListAPIView to create new Provider object
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ProviderDetail viewset (for Read, Update, Delete operations) using REST framework generics classes
    It uses pk as a URL arg to filter out an individual Provider
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaCreate(generics.ListCreateAPIView):
    """
    ServiceAreaCreate viewset using DRF ListCreateAPI to create new ServiceArea object
    """
    queryset = ServiceArea.objects.all()
    serializer_class = PolygonSerializer


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ServiceAreaDetail viewset for read, update, delete operations using DRF generics classes
    """
    queryset = ServiceArea.objects.all()
    serializer_class = PolygonSerializer


@api_view(["GET"])
def FilterServiceArea(request):
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)

    if latitude is None or longitude is None:
        return HttpResponse('Wrong')

    point = PointGeometry(float(latitude), float(longitude))
    selected = []
    queryset = ServiceArea.objects.all()
    # import pdb;pdb.set_trace()
    for polygon in queryset:
        poly_coord = polygon.geojson
        eval_poly_coord = eval(poly_coord)
        polygon_geometry = PolygonGeometry(eval_poly_coord)
        print(polygon_geometry.is_valid)
        if point.within(polygon_geometry):
            selected.append(polygon)

    if len(selected) == 0:
        return Response('No Providers available for the given coordinates')

    serializer = FilterServiceAreaSerializer(selected, many=True)
    return Response(serializer.data)
