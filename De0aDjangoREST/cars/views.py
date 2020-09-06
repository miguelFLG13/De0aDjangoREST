from rest_framework import generics
from rest_framework import filters as df

from .models import Brand, Car
from .paginations import SmallResultsSetPagination
from .serializers import BrandSerializer, CarSerializer


class BrandListView(generics.ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    pagination_class = SmallResultsSetPagination
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )


class BrandCreateView(generics.CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()


class BrandRetrieveView(generics.RetrieveAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandUpdateView(generics.UpdateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandDestroyView(generics.DestroyAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class CarListCreateView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    permission_classes = ()
    queryset = Car.objects.all()
    pagination_class = SmallResultsSetPagination
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('model', )
    ordering_fields = ('model', )


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    permission_classes = ()
    queryset = Car.objects.all()
    lookup_field = 'id'

