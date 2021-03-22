# views.py
from rest_framework import viewsets

from .serializers import UserSerializer, SubmissionSerializer
from .models import User, Submission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all().order_by('name')
    serializer_class = SubmissionSerializer
