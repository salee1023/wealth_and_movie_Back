from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail_follow(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(person)
        return Response(serializer.data)
    else:
        user = get_object_or_404(User, username=request.data['username'])
        if user != person:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                follow = False
            else:
                person.followers.add(user)
                follow = True
            return Response({ 'follow': follow })
        else:
            return Response({ 'error': '팔로우 할 수 없습니다.' }, status=status.HTTP_403_FORBIDDEN)