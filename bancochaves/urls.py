from django.contrib import admin
from django.urls import path, include
from contas.views import ContasViewSet, DepositoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Contas', ContasViewSet, basename='Contas')
router.register('Depositos', DepositoViewSet, basename='Deposito')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]