from rest_framework.routers import DefaultRouter
from django.urls import include, path
from Career.views import JobViewSet, ApplicationViewSet

router = DefaultRouter()
router.register('job', JobViewSet, basename='job')
router.register('application', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]