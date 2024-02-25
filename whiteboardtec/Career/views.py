from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Career.models import Job, Application
from Career.serializer import JobSerializer, ApplicationSerializer

class JobViewSet(ModelViewSet):
    "Viewset for Job"
    serializer_class = JobSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Job.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Job.objects.all()
        else:
            return Job.objects.filter(is_active=True)

class ApplicationViewSet(ModelViewSet):
    "Viewset for Application"
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Application.objects.all()
        else:
            return Application.objects.none()