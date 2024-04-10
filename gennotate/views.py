from rest_framework.response import Response
from rest_framework.decorators import api_view
from .api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status

@api_view(['GET'])
def get_all_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)