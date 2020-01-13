from django.urls import path

from .views import BrandListView


urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brands'),
]