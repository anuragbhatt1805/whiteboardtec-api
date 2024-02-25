from rest_framework.routers import DefaultRouter
from django.urls import include, path
from Connect.views import (
    ConnectViewSet, ContactViewSet,
    EmailViewSet, AddressViewSet,
    SocialViewSet
)

router = DefaultRouter()
router.register('connect', ConnectViewSet, basename='connect')
router.register('contact', ContactViewSet, basename='contact')
router.register('email', EmailViewSet, basename='email')
router.register('address', AddressViewSet, basename='address')
router.register('social', SocialViewSet, basename='social')

urlpatterns = [
    path('', include(router.urls)),
]