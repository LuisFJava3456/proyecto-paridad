from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('verificar/', views.verificar_paridad, name='verificar'),
    path('api/', include(router.urls)),
]