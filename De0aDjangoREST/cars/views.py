from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Brand
from .serializers import BrandSerializer


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()


class BrandCreateView(CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
