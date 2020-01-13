from django.urls import path

from .views import BrandCreateView, BrandListView


urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brands'),
    path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
]
