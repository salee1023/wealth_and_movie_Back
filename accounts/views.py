from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializer


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
def user_detail_follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'GET':
        if user_pk == 0:
            person = request.user
        serializer = ProfileSerializer(person)
        return Response(serializer.data)
    else:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if not request.user.is_authenticated:
            return Response({ 'error': '권한이 없습니다.' }, status=status.HTTP_401_UNAUTHORIZED)
        if request.user != person:
            if person.followers.filter(user_id=request.user.id).exists():
                person.followers.remove(request.user)
                follow = False
            else:
                person.followers.add(request.user)
                follow = True
            return Response({ 'follow': follow, 'follow_cnt': person.followers.count() })
        else:
            return Response({ 'error': '팔로우 할 수 없습니다.' }, status=status.HTTP_403_FORBIDDEN)