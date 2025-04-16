from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet, FuncionarioViewSet, ProdutoViewSet, CupomViewSet
from . import views

router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'cupons', CupomViewSet)

urlpatterns = [
    path('produtos/', views.homepage, name='home'),
    path('', include(router.urls)),
]