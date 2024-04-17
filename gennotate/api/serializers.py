from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from ..models import Image
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'password', 'date_joined']
class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'user', 'urll', 'type', 'generated', 'question1', 'question2', 'question3', 'question4', 'grade']