from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producer

from django.contrib.auth.models import User
class UserEditAPIView(APIView):
    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user_instance = User.objects.get(pk=user_id)
        serializer = UserEditSerializer(user_instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)