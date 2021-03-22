# serializers.py

from rest_framework import serializers
from .models import User, Submission

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'birthdate', 'job', 'elo', 'submissions')

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'name', 'code', 'author')
