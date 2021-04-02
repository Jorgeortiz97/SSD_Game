# views.py
from rest_framework import viewsets
from .serializers import *
from .models import *

# Authentication
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ["create", "retrieve", "list"]:
            return [AllowAny()]
        return [IsAuthenticated()]

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer

    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ["retrieve", "list"]:
            return [AllowAny()]
        return [IsAuthenticated()]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all().order_by('name')
    serializer_class = SubmissionSerializer

    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ["create", "retrieve", "list"]:
            return [AllowAny()]
        elif self.action in ["update", "partial_update"]:
            return [IsAdminUser()]
        return [IsAuthenticated()]

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ["create", "retrieve", "list"]:
            return [AllowAny()]
        elif self.action in ["update", "partial_update"]:
            return [IsAdminUser()]
        return [IsAuthenticated()]