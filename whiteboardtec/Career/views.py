from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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

    @action(detail=True, methods=['get'])
    def applications(self, request, pk=None):
        "Get applications for a job"
        job = self.get_object()
        applications = Application.objects.filter(job=job)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationViewSet(ModelViewSet):
    "Viewset for Application"
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Application.objects.all()
        else:
            return Application.objects.none()