from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from student_accounts.serializers import RegistrationSerializer
from student_accounts.models import create_auth_token # noqa

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.save()
        token = Token.objects.get(user=user).key
        data = {
            "message": f"{user.username} Succesfully registerd !",
            "token": token
        }
        data.update(serializer.data)
        return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = f"{request.user.username} logged out Successfully !"
        return Response(data=data, status=status.HTTP_200_OK)