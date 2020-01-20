from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)

from .models import Brand
from .serializers import BrandSerializer


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()


class BrandCreateView(CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()


class BrandRetrieveView(RetrieveAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandUpdateView(UpdateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'
