from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ChangePasswordView(UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User
        #permission_classes = (IsAuthenticated,)

        def update(self, request, *args, **kwargs):
            id_user = self.kwargs['pk']
            
            user = get_object_or_404(User, pk=id_user)
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not check_password(user.password, request.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
              
                user.password = request.data.get("new_password")
                user.save()
                
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

def check_password(password_saved, old_password):
    return password_saved == old_password
           