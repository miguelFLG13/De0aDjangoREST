from django.urls import path

from . import views


urlpatterns = [
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:id>/', views.BrandRetrieveView.as_view(), name='brand'),
    path('brands/<int:id>/update/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:id>/delete/', views.BrandDestroyView.as_view(), name='brand_delete'),
    path('cars/', views.CarListCreateView.as_view(), name='cars'),
    path('cars/<int:id>/', views.CarRetrieveUpdateDestroyView.as_view(), name='car'),
]

