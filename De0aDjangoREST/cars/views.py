from rest_framework.generics import ListAPIView

from .models import Brand
from .serializers import BrandSerializer


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
