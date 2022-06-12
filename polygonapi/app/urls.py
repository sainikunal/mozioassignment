from django.urls import path
from app.views import ProviderCreate, ProviderDetail, ServiceAreaCreate, ServiceAreaDetail, FilterServiceArea

urlpatterns = [
    path('provider/', ProviderCreate.as_view()),
    path('provider/<int:pk>/', ProviderDetail.as_view()),
    path('area/', ServiceAreaCreate.as_view()),
    path('area/<int:pk>/', ServiceAreaDetail.as_view()),
    path('filter/', FilterServiceArea),
]
