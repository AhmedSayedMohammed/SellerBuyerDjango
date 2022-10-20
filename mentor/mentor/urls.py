from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from product.views import ProductViewSet
from myuser.views import UserViewSet

from myuser import views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
