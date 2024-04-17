from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer, ImageSerializer
from ..models import Image

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer