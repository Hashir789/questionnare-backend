from rest_framework.response import Response
from rest_framework.decorators import api_view
from .api.serializers import UserSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)