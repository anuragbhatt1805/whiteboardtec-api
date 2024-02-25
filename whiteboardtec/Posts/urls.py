from rest_framework.routers import DefaultRouter
from django.urls import include, path
from Posts.views import PostViewSet


router = DefaultRouter()
router.register('event', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]