from rest_framework.routers import DefaultRouter
from django.urls import include, path
from User.views import (
    UserViewSet,
    UserLoginApiView
)


router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view(), name='login')
]