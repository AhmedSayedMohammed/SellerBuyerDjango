from rest_framework import viewsets, serializers
from rest_framework import permissions

from product.models import Product

from myuser.views import CreatorOnly


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CreatorOnly]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            instance = serializer.save(owner=self.request.user)
        else:
            instance = serializer.save()


def get_queryset(self, *args, **kwargs):
    if self.request.user.groups.filter(name='buyer').exists():
        return Product.objects.all().filter(owner=self.request.user)
