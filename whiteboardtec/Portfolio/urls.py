from rest_framework.routers import DefaultRouter
from django.urls import include, path
from Portfolio.views import PortfolioViewSet

router = DefaultRouter()
router.register('portfolio', PortfolioViewSet, basename='connect')

urlpatterns = [
    path('', include(router.urls)),
]